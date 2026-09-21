#!/usr/bin/env bash
# Builds the published site into <quartz-dir>/public.
# Usage: .site/build.sh <quartz-dir> [--serve]   (a checkout of github.com/jackyzha0/quartz)
# Extra arguments are passed to `quartz build`, so --serve previews it at http://localhost:8080
set -euo pipefail

vault="$(cd "$(dirname "$0")/.." && pwd)"
quartz="$(cd "$1" && pwd)"
shift

cp "$vault/.site/quartz.config.yaml" "$quartz/quartz.config.yaml"
cp "$vault/.site/custom.scss" "$quartz/quartz/styles/custom.scss"

# Copy the vault in as content; the vault's Index.md becomes the homepage
rm -rf "$quartz/content"
mkdir "$quartz/content"
tar -C "$vault" --exclude=./.git --exclude=./.github --exclude=./.site --exclude=./.quartz-src -cf - . | tar -C "$quartz/content" -xf -
mv "$quartz/content/Index.md" "$quartz/content/index.md"
python3 "$vault/.site/prepare_content.py" "$quartz/content"

cd "$quartz"
# Reuse an existing install when previewing locally; CI always starts fresh
[ -d node_modules ] || npm ci --no-audit --no-fund
npx quartz plugin install
# The theme named in quartz.config.yaml; Quartz can't load it if it installs it mid-build
npm install --no-save --no-audit --no-fund @quartz-themes/obsidian-gruvbox@1.0.1

# The graph colours notes you've visited differently, with no option to turn
# it off; drop the "visited" check so only the current note stands out
visited='K.has(i.id)||i.id.startsWith("tags/")'
for graph in node_modules/@quartz-community/graph/dist/{index.js,components/index.js}; do
  if grep -qF "$visited" "$graph"; then
    sed -i "s/K.has(i.id)||i.id.startsWith/i.id.startsWith/" "$graph"
  elif ! grep -qF '?Ie:i.id.startsWith("tags/")' "$graph"; then
    echo "build.sh: couldn't find the graph's visited-note colour to patch in $graph" >&2
    exit 1
  fi
done

# Each .base file also becomes a standalone page, cluttering the explorer and
# search; they're only wanted embedded in module pages, so mark them unlisted
bases=node_modules/@quartz-community/bases-page/dist/index.js
if grep -qF 'frontmatter: { title: baseName, tags: [] },' "$bases"; then
  sed -i 's/frontmatter: { title: baseName, tags: \[\] },/frontmatter: { title: baseName, tags: [] },\n          unlisted: true,/' "$bases"
elif ! grep -qF 'unlisted: true,' "$bases"; then
  echo "build.sh: couldn't find the bases page data to patch in $bases" >&2
  exit 1
fi

npx quartz build "$@"
