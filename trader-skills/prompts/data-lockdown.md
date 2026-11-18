---
title: The Trading Data Lockdown
keyword: LOCKDOWN
promise: What your AI has stored about your money, the one email a scammer would send you, and what to delete today.
---

# The Trading Data Lockdown

**Traders paste everything into AI: screenshots of balances, broker names, API keys "just to debug".** This prompt makes your assistant show you what it holds, how a scammer would use it, and what to delete.

## The prompt

```text
Do a security review of me as a trader, using only what you have stored or can see in
our past chats (memories, chat history, uploaded files). Be specific and blunt.

1. MONEY FACTS: every fact you hold about my money: brokers, exchanges, wallets,
   balances, account sizes, positions, income, bank. Quote where it came from.
2. SECRETS: any API key, secret, seed phrase, password, 2FA code or account number
   I've ever pasted. Show only the first 4 characters and where it appeared.
   If you find any, start your answer with "ROTATE NOW:" and the list.
3. IDENTITY: name, location, employer, family, email, phone, handles.
4. THE DOSSIER: in 5 lines, what a stranger would know about me from all of the above.
5. THE SCAM EMAIL: write the single most convincing phishing email a scammer could
   send me using only these facts (fake broker security alert style). Label it
   "EXAMPLE SCAM - DO NOT SEND". Then list the 3 details that make it convincing.
6. THE DM SCAM: same, as an Instagram/Telegram DM from a "trading mentor".
7. DELETE LIST: exactly which memories, chats and files I should delete, in order of risk.
8. SETTINGS: which settings in this assistant I should change (memory, training on my
   data, chat history) and where they are.
9. NEVER-PASTE LIST: the 8 things I should never give any AI again.
10. WHAT YOU CAN'T SEE: be honest about what this review can't cover.
```

## The never-paste list (keep this)

1. API **secret** keys (the public key ID alone is low risk; the secret is not)
2. Seed phrases or private keys. **Ever.** No exception, no "just to check"
3. 2FA codes and backup codes
4. Passwords, including "old" ones
5. Full account numbers and routing numbers
6. Screenshots with your full name + broker + balance together
7. Tax documents with your SSN/national ID
8. Withdrawal-enabled exchange keys. Make trading keys **trade-only, no withdrawals, IP-locked**

## If the review finds a key

1. Go to the broker/exchange now. Delete the key. Make a new one, trade-only, no withdrawals.
2. Delete the chat where it appeared.
3. Check the account's API log and recent orders for anything you didn't do.
4. Put keys in a `.env` file next to your bot, and add `.env` to `.gitignore`.

> Educational only. Not financial or security advice for your specific situation.
