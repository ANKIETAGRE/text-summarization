# 🦜 LangChain: YouTube & Website Text Summarizer

An AI-powered Streamlit application that extracts content from **YouTube videos or websites** and generates concise summaries using **LangChain and Groq LLMs**.

## 🚀 Features

* 🎥 Summarize YouTube video transcripts
* 🌐 Summarize content from any valid website URL
* 🤖 Powered by Groq LLMs
* 🔗 Built with LangChain
* 📝 Custom prompt-based summarization
* ⚡ Fast AI-powered text processing
* 🖥️ Simple and interactive Streamlit interface
* 🔐 Groq API key entered securely through the Streamlit sidebar

## 🏗️ How It Works
<img width="807" height="443" alt="image" src="https://github.com/user-attachments/assets/4c03bc1a-bbf9-432a-b85b-7213d3b3b550" />


```text
                User
                 │
                 ▼
          Enter URL + API Key
                 │
                 ▼
          Streamlit Interface
                 │
        ┌────────┴────────┐
        ▼                 ▼
   YouTube URL       Website URL
        │                 │
        ▼                 ▼
 YoutubeLoader    UnstructuredURLLoader
        │                 │
        └────────┬────────┘
                 ▼
            Extract Content
                 │
                 ▼
          LangChain Prompt
                 │
                 ▼
             Groq LLM
                 │
                 ▼
          Generated Summary
                 │
                 ▼
          Streamlit Output
```

## 🔗 LangChain Document Summarization

The project is based on LangChain's document summarization approach.

The three commonly used document-combining strategies are:

### 1. Stuff

All documents are combined and passed to the LLM in a single prompt.

```text
Documents
    ↓
Combine documents
    ↓
Prompt
    ↓
LLM
    ↓
Summary
```

This approach is simple and works well when the total document content fits within the model's context window.

### 2. Map-Reduce

Each document or chunk is summarized independently first. The individual summaries are then combined into a final summary.

```text
Documents
   ↓
Split into chunks
   ↓
Individual summaries
   ↓
Combine summaries
   ↓
Final summary
```

### 3. Refine

The model generates an initial summary and then progressively improves it using additional document chunks.

```text
Document 1 → Initial Summary
                  ↓
Document 2 → Refined Summary
                  ↓
Document 3 → Further Refined Summary
```

The current project focuses on the **Stuff-style document summarization workflow** for concise content summarization.

## 🛠️ Tech Stack

| Technology             | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| Python                 | Core programming language                 |
| Streamlit              | Web application interface                 |
| LangChain              | LLM orchestration and document processing |
| LangChain Community    | YouTube and URL document loaders          |
| LangChain Core         | Prompt templates and document components  |
| Groq                   | LLM inference                             |
| YouTube Transcript API | YouTube transcript retrieval              |
| Unstructured           | Website content extraction                |

## 📂 Project Structure

```text
text-summarization/
│
├── app.py
├── requirements.txt
├── text_summarization.ipynb
├── .gitignore
└── .vscode/
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ANKIETAGRE/text-summarization.git
cd text-summarization
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Groq API Key

The application requires a Groq API key.

The key is entered through the **Streamlit sidebar** and is not stored directly in the source code.

For security, never commit API keys, passwords, or other secrets to GitHub.

## ▶️ Run the Application

After activating the virtual environment:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🧪 Example

Enter a YouTube or website URL such as:

```text
https://docs.langchain.com/langsmith/deployment
```

Then click:

**Summarize the Content from YT or Website**

The application extracts the content and generates an approximately 300-word summary.

## 📸 Application

The application provides a simple interface containing:

* Groq API key input
* URL input
* Summarization button
* Generated summary output

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

* LangChain
* LLM integration
* Prompt engineering
* Document loaders
* Document summarization
* YouTube transcript extraction
* Web content extraction
* Streamlit application development
* API integration
* Generative AI application development

## 🚀 Future Improvements

* Add Map-Reduce summarization
* Add Refine summarization
* Support PDF and DOCX files
* Add adjustable summary length
* Add multiple LLM options
* Add chat functionality over extracted content
* Add RAG-based question answering
* Deploy the application publicly
* Add summary download functionality

## 👨‍💻 Author

**Aniket Agre**

B.Tech Computer Science & Engineering
AI/ML & Generative AI Enthusiast

GitHub: https://github.com/ANKIETAGRE

---

⭐ If you find this project useful, consider giving the repository a star.
