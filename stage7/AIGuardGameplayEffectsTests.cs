using NUnit.Framework;

public class AIGuardGameplayEffectsTests
{
    [Test]
    public void ApplyResponse_GrantsTimeBonusOnlyOnce()
    {
        AIGuardGameplayRules rules = new AIGuardGameplayRules();

        AIGuardGameplayRules.EffectResult first = rules.ApplyResponse("none");
        AIGuardGameplayRules.EffectResult second = rules.ApplyResponse("none");

        Assert.That(first.grantTimeBonus, Is.True);
        Assert.That(second.grantTimeBonus, Is.False);
    }

    [Test]
    public void ApplyResponse_AllowsFalseRouteToBeCorrectedByTrueRoute()
    {
        AIGuardGameplayRules rules = new AIGuardGameplayRules();

        AIGuardGameplayRules.EffectResult falseResult = rules.ApplyResponse("false_route");
        AIGuardGameplayRules.EffectResult trueResult = rules.ApplyResponse("true_route");

        Assert.That(falseResult.routeHint, Does.Contain("往上走"));
        Assert.That(trueResult.routeHint, Does.Contain("第二个口子"));
        Assert.That(trueResult.routeHint, Does.Contain("暗道"));
    }

    [Test]
    public void ApplyResponse_WeakensSafeRouteGuardOnlyOnce()
    {
        AIGuardGameplayRules rules = new AIGuardGameplayRules();

        AIGuardGameplayRules.EffectResult first = rules.ApplyResponse("true_route");
        AIGuardGameplayRules.EffectResult second = rules.ApplyResponse("true_route");

        Assert.That(first.weakenSafeRouteGuard, Is.True);
        Assert.That(second.weakenSafeRouteGuard, Is.False);
    }
}
