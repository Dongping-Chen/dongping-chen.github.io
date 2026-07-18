# Wiki Academic Homepage Design

## Objective

Restyle Dongping Chen's existing Jekyll homepage into a Wikipedia-inspired academic profile, based on the approved “Wiki × academic editorial page” direction. Preserve the current biography edit, all 17 visible publications in `_pages/about.md`, their existing links, and their repository images. Add an explicit visual credit to Linxin Song.

## Provenance

The current repository and Linxin Song's site share the AcadHomepage/Jekyll lineage. Linxin's public implementation is available at <https://github.com/LinxinS97/LinxinS97.github.io> and is itself forked from Jieyu Zhang's homepage. The finished page will include a footer credit linking to Linxin Song's homepage and source repository.

## Information Architecture

1. A Wikipedia-style page title and short research tagline.
2. A concise biography beside a structured infobox containing the existing portrait, institution, research fields, profile links, and contact information.
3. A compact contents navigation linking to Biography, Research Interests, Publications, and Education.
4. Research-interest tags derived from the current biography and commented research-interest copy.
5. Publications split using the current contribution model:
   - Five “Primary Contributions” entries use image-led editorial cards.
   - Twelve “Projects Led” entries use denser horizontal rows with smaller images, venue labels, links, and a project-lead marker.
6. The existing three education entries.
7. A quiet page credit: “Design inspired by Linxin Song,” with links to the site and public source.

News, Teaching, Internships, and Services are excluded from the first version because they are not active content in the current page.

## Visual Direction

- Use Wikipedia's neutral paper-gray palette, blue links, fine gray rules, serif editorial typography, and a compact infobox.
- Keep the site distinctive through a two-density publication layout rather than copying Linxin's plain bullet list.
- Keep project images because they provide fast visual recognition and already exist in the repository.
- Use subtle hover and focus states, not decorative animation.
- Collapse the infobox and publication grids cleanly on mobile.

## Technical Design

- Keep Jekyll, Kramdown, and the existing AcadHomepage theme.
- Keep publication content in `_pages/about.md`; no data migration or new JavaScript framework.
- Add a focused `_sass/_homepage.scss` partial and import it from `assets/css/main.scss`.
- Use semantic HTML sections and anchor links in `_pages/about.md`.
- Remove the old tab JavaScript because both publication groups will be visible and linkable.
- Retain the existing global scripts and Google Scholar integration even though the redesigned publication entries do not depend on it.

## Content and Failure Handling

- All publication links and image paths come from the current visible entries.
- Images receive descriptive `alt` text and fixed aspect-ratio containers; the layout remains usable if an image fails.
- External links are ordinary links and do not block rendering.
- Long author lists wrap naturally and remain readable on narrow screens.

## Verification

- Build with `bundle exec jekyll build`.
- Confirm all 17 visible publication titles and image assets are present in generated HTML.
- Check that internal section anchors and repository-local image paths resolve.
- Render the built page at desktop and mobile widths and inspect it visually.
- Preserve the pre-existing unstaged biography change while committing the implementation.
