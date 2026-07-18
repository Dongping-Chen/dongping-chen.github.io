# Homepage Publication Tabs Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Match the homepage typography more closely to Linxin Song's site and present all twenty publications in two accessible tabs with uncropped, equal-width images.

**Architecture:** Keep the existing Jekyll page and Sass partial. Normalize both publication groups to a shared horizontal row component, add progressive-enhancement tab behavior directly to the page, and encode the visual requirements in the existing Python build tests.

**Tech Stack:** Jekyll, Liquid/Kramdown HTML, Sass, vanilla JavaScript, Python `unittest`.

---

## Chunk 1: Regression Contract

### Task 1: Specify tab, typography, and image behavior

**Files:**
- Modify: `tests/test_homepage.py`

- [ ] **Step 1: Write failing source tests**

Add assertions that the page contains two tab buttons and panels with the appropriate ARIA relationships, all six contribution entries use the shared row class, explanatory group microcopy is absent, and a progressive-enhancement script marks the tab container as enabled.

- [ ] **Step 2: Write failing style tests**

Assert that `_sass/_homepage.scss` defines Trebuchet-based homepage typography, shared publication rows, `height: auto` for publication images, tab focus/selected states, and no fixed publication aspect ratio or `object-fit: cover`.

- [ ] **Step 3: Run focused tests and confirm red state**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_homepage.HomepageSourceTests \
  tests.test_homepage.HomepageStyleTests -v
```

Expected: new tab, typography, and image assertions fail against the current implementation.

## Chunk 2: Page Structure and Behavior

### Task 2: Convert publication groups into accessible tabs

**Files:**
- Modify: `_pages/about.md`

- [ ] **Step 1: Simplify the Publications heading**

Remove the selected-work count, numbered group labels, and both group-description paragraphs. Keep the contribution marker note.

- [ ] **Step 2: Add the tab list**

Create `Main Contributions` and `Projects Led` buttons with `role="tab"`, stable IDs, `aria-controls`, and correct initial `aria-selected`/`tabindex` values.

- [ ] **Step 3: Add tab panels**

Wrap the six contribution entries and fourteen led-project entries in labelled `role="tabpanel"` containers. Keep Contributions selected by default.

- [ ] **Step 4: Normalize publication markup**

Convert contribution cards to the same horizontal `publication-row` structure as the led projects while preserving all titles, authors, links, images, venues, and alt text.

- [ ] **Step 5: Add progressive enhancement**

Add a small self-contained script that:

- applies an enabled class only after JavaScript starts;
- hides the inactive panel;
- switches on click, Left/Right, Home, and End;
- maintains `aria-selected`, `tabindex`, and focus;
- leaves both panels visible when JavaScript is unavailable.

- [ ] **Step 6: Run source tests**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_homepage.HomepageSourceTests -v
```

Expected: source tests pass.

## Chunk 3: Visual System

### Task 3: Match reference typography and preserve image ratios

**Files:**
- Modify: `_sass/_homepage.scss`

- [ ] **Step 1: Update typography**

Use `"Trebuchet MS", Helvetica, sans-serif` for the homepage, headings, publication titles, navigation, and infobox. Set a compact 14–15px base size and reference-like line height.

- [ ] **Step 2: Style the tab controls**

Use a compact bottom-rule tab bar with clear selected, hover, and `:focus-visible` states. Ensure buttons inherit the homepage typeface.

- [ ] **Step 3: Unify paper rows**

Use one horizontal grid for both panels with an equal-width image column and flexible text column. Remove the contribution card grid, fixed aspect-ratio media containers, hover zoom, cropping, and special odd-card behavior.

- [ ] **Step 4: Preserve natural image dimensions**

Set publication images to `display: block`, `width: 100%`, and `height: auto`. Keep the media wrapper free of clipping and fixed heights.

- [ ] **Step 5: Refine responsive behavior**

At tablet/mobile widths, reduce the image-column width; at phone width, stack image above text. Do not reintroduce fixed heights or crop rules.

- [ ] **Step 6: Run focused source and style tests**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_homepage.HomepageSourceTests \
  tests.test_homepage.HomepageStyleTests -v
```

Expected: all focused tests pass.

## Chunk 4: Build Verification

### Task 4: Verify generated site and commit

**Files:**
- Verify: `_site/index.html`
- Verify: `_site/assets/css/main.css`
- Modify if necessary: `tests/test_homepage.py`

- [ ] **Step 1: Build the Jekyll site**

Run:

```bash
BUNDLE_PATH=/tmp/wiki-homepage-cleanup.f1q5co/vendor/bundle \
  /Users/cdp/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Expected: build exits zero.

- [ ] **Step 2: Run all homepage tests**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_homepage.py -v
```

Expected: all tests pass with zero failures.

- [ ] **Step 3: Inspect generated artifacts**

Confirm `_site/index.html` contains both tab panels, all twenty publication images and titles, and the tab script. Confirm compiled CSS uses natural-height publication images and no publication crop rules.

- [ ] **Step 4: Check the diff**

Run:

```bash
git diff --check
git status --short
```

Restore any platform-only `Gemfile.lock` changes produced by the local build.

- [ ] **Step 5: Commit the implementation**

```bash
git add _pages/about.md _sass/_homepage.scss tests/test_homepage.py
git commit -m "feat(homepage): add uncropped publication tabs"
```

