# Let Claude Code set it up with you

Open [Claude Code](https://claude.com/claude-code) in this folder (the one with `00-START-HERE.md` in it) and paste the text below. It will do the steps with you, one at a time.

**Never paste your API keys or tokens into the chat.** Claude Code will tell you which file to put them in, and you type them there yourself.

```text
Help me set up the Claude Chart Analyst alerts in this folder. Read 00-START-HERE.md (Part 2) and 07-setup-alerts-and-python-webhook.md first and follow them. Explain each step in plain, simple words, like I've never used a terminal.

1. Check I have Python 3.10 or newer. If not, tell me how to install it.
2. Walk me through adding code/setup-alerts.pine to TradingView and setting the Webhook secret.
3. In the code folder, create the Python environment, install app-requirements.txt and copy app.env.example to app.env.
4. Tell me to open code/app.env myself and fill in WEBHOOK_SECRET, ANTHROPIC_API_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, ACCOUNT_SIZE and RISK_PCT. Help me get the Telegram values. Never read, print or ask me for my keys.
5. When I say I'm done, run app.py --check. Ask me before running app.py --test-alert, then help me confirm the message reached my phone.
6. Help me put the app online on a host I choose, using the host's secret settings (not a file), and check the /health page.
7. Walk me through creating the TradingView alert and testing it on a 1-minute chart.

Never connect a broker or place trades. This is educational, not financial advice.
