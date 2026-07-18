import re
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABOUT = ROOT / "_pages" / "about.md"
HOMEPAGE_SCSS = ROOT / "_sass" / "_homepage.scss"
MAIN_SCSS = ROOT / "assets" / "css" / "main.scss"
BUILT_INDEX = ROOT / "_site" / "index.html"
BUILT_CSS = ROOT / "_site" / "assets" / "css" / "main.css"

PUBLICATION_TITLES = (
    "Interleaved Scene Graph for Interleaved Text-and-Image Generation Assessment",
    "GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents",
    "Toward an Honest and Helpful Large Language Model",
    "MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark",
    "LLM-as-a-Coauthor: The Challenges of Detecting LLM-Human Mixcase",
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
        self.assertIn('class="wiki-home"', self.source)
        for section_id in ("biography", "research-interests", "publications", "education"):
            self.assertIn(f'id="{section_id}"', self.source)
            self.assertIn(f'href="#{section_id}" target="_self"', self.source)

    def test_preserves_all_visible_publications(self):
        for title in PUBLICATION_TITLES:
            with self.subTest(title=title):
                self.assertIn(title, self.source)

        self.assertEqual(5, self.source.count('<article class="publication-card">'))
        self.assertEqual(12, self.source.count('<article class="publication-row">'))

    def test_publication_images_exist(self):
        image_paths = re.findall(
            r'<(?:article)[^>]+class="publication-(?:card|row)[^"]*"[\s\S]*?<img[^>]+src=["\']([^"\']+)',
            self.source,
        )
        self.assertEqual(17, len(image_paths))
        for image_path in image_paths:
            with self.subTest(image=image_path):
                self.assertTrue((ROOT / image_path).is_file(), image_path)

    def test_credits_linxin_song_and_source(self):
        self.assertIn("Design inspired by", self.source)
        self.assertIn("https://linxins.net/", self.source)
        self.assertIn("https://github.com/LinxinS97/LinxinS97.github.io", self.source)

    def test_keeps_scholar_stats_target_and_matching_publication_links(self):
        self.assertIn('id="total_cit"', self.source)
        self.assertIn(
            'href="https://arxiv.org/pdf/2503.02879">Wikipedia in the Era of LLMs: Evolution and Risks',
            self.source,
        )
        self.assertEqual(1, self.source.count("https://gui-world.github.io"))


class HomepageStyleTests(unittest.TestCase):
    def test_imports_dedicated_homepage_styles(self):
        self.assertTrue(HOMEPAGE_SCSS.is_file())
        self.assertIn('@import "homepage";', MAIN_SCSS.read_text(encoding="utf-8"))

    def test_styles_core_layout_and_accessibility_states(self):
        self.assertTrue(HOMEPAGE_SCSS.is_file())
        styles = HOMEPAGE_SCSS.read_text(encoding="utf-8")
        for selector in (
            ".wiki-infobox",
            ".wiki-contents",
            ".publication-grid",
            ".publication-row",
            ":focus-visible",
            "@media (max-width:",
            "@media print",
        ):
            with self.subTest(selector=selector):
                self.assertIn(selector, styles)


class WikiContentParser(HTMLParser):
    VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.ids = set()
        self.local_paths = set()

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

        for attribute in ("src", "href"):
            value = attributes.get(attribute, "")
            if value and not value.startswith(("http://", "https://", "mailto:", "#")):
                self.local_paths.add(value.split("?", 1)[0].lstrip("/"))

    def handle_endtag(self, tag):
        if self.depth:
            self.depth -= 1

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


class HomepageBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.html = BUILT_INDEX.read_text(encoding="utf-8")
        cls.css = BUILT_CSS.read_text(encoding="utf-8")

    def test_generated_homepage_contains_complete_content(self):
        self.assertIn("Dongping Chen", self.html)
        self.assertNotIn('class="sidebar', self.html)
        for title in PUBLICATION_TITLES:
            with self.subTest(title=title):
                self.assertIn(title, self.html)
        self.assertIn("https://linxins.net/", self.html)
        self.assertIn("https://github.com/LinxinS97/LinxinS97.github.io", self.html)

    def test_generated_homepage_has_sections_and_resolvable_local_assets(self):
        parser = WikiContentParser()
        parser.feed(self.html)
        self.assertTrue({"biography", "research-interests", "publications", "education"} <= parser.ids)
        for local_path in parser.local_paths:
            with self.subTest(path=local_path):
                self.assertTrue((ROOT / "_site" / local_path).is_file(), local_path)

    def test_compiled_css_contains_homepage_system(self):
        self.assertIn(".wiki-home", self.css)
        self.assertIn(".publication-grid", self.css)
        self.assertIn(".publication-row", self.css)


if __name__ == "__main__":
    unittest.main()
