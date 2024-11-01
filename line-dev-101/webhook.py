from fastapi import FastAPI, Request, HTTPException
from linebot.v3 import WebhookHandler
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi
from linebot.v3.messaging import ReplyMessageRequest, TextMessage, StickerMessage
from linebot.v3.webhooks import MessageEvent, TextMessageContent, StickerMessageContent

app = FastAPI()

# Initialize Line Bot API and Handler with your Channel Access Token and Channel Secret
configuration = Configuration(access_token='Your_Channel_Access_Token')
handler = WebhookHandler(channel_secret='Your_Channel_Secret')

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