# Homepage Publication Tabs Design

## Objective

Refine the Wikipedia-inspired academic homepage so its typography and publication presentation feel closer to Linxin Song's site while accommodating twenty projects with differently proportioned images.

## Approved Direction

Use a reference-faithful, compact academic layout with two publication tabs. The homepage keeps its existing biography, infobox, contents navigation, education section, twenty publications, and Linxin Song credit.

## Typography

- Use the same practical sans-serif direction as the reference: `"Trebuchet MS", Helvetica, sans-serif`.
- Keep the base text compact at approximately 14–15px with a 1.5–1.6 line height.
- Use the same family for headings so the page feels cohesive rather than editorially mixed.
- Retain the restrained Wikipedia colors, rules, and blue links.

## Publication Navigation

- Replace the simultaneously visible publication groups with two accessible tabs:
  - `Main Contributions`, selected by default.
  - `Projects Led`.
- Clicking a tab switches content without navigation or reload.
- Tabs use buttons with `role="tab"`, `aria-selected`, `aria-controls`, and keyboard navigation.
- With JavaScript unavailable, both panels remain visible so publication content is never lost.

## Publication Layout

- Use the same horizontal paper-row structure in both tabs.
- Give every image column the same width, but do not force a shared height.
- Render images with `width: 100%` and `height: auto`; do not use `object-fit: cover`, fixed aspect ratios, clipping, or cropping.
- Allow each row to grow according to the source image's natural aspect ratio.
- Keep venue badges close to the image while ensuring the full image remains visible.
- On narrow screens, stack the image above the text and preserve its natural ratio.

## Content Simplification

- Remove group-description copy such as “Six representative works with substantial direct contribution.”
- Remove publication count copy such as “20 selected works.”
- Remove numbered group labels and unnecessary visual prose.
- Keep only the Publications heading, contribution marker note, tab controls, and publication entries.

## Technical Design

- Keep publication content in `_pages/about.md`.
- Add a small progressive-enhancement script in the page for tab behavior.
- Update `_sass/_homepage.scss` rather than introducing another style layer.
- Reuse existing publication classes where practical, but normalize both groups to one row pattern.
- Extend `tests/test_homepage.py` to cover tab accessibility, the no-JavaScript fallback, natural-ratio image styles, all twenty publications, and the removal of explanatory microcopy.

## Verification

- Run the homepage unit tests through a red-green cycle.
- Build the site with Jekyll.
- Confirm the generated homepage contains both tab panels, all twenty titles and images, and the tab script.
- Confirm compiled CSS has natural-ratio image rules and contains no publication image cropping rules.
- Check local asset resolution and mobile layout rules.

