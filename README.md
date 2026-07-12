# Research_summarizer
# AI Research Paper Summarizer

An agile web dashboard built with Flask and Gemini AI that pulls raw academic data directly from the arXiv API, parses relevant entries using BeautifulSoup, and delivers beautiful, structured summaries of complex research topics.

## 🌐 Live Demo

You can access the live, deployed version of the application here:
 [View Live Web Application](researchsummarizer-production.up.railway.app)
## Application Preview

### Main Dashboard & Query Interface
Enter any academic topic into the search field to fetch real-time papers from arXiv.
![Dashboard UI] <img width="1920" height="834" alt="image" src="https://github.com/user-attachments/assets/ecf566a2-100a-4c89-a7f2-da64c3a51fe2" />


### 📊 AI Summary Output
The dashboard renders structured breakdowns using markdown processing, highlighting objectives, methodologies, and limitations.
![Summary Results] 

---

## ⚡ Features

*   Live arXiv Integration: Dynamically query arXiv's massive catalog by entering any research topic.
*   Intelligent Parsing: Uses BeautifulSoup to extract and clean unstructured XML query metadata.
*   AI-Powered Summarization: Leverages the gemini-2.5-flash model to analyze papers and instantly extract critical research metrics.
*   Clean Markdown Output: Generates clear, structured layouts containing core objectives, methodologies, metrics, and limitations for each paper.

---

## 🛠️ Tech Stack

*   Backend: Python 3, Flask
*   AI Engine: Google GenAI SDK (`gemini-2.5-flash`)
*   Web Scraping & Parsing: BeautifulSoup4 (`bs4`)
*   Frontend: HTML5, CSS3 (Custom Responsive Layout), Jinja2 Templating

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone [https://github.com/aryanshende86-lang/Research_summarizer.git](https://github.com/aryanshende86-lang/Research_summarizer.git)
cd Research_summarizer
