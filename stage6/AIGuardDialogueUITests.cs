using NUnit.Framework;

public class AIGuardDialogueUITests
{
    [Test]
    public void CanSend_RejectsEmptyMessage()
    {
        Assert.That(AIGuardDialogueUI.CanSend("   ", false), Is.False);
    }

    [Test]
    public void CanSend_RejectsMessageWhileRequestIsRunning()
    {
        Assert.That(AIGuardDialogueUI.CanSend("别怕", true), Is.False);
    }

    [Test]
    public void ParseResponse_ReadsChineseReplyAndEmotion()
    {
        const string json =
            "{\"reply\":\"我开始相信你了。\",\"emotion\":\"开始信任你\"," +
            "\"trust\":100,\"fear\":25,\"intent\":\"comfort\",\"intel_result\":\"none\"}";

        AIGuardDialogueUI.GuardChatResponse response = AIGuardDialogueUI.ParseResponse(json);

        Assert.That(response.reply, Is.EqualTo("我开始相信你了。"));
        Assert.That(response.emotion, Is.EqualTo("开始信任你"));
    }
}
