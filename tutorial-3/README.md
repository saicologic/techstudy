
# Step
##  Create APP:
https://api.slack.com/apps

##  Create New Command
https://api.slack.com/apps/[YOUR APP ID]/slash-commands?

### for Development

Create Request url from ngrok.

for example: `https://[RandomID].ngrok.io/sample_ping`

##  Start Server

### Required library

```
pip install flask
pip install requests
```

### Setting environment

```
export SLACK_ACCESS_TOKEN=""
```

Get legacy-tokens:
https://api.slack.com/custom-integrations/legacy-tokens

Get `Token` and set to `SLACK_ACCESS_TOKEN`

### Run Server

```
python app.py
```

# Demo
## Ping/Pong

slack_command: `/sample_ping`

## Get image

slack_command: `/sample_getimage`
