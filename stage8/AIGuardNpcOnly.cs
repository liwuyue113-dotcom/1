using UnityEngine;

public class AIGuardNpcOnly : MonoBehaviour
{
    [SerializeField] private bool isNpcOnly = true;
    [SerializeField] private GameObject attackArea;
    [SerializeField] private Behaviour[] hostileBehaviours;
    [SerializeField] private Collider2D[] damageColliders;

    private void Awake()
    {
        ApplyNpcOnlyConfiguration();
    }

    public void ApplyNpcOnlyConfiguration()
    {
        if (!isNpcOnly)
        {
            return;
        }

        gameObject.tag = "Untagged";
        gameObject.layer = LayerMask.NameToLayer("Default");

        if (attackArea != null)
        {
            attackArea.SetActive(false);
        }

        foreach (Behaviour hostileBehaviour in hostileBehaviours)
        {
            if (hostileBehaviour != null)
            {
                hostileBehaviour.enabled = false;
            }
        }

        foreach (Collider2D damageCollider in damageColliders)
        {
            if (damageCollider != null)
            {
                damageCollider.enabled = false;
            }
        }
    }
}
