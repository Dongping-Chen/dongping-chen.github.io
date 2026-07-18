import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ABOUT = ROOT / "_pages" / "about.md"
HOMEPAGE_SCSS = ROOT / "_sass" / "_homepage.scss"
MAIN_SCSS = ROOT / "assets" / "css" / "main.scss"

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
        self.assertIn('class="wiki-home"', self.source)
        for section_id in ("biography", "research-interests", "publications", "education"):
            self.assertIn(f'id="{section_id}"', self.source)

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


if __name__ == "__main__":
    unittest.main()
