# Let Claude Code set it up with you

Open [Claude Code](https://claude.com/claude-code) in this folder (the one with `00-START-HERE.md` in it) and paste the text below. Claude Code will run the commands with you, one step at a time.

**Never paste your API keys or tokens into the chat.** Claude Code will tell you which file to put them in, and you type them there yourself.

```text
Help me set up the 24/7 AI Trader in this folder. Read 00-START-HERE.md and 08-the-full-ai-trader.md first, and follow them. Explain each step in plain, simple words, like I've never used a terminal.

1. Check I have Python 3.10 or newer. If not, tell me how to install it for my computer.
2. Run: bash install/setup.sh ./ai-desk-work  (On Windows without bash, help me do the same steps another way.)
3. Tell me to open ai-desk-work/code/trader.env myself and set WATCHLIST, ACCOUNT and RISK_PCT, and (optional) ANTHROPIC_API_KEY. Never read, print or ask me for my keys.
4. When I say I'm done, run trader.py --check and help me compare the price it shows with a chart.
5. Ask me before you run anything that sends a message or uses my API key. Then run the bot once and explain the result. "No setups" is a normal result.
6. Help me set up Telegram so the answers reach my phone, then run --test-notification.
7. Help me schedule it to run every weekday after the market closes (GitHub Actions or my computer's scheduler).

Never connect a broker or place trades. This is educational, not financial advice.
```
