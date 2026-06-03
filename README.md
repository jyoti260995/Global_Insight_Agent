<img width="1440" height="900" alt="Screenshot 2026-06-03 at 12 11 47 PM" src="https://github.com/user-attachments/assets/56791451-04b1-438f-a8f6-e76d41e91542" />

# 🌍 GlobalInsight Agent

> Real-time weather & local news for any location on Earth — powered by LangChain, Mistral AI, and GNews.

---

## 📸 Preview

```
Enter a city → Get current weather + top 5 headlines instantly
```

---

## 🚀 Features

- 🌡 **Live Weather** — Temperature, conditions, humidity, and wind speed for any city worldwide
- 📰 **Local News** — Top 5 latest headlines with source links, fetched via GNews API
- 🌐 **Global Coverage** — Works for any city, country, or region on Earth
- ⚡ **Instant Results** — Structured JSON response from the agent for reliable parsing
- 🎨 **Beautiful UI** — Dark-themed Streamlit interface with animated globe and card layout

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **LLM** | Mistral AI (`mistral-large-latest`) |
| **Agent Framework** | LangChain |
| **Weather Tool** | OpenWeatherMap API |
| **News Tool** | GNews API |
| **Frontend** | Streamlit |

---

## 📁 Project Structure

```
GlobalInsight/
├── app.py              # Streamlit UI
├── agent.py            # LangChain agent setup
├── weather_tool.py     # Weather fetching tool
├── news_tool.py        # News fetching tool (GNews)
├── .env                # API keys (never commit this)
├── requirements.txt    # Python dependencies
└── README.md
```

---

## ⚙️ Setup & Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/globalinsight.git
cd globalinsight
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Get your API keys

| Service | Sign up at | Free tier |
|---|---|---|
| **Mistral AI** | [console.mistral.ai](https://console.mistral.ai) | ✅ Yes |
| **GNews** | [gnews.io](https://gnews.io) | ✅ 100 req/day |
| **OpenWeatherMap** | [openweathermap.org](https://openweathermap.org/api) | ✅ 1000 req/day |

### 5. Create your `.env` file
```env
MISTRAL_API_KEY=your_mistral_key_here
GNEWS_API_KEY=your_gnews_key_here
OPENWEATHER_API_KEY=your_openweather_key_here
```

### 6. Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

---

## 📦 requirements.txt

```
streamlit
langchain
langchain-mistralai
langchain-community
python-dotenv
requests
```

---

## 🧠 How It Works

```
User types a city
       ↓
LangChain Agent (Mistral LLM)
       ↓
  ┌────┴────┐
  ↓         ↓
Weather    News
Tool       Tool
(OWM API) (GNews API)
  ↓         ↓
  └────┬────┘
       ↓
  Structured JSON
  { weather: {...}, news: [...] }
       ↓
  Streamlit renders
  Weather card + News list
```

The agent is prompted to return **structured JSON only**, which makes parsing reliable and avoids formatting issues.

---

## 🗺 Supported Locations

Works with any of the following formats:
- City name: `Delhi`, `Tokyo`, `Cairo`
- City + Country: `Sydney, Australia`
- Country name: `Germany`, `Brazil`
- Region: `Midwest USA`, `Southeast Asia`

---

## 🔒 Environment Variables

Never commit your `.env` file. Add it to `.gitignore`:

```bash
echo ".env" >> .gitignore
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m "Add my feature"`
4. Push to branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

## 👨‍💻 Author

Built with ❤️ as a learning project to explore LangChain agents, Mistral AI, and real-time data APIs.

> *"The world at your fingertips — one query at a time."*
