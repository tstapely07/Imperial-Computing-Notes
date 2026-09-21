#!/usr/bin/env bash
# Builds the published site into <quartz-dir>/public.
# Usage: .site/build.sh <quartz-dir>   (a checkout of github.com/jackyzha0/quartz)
set -euo pipefail

vault="$(cd "$(dirname "$0")/.." && pwd)"
quartz="$(cd "$1" && pwd)"

cp "$vault/.site/quartz.config.yaml" "$quartz/quartz.config.yaml"

# Copy the vault in as content; the vault's Index.md becomes the homepage
rm -rf "$quartz/content"
mkdir "$quartz/content"
tar -C "$vault" --exclude=./.git --exclude=./.github --exclude=./.site --exclude=./.quartz-src -cf - . | tar -C "$quartz/content" -xf -
mv "$quartz/content/Index.md" "$quartz/content/index.md"
python3 "$vault/.site/prepare_content.py" "$quartz/content"

cd "$quartz"
npm ci --no-audit --no-fund
npx quartz plugin install
npx quartz build
