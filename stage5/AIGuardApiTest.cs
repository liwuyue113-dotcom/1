using System.Collections;
using System.Text;
using UnityEngine;
using UnityEngine.Networking;

public class AIGuardApiTest : MonoBehaviour
{
    [SerializeField] private string apiUrl = "http://127.0.0.1:8000/npc/chat";
    [SerializeField] private string testMessage = "别怕，我不会伤害你";
    [SerializeField] private int timeoutSeconds = 15;

    private void Start()
    {
        StartCoroutine(SendTestMessage());
    }

    private IEnumerator SendTestMessage()
    {
        string requestJson = JsonUtility.ToJson(new GuardChatRequest(testMessage));
        byte[] requestBody = Encoding.UTF8.GetBytes(requestJson);

        using (UnityWebRequest request = new UnityWebRequest(apiUrl, UnityWebRequest.kHttpVerbPOST))
        {
            request.uploadHandler = new UploadHandlerRaw(requestBody);
            request.downloadHandler = new DownloadHandlerBuffer();
            request.SetRequestHeader("Content-Type", "application/json");
            request.timeout = timeoutSeconds;

            Debug.Log($"正在向胆小守卫发送消息：{testMessage}");
            yield return request.SendWebRequest();

            if (request.result == UnityWebRequest.Result.Success)
            {
                Debug.Log($"胆小守卫 API 返回：{request.downloadHandler.text}");
            }
            else
            {
                Debug.LogError($"胆小守卫 API 请求失败：{request.error}");
            }
        }
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
}
