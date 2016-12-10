
import requests
import json
import os
import time
import datetime


github_oauth_token=os.environ['GITHUB_OAUTH_TOKEN']
slack_webhook=os.environ['SLACK_WEBHOOK']
DELTA_MINUTES=5


while True:
    headers = {
        'Authorization': "token " + github_oauth_token,
        'If-Modified-Since': (datetime.datetime.utcnow() - datetime.timedelta(minutes=DELTA_MINUTES)).strftime('%a, %d %b %Y %H:%M:%S GMT')
    }
    notifications = requests.get("https://api.github.com/notifications", headers=headers)
    if notifications.status_code is 200:
        for notif in notifications.json():
            url = ""
            author = ""
            details = requests.get(notif["subject"]["url"], headers=headers)
            if details.status_code == 200:
                try:
                    url = details.json()["html_url"]
                    author = details.json()["user"]["login"]
                except:
                    pass
            payload = {
                "username": "Github",
                "icon_url": "https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png",
                "text": "_" + notif["subject"]["type"] + "_ =>   " + notif["repository"]["full_name"] + "    -    *" + notif["subject"]["title"] + "*\n" + author + "  -  " + url
            }
            requests.post(slack_webhook, json.dumps(payload), headers={'content-type': 'application/json'})

    time.sleep(60 * DELTA_MINUTES)

