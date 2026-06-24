import unittest

import numpy as np

from rag.embedding_service import LocalTextEmbeddingModel, build_embedding_text


class EmbeddingServiceTests(unittest.TestCase):
    def test_local_embedding_returns_normalized_vectors(self):
        model = LocalTextEmbeddingModel(dimensions=128)

        vectors = model.encode(["真实路线是暗道", "往上走是危险路线"])

        self.assertEqual(vectors.shape, (2, 128))
        self.assertAlmostEqual(float(np.linalg.norm(vectors[0])), 1.0)

    def test_related_texts_are_more_similar_than_unrelated_texts(self):
        model = LocalTextEmbeddingModel(dimensions=256)
        query = model.encode(["胆小守卫的真实路线"])[0]
        candidates = model.encode(["守卫提供真实暗道路线", "玩家使用长剑攻击"])

        related_score = float(candidates[0] @ query)
        unrelated_score = float(candidates[1] @ query)

        self.assertGreater(related_score, unrelated_score)

    def test_build_embedding_text_combines_heading_and_text(self):
        chunk = {
            "heading": "威胁胆小守卫的结果",
            "text": "玩家威胁胆小守卫会降低信任并提高恐惧。",
        }

        result = build_embedding_text(chunk)

        self.assertEqual(
            result,
            "威胁胆小守卫的结果：玩家威胁胆小守卫会降低信任并提高恐惧。",
        )

    def test_build_embedding_text_uses_text_when_heading_is_empty(self):
        chunk = {
            "heading": "",
            "text": "玩家需要在倒计时结束前完成人质营救。",
        }

        result = build_embedding_text(chunk)

        self.assertEqual(result, "玩家需要在倒计时结束前完成人质营救。")


if __name__ == "__main__":
    unittest.main()
