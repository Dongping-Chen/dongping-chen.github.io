# Homepage Intro Grid Design

## Objective

Remove the excessive whitespace in the homepage introduction and make the page feel substantially wider, while keeping the existing Wikipedia-inspired visual language and publication tabs.

## Approved Layout

Use a dedicated two-column intro grid at desktop widths:

- The left column contains the hero, Biography, and Research Interests.
- The right column contains the profile infobox.
- The infobox top aligns with the `Dongping Chen` hero title area rather than the Biography text.
- Publications and Education sit below the intro grid and span the complete content width.

This structure prevents the portrait from stretching the Biography section and delaying all following sections.

## Width and Spacing

- Increase the homepage paper width from `1180px` to approximately `1380px`.
- Remove the table of contents and its dedicated 164px column.
- Use a flexible main column and an approximately 310–330px infobox column.
- Keep a restrained desktop gutter between the two columns.

## Infobox Content

Keep:

- Chinese name
- Institution
- Websites
- Contact

Remove:

- Occupation
- Fields
- Citations

The portrait remains uncropped from the existing approved presentation unless responsive constraints require scaling.

## Responsive Behavior

At narrow widths, use the following document order:

1. Hero
2. Infobox
3. Biography
4. Research Interests
5. Publications
6. Education

The infobox becomes full-width up to a sensible maximum, and all lower sections remain single-column.

## Technical Design

- Update `_pages/about.md` to remove the contents navigation, move the infobox out of the Biography section, and wrap the hero, infobox, Biography, and Research Interests in a `wiki-intro` grid.
- Update `_sass/_homepage.scss` to replace the global contents/main grid with explicit `wiki-intro` areas.
- Preserve the current publication tab behavior and all twenty publication entries.
- Preserve the user's current uncommitted Research Interests copy.
- Extend `tests/test_homepage.py` to assert the new source order, removed fields, absence of the contents navigation, wider canvas, desktop grid areas, and mobile order.

## Verification

- Use a red-green regression cycle for source and style requirements.
- Build with Jekyll.
- Confirm all twenty publications and both tab panels remain in generated HTML.
- Confirm the generated homepage omits the contents navigation and removed infobox rows.
- Confirm compiled CSS contains the desktop intro grid and mobile single-column layout.

