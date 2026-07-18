import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABOUT = ROOT / "_pages" / "about.md"
HOMEPAGE_SCSS = ROOT / "_sass" / "_homepage.scss"
MAIN_SCSS = ROOT / "assets" / "css" / "main.scss"
DEFAULT_LAYOUT = ROOT / "_layouts" / "default.html"
SCHOLAR_STATS_INCLUDE = ROOT / "_includes" / "fetch_google_scholar_stats.html"
BUILT_INDEX = ROOT / "_site" / "index.html"
BUILT_CSS = ROOT / "_site" / "assets" / "css" / "main.css"

PUBLICATION_TITLES = (
    "Measuring Visual Generative Intelligence",
    "Interleaved Scene Graph for Interleaved Text-and-Image Generation Assessment",
    "GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents",
    "Toward an Honest and Helpful Large Language Model",
    "MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark",
    "LLM-as-a-Coauthor: The Challenges of Detecting LLM-Human Mixcase",
    "Paper2Web: Let's Make Your Paper Alive!",
    "Are We on the Right Way to Assessing LLM-as-a-Judge?",
    "Reinforced Visual Perception with Tools",
    "Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?",
    "code_transformed: The Influence of Large Language Models on Code",
    "Optimizing Length Compression in Large Reasoning Models",
    "Seeking and Updating with Live Visual Knowledge",
    "MultiRef: Controllable Image Generation with Multiple Visual References",
    'Wait, We Don\'t Need to "Wait"! Removing Thinking Tokens Improves Reasoning Efficiency',
    "Judge Anything: MLLM as a Judge Across Any Modality",
    "Wikipedia in the Era of LLMs: Evolution and Risks",
    "CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale",
    "nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow",
    "The Impact of Large Language Models in Academia: from Writing to Speaking",
)


class HomepageSourceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source = ABOUT.read_text(encoding="utf-8")

    def test_uses_semantic_wiki_homepage_structure(self):
        self.assertIn("author_profile: false", self.source)
        self.assertIn("body_class: wiki-home-page", self.source)
        self.assertIn('class="wiki-home"', self.source)
        for section_id in ("biography", "research-interests", "publications", "education"):
            self.assertIn(f'id="{section_id}"', self.source)
        self.assertNotIn('class="wiki-contents"', self.source)

    def test_intro_grid_orders_content_and_simplifies_infobox(self):
        self.assertIn('class="wiki-intro"', self.source)
        intro_index = self.source.index('class="wiki-intro"')
        hero_index = self.source.index('class="wiki-hero"', intro_index)
        infobox_index = self.source.index('class="wiki-infobox"', intro_index)
        biography_index = self.source.index('id="biography"', intro_index)
        research_index = self.source.index('id="research-interests"', intro_index)
        publications_index = self.source.index('id="publications"', intro_index)

        self.assertLess(hero_index, infobox_index)
        self.assertLess(infobox_index, biography_index)
        self.assertLess(biography_index, research_index)
        self.assertLess(research_index, publications_index)
        for removed_fact in ("Occupation", "Fields", "Citations"):
            with self.subTest(removed_fact=removed_fact):
                self.assertNotIn(f"<dt>{removed_fact}</dt>", self.source)
        for retained_fact in ("Chinese name", "Institution", "Websites", "Contact"):
            with self.subTest(retained_fact=retained_fact):
                self.assertIn(f"<dt>{retained_fact}</dt>", self.source)

    def test_preserves_all_visible_publications(self):
        for title in PUBLICATION_TITLES:
            with self.subTest(title=title):
                self.assertIn(title, self.source)

        self.assertNotIn('class="publication-card"', self.source)
        self.assertEqual(20, self.source.count('<article class="publication-row">'))

        for venue in ("CVPR 2026 Findings", "EACL 2026", "KDD 2025 D&amp;B Oral", "TMLR"):
            with self.subTest(venue=venue):
                self.assertIn(venue, self.source)

    def test_publication_images_exist(self):
        image_paths = re.findall(
            r'<(?:article)[^>]+class="publication-(?:card|row)[^"]*"[\s\S]*?<img[^>]+src=["\']([^"\']+)',
            self.source,
        )
        self.assertEqual(20, len(image_paths))
        for image_path in image_paths:
            with self.subTest(image=image_path):
                self.assertTrue((ROOT / image_path).is_file(), image_path)

    def test_publications_use_accessible_progressive_tabs(self):
        self.assertIn('class="publication-tabs" role="tablist"', self.source)
        self.assertIn('id="publication-tab-contributions"', self.source)
        self.assertIn('aria-controls="publication-panel-contributions"', self.source)
        self.assertIn('aria-selected="true"', self.source)
        self.assertIn('id="publication-tab-led"', self.source)
        self.assertIn('aria-controls="publication-panel-led"', self.source)
        self.assertIn('aria-selected="false"', self.source)
        self.assertIn('id="publication-panel-contributions"', self.source)
        self.assertIn('aria-labelledby="publication-tab-contributions"', self.source)
        self.assertIn('id="publication-panel-led"', self.source)
        self.assertIn('aria-labelledby="publication-tab-led"', self.source)
        self.assertNotRegex(self.source, r'<section[^>]+role="tabpanel"[^>]+hidden')
        for script_token in (
            "publication-tabs--enhanced",
            "aria-selected",
            "ArrowLeft",
            "ArrowRight",
            "Home",
            "End",
        ):
            with self.subTest(script_token=script_token):
                self.assertIn(script_token, self.source)

    def test_removes_publication_group_microcopy(self):
        for removed_copy in (
            "20 selected works",
            "Six representative works with substantial direct contribution.",
            "Fourteen projects organized as a compact, scannable research index.",
            "publication-group__index",
        ):
            with self.subTest(removed_copy=removed_copy):
                self.assertNotIn(removed_copy, self.source)

    def test_credits_linxin_song_and_source(self):
        self.assertIn("Design inspired by", self.source)
        self.assertIn("https://linxins.net/", self.source)
        self.assertIn("https://github.com/LinxinS97/LinxinS97.github.io", self.source)

    def test_keeps_matching_publication_links(self):
        self.assertIn(
            'href="https://arxiv.org/pdf/2503.02879">Wikipedia in the Era of LLMs: Evolution and Risks',
            self.source,
        )
        self.assertEqual(1, self.source.count("https://gui-world.github.io"))

    def test_scholar_stats_tolerate_homepage_without_citation_field(self):
        scholar_script = SCHOLAR_STATS_INCLUDE.read_text(encoding="utf-8")
        self.assertIn("if (totalCitationElement)", scholar_script)


class HomepageStyleTests(unittest.TestCase):
    def test_imports_dedicated_homepage_styles(self):
        self.assertTrue(HOMEPAGE_SCSS.is_file())
        self.assertIn('@import "homepage";', MAIN_SCSS.read_text(encoding="utf-8"))

    def test_styles_core_layout_and_accessibility_states(self):
        self.assertTrue(HOMEPAGE_SCSS.is_file())
        styles = HOMEPAGE_SCSS.read_text(encoding="utf-8")
        for selector in (
            ".wiki-infobox",
            ".wiki-intro",
            ".publication-tabs",
            ".publication-row",
            ":focus-visible",
            "@media (max-width:",
            "@media print",
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, styles)

    def test_widens_canvas_and_uses_intro_grid_areas(self):
        styles = HOMEPAGE_SCSS.read_text(encoding="utf-8")
        self.assertIn("max-width: 1380px;", styles)
        self.assertIn("grid-template-columns: minmax(0, 1fr) 320px;", styles)
        self.assertIn("margin: 1.45rem 0 0;", styles)
        for area in ('"hero info"', '"bio info"', '"research info"'):
            with self.subTest(area=area):
                self.assertIn(area, styles)
        for mobile_area in ('"hero"', '"info"', '"bio"', '"research"'):
            with self.subTest(mobile_area=mobile_area):
                self.assertIn(mobile_area, styles)
        self.assertNotIn(".wiki-contents", styles)

    def test_publication_images_keep_natural_ratio_and_reference_typography(self):
        styles = HOMEPAGE_SCSS.read_text(encoding="utf-8")
        self.assertIn('--wiki-sans: "Trebuchet MS", Helvetica, sans-serif;', styles)
        media_selector = r"(?:\.publication-row__media|&__media)"
        self.assertRegex(styles, media_selector + r"[\s\S]{0,500}height:\s*auto")
        self.assertNotRegex(styles, media_selector + r"\s*\{[^}]*aspect-ratio")
        self.assertNotRegex(styles, media_selector + r"[\s\S]{0,500}object-fit:\s*cover")
        self.assertIn(".publication-tabs--enhanced", styles)

    def test_homepage_layout_uses_explicit_body_class_without_has_dependency(self):
        layout = DEFAULT_LAYOUT.read_text(encoding="utf-8")
        styles = HOMEPAGE_SCSS.read_text(encoding="utf-8")
        self.assertIn('class="{{ page.body_class | default: \'\' }}"', layout)
        self.assertIn("body.wiki-home-page", styles)
        self.assertNotIn("body:has(.wiki-home)", styles)


