import os

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.shortcut("save_message")
def message_hello(ack, shortcut, client):
    ack()
    print(shortcut)
    if 'thread_ts' in shortcut['message']:
         #buscar a mensagem e verificar sehá threads
        slack_response = client.conversations_replies(
            channel=shortcut['channel']['id'],
            ts=shortcut['message']['thread_ts']
        )
        # print(slack_response)
        # print('\n')
# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()



channel_id, thread_ts