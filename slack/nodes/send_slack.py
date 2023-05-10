import requests
import json

SLACK_URL = "https://slack.com/api/chat.postMessage"


class SendSlack:
    
    def send_slack(self,message_slack):
        header = {
            "Content-Type": "application/json",
            "Authorization": "Bearer xoxb-5227628382162-5228706929107-Nunf8k3RN49fnCH2ppQ3n8G7"
        }
        response = requests.post(url=SLACK_URL, headers=header, data=json.dumps(message_slack))
        if response.ok:
            print("Successfully send message to slack")
        else:
            print(response.status_code, response.text)