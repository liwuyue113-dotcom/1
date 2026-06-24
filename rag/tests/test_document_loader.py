import unittest
from pathlib import Path

from rag.document_loader import load_markdown_chunks, split_markdown


class DocumentLoaderTests(unittest.TestCase):
    def test_split_markdown_preserves_heading_and_source(self):
        text = """# 城堡设定

城堡由黑石军团控制，内部戒备森严。

## 暗道

往前第二个口子跳下去有一条暗道，几乎无人镇守。
"""

        chunks = split_markdown(text, "docs/world.md", min_length=10)

        self.assertEqual(
            chunks,
            [
                {
                    "text": "城堡由黑石军团控制，内部戒备森严。",
                    "source": "docs/world.md",
                    "heading": "城堡设定",
                },
                {
                    "text": "往前第二个口子跳下去有一条暗道，几乎无人镇守。",
                    "source": "docs/world.md",
                    "heading": "暗道",
                },
            ],
        )

    def test_split_markdown_ignores_short_paragraphs(self):
        text = """# 角色

未知

胆小守卫听到砍杀声后躲在 Level1 深处。
"""

        chunks = split_markdown(text, "docs/characters.md", min_length=10)

        self.assertEqual(
            [chunk["text"] for chunk in chunks],
            ["胆小守卫听到砍杀声后躲在 Level1 深处。"],
        )

    def test_load_markdown_chunks_reads_only_selected_sources(self):
        root = Path(__file__).parent / "fixtures"

        chunks = load_markdown_chunks(root, ["docs/game.md"], min_length=5)

        self.assertEqual(len(chunks), 1)
        self.assertEqual(chunks[0]["source"], "docs/game.md")
        self.assertNotIn("进度", chunks[0]["text"])


if __name__ == "__main__":
    unittest.main()
