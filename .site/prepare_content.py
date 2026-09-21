"""Smooths over places where Quartz reads the vault differently to Obsidian.

- Multi-line display maths: Obsidian renders `$$\\begin{gather}...\n...$$`,
  but Quartz only treats $$ as a display block when it sits on its own line.
- Folder notes: Quartz publishes `X/X.md` as the folder page for `X/`, but
  can't resolve a bare `[[X]]` to it, so those links are made path-qualified.

Rewrites every .md under the given directory in place (run on the build copy,
never the vault).
"""
import pathlib
import re
import sys

# Leading callout/blockquote markers and indentation, e.g. "> " or ">> \t"
PREFIX = re.compile(r"^[\s>]*")
FENCE = re.compile(r"^[\s>]*(```|~~~)")


def normalise(text):
    lines = text.split("\n")
    out = []
    in_code = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if FENCE.match(line):
            in_code = not in_code
        prefix = PREFIX.match(line).group(0)
        body = line[len(prefix):]
        # A display block opening with content on the same line that is not
        # closed on that line
        if not in_code and body.startswith("$$") and body.count("$$") == 1 and body.strip() != "$$":
            end = i + 1
            while end < len(lines) and "$$" not in lines[end]:
                end += 1
            if end < len(lines):
                # Obsidian allows continuation lines inside a callout to omit
                # the ">", but a split-out display block does not
                def quoted(l):
                    return l if ">" not in prefix or l.lstrip().startswith(">") else prefix + l

                closing = quoted(lines[end])
                cprefix = PREFIX.match(closing).group(0)
                cbody = closing[len(cprefix):]
                before, _, after = cbody.partition("$$")
                out.append(prefix + "$$")
                out.append(prefix + body[2:])
                out.extend(quoted(l) for l in lines[i + 1:end])
                if before.strip():
                    out.append(cprefix + before)
                out.append(cprefix + "$$")
                if after.strip():
                    out.append(cprefix + after)
                i = end + 1
                continue
        out.append(line)
        i += 1
    return "\n".join(out)


# Content before a closing $$ on the last line of an otherwise well-formed
# block, e.g. "$$\n...\n0 & d_n\\end{bmatrix}$$"
def normalise_closers(text):
    lines = text.split("\n")
    out = []
    in_code = False
    in_math = False
    for line in lines:
        if FENCE.match(line):
            in_code = not in_code
        prefix = PREFIX.match(line).group(0)
        body = line[len(prefix):]
        if in_code:
            out.append(line)
            continue
        if not in_math and body.strip() == "$$":
            in_math = True
        elif in_math and body.strip() == "$$":
            in_math = False
        elif in_math and body.rstrip().endswith("$$") and body.count("$$") == 1:
            out.append(prefix + body.rstrip()[:-2])
            out.append(prefix + "$$")
            in_math = False
            continue
        out.append(line)
    return "\n".join(out)


def folder_note_paths(root):
    """Maps each folder note's name to its path, e.g. Haskell -> Notes/Haskell/Haskell"""
    notes = {}
    for path in root.rglob("*.md"):
        if path.stem == path.parent.name:
            notes[path.stem] = path.relative_to(root).with_suffix("").as_posix()
    return notes


def qualify_folder_note_links(text, notes):
    if not notes:
        return text
    names = "|".join(re.escape(n) for n in notes)
    # [[X]], [[X|alias]], [[X#heading]], ![[X]]
    pattern = re.compile(r"\[\[(" + names + r")(?=[\]|#^])")
    return pattern.sub(lambda m: "[[" + notes[m.group(1)], text)


if __name__ == "__main__":
    root = pathlib.Path(sys.argv[1])
    notes = folder_note_paths(root)
    changed = 0
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        new = qualify_folder_note_links(normalise_closers(normalise(text)), notes)
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"prepare_content: rewrote {changed} files")
