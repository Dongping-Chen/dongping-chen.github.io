# Homepage Publication Refresh Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refresh the homepage profile and research chips, add and regroup recent publications, and enlarge uncropped publication figures responsively.

**Architecture:** Keep the current direct HTML publication rows in `_pages/about.md`, the existing BEM-style rules in `_sass/_homepage.scss`, and the existing Python source/build tests. Add the two user-provided PNG assets without pixel changes; do not add a data layer, dependency, publication count, or new interaction.

**Tech Stack:** Jekyll, Liquid/HTML, SCSS, vanilla JavaScript tabs, Python `unittest`.

---

## Chunk 1: Content, Styling, and Verification

### Task 1: Add Failing Homepage Content Tests

**Files:**
- Modify: `tests/test_homepage.py`
- Reference: `docs/superpowers/specs/2026-07-18-publication-refresh-design.md`

- [ ] **Step 1: Extend the publication title fixture**

Add both titles to `PUBLICATION_TITLES`:

```python
"Sandboxed Coding Agents are Competitive Omni-modal Task Solvers",
"Worldwide LiveVQA: Real-Time Visual Knowledge Seeking and Updating Across Languages",
```

Replace hard-coded publication/image totals with `len(PUBLICATION_TITLES)` so the test checks completeness without adding any visible page count.

- [ ] **Step 2: Add an article extraction helper**

Add a source-only helper that returns the `<article class="publication-row">...</article>` block containing a title:

```python
def publication_article(source, title):
    title_index = source.index(title)
    article_start = source.rindex('<article class="publication-row">', 0, title_index)
    article_end = source.index("</article>", title_index) + len("</article>")
    return source[article_start:article_end]
```

- [ ] **Step 3: Test profile and research-chip requirements**

Add a source test asserting:

```python
self.assertNotIn('class="wiki-infobox__name"', self.source)
self.assertIn('class="research-topic research-topic--multimodal"', self.source)
self.assertIn('class="research-topic research-topic--agentic"', self.source)
self.assertNotIn('class="lead-label"', self.source)
self.assertNotRegex(self.source, r"\b\d+\s+selected works\b")
self.assertNotIn("publication-count", self.source)
```

- [ ] **Step 4: Test new metadata and exact tab placement**

Slice the two tab panels at their IDs and assert:

```python
main_start = self.source.index('id="publication-panel-contributions"')
led_start = self.source.index('id="publication-panel-led"')
main_panel = self.source[main_start:led_start]
led_panel = self.source[led_start:]

self.assertIn("Sandboxed Coding Agents are Competitive Omni-modal Task Solvers", main_panel)
self.assertIn('images/OmniCoding.png', main_panel)
self.assertIn('https://arxiv.org/pdf/2606.00579', main_panel)
self.assertIn('https://github.com/Dongping-Chen/OmniCoding', main_panel)
self.assertIn('Wait, We Don\'t Need to "Wait"!', main_panel)
self.assertNotIn('Wait, We Don\'t Need to "Wait"!', led_panel)
self.assertIn("Worldwide LiveVQA: Real-Time Visual Knowledge Seeking and Updating Across Languages", led_panel)
self.assertIn('images/worldwide-livevqa.png', led_panel)
self.assertIn('https://aclanthology.org/2026.findings-acl.1984.pdf', led_panel)
self.assertIn('ACL 2026 Demo Track', publication_article(self.source, "Paper2Web"))
self.assertIn('ACL 2026 Findings', publication_article(self.source, "Worldwide LiveVQA"))
self.assertEqual(1, self.source.count('Wait, We Don\'t Need to "Wait"!'))
```

Extract the two new article blocks and assert the exact approved author markup and order:

```python
omnicoding_article = publication_article(
    self.source,
    "Sandboxed Coding Agents are Competitive Omni-modal Task Solvers",
)
worldwide_article = publication_article(self.source, "Worldwide LiveVQA")

self.assertIn(
    '<p class="publication-authors"><strong class="author-me">Dongping Chen</strong>, '
    'Xuanao Huang, Zhihan Hu, Qingyuan Shi, Dianqi Li, Tianyi Zhou</p>',
    omnicoding_article,
)
self.assertIn(
    '<p class="publication-authors">Xuanao Huang *, Xingjia Liu *, Zetong Zhou, Yuyang Peng, '
    'Yao Wan‡, <strong class="author-me">Dongping Chen</strong>‡</p>',
    worldwide_article,
)
```

