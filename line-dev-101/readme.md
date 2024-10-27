# Line Chat Bot: Zero to Hero

## Line Developer 101
An introduction to developing with the Line Messaging API, covering essential tools and setup for creating a Line Official Account (OA), generating tokens, and building a webhook with FastAPI. This section provides the foundational steps to connect and manage your bot with the Line platform.

## Presentation
For a detailed presentation on this project, please refer to the [Canva presentation](https://www.canva.com/design/DAGUsXVCExs/APba5pNI2hQmac9oW5kLGw/view?utm_content=DAGUsXVCExs&utm_campaign=designshare&utm_medium=link&utm_source=editor).

---

## API Example
Example API concept.

### Run
1. Navigate to the directory:
   ```bash
   cd line-dev-101
   ```

2. Run API using fastapi cli
   ```bash
   fastapi dev api.py
   ```

To stop the API, press `Ctrl + C` in the terminal where the API is running.

---

## Webhook Example
Example Webhook for Line Chatbot.

### Configuration
Before running the API, make sure to update your Line access token and channel secret in the code. Locate the following configuration lines in `webhook.py` and replace them with your own values:

```python
configuration = Configuration(access_token='Your_Channel_Access_Token')
handler = WebhookHandler(channel_secret='Your_Channel_Secret')
```

Replace `'Your_Channel_Access_Token'` and `'Your_Channel_Secret'` with your actual Line channel access token and channel secret, respectively.

### Run
1. Run API using fastapi cli
   ```bash
   fastapi dev webhook.py
   ```

2. Run API using fastapi cli
   ```bash
   fastapi dev webhook.py
   ```

3. Deploy your webhook online
   Open a new Terminal and run this command
   ```bash
   ngrok http http://localhost:8080
   ```

   Copy the HTTPS link provided by ngrok (e.g., `https://your-ngrok-id.ngrok.io`), add `/webhook` at the end, and paste the full URL into the **Webhook URL** field in the [Line Developer Console](https://developers.line.biz/console/). This setup enables Line to send events to your local server via the secure tunnel created by ngrok.


To stop the Webhook and Ngrok, press `Ctrl + C` in the terminal where the Webhook and Ngrok is running.