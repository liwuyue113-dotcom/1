using UnityEngine;

public class AIGuardInteractionZone : MonoBehaviour
{
    [SerializeField] private GameObject dialoguePanel;

    private void Start()
    {
        SetDialogueVisible(false);
    }

    private void OnTriggerEnter2D(Collider2D other)
    {
        if (ShouldShowDialogue(other.tag))
        {
            SetDialogueVisible(true);
        }
    }

    private void OnTriggerExit2D(Collider2D other)
    {
        if (ShouldShowDialogue(other.tag))
        {
            SetDialogueVisible(false);
        }
    }

    private void SetDialogueVisible(bool visible)
    {
        if (dialoguePanel != null)
        {
            dialoguePanel.SetActive(visible);
        }
    }

    public static bool ShouldShowDialogue(string objectTag)
    {
        return objectTag == "Player";
    }
}
