# Telegram WhatsApp Link Bot

A small aiogram bot that receives a phone number in free form and replies with a direct WhatsApp link.

Example:

```text
0544445811
```

Bot reply:

```text
https://wa.me/+972544445811
```

## Setup

```bash
uv sync
cp .env.example .env
```

Edit `.env` and set `BOT_TOKEN` to the token from BotFather.

## Run

```bash
uv run wa-link-bot
```

The bot reads `.env` automatically when it starts.

`DEFAULT_COUNTRY_CODE` defaults to `972`. Local numbers that start with `0` are converted by replacing that leading `0` with the default country code.

## Docker

```bash
docker build -t wa-link-bot .
docker run --env-file .env wa-link-bot
```
