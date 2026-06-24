using TMPro;
using UnityEngine;
using UnityEngine.Events;

public class AIGuardGameplayEffects : MonoBehaviour
{
    [SerializeField] private TMP_Text routeHintText;
    [SerializeField] private UnityEvent onGrantTwentySeconds = new UnityEvent();
    [SerializeField] private UnityEvent onWeakenSafeRouteGuard = new UnityEvent();

    private readonly AIGuardGameplayRules rules = new AIGuardGameplayRules();

    public void ApplyResponse(string intelResult)
    {
        AIGuardGameplayRules.EffectResult result = rules.ApplyResponse(intelResult);

        if (result.grantTimeBonus)
        {
            onGrantTwentySeconds.Invoke();
        }

        if (!string.IsNullOrEmpty(result.routeHint) && routeHintText != null)
        {
            routeHintText.text = result.routeHint;
        }

        if (result.weakenSafeRouteGuard)
        {
            onWeakenSafeRouteGuard.Invoke();
        }
    }
}
