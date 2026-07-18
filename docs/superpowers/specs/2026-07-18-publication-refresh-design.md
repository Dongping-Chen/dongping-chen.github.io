# Homepage Publication Refresh Design

## Goal

Refresh the homepage profile and publication presentation without changing the existing Wikipedia-inspired structure or the two-tab interaction. The update should make publication figures readable, add two recent works, correct publication grouping and venue metadata, and simplify repeated labels.

## Profile and Research Interests

- Remove the visible `Dongping Chen` heading from the right-hand infobox because the name already appears in the page hero.
- Keep the portrait, Chinese name, institution, websites, and contact facts unchanged.
- Give the two research-topic chips explicit semantic modifier classes:
  - `Multimodal Understanding and Generation`: pale blue background, blue-gray border, and darker blue text.
  - `Agentic AI`: pale red background, muted red border, and darker red text.
- Preserve the existing topic wording and responsive behavior.

## Publication Presentation

- Keep the existing `Main Contributions` and `Projects Led` accessible tabs.
- Do not add any total-publication count or group-count copy.
- Remove every visible red `Project lead` badge from Projects Led entries and remove the now-unused badge styling.
- Keep `‡ indicates project leaders` in the publication note because author-line project-lead markers remain on other led projects.
- Increase publication image width while preserving each image's natural aspect ratio:
  - Desktop: `360px` image column.
  - Tablet (`max-width: 680px`): `240px` image column.
  - Small mobile (`max-width: 450px`): stack image above text at full row width.
- Continue to use `height: auto`; do not crop, cap, or force a shared aspect ratio.

## Publication Content Changes

### Main Contributions

Add the following work near the top of the Main Contributions list:

- Title: `Sandboxed Coding Agents are Competitive Omni-modal Task Solvers`
- Venue: `Tech Report`
- Authors: Dongping Chen, Xuanao Huang, Zhihan Hu, Qingyuan Shi, Dianqi Li, Tianyi Zhou
- Image: `images/OmniCoding.png`
- PDF: `https://arxiv.org/pdf/2606.00579`
- GitHub: `https://github.com/Dongping-Chen/OmniCoding`

Move the existing work below from Projects Led into Main Contributions:

- `Wait, We Don't Need to "Wait"! Removing Thinking Tokens Improves Reasoning Efficiency`
- Preserve its venue, image, PDF, and resource text.
- Remove the `‡` marker after Dongping Chen's name.
- Ensure the paper appears exactly once.

### Projects Led

Update Paper2Web:

- Change its venue from `Tech Report` to `ACL 2026 Demo Track`.
- Preserve the existing image, authors, PDF, and GitHub links.

Add the following work after Paper2Web:

- Title: `Worldwide LiveVQA: Real-Time Visual Knowledge Seeking and Updating Across Languages`
- Venue: `ACL 2026 Findings`
- Authors: Xuanao Huang *, Xingjia Liu *, Yuyang Peng, Zetong Zhou, Yao Wan‡, Dongping Chen‡
- Image: `images/worldwide-livevqa.png`
- PDF: `https://aclanthology.org/2026.findings-acl.1984.pdf`

## Implementation Boundaries

- Continue using direct publication HTML in `_pages/about.md`; do not introduce a data layer or new dependency.
- Continue using the existing BEM-style SCSS in `_sass/_homepage.scss`.
- Preserve all unrelated publications, links, images, tab keyboard behavior, profile facts, and the Linxin Song credit.
- Treat `images/OmniCoding.png` and `images/worldwide-livevqa.png` as user-provided assets and add them without modifying their pixels.

## Verification

Update the existing Python homepage tests before production changes and verify the red-green cycle. Tests should cover:

- The infobox no longer renders the duplicate visible name.
- Research topic modifier classes and both pale color treatments exist.
- The two new publication titles, venues, image paths, authors, and primary links are present.
- Paper2Web uses `ACL 2026 Demo Track`.
- The Wait paper is inside Main Contributions, appears once, and has no `‡` marker on Dongping Chen.
- No `lead-label` markup or styling remains.
- Publication figures use `360px`, `240px`, and full-width mobile sizing while retaining natural height and no cropping.
- All publication images resolve in the built site.
- Jekyll builds successfully and the complete homepage test suite passes.

