# Research_summarizer
# AI Research Paper Summarizer

An agile web dashboard built with Flask and Gemini AI that pulls raw academic data directly from the arXiv API, parses relevant entries using BeautifulSoup, and delivers beautiful, structured summaries of complex research topics.

## 🌐 Live Demo

You can access the live, deployed version of the application here:
 [View Live Web Application](https://researchsummarizer-production.up.railway.app)
## Application Preview

### Main Dashboard & Query Interface
Enter any academic topic into the search field to fetch real-time papers from arXiv.
![Dashboard UI] <img width="1920" height="834" alt="image" src="https://github.com/user-attachments/assets/ecf566a2-100a-4c89-a7f2-da64c3a51fe2" />


### 📊 AI Summary Output
The dashboard renders structured breakdowns using markdown processing, highlighting objectives, methodologies, and limitations.

<img width="1103" height="825" alt="image" src="https://github.com/user-attachments/assets/65591175-83db-4c73-a05f-11e57157e86b" />

<img width="1130" height="598" alt="image" src="https://github.com/user-attachments/assets/9e2e16a7-824c-484d-b9e5-86096bfe506c" />

### Error Hnadling and Alerts
It shows errors or alerts you whenever you write invalid subjects and when you try to summarize without giving any subject.

<img width="1091" height="541" alt="image" src="https://github.com/user-attachments/assets/8dcf5004-d662-4c11-9531-c63ca3a23fe9" />

<img width="1057" height="441" alt="image" src="https://github.com/user-attachments/assets/d85dfab2-a94a-43bd-a072-7a472a86d2ae" />

## ⚡ Features

*   **Live arXiv Integration**: Dynamically query arXiv's massive catalog by entering any research topic.
*   **Intelligent Parsing**: Uses BeautifulSoup to extract and clean unstructured XML query metadata.
*   **AI-Powered Summarization**: Leverages the gemini-2.5-flash model to analyze papers and instantly extract critical research metrics.
*   **Clean Markdown Output**: Generates clear, structured layouts containing core objectives, methodologies, metrics, and limitations for each paper.

## 🛠️ Tech Stack

*   **Backend**: Python 3, Flask
*  **AI Engine**: Google GenAI SDK (`gemini-2.5-flash`)
*   **Web Scraping & Parsing**: BeautifulSoup4 (`bs4`)
*   **Frontend**: HTML5, CSS3 (Custom Responsive Layout), Jinja2 Templating

## 🚀 Getting Started

### 1. Clone the Repository

git clone [https://github.com/aryanshende86-lang/Research_summarizer.git]
cd Research_summarizer

### 2. Set Up Environmental Variables
create a .env file in the root directory using :
**cp .env.example .env**

open .env and add your unique Gemini API token :
**GEMINI_API_KEY=your_actual_api_key_here**

### 3. Install Dependencies
**pip install -r reuirements.txt**

### 4. Run the Application Locally
**python app.py**

open your browser and navigate to
*http://127.0.0.1:8080*

## Deployment via Railway App
To host this Flask application live on Railway:

**Prepare Repository**: Ensure your project directory contains a requirements.txt file and a Procfile containing the entry point command.
**Connect GitHub**: Log into Railway, click New Project, and select Deploy from GitHub repo. Choose this repository.
**Configure Environment Variables**:
Navigate to the Variables tab in your Railway project dashboard.
Add your GEMINI_API_KEY along with your secret token value.
**Deploy**: Railway automatically detects the Python environment and builds the containerized app live.

## Project Reflection

**What was the hardest part of building this?**
Coming from a mechanical engineering background, I had never built a web app before. The hardest part was figuring out how to connect my Python backend with the HTML frontend and managing errors. At first, if I left the input box empty or if my internet dropped, the whole app would crash with an ugly technical error screen. Learning how to use try-except blocks in Python and using Flask's flash messages to show a friendly error popup on the screen instead of letting the app break took me hours of debugging, but it taught me a lot about making robust code.

**What would you improve with more time?**
Right now, the app only works if you copy and paste text directly into a box. If I had more time, I would add a file upload feature so users could drop a full PDF research paper directly into the app. I also want to learn how to connect a simple database like SQLite so users can save their past summaries and look at them later instead of losing them when they refresh the page.

**What skill from this program do you now feel genuinely confident in?**
I feel really confident in working with the Gemini API and prompt engineering. At first, APIs sounded like complex software jargon, but now I know exactly how to write a Python script to send requests, catch API errors gracefully, and get structured data back. Learning how to control the AI's output using clean prompts was super exciting and makes me want to build more smart tools.

## Author
*Aryan Shende*
