import unittest

import numpy as np

from rag.vector_store import search_vectors


class VectorStoreTests(unittest.TestCase):
    def test_search_vectors_orders_results_by_cosine_similarity(self):
        query = np.array([1.0, 0.0])
        embeddings = np.array(
            [
                [0.0, 1.0],
                [0.8, 0.2],
                [1.0, 0.0],
            ]
        )
        chunks = [
            {"text": "无关", "source": "docs/a.md", "heading": "A"},
            {"text": "相关", "source": "docs/b.md", "heading": "B"},
            {"text": "最相关", "source": "docs/c.md", "heading": "C"},
        ]

        results = search_vectors(query, embeddings, chunks, top_k=3)

        self.assertEqual(
            [result["text"] for result in results],
            ["最相关", "相关", "无关"],
        )

    def test_search_vectors_respects_top_k_and_preserves_metadata(self):
        query = np.array([1.0, 0.0])
        embeddings = np.array([[1.0, 0.0], [0.5, 0.5]])
        chunks = [
            {"text": "暗道", "source": "docs/game.md", "heading": "路线"},
            {"text": "守卫", "source": "docs/npc.md", "heading": "角色"},
        ]

        results = search_vectors(query, embeddings, chunks, top_k=1)

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["source"], "docs/game.md")
        self.assertEqual(results[0]["heading"], "路线")
        self.assertAlmostEqual(results[0]["score"], 1.0)


if __name__ == "__main__":
    unittest.main()
