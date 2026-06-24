using NUnit.Framework;

public class AIGuardApiClientTests
{
    [Test]
    public void BuildRequestJson_PreservesChinesePlayerMessage()
    {
        string json = AIGuardApiClient.BuildRequestJson("我不会伤害你");

        StringAssert.Contains("\"player_message\":\"我不会伤害你\"", json);
    }

    [Test]
    public void ParseResponse_ReadsGuardReplyEmotionAndIntelResult()
    {
        string json =
            "{\"reply\":\"我还不能告诉你。\",\"emotion\":\"非常害怕\"," +
            "\"trust\":0,\"fear\":70,\"intent\":\"ask_route\",\"intel_result\":\"false_route\"}";

        AIGuardApiClient.GuardChatResponse response = AIGuardApiClient.ParseResponse(json);

        Assert.That(response.reply, Is.EqualTo("我还不能告诉你。"));
        Assert.That(response.emotion, Is.EqualTo("非常害怕"));
        Assert.That(response.intel_result, Is.EqualTo("false_route"));
    }
}
