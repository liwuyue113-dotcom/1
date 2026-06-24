public class AIGuardGameplayRules
{
    public const string TrueRouteHint = "真实情报：往前第二个口子跳下去有一条暗道，几乎无人镇守。";
    public const string FalseRouteHint = "守卫声称：往上走最安全。";

    private bool timeBonusGranted;
    private bool safeRouteGuardWeakened;

    public EffectResult ApplyResponse(string intelResult)
    {
        EffectResult result = new EffectResult
        {
            grantTimeBonus = !timeBonusGranted
        };

        timeBonusGranted = true;

        if (intelResult == "true_route")
        {
            result.routeHint = TrueRouteHint;
            result.weakenSafeRouteGuard = !safeRouteGuardWeakened;
            safeRouteGuardWeakened = true;
        }
        else if (intelResult == "false_route")
        {
            result.routeHint = FalseRouteHint;
        }

        return result;
    }

    public class EffectResult
    {
        public bool grantTimeBonus;
        public string routeHint;
        public bool weakenSafeRouteGuard;
    }
}
