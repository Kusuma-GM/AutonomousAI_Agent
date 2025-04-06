
# 🤖 AutonomousAI_Agent

An intelligent Python agent that can process natural language instructions to:
- ✅ Fetch top AI news headlines
- ✅ Extract smartphone reviews (pros/cons)
- ✅ Analyze renewable energy trends and generate a PDF report with a chart

---

## 📁 Features

- 🌐 **Fetch AI News** — Uses NewsAPI to get top 5 AI headlines and saves them to a file.
- 📱 **Smartphone Reviews** — Scrapes reviews, extracts pros/cons, and summarizes the data.
- ⚡ **Renewable Energy Report** — Analyzes energy trends and creates a summary PDF with charts.

---

## 🛠 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Kusuma-GM/AutonomousAI_Agent.git
cd AutonomousAI_Agent
```

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 🔐 Add your NewsAPI key

Open `ai_news_fetcher.py` and replace:

```python
api_key = "YOUR_API_KEY"
```

with your actual NewsAPI key:

```python
api_key = "ef2f76a804ed4fb8bf299e40fffba6b9"
```

---

## 🚀 How to Use

Run the program using:

```bash
python main.py
```

You can now enter instructions like:

```shell
> fetch ai news
> AI news file contains 5 headlines
> Search smartphone reviews, extract pros/cons
> Research renewable energy, create pdf
```

---

## 📦 Output Files

- `output/web_data.txt` → AI News Headlines
- `output/smartphone_reviews.txt` → Review summaries
- `output/renewable_energy_report.pdf` → PDF report with chart

---

