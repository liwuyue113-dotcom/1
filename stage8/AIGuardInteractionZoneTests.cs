using NUnit.Framework;

public class AIGuardInteractionZoneTests
{
    [Test]
    public void ShouldShowDialogue_AcceptsPlayerTag()
    {
        Assert.That(AIGuardInteractionZone.ShouldShowDialogue("Player"), Is.True);
    }

    [Test]
    public void ShouldShowDialogue_RejectsOtherTags()
    {
        Assert.That(AIGuardInteractionZone.ShouldShowDialogue("Enemy"), Is.False);
    }
}
