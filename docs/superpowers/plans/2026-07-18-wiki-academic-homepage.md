# Wiki Academic Homepage Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a deployable Wikipedia-inspired academic homepage that preserves the current 17 publications and repository images, with explicit credit to Linxin Song.

**Architecture:** Keep the existing Jekyll/AcadHomepage stack and content ownership in `_pages/about.md`. Add semantic homepage markup plus a dedicated Sass partial imported by the existing stylesheet, and verify source/build invariants with a standard-library Python test.

**Tech Stack:** Jekyll, Kramdown, HTML, SCSS, Python `unittest`

---

## File Map

- Modify `_pages/about.md`: biography, infobox, contents navigation, research interests, 17 publication entries, education, and credit.
- Create `_sass/_homepage.scss`: page-scoped Wikipedia/editorial styling and responsive behavior.
- Modify `assets/css/main.scss`: import the new homepage partial and remove obsolete global publication-card rules.
- Create `tests/test_homepage.py`: source and generated-site assertions without third-party dependencies.
- Reference `docs/superpowers/specs/2026-07-18-wiki-academic-homepage-design.md`: approved design and content constraints.

The current workspace is used instead of a new worktree because `_pages/about.md` contains the user's unstaged biography update that must be preserved.

## Chunk 1: Structure and Content

### Task 1: Add homepage source checks

**Files:**
- Create: `tests/test_homepage.py`
- Test: `_pages/about.md`

- [ ] **Step 1: Write failing source tests**

Add tests that assert:

```python
assert 'class="wiki-home"' in source
assert 'id="publications"' in source
assert source.count('class="publication-card') == 5
assert source.count('class="publication-row') == 12
assert 'Design inspired by' in source
assert 'https://linxins.net/' in source
```

Extract every `images/...` path from publication markup and assert that each file exists under the repository root. Assert that all 17 existing visible publication titles remain present.

- [ ] **Step 2: Run the test and verify failure**

Run: `python3 -m unittest tests/test_homepage.py -v`

Expected: FAIL because the new page structure and credit do not exist.

- [ ] **Step 3: Commit the failing test**

```bash
git add tests/test_homepage.py
git commit -m "test(homepage): define wiki redesign content contract"
```

### Task 2: Implement semantic homepage markup

**Files:**
- Modify: `_pages/about.md`
- Test: `tests/test_homepage.py`

- [ ] **Step 1: Replace the current presentation markup**

Keep the existing front matter and Google Scholar URL assignments. Replace the old heading, tab CSS, tab buttons, paper boxes, and tab JavaScript with:

```html
<div class="wiki-home">
  <header class="wiki-hero">...</header>
  <nav class="wiki-contents" aria-label="Page contents">...</nav>
  <section id="biography">...</section>
  <section id="research-interests">...</section>
  <section id="publications">...</section>
  <section id="education">...</section>
  <footer class="site-credit">...</footer>
</div>
```

Use the current biography text, existing portrait `images/head_2025_hq.png`, configuration-backed social/profile links, the five current primary-contribution papers as image cards, and the twelve current led projects as compact rows. Preserve every title, author list, badge, URL, image, and education entry.

- [ ] **Step 2: Add accessible details**

Provide meaningful image `alt` text, semantic headings, `aria-label` text for link groups, and visible keyboard focus targets. Do not set a global `<base target="_blank">`; external links open normally.

- [ ] **Step 3: Add source credit**

Add a subtle footer sentence linking to both <https://linxins.net/> and <https://github.com/LinxinS97/LinxinS97.github.io>.

- [ ] **Step 4: Run source tests**

Run: `python3 -m unittest tests/test_homepage.py -v`

Expected: publication/content tests pass; style/build checks may still fail until Chunk 2.

- [ ] **Step 5: Commit structure and content**

```bash
git add _pages/about.md
git commit -m "feat(homepage): restructure academic profile content"
```

## Chunk 2: Visual System and Responsive Layout

### Task 3: Add style contract tests

