import requests
import json

SLACK_URL = "https://slack.com/api/chat.postMessage"


class SendSlack:
    
    def send_slack(self,message_slack):
        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer XXXXXXX"
        }
        response = requests.post(url=SLACK_URL, headers=header, data=json.dumps(message_slack))
        if response.ok:
            print("Successfully send message to slack")
        else:
            print(response.status_code, response.text)