Also assert the OmniCoding article contains `Tech Report`, both new images have the approved descriptive `alt` text, and the Wait article contains `<strong class="author-me">Dongping Chen</strong>` without an immediately following `‡`.

- [ ] **Step 5: Run focused tests and verify RED**

Run:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_homepage.HomepageSourceTests.test_refreshes_profile_and_research_topics \
  tests.test_homepage.HomepageSourceTests.test_adds_and_regroups_recent_publications -v
```

Expected: FAIL because the duplicate infobox name, old chips, old Paper2Web venue, old Wait placement, lead badges, and missing publications remain.

- [ ] **Step 6: Commit the failing tests**

```bash
git add tests/test_homepage.py
git commit -m "test(homepage): cover publication refresh"
```

### Task 2: Implement Profile and Publication Content

**Files:**
- Modify: `_pages/about.md`
- Add: `images/OmniCoding.png`
- Add: `images/worldwide-livevqa.png`
- Test: `tests/test_homepage.py`

- [ ] **Step 1: Copy the approved binary assets into the worktree**

Copy, do not transform, the user-owned files from the main checkout:

```bash
cp /Users/cdp/Downloads/dongping-chen.github.io/images/OmniCoding.png images/OmniCoding.png
cp /Users/cdp/Downloads/dongping-chen.github.io/images/worldwide-livevqa.png images/worldwide-livevqa.png
```

Verify byte identity:

```bash
shasum /Users/cdp/Downloads/dongping-chen.github.io/images/OmniCoding.png images/OmniCoding.png
shasum /Users/cdp/Downloads/dongping-chen.github.io/images/worldwide-livevqa.png images/worldwide-livevqa.png
```

Expected: each source/destination pair has matching hashes.

- [ ] **Step 2: Simplify the profile and identify the research topics**

In `_pages/about.md`:

- Delete `<div class="wiki-infobox__name">Dongping Chen</div>`.
- Change the research items to:

```html
<li class="research-topic research-topic--multimodal">Multimodal Understanding and Generation</li>
<li class="research-topic research-topic--agentic">Agentic AI</li>
```

- [ ] **Step 3: Add OmniCoding to Main Contributions**

Insert a new first publication row with:

- `images/OmniCoding.png`
- Alt: `Sandboxed coding agents for omni-modal tasks overview`
- Venue: `Tech Report`
- Title/PDF: `https://arxiv.org/pdf/2606.00579`
- Authors: Dongping Chen, Xuanao Huang, Zhihan Hu, Qingyuan Shi, Dianqi Li, Tianyi Zhou
- GitHub: `https://github.com/Dongping-Chen/OmniCoding`

Highlight Dongping Chen using the existing `author-me` class and do not invent contribution markers.

- [ ] **Step 4: Move the Wait paper into Main Contributions**

Move its complete article block from Projects Led into Main Contributions after the 2026 entries and before the existing ICLR 2025 entries. Preserve its venue, image, PDF, and `Code coming soon` text. Change Dongping's author markup to:

```html
<strong class="author-me">Dongping Chen</strong>,
```

Ensure the title occurs exactly once.

- [ ] **Step 5: Refresh Projects Led**

- Change Paper2Web's venue label to `ACL 2026 Demo Track`.
- Add Worldwide LiveVQA immediately after Paper2Web with:
  - `images/worldwide-livevqa.png`
  - Alt: `Worldwide LiveVQA multilingual visual knowledge preview`
  - Venue: `ACL 2026 Findings`
  - Title/PDF: `https://aclanthology.org/2026.findings-acl.1984.pdf`
  - Authors: Xuanao Huang *, Xingjia Liu *, Zetong Zhou, Yuyang Peng, Yao Wan‡, Dongping Chen‡
- Remove every `<span class="lead-label">Project lead</span>` from the Projects Led panel.
- Keep author-line `‡` markers on led projects other than Wait.

- [ ] **Step 6: Run focused content tests and verify GREEN**

Run the two focused tests from Task 1.

Expected: PASS.