**Files:**
- Modify: `tests/test_homepage.py`
- Test: `_sass/_homepage.scss`
- Test: `assets/css/main.scss`

- [ ] **Step 1: Add failing style tests**

Assert that `_sass/_homepage.scss` exists, `assets/css/main.scss` imports `homepage`, and the partial contains desktop and mobile rules for `.wiki-infobox`, `.publication-grid`, `.publication-row`, `.wiki-contents`, and `:focus-visible`.

- [ ] **Step 2: Run tests and verify failure**

Run: `python3 -m unittest tests/test_homepage.py -v`

Expected: FAIL because the partial/import do not exist.

### Task 4: Implement the Wikipedia/editorial Sass partial

**Files:**
- Create: `_sass/_homepage.scss`
- Modify: `assets/css/main.scss`
- Test: `tests/test_homepage.py`

- [ ] **Step 1: Add scoped layout tokens and base skin**

Define page-scoped CSS custom properties for paper, canvas, ink, muted ink, rules, link blue, visited blue, and lead red. Hide the legacy masthead/sidebar only when the homepage body contains `.wiki-home`, expand the page container, and apply the serif editorial type stack.

- [ ] **Step 2: Style the hero, infobox, and contents navigation**

Implement a float-based infobox on wide screens, Wikipedia-style title rules, compact metadata rows, and a contents block with anchor links.

- [ ] **Step 3: Style both publication densities**

Use a two-column grid for five primary contribution cards. Use compact horizontal rows for twelve led projects. Give images stable aspect ratios, venue labels neutral borders, and the project-lead label a restrained red accent.

- [ ] **Step 4: Add responsive and accessibility rules**

At narrow widths, stack the infobox, collapse card grids to one column, shrink image columns, and allow long author/link text to wrap. Add `:focus-visible`, reduced-motion, and print rules.

- [ ] **Step 5: Import the partial and remove obsolete card styles**

Add `@import "homepage";` after page/sidebar imports. Remove the old `.paper-box` and `.badge` rules that no longer have consumers, keeping the global anchor-offset rule only if still needed.

- [ ] **Step 6: Run tests**

Run: `python3 -m unittest tests/test_homepage.py -v`

Expected: PASS for source and style contracts.

- [ ] **Step 7: Commit styles and tests**

```bash
git add _sass/_homepage.scss assets/css/main.scss tests/test_homepage.py
git commit -m "style(homepage): add responsive wiki editorial system"
```

## Chunk 3: Build and Browser Verification

### Task 5: Verify generated site

**Files:**
- Modify: `tests/test_homepage.py`
- Generated: `_site/index.html` (ignored)

- [ ] **Step 1: Add generated-output assertions**

When `_site/index.html` exists, assert it contains the title, all 17 paper titles, credit links, section anchors, and compiled homepage selectors.

- [ ] **Step 2: Build the site**

Run: `bundle exec jekyll build`

Expected: exit 0 and `_site/index.html` generated.

- [ ] **Step 3: Run the complete test suite**

Run: `python3 -m unittest tests/test_homepage.py -v`

Expected: all tests PASS.

- [ ] **Step 4: Run a local server**

Run: `bundle exec jekyll serve --host 127.0.0.1 --port 4000`

Expected: homepage available at `http://127.0.0.1:4000/`.

- [ ] **Step 5: Inspect desktop and mobile layouts**

Check approximately 1440×1000 and 390×844 viewports. Confirm that the infobox, contents navigation, publication images, long author lists, link wrapping, education rows, and credit are readable and do not overflow.

- [ ] **Step 6: Check repository-local links and images**

Verify every local `src`/`href` from the generated homepage resolves to an existing generated file and internal anchors resolve to an element ID.

- [ ] **Step 7: Review changes and commit verification updates**

```bash
git diff --check
git status --short
git add tests/test_homepage.py
git commit -m "test(homepage): verify generated academic profile"
```

Do not stage `.superpowers/` mockups. Preserve unrelated user changes.
