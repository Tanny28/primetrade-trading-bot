# 🤖 PrimeTrade Futures Trading Bot (Binance Testnet)

A modular Python project that connects to Binance Futures **Testnet**, allowing users to place market and limit orders via a secure and intuitive **Streamlit-based web interface**. Designed for developers, interns, or traders learning to automate crypto trading safely.

---

## 📸 Demo

🌐 [Live Streamlit App](https://primetrade-trading-bot-tanmay.streamlit.app/)

---

## 🚀 Features

- ✅ Trade on Binance Futures **Testnet**
- ✅ Secure API management using `.env`
- ✅ Clean **Streamlit UI** to place orders easily
- ✅ Logs every trade and error to a local file
- ✅ Modular architecture with validation and logging
- ✅ Built with `python-binance`, `streamlit`, `dotenv`

---

## 🧠 How It Works

1. User enters symbol (e.g., BTCUSDT), quantity, order type.
2. Streamlit UI sends details to backend logic.
3. Binance API places the order (Market or Limit).
4. Results are shown + logged in `logs/order_log.txt`.

---

## 📁 Folder Structure

primetrade-trading-bot/

├── .env # Your Binance API credentials

├── .gitignore # Prevents uploading secrets

├── README.md # This file

├── requirements.txt # Dependencies

├── bot.py # Bot logic using Binance API

├── config.py # Loads keys from .env

├── ui.py # Streamlit app

├── logs/

│ └── order_log.txt # Trade and error logs

└── utils/

├── logger.py # Logging helper

└── validator.py # Input validation

---

## 🛠 Local Setup Instructions

### ✅ 1. Clone the Repository
```bash
git clone https://github.com/Tanny28/primetrade-trading-bot.git
cd primetrade-trading-bot
```
Install Required Packages
```bash
pip install -r requirements.txt
```

🎯 Set Up Your .env File
Create a .env file in the root directory with:

```bash
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```
Use Binance Futures Testnet to generate free test API keys.

✅ Run the App

```bash
streamlit run ui.py
```
OUTPUT : 
![Screenshot 2025-06-24 150515](https://github.com/user-attachments/assets/79c30b92-5a39-4aac-8748-6bb399fb85ba)


