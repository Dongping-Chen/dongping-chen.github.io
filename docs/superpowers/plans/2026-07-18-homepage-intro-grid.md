# Homepage Intro Grid Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Widen the homepage and replace the whitespace-producing contents/float layout with a compact intro grid whose infobox aligns with the hero title.

**Architecture:** Introduce a `wiki-intro` wrapper containing the hero, infobox, Biography, and Research Interests as explicit grid areas. Keep Publications and Education outside the wrapper so they span the full paper width and remain independent of portrait height.

**Tech Stack:** Jekyll, semantic HTML, Sass, Python `unittest`.

---

## Chunk 1: Regression Contract

### Task 1: Define the wider intro layout requirements

**Files:**
- Modify: `tests/test_homepage.py`

- [ ] Add source tests asserting `wiki-intro`, hero/infobox/biography/research source order, no `wiki-contents`, and no Occupation, Fields, or Citations facts.
- [ ] Add style tests asserting a `1380px` paper width, `wiki-intro` grid areas, a 310–330px infobox column, full-width Publications/Education, and a mobile single-column grid order.
- [ ] Run focused source/style tests and confirm failures are caused by the old contents/float layout.

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_homepage.HomepageSourceTests \
  tests.test_homepage.HomepageStyleTests -v
```

## Chunk 2: Intro Markup

### Task 2: Reorganize the homepage introduction

**Files:**
- Modify: `_pages/about.md`

- [ ] Remove the contents navigation.
- [ ] Add the `wiki-intro` wrapper.
- [ ] Make the hero, infobox, Biography, and Research Interests direct intro children in the approved order.
- [ ] Remove Occupation, Fields, and Citations from the infobox while retaining Chinese name, Institution, Websites, and Contact.
- [ ] Close the intro wrapper before Publications so Publications and Education remain full-width siblings.
- [ ] Preserve the current Research Interests copy, all publications, tabs, education entries, and credit.
- [ ] Run source tests and confirm they pass.

## Chunk 3: Grid and Responsive Styles

### Task 3: Replace the contents/float layout

**Files:**
- Modify: `_sass/_homepage.scss`

- [ ] Increase `#main` maximum width to `1380px`.
- [ ] Change `wiki-home` to a single flow column.
- [ ] Remove all `wiki-contents` styling.
- [ ] Define `wiki-intro` areas for hero, bio, research, and infobox with a flexible left column and a 320px right column.
- [ ] Remove the infobox float and give it the `info` grid area aligned to the top.
- [ ] Make ordinary `wiki-section` blocks full width and reset intro section spacing where needed.
- [ ] Add the mobile grid order: hero, infobox, biography, research.
- [ ] Run focused source/style tests and confirm they pass.

## Chunk 4: Build and Integration

### Task 4: Verify and commit

**Files:**
- Verify: `_site/index.html`
- Verify: `_site/assets/css/main.css`

- [ ] Build with Jekyll.
- [ ] Run all homepage tests.
- [ ] Confirm generated HTML omits the contents navigation and removed facts while preserving 20 publication rows and 2 tab panels.
- [ ] Confirm compiled CSS includes the 1380px canvas, desktop intro grid, and mobile grid order.
- [ ] Run `git diff --check` and restore any local Bundler platform noise.
- [ ] Commit as `feat(homepage): widen and compact intro layout`.

