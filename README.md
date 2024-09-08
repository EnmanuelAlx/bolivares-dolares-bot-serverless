# Bolivares Dolares Bot

## Telegram Bot for Bolivar to Dollar Conversion

A Telegram bot to convert Bolivars to Dollars using the official exchange rate from the Central Bank of Venezuela. Leveraging Serverless Framework for easy deployment on AWS using Lambda functions.

**Bot URL: https://t.me/BolivarDolarBot**


### Features
- Real-time exchange rates: Fetches the latest exchange rate directly from the Central Bank of Venezuela's website.
- Simple command: Use the `/bcv` command followed by numbers to perform calculations.
- Serverless architecture: Deployed on AWS Lambda for scalability and cost-efficiency.

### Installation
- Clone the repository
- Create a virtual environment and install dependencies:
```bash
npm i serverless -g
cd bolivares-dolares-bot
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```
- Generate a public URL
    - Use ngrok or a similar tool to expose your local server.
- Set the webhook:
```bash
https://api.telegram.org/bot<TOKEN>/setWebhook?url=<URL>
```
- Deploy to AWS:
```bash
serverless deploy
```

### How it works

The bot periodically scrapes the Central Bank of Venezuela's website to obtain the latest exchange rate.

When a user sends the /bcv command followed by numbers, the bot calculates the equivalent value in dollars using the fetched exchange rate.

### Contributing
Contributions are welcome! Please open an issue to discuss new features or improvements.

### License
This project is licensed under the MIT License.

