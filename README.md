# 🧠 MindVault — Personal Knowledge Base AI

> A local RAG (Retrieval-Augmented Generation) chatbot that answers questions **strictly from your own documents** — PDFs, text files, URLs, and Q&A pairs — with full source citations.

Built by **Aarnav Kejriwal** · [aarnkej@gmail.com](mailto:aarnkej@gmail.com)

---

## ✨ Features

- 📄 **Multi-format ingestion** — PDF, TXT, MD, DOCX, URLs, and raw Q&A pairs
- 🔍 **RAG pipeline** — keyword-scored chunk retrieval + Claude Sonnet answering
- 📎 **Source citations** — every answer shows which documents were used
- 🎛️ **3 answer modes** — Precise · Creative · Summary
- 🔒 **Privacy-first** — documents never leave your machine (only relevant chunks sent to Anthropic's API)
- 🖥️ **Fully local** — runs as a Flask server on your own computer

---

## 🗂️ Project Structure

```
mindvault/
├── app.py                  ← Flask backend (API proxy + routing)
├── requirements.txt        ← Python dependencies
├── .env.example            ← Environment variable template
├── .gitignore
├── start_windows.bat       ← One-click start for Windows
├── start_mac_linux.sh      ← One-click start for Mac/Linux
├── templates/
│   └── index.html          ← Full frontend UI (HTML + CSS + JS)
└── static/                 ← Static assets (empty by default)
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher — [python.org](https://www.python.org/downloads/)
- An Anthropic API key — [console.anthropic.com](https://console.anthropic.com)

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/mindvault.git
cd mindvault
```

### 2. Set up your API key

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder:

```
ANTHROPIC_API_KEY=sk-ant-YOUR_REAL_KEY_HERE
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

Then open your browser at **http://localhost:5000** 🎉

---

## ⚡ One-Click Start Scripts

| Platform | Script |
|----------|--------|
| Windows | Double-click `start_windows.bat` |
| Mac / Linux | Run `bash start_mac_linux.sh` |

Both scripts will prompt you for your API key if it's not already set.

---

## 📖 How to Use

### Step 1 — Add Documents (left sidebar)

| Tab | Accepts |
|-----|---------|
| **PDF** | Drag & drop `.pdf` files |
| **TEXT** | Drop `.txt`, `.md`, `.docx` files |
| **URL** | Paste any website URL + optional label |
| **Q&A** | Paste `Question \| Answer` pairs or raw notes |

### Step 2 — Choose a Mode

| Mode | Behaviour |
|------|-----------|
| **Precise** | Factual answers, strictly from your docs |
| **Creative** | Draws connections and insights across sources |
| **Summary** | Concise bullet-point summaries |

### Step 3 — Ask Anything

Type your question in the chat box. MindVault will:
1. Search your indexed documents for relevant chunks
2. Send only the most relevant context to Claude
3. Return an answer with source badges

---

## 🧪 Quick Test Data

Paste this into the **Q&A tab → Raw Notes** box to test immediately:

```
What is RAG?
RAG stands for Retrieval-Augmented Generation. It fetches relevant documents before generating an answer, making responses accurate and grounded.

What is a neural network?
A neural network is a system of algorithms modeled after the human brain that processes input through layers of interconnected nodes and learns patterns from data.

What is the difference between AI and ML?
AI is the broad field of making machines intelligent. ML is a subset of AI focused on learning from data automatically without explicit programming.

What is Claude?
Claude is an AI assistant made by Anthropic, a safety-focused AI company founded in 2021 by former OpenAI researchers including Dario and Daniela Amodei.

What is a transformer model?
A transformer is a deep learning architecture that uses self-attention mechanisms to process sequences in parallel. It is the foundation of modern LLMs like GPT-4, Claude, and Gemini.

What is the context window?
The context window is the maximum amount of text (measured in tokens) that a language model can process in a single request. Larger context windows allow models to handle longer documents.
```

Then try asking: *"What is RAG and how does it work?"* or *"Who made Claude?"*

---

## 🔑 API Key Options

**Option A — `.env` file (recommended)**

```bash
cp .env.example .env
# Edit .env and set ANTHROPIC_API_KEY
```

**Option B — Environment variable**

```bash
# Mac/Linux
export ANTHROPIC_API_KEY=sk-ant-...
python app.py

# Windows
set ANTHROPIC_API_KEY=sk-ant-...
python app.py
```

**Option C — In-browser (session only)**

If no key is configured on the server, a banner appears at the top of the UI. Paste your key there — it's saved only for that browser session and is never stored on disk.

---

## 🛠️ Configuration

| Environment Variable | Default | Description |
|----------------------|---------|-------------|
| `ANTHROPIC_API_KEY` | *(required)* | Your Anthropic API key |
| `PORT` | `5000` | Port to run the Flask server on |
| `FLASK_DEBUG` | `true` | Enable Flask debug mode |

---

## 🛡️ Privacy & Security

- Documents are processed **entirely in your browser** (chunking, indexing, retrieval)
- Only the **most relevant text chunks** for each query are sent to Anthropic's API
- **No data is stored on disk** — everything lives in browser memory
- Closing the browser tab clears all documents and chat history
- Your API key is stored only in your `.env` file (which is git-ignored)

---

## 🐛 Troubleshooting

| Problem | Fix |
|---------|-----|
| `pip` not found | Install Python 3.8+ from [python.org](https://python.org) |
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again |
| Port 5000 already in use | Set `PORT=5001` in `.env` or export it |
| Invalid API key error | Check key starts with `sk-ant-` and has no extra spaces |
| CORS errors | Access via `http://localhost:5000`, not by opening the HTML file directly |
| Blank page | Check terminal output for Python errors |

---

## 🔧 Extending MindVault

### Add semantic search (embeddings)
Replace the keyword scorer in `templates/index.html` (`retrieveChunks`) with calls to the [Anthropic Embeddings API](https://docs.anthropic.com) for true semantic similarity.

### Persist your knowledge base
Save `knowledgeBase` to `localStorage` or a backend SQLite database so documents survive page refreshes.

### Support more file types
Integrate [pdf.js](https://mozilla.github.io/pdf.js/) for proper PDF text extraction, or use Python libraries like `pypdf` or `python-docx` on the backend.

---

## 📦 Dependencies

| Package | Purpose |
|---------|---------|
| `flask` | Web framework / local server |
| `flask-cors` | Cross-origin request handling |
| `anthropic` | Official Anthropic Python SDK |
| `python-dotenv` | Load `.env` files automatically |

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

## 👤 Author

**Aarnav Kejriwal**
📧 [aarnkej@gmail.com](mailto:aarnkej@gmail.com)

---

*Powered by [Claude Sonnet](https://www.anthropic.com) · Built with Flask*
