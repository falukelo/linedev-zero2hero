from fastapi import FastAPI, Request, HTTPException
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging import ReplyMessageRequest, TextMessage, StickerMessage
from linebot.v3.webhooks import MessageEvent, TextMessageContent, StickerMessageContent

app = FastAPI()

# Initialize Line Bot API and Handler with your Channel Access Token and Channel Secret
configuration = Configuration(access_token='44ub+Pztj0Xlk3zluS0vBTVdxlydxb1DqqNw/wU96NGnMxJ0B5IYqzujzywwiQ/Wi3MD7tYhwB9kc/LGXbXpMAUyQU3/gJ4k3Une3yMvSw/fw5jS6jlsdJJAvSIvtQ39hfrOTZF7jpsjTFW7MLi/bgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler(channel_secret='2e8dfc9b508bbff98b5f5c48433d9363')

@app.post("/webhook")
async def webhook(request: Request):
    signature = request.headers.get("x-line-signature")
    body = await request.body()

    try:
        # Parse the request and verify the signature
        handler.handle(body.decode("utf-8"), signature)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return {"status": "success"}

@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        if event.message.text == "สวัสดี":
            reply_text = "สวัสดีครับ"
        else:
            reply_text = "ไม่เข้าใจครับ"
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=reply_text)]
            )
        )

@handler.add(MessageEvent, message=StickerMessageContent)
def handle_sticker(event):
     with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[StickerMessage(package_id = "1070", sticker_id = "17841")]
            )
        )