- [ ] **Step 7: Run all source tests**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests.test_homepage.HomepageSourceTests -v
```

Expected: PASS with all titles and local image files present.

- [ ] **Step 8: Commit content and assets**

```bash
git add _pages/about.md images/OmniCoding.png images/worldwide-livevqa.png
git commit -m "content(homepage): refresh recent publications"
```

### Task 3: Add Topic Colors and Enlarge Publication Figures

**Files:**
- Modify: `tests/test_homepage.py`
- Modify: `_sass/_homepage.scss`

- [ ] **Step 1: Add failing style assertions**

Add tests requiring:

```python
self.assertRegex(
    styles,
    r"\.research-topic--multimodal\s*\{[^}]*color:\s*#315f88;"
    r"[^}]*background:\s*#eef6ff;[^}]*border-color:\s*#a9c7e8;",
)
self.assertRegex(
    styles,
    r"\.research-topic--agentic\s*\{[^}]*color:\s*#93463f;"
    r"[^}]*background:\s*#fff1ef;[^}]*border-color:\s*#e3b4ae;",
)

tablet_start = styles.index("@media (max-width: 680px)")
mobile_start = styles.index("@media (max-width: 450px)")
desktop_styles = styles[:tablet_start]
tablet_styles = styles[tablet_start:mobile_start]
mobile_styles = styles[mobile_start:]

self.assertIn("grid-template-columns: 360px minmax(0, 1fr);", desktop_styles)
self.assertIn("width: 360px;", desktop_styles)
self.assertIn("grid-template-columns: 240px minmax(0, 1fr);", tablet_styles)
self.assertIn("width: 240px;", tablet_styles)
self.assertIn("grid-template-columns: 1fr;", mobile_styles)
self.assertIn("width: 100%;", mobile_styles)
self.assertNotIn(".lead-label", styles)
self.assertNotIn("--wiki-lead", styles)
```

Keep the existing natural-height/no-cropping assertions.

- [ ] **Step 2: Run the focused style test and verify RED**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_homepage.HomepageStyleTests.test_styles_research_topics_and_larger_publication_media -v
```

Expected: FAIL because the modifier colors and new widths do not exist and lead-label styling remains.

- [ ] **Step 3: Implement the approved research-topic colors**

Keep shared chip geometry under `.research-topic` and add explicit modifiers:

```scss
.research-topic--multimodal {
  color: #315f88;
  background: #eef6ff;
  border-color: #a9c7e8;
}

.research-topic--agentic {
  color: #93463f;
  background: #fff1ef;
  border-color: #e3b4ae;
}
```

- [ ] **Step 4: Remove obsolete lead-badge styles**

Delete `--wiki-lead`, `.lead-label` from the shared label selector, and the standalone `.lead-label` rule.

- [ ] **Step 5: Implement responsive natural-ratio figure widths**

Set desktop publication rows to:

```scss
grid-template-columns: 360px minmax(0, 1fr);

&__media {
  width: 360px;
}
```

At `max-width: 680px`, set `240px` for both the grid column and media width. Preserve the existing `max-width: 450px` stacked layout and `width: 100%`. Do not add `aspect-ratio`, `object-fit`, `max-height`, or a fixed image height.

- [ ] **Step 6: Run the focused style test and verify GREEN**

Run the focused style test from Step 2.

Expected: PASS.

- [ ] **Step 7: Run the full source/style suite**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest \
  tests.test_homepage.HomepageSourceTests \
  tests.test_homepage.HomepageStyleTests -v
```

Expected: PASS.

- [ ] **Step 8: Commit the style change and tests**

```bash
git add _sass/_homepage.scss tests/test_homepage.py
git commit -m "style(homepage): enlarge publication figures"
```

### Task 4: Build, Review, and Integrate

**Files:**
- Verify: `_site/index.html`
- Verify: `_site/assets/css/main.css`
- Verify: all changed source and asset files

- [ ] **Step 1: Build the Jekyll site**

```bash
BUNDLE_PATH=/tmp/wiki-homepage-cleanup.f1q5co/vendor/bundle \
  /Users/cdp/.gem/ruby/2.6.0/bin/bundle exec jekyll build
```

Expected: exit 0. Restore any Bundler-only `Gemfile.lock` platform rewrite before committing or merging.

- [ ] **Step 2: Run the complete homepage suite**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest tests/test_homepage.py -v
```

Expected: all tests pass with zero failures.

- [ ] **Step 3: Run repository hygiene checks**

```bash
git diff --check
git status --short
```

Expected: no whitespace errors and no unintended files.

- [ ] **Step 4: Request code review**

Dispatch a reviewer against the design spec and branch diff. Fix all Critical and Important findings, then rerun build and tests.

- [ ] **Step 5: Complete the branch workflow**

Use `superpowers:finishing-a-development-branch`. The user's established preference is local merge to `main`; fast-forward merge when possible, rebuild and rerun the complete suite on merged `main`, then remove the temporary worktree and feature branch.
