---
id: alert-inbox
title: The Alert Inbox skill
category: research
summary: Forty trading emails a day into one morning brief: real alerts by ticker, newsletters in 2 lines, hype counted and ignored, scams flagged. Drafts replies, never sends, never trades.
---

# ALERT INBOX

Forty trading emails a day. Three matter. This finds the three.

## SETUP (once)

1. Connect Gmail to Claude (claude.ai connector or a Gmail MCP server). Read access plus "create draft" is all it needs.
2. Copy `RULES.md` next to this file and fill every `[bracket]`: your watchlist, your brokers, the newsletters you actually pay for, senders to always ignore.
3. Run `/alert-inbox today`.

## THE BUCKETS

Every email goes in exactly one:

| Bucket | What it is | What happens |
|---|---|---|
| **ACTION** | Broker margin call, order rejected, deposit/withdrawal, login from new device, bot error alert, 2FA change | Top of the brief in bold. Never summarized away. |
| **SIGNAL** | Your own TradingView/bot alerts, earnings date for a ticker you hold, filings for your watchlist | Grouped by ticker. Price level + time. |
| **READ** | Paid newsletters and research you chose to get | 2-line summary + every ticker named, with the author's stance (bullish/bearish/neutral) |
| **HYPE** | "This stock could 10x", countdown timers, "last chance", unnamed "AI picks", sponsored promos | One line total: "12 promo emails, 7 tickers pushed: …" |
| **SCAM** | See red flags below | Listed by sender with the flag that tripped. Never opened links. |
| **IGNORE** | Receipts, socials, everything on your never-list | Count only |

## SCAM AND PUMP RED FLAGS (any one = SCAM bucket)

- Asks you to move money, connect a wallet, or "verify" your account through a link
- Guaranteed returns, "risk-free", or a fixed daily/weekly % profit
- Sender display name is a broker but the domain is not the broker's real domain
- A micro-cap or new token pushed by someone you've never subscribed to
- Urgency + secrecy ("don't share this", "only 50 spots")
- Asks for your seed phrase, API secret or 2FA code. Always a scam. Say so in caps.

## THE BRIEF (output)

```
MORNING BRIEF · <date> · <N> emails scanned

⚠ ACTION (do these first)
- <broker>: <what happened> → <what to do>

📈 SIGNALS BY TICKER
NVDA  your alert "break above 20d high" fired 9:41 ET · earnings in 6 days
SPY   …

📰 WORTH READING (2)
- <newsletter>: <2 lines>. Tickers: AAPL (bullish), TLT (bearish)

🗑 HYPE: 14 promos pushed 9 tickers (list). Ignored.
🚩 SCAM: 2 (sender → flag)

Drafts saved: 1 (reply to <broker> support thread)
```

Write it to `./briefs/<YYYY-MM-DD>.md` as well.

## DRAFTS

Only draft a reply when a human is waiting on you (broker support, a partner, a customer). Save it as a Gmail draft **on the same thread**. Short, polite, factual. Never paste account numbers, balances or keys into a draft.

## SCHEDULED MODE

`/alert-inbox schedule` writes a cron line (or a Claude Code scheduled task) that runs `today` at 7:30 AM your time on weekdays and saves the brief. It still never sends.

## HARD RULES

- **No send tool. No trade tool.** If asked to send or trade, say: "I can't. Here's the draft / here's the order you'd place by hand."
- **Never click links in SCAM or HYPE emails.** Read the text only.
- **Never copy a ticker from HYPE into SIGNALS.** Promo picks are not signals.
- **Never repeat a newsletter's price target as fact.** Write "X says".
- Educational only. Not financial advice.
