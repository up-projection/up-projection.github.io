# yaya-sy.github.io


## Writing articles

Create a Markdown file in `docs/blog/posts/` with front matter:

```markdown
---
draft: true
date: 2026-09-23
---

# Article title

Your article goes here.
```

- **Writing:** `draft: true` hides the article from the Blog list and excludes its
  page from production builds and the sitemap.
- **Publish:** change to `draft: false` and set the publication date. The Blog list
  updates automatically, newest first; no manual link needs to be added.
- **Local preview:** run `mkdocs serve`. Draft pages are available directly at
  `/blog/<title-slug>/` but remain hidden from the Blog list. For example,
  `/blog/learning-the-random/`. Local preview can include drafts in other
  navigation, so it is for your own use.
- `mkdocs build --strict` checks the production build. Commit and deploy when ready
  to make a published article live.

Drafts are not private files: their Markdown remains visible to anyone with access
to this repository.
# up-projection.github.io
# up-projection.github.io
# up-projection.github.io
