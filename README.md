# 🔬 ScoutAI – AI Research Intelligence Platform

> **Discover • Analyze • Prioritize • Learn**

ScoutAI is an AI-powered research intelligence platform that aggregates the latest AI research from multiple sources, analyzes each paper using task-specific Large Language Models (LLMs), ranks research based on user interests, and generates a personalized daily research digest.

Instead of manually browsing dozens of research papers every day, ScoutAI automatically identifies the most relevant breakthroughs, summarizes key findings, recommends what to read first, and presents everything through an interactive dashboard.

---

# ✨ Features

## 📚 Multi-Source Research Collection

ScoutAI collects the latest research from multiple platforms.

- arXiv
- GitHub
- Papers With Code *(extensible)*

---

## 🧠 AI-Powered Research Analysis

Every research paper is analyzed using task-specific LLM prompts.

The system generates:

- Executive summary
- Relevance score
- Priority level
- Topics
- Why the research matters

---

## 🎯 Personalized Research Feed

Users can select multiple interests such as:

- Agentic AI
- Multi-Agent Systems
- RAG
- LLM Engineering
- AI Infrastructure
- Machine Learning
- Deep Learning
- Reinforcement Learning

ScoutAI automatically prioritizes research matching those interests.

---

## 📈 AI Research Digest

Every run generates a personalized research briefing including:

- Executive Summary
- Biggest Breakthrough
- Emerging Trends
- Featured Papers
- Featured GitHub Repositories
- Reading Plan
- Key Takeaways
- Recommended Audience

---

## 📊 Interactive Dashboard

Built using Streamlit.

Features include:

- Executive Overview
- Research Metrics
- AI Landscape
- Breakthrough Highlights
- Featured Papers
- GitHub Repository Explorer
- Reading Plan
- Research Feed Explorer

---

## 🔗 Direct Resource Access

Every recommendation contains direct links to:

- Original arXiv paper
- GitHub Repository

allowing users to immediately continue reading.

---

# 🏗 Architecture

```
                    +----------------------+
                    |   User Interests     |
                    |   (Streamlit UI)     |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |  Scout Service       |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    |  Feed Manager        |
                    +----------+-----------+
                               |
              +----------------+----------------+
              |                                 |
              v                                 v

     +-------------------+             +--------------------+
     | arXiv Collector   |             | GitHub Collector   |
     +-------------------+             +--------------------+

              \                               /
               \                             /
                +---------------------------+
                |      Research Feed        |
                +---------------------------+
                              |
                              v

                +---------------------------+
                | Research Analyst (LLM)    |
                +---------------------------+
                              |
                              v

                +---------------------------+
                | Digest Generator (LLM)    |
                +---------------------------+
                              |
                              v

                +---------------------------+
                | Streamlit Dashboard       |
                +---------------------------+
```

---

# 🧩 Project Structure

```
ai-research-scout/

│
├── app/
│   ├── analyst/
│   ├── collectors/
│   ├── config/
│   ├── digest/
│   ├── feed/
│   ├── models/
│   ├── providers/
│   └── services/
│
├── ui/
│   ├── components/
│   └── streamlit_app.py
│
├── tests/
│
├── .streamlit/
│
├── requirements.txt
├── README.md
├── main.py
└── .gitignore
```

---

# 🚀 Technology Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| UI | Streamlit |
| LLM Routing | OpenRouter |
| AI Models | GPT OSS / DeepSeek / Gemini *(configurable)* |
| Research Source | arXiv API |
| Repository Source | GitHub REST API |
| Configuration | YAML |
| Data Validation | Pydantic |
| HTTP Client | Requests |

---

# ⚙ How It Works

### Step 1

Collect latest research from:

- arXiv
- GitHub

---

### Step 2

Rank research according to user interests.

---

### Step 3

Analyze every research item using a task-specific LLM.

The AI generates:

- Summary
- Relevance
- Topics
- Priority
- Why it matters

---

### Step 4

Generate a complete research digest containing:

- Executive Summary
- Emerging Trends
- Biggest Breakthrough
- Reading Plan
- Featured Papers
- Repository Recommendations

---

### Step 5

Display everything inside an interactive Streamlit dashboard.

---

# 🖥 Screenshots

## Dashboard

> *(Add screenshot here)*

---

## Executive Overview

> *(Add screenshot here)*

---

## Featured Papers

> *(Add screenshot here)*

---

## Research Feed

> *(Add screenshot here)*

---

# ⚙ Installation

Clone the repository.

```bash
git clone https://github.com/Pavan0852/ai-research-scout.git

cd ai-research-scout
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Create a `.env` file.

```
OPENROUTER_API_KEY=YOUR_API_KEY
```

Run the application.

```bash
streamlit run ui/streamlit_app.py
```

---

# 📌 Example Workflow

```
Select Interests
        │
        ▼

Collect Latest Research

        │

Analyze with LLM

        │

Generate Digest

        │

Display Interactive Dashboard

        │

Open Papers Directly
```

---

# 🎯 Current Capabilities

✅ Multi-source research aggregation

✅ Personalized recommendations

✅ AI-powered research summaries

✅ Research prioritization

✅ Emerging trend detection

✅ Executive daily digest

✅ Interactive Streamlit dashboard

✅ GitHub repository recommendations

✅ Reading plan generation

✅ Direct paper links

---

# 🔮 Future Roadmap

- AI Research Chat Assistant
- Semantic Search
- Historical Digest Archive
- Weekly Email Digest
- PDF Export
- Slack / Teams Integration
- User Authentication
- Research Collections
- Vector Database Integration
- Knowledge Graph for Research Relationships

---

# 🤝 Contributing

Contributions are welcome.

If you'd like to improve ScoutAI:

- Fork the repository
- Create a feature branch
- Commit your changes
- Submit a Pull Request

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Pavan Kumar Gudla**

AI Engineer | Generative AI | Agentic AI | Knowledge Graphs | LLM Systems

LinkedIn: *(https://www.linkedin.com/in/pavan-kumar-gudla-058857167/)*

GitHub: *(https://github.com/Pavan0852)*

---

# ⭐ Support

If you found this project useful,

⭐ Star the repository

🍴 Fork it

📢 Share it with fellow AI researchers.