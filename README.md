# 🌍 City AI Assistant

An AI-powered city assistant that helps users explore current weather conditions and the latest news about cities through natural language conversations.

Built using **LangChain, Google Gemini, Tavily Search, OpenWeather API, and Streamlit**.

## ✨ Features

- 🌦️ **Weather Updates:** Get current weather conditions, temperature, and descriptions for Indian cities.
- 📰 **Latest City News:** Search for recent news and updates about a city using Tavily.
- 🤖 **AI-Powered Agent:** Uses Google Gemini to understand user queries and decide which tools to use.
- 💬 **Interactive Chat Interface:** Chat with the AI assistant through a clean Streamlit interface.
- 🧰 **Tool Integration:** Integrates external APIs as tools using LangChain.
- 🔐 **API Key Management:** Stores API credentials in environment variables.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | AI agent and tool integration |
| Google Gemini 2.5 Flash Lite | Language model |
| Tavily Search API | Latest news search |
| OpenWeather API | Current weather information |
| Streamlit | Web application interface |
| python-dotenv | Environment variable management |
| Requests | HTTP API requests |

## 🏗️ Project Architecture

```text
User
  |
  v
Streamlit Chat Interface
  |
  v
LangChain AI Agent
  |
  v
Google Gemini 2.5 Flash Lite
  |
  +----------------------+
  |                      |
  v                      v
Weather Tool          News Tool
  |                      |
  v                      v
OpenWeather API       Tavily Search API
  |                      |
  +----------+-----------+
             |
             v
       Tool Results
             |
             v
       Gemini Response
             |
             v
       Streamlit UI
```

## 📁 Project Structure

```text
GenAI-3/
│
├── .streamlit/
│   └── config.toml
│
├── Agents.py
├── app.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

```bash
cd GenAI-3
```

### 2. Create a virtual environment

```bash
uv venv
```

### 3. Activate the environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 5. Configure API keys

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Get your API keys:

- Google Gemini: https://aistudio.google.com/
- OpenWeather: https://openweathermap.org/api
- Tavily: https://app.tavily.com/

### 6. Run the application

```bash
uv run streamlit run app.py
```

The application will open in your browser.

## 🔄 How It Works

1. The user enters a question through the Streamlit chat interface.
2. The LangChain agent receives the user's query.
3. Google Gemini understands the request and decides which tool is required.
4. For weather queries, the agent calls the OpenWeather API.
5. For news queries, the agent uses Tavily Search.
6. The tool results are returned to the agent.
7. Gemini generates a natural-language response.
8. Streamlit displays the response to the user.

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Google Gemini API key |
| `OPENWEATHER_API_KEY` | OpenWeather API key |
| `TAVILY_API_KEY` | Tavily Search API key |

**Important:** Never upload your `.env` file or expose API keys in your public repository.

## 🚀 Future Improvements

- Add human approval buttons directly inside Streamlit.
- Add weather forecasts and additional weather information.
- Improve news filtering and source presentation.
- Add support for international cities.
- Add conversation memory and persistent chat history.
- Deploy the application online.

## 👨‍💻 Author

**Dhruvil Kayasth**

GitHub: https://github.com/DhruvilKayasth

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with Python, Generative AI, and curiosity.**
