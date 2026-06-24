import unittest

from rag.document_loader import load_markdown_chunks
from rag.embedding_service import LocalTextEmbeddingModel, encode_texts
from rag.rag_config import PROJECT_ROOT, SOURCE_FILES
from rag.vector_store import search_vectors


class RagAcceptanceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.chunks = load_markdown_chunks(PROJECT_ROOT, SOURCE_FILES)
        cls.model = LocalTextEmbeddingModel()
        cls.embeddings = encode_texts(
            cls.model,
            [chunk["text"] for chunk in cls.chunks],
        )

    def retrieve(self, question):
        query = encode_texts(self.model, [question])[0]
        return search_vectors(query, self.embeddings, self.chunks, top_k=3)

    def test_default_index_uses_only_confirmed_setting_documents(self):
        self.assertEqual(SOURCE_FILES, ["docs/rag_setting.md"])

    def test_real_route_question_retrieves_hidden_passage(self):
        matches = self.retrieve("胆小守卫提供的真实路线在哪里？")

        self.assertTrue(any("第二个口子" in match["text"] for match in matches))

    def test_threat_question_retrieves_false_route(self):
        matches = self.retrieve("威胁胆小守卫可能得到什么情报？")

        self.assertTrue(any("往上走最安全" in match["text"] for match in matches))

    def test_rescue_motive_is_now_confirmed(self):
        matches = self.retrieve("姬野为什么要营救吕归尘？")

        self.assertTrue(any("昔日战友" in match["text"] for match in matches))

    def test_guard_setting_contains_single_purpose_answer_chunks(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        expected_facts = {
            "安抚胆小守卫的结果": ["安抚", "提高信任", "降低恐惧"],
            "威胁胆小守卫的结果": ["威胁", "降低信任", "提高恐惧"],
            "获得真实路线的条件": ["信任大于等于 50", "提供真实路线"],
            "获得虚假路线的条件": ["恐惧大于等于信任加 30", "提供虚假路线"],
            "真实安全路线": ["第二个口子", "暗道", "几乎无人镇守"],
            "虚假危险路线": ["往上走最安全", "虚假"],
        }

        for heading, facts in expected_facts.items():
            self.assertIn(heading, chunks_by_heading)
            for fact in facts:
                self.assertIn(fact, chunks_by_heading[heading])

    def test_guard_setting_removes_stale_unconfirmed_rescue_motive(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        self.assertNotIn("未确认设定", chunks_by_heading)

    def test_core_story_setting_contains_confirmed_rescue_facts(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        expected_facts = {
            "项目同人定位": ["九州缥缈录", "原创同人支线"],
            "主角与营救目标": ["姬野", "吕归尘", "昔日战友"],
            "吕归尘被关押的原因与地点": ["离国军", "离国边境城堡", "审问"],
            "限时营救原因": ["黎明前", "转移", "主力军营"],
            "关卡通关条件": ["找到吕归尘", "关卡完成"],
            "关卡失败条件": ["倒计时结束前", "未找到吕归尘"],
            "当前版本不包含的营救玩法": ["不包含", "护送", "逃离"],
        }

        for heading, facts in expected_facts.items():
            self.assertIn(heading, chunks_by_heading)
            for fact in facts:
                self.assertIn(fact, chunks_by_heading[heading])

    def test_three_route_setting_contains_confirmed_play_differences(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        expected_facts = {
            "三条潜入路线总览": ["三条主路", "上路", "中路", "下方暗道路线", "胆小守卫"],
            "上路": ["正常路线", "路线较长", "敌人数量一般", "不需要胆小守卫情报解锁"],
            "中路": ["正常路线", "长度一般", "敌人数量略多", "不需要胆小守卫情报解锁"],
            "下方暗道路线": ["胆小守卫", "真实路线情报", "第二个口子", "暗道", "敌人最少"],
        }

        for heading, facts in expected_facts.items():
            self.assertIn(heading, chunks_by_heading)
            for fact in facts:
                self.assertIn(fact, chunks_by_heading[heading])

    def test_normal_route_question_retrieves_direct_routes(self):
        matches = self.retrieve("不需要胆小守卫情报解锁的路线有哪些？")

        self.assertTrue(any("正常路线" in match["text"] and "不需要胆小守卫情报解锁" in match["text"] for match in matches))

    def test_hidden_route_question_retrieves_secret_passage_route(self):
        matches = self.retrieve("哪条主路需要胆小守卫提供真实情报？")

        self.assertTrue(any("下方暗道路线" in match["text"] and "真实路线情报" in match["text"] for match in matches))

    def test_hidden_route_question_retrieves_ai_guard_unlock(self):
        matches = self.retrieve("AI 守卫的真实情报能解锁什么路线？")

        self.assertTrue(any("下方暗道路线" in match["text"] and "真实路线情报" in match["text"] for match in matches))

    def test_route_length_and_enemy_questions_retrieve_confirmed_differences(self):
        long_route_matches = self.retrieve("哪条路比较长但是敌人一般？")
        more_enemy_matches = self.retrieve("哪条路长度一般但是敌人略多？")
        fewest_enemy_matches = self.retrieve("哪条路敌人最少？")

        self.assertTrue(any("上路" in match["heading"] and "路线较长" in match["text"] for match in long_route_matches))
        self.assertTrue(any("中路" in match["heading"] and "敌人数量略多" in match["text"] for match in more_enemy_matches))
        self.assertTrue(any("下方暗道路线" in match["heading"] and "敌人最少" in match["text"] for match in fewest_enemy_matches))

    def test_route_hint_setting_contains_confirmed_player_cues(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        expected_facts = {
            "上路提示方式": ["更远", "更绕", "较长走廊", "拐弯", "远处火把"],
            "中路提示方式": ["入口附近", "更多守卫", "密集的巡逻点", "敌人略多"],
            "下方暗道提示方式": ["默认不明显", "真实情报", "往前第二个口子跳下去"],
        }

        for heading, facts in expected_facts.items():
            self.assertIn(heading, chunks_by_heading)
            for fact in facts:
                self.assertIn(fact, chunks_by_heading[heading])

    def test_route_hint_questions_retrieve_confirmed_player_cues(self):
        upper_matches = self.retrieve("上路入口怎么提示玩家这条路更长？")
        middle_matches = self.retrieve("中路怎么提示玩家敌人略多？")
        tunnel_matches = self.retrieve("下方暗道默认怎么提示？")

        self.assertTrue(any("上路提示方式" in match["heading"] and "更远" in match["text"] for match in upper_matches))
        self.assertTrue(any("中路提示方式" in match["heading"] and "更多守卫" in match["text"] for match in middle_matches))
        self.assertTrue(any("下方暗道提示方式" in match["heading"] and "默认不明显" in match["text"] for match in tunnel_matches))

    def test_route_enemy_position_setting_contains_confirmed_guard_layouts(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        expected_facts = {
            "上路敌人站位": ["开始很分散", "一个一个的守卫", "后面", "连续几个守卫站岗"],
            "中路敌人站位": ["敌人分布很多", "好几个守卫站岗"],
            "下方暗道敌人站位": ["暗道内部", "一个站岗"],
        }

        for heading, facts in expected_facts.items():
            self.assertIn(heading, chunks_by_heading)
            for fact in facts:
                self.assertIn(fact, chunks_by_heading[heading])

    def test_route_enemy_position_questions_retrieve_confirmed_guard_layouts(self):
        upper_matches = self.retrieve("上路敌人是怎么站位的？")
        middle_matches = self.retrieve("中路哪里守卫比较多？")
        tunnel_matches = self.retrieve("下方暗道里面有几个守卫？")

        self.assertTrue(any("上路敌人站位" in match["heading"] and "连续几个守卫站岗" in match["text"] for match in upper_matches))
        self.assertTrue(any("中路敌人站位" in match["heading"] and "好几个守卫站岗" in match["text"] for match in middle_matches))
        self.assertTrue(any("下方暗道敌人站位" in match["heading"] and "一个站岗" in match["text"] for match in tunnel_matches))

    def test_route_patrol_setting_contains_confirmed_pressure_patterns(self):
        chunks_by_heading = {
            chunk["heading"]: chunk["text"]
            for chunk in self.chunks
            if chunk["source"] == "docs/rag_setting.md"
        }

        expected_facts = {
            "上路巡逻方式": ["前半段", "分散站岗", "短距离巡逻", "后半段", "固定站岗", "压力区"],
            "中路巡逻方式": ["守卫更密集", "多个守卫同时站岗", "正面压力较高", "等待空隙"],
            "下方暗道巡逻方式": ["一个站岗守卫", "不做复杂巡逻", "找到暗道入口"],
        }

        for heading, facts in expected_facts.items():
            self.assertIn(heading, chunks_by_heading)
            for fact in facts:
                self.assertIn(fact, chunks_by_heading[heading])

    def test_route_patrol_questions_retrieve_confirmed_pressure_patterns(self):
        upper_matches = self.retrieve("上路后半段有什么巡逻压力？")
        middle_matches = self.retrieve("中路为什么正面压力更高？")
        tunnel_matches = self.retrieve("下方暗道有没有复杂巡逻？")

        self.assertTrue(any("上路巡逻方式" in match["heading"] and "压力区" in match["text"] for match in upper_matches))
        self.assertTrue(any("中路巡逻方式" in match["heading"] and "多个守卫同时站岗" in match["text"] for match in middle_matches))
        self.assertTrue(any("下方暗道巡逻方式" in match["heading"] and "不做复杂巡逻" in match["text"] for match in tunnel_matches))


if __name__ == "__main__":
    unittest.main()
