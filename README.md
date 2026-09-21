# Imperial Computing Notes

My notes from the BEng Computing at Imperial College London, written in [Obsidian](https://obsidian.md) and published as a website to help students coming through the course after me.

**Read them at [tstapely07.github.io/Imperial-Computing-Notes](https://tstapely07.github.io/Imperial-Computing-Notes)**. The site has search, link previews and a graph of how the notes connect, none of which work when browsing the files here.

These are unofficial notes written while learning the material, so they will contain mistakes. Some content, including diagrams and screenshots, comes from Imperial's lecture material, which I don't own. If you're from Imperial and would like anything removed, open an issue or email me at [tas225@ic.ac.uk](mailto:tas225@ic.ac.uk).

## Layout

- `Index.md`: the site's homepage
- `Year 1/`: one folder per module. Each holds a module page named after the folder, a `.base` table listing its topics, and the notes themselves
- `Attachments/`: every image the notes embed
- `Templates/`, `Useful/`: Obsidian helpers, not published

## How publishing works

Every push to `master` runs `.github/workflows/deploy.yml`, which builds the vault into a site with [Quartz](https://quartz.jzhao.xyz) and deploys it to GitHub Pages. Everything the build needs lives in `.site/`:

- `quartz.config.yaml`: site settings, theme and plugins, including `ignorePatterns`, the folders kept off the site
- `build.sh`: copies the vault into a pinned Quartz checkout and builds it, with a few small patches to Quartz plugins explained in its comments
- `prepare_content.py`: adjusts the copied notes where Quartz reads markdown differently to Obsidian (multi-line maths, folder note links, text after bullets)
- `custom.scss`: style tweaks on top of the theme

To keep notes off the site, put them in a folder listed under `ignorePatterns` (`Year 2` is there until it's ready to release) or add `draft: true` to a note's frontmatter.

To preview locally, with Node.js 22+ and a checkout of [Quartz](https://github.com/jackyzha0/quartz) at the commit pinned in the workflow:

```sh
.site/build.sh path/to/quartz --serve   # then open http://localhost:8080
```
