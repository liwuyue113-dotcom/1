using System.Collections;
using System.Text;
using TMPro;
using UnityEngine;
using UnityEngine.Networking;
using UnityEngine.UI;

public class AIGuardDialogueUI : MonoBehaviour
{
    [SerializeField] private string apiUrl = "http://127.0.0.1:8000/npc/chat";
    [SerializeField] private int timeoutSeconds = 15;
    [SerializeField] private TMP_InputField playerInput;
    [SerializeField] private Button sendButton;
    [SerializeField] private TMP_Text guardReplyText;
    [SerializeField] private TMP_Text guardEmotionText;
    [SerializeField] private AIGuardGameplayEffects gameplayEffects;

    private bool isRequestInProgress;

    private void Awake()
    {
        sendButton.onClick.AddListener(SendPlayerMessage);
    }

    private void OnDestroy()
    {
        sendButton.onClick.RemoveListener(SendPlayerMessage);
    }

    public void SendPlayerMessage()
    {
        if (!CanSend(playerInput.text, isRequestInProgress))
        {
            return;
        }

        StartCoroutine(SendChatRequest(playerInput.text.Trim()));
    }

    private IEnumerator SendChatRequest(string playerMessage)
    {
        SetRequestInProgress(true);
        guardReplyText.text = "守卫正在回答……";

        string requestJson = JsonUtility.ToJson(new GuardChatRequest(playerMessage));
        byte[] requestBody = Encoding.UTF8.GetBytes(requestJson);

        using (UnityWebRequest request = new UnityWebRequest(apiUrl, UnityWebRequest.kHttpVerbPOST))
        {
            request.uploadHandler = new UploadHandlerRaw(requestBody);
            request.downloadHandler = new DownloadHandlerBuffer();
            request.SetRequestHeader("Content-Type", "application/json");
            request.timeout = timeoutSeconds;

            yield return request.SendWebRequest();

            if (request.result == UnityWebRequest.Result.Success)
            {
                GuardChatResponse response = ParseResponse(request.downloadHandler.text);
                guardReplyText.text = response.reply;
                guardEmotionText.text = $"情绪：{response.emotion}";
                if (gameplayEffects != null)
                {
                    gameplayEffects.ApplyResponse(response.intel_result);
                }
                playerInput.text = string.Empty;
                playerInput.ActivateInputField();
            }
            else
            {
                guardReplyText.text = "守卫没有回应，请稍后再试。";
                Debug.LogError($"胆小守卫 API 请求失败：{request.error}");
            }
        }

        SetRequestInProgress(false);
    }

    private void SetRequestInProgress(bool value)
    {
        isRequestInProgress = value;
        sendButton.interactable = !value;
        playerInput.interactable = !value;
    }

    public static bool CanSend(string playerMessage, bool requestInProgress)
    {
        return !requestInProgress && !string.IsNullOrWhiteSpace(playerMessage);
    }

    public static GuardChatResponse ParseResponse(string json)
    {
        return JsonUtility.FromJson<GuardChatResponse>(json);
    }

    [System.Serializable]
    private class GuardChatRequest
    {
        public string player_message;

        public GuardChatRequest(string playerMessage)
        {
            player_message = playerMessage;
        }
    }

    [System.Serializable]
    public class GuardChatResponse
    {
        public string reply;
        public string emotion;
        public int trust;
        public int fear;
        public string intent;
        public string intel_result;
    }
}
