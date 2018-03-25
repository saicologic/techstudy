import os
from flask import Flask, request
import requests

app = Flask(__name__)
accessToken = os.environ.get('SLACK_ACCESS_TOKEN')


@app.route("/sample_ping", methods=['POST'])
def ping():
    return "Pong"


@app.route("/sample_getimage", methods=['POST'])
def get_image():
    files = {'file': open('./images/seikou_banzai_man.png', 'rb')}
    channelId = request.form['channel_id']
    param = {
        'token': accessToken,
        'channels': channelId
    }
    resp = requests.post(
        url="https://slack.com/api/files.upload",
        params=param,
        files=files
    )
    return (resp.text, resp.status_code, resp.headers.items())

if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True, threaded=True)