class WikiContentParser(HTMLParser):
    VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.ids = set()
        self.local_paths = set()
        self.element_stack = []
        self.parent_classes = {}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        classes = attributes.get("class", "").split()
        if "wiki-home" in classes:
            self.depth = 1
        elif self.depth and tag not in self.VOID_ELEMENTS:
            self.depth += 1

        if not self.depth:
            return

        if attributes.get("id"):
            self.ids.add(attributes["id"])
            self.parent_classes[attributes["id"]] = set(self.element_stack[-1][1]) if self.element_stack else set()

        for attribute in ("src", "href"):
            value = attributes.get(attribute, "")
            if value and not value.startswith(("http://", "https://", "mailto:", "#")):
                self.local_paths.add(value.split("?", 1)[0].lstrip("/"))

        if tag not in self.VOID_ELEMENTS:
            self.element_stack.append((tag, classes))

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1
            self.element_stack.pop()

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


class HomepageBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = BUILT_INDEX.read_text(encoding="utf-8")
        cls.css = BUILT_CSS.read_text(encoding="utf-8")

    def test_generated_homepage_contains_complete_content(self):
        self.assertIn("Dongping Chen", self.html)
        self.assertIn('<body class="wiki-home-page">', self.html)
        self.assertNotIn('class="sidebar', self.html)
        for title in PUBLICATION_TITLES:
            with self.subTest(title=title):
                self.assertIn(title, self.html)
        self.assertIn("https://linxins.net/", self.html)
        self.assertIn("https://github.com/LinxinS97/LinxinS97.github.io", self.html)
        self.assertIn('role="tablist"', self.html)
        self.assertEqual(2, self.html.count('role="tabpanel"'))
        self.assertNotIn('class="wiki-contents"', self.html)
        for removed_fact in ("Occupation", "Fields", "Citations"):
            self.assertNotIn(f"<dt>{removed_fact}</dt>", self.html)

    def test_generated_homepage_has_sections_and_resolvable_local_assets(self):
        parser = WikiContentParser()
        parser.feed(self.html)
        self.assertTrue({"biography", "research-interests", "publications", "education"} <= parser.ids)
        self.assertIn("wiki-intro", parser.parent_classes["biography"])
        self.assertIn("wiki-intro", parser.parent_classes["research-interests"])
        self.assertIn("wiki-home", parser.parent_classes["publications"])
        self.assertIn("wiki-home", parser.parent_classes["education"])
        for local_path in parser.local_paths:
            with self.subTest(path=local_path):
                self.assertTrue((ROOT / "_site" / local_path).is_file(), local_path)

    def test_compiled_css_contains_homepage_system(self):
        self.assertIn(".wiki-home", self.css)
        self.assertIn(".publication-tabs", self.css)
        self.assertIn(".publication-row", self.css)
        self.assertRegex(self.css, r"\.publication-row__media img\{[^}]*height:auto")
        self.assertNotRegex(
            self.css,
            r"\.publication-row__media(?: img)?\{[^}]*(?:aspect-ratio|object-fit|max-height)",
        )
        self.assertIn("max-width:1380px", self.css)
        self.assertIn("grid-template-columns:minmax(0, 1fr) 320px", self.css)


if __name__ == "__main__":
    unittest.main()
