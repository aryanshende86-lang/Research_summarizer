import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from google import genai
from bs4 import BeautifulSoup 
import markdown 

load_dotenv()

app = Flask(__name__)
client = genai.Client()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/summarize', methods=['POST'])
def summarize():
    topic = request.form.get('topic')
    
    if not topic:
        return jsonify({"error": "Please provide a valid topic"}), 400
        
   
    url = f"http://export.arxiv.org/api/query?search_query=all:{topic}&max_results=2"
    response = requests.get(url)
    arxiv_txt = response.text

    soup = BeautifulSoup(response.text, 'xml')
    entries = soup.find_all('entry')
    
    cleaned_papers_text = ""
    for index, entry in enumerate(entries, start=1):
        title = entry.find('title').text.strip() if entry.find('title') else "No Title"
        summary = entry.find('summary').text.strip() if entry.find('summary') else "No Summary"
        
        cleaned_papers_text += f"Paper {index}:\nTitle: {title}\nSummary Paragraph: {summary}\n\n"

    prompt = f"""
    You are an expert academic assistant and creative writer. Below is the text extracted from the latest research papers.
    For each paper provided, generate a clean breakdown using this exact layout with clear line breaks:
    Also make headings bold.
     [Paper Title Here]
     **Core Objective:** 1-2 sentences on a new line
     **Methodology:** 1-2 sentences on a new line
     **Key Finding/Metric:** 1-2 sentences on a new line
     **Limitations:** 1-2 sentences on a new line
    STRICT RULES: 
    1. DO NOT use any HTML tags like <p>, <strong>, <h3>, or <ul>.
    2. Output only clean, normal plain text.

    Papers Data:
    {cleaned_papers_text}
    """
    
    try:
        ai_response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
             )
        pretty_html_summary = markdown.markdown(ai_response.text)
        return render_template('index.html', summary=pretty_html_summary, topic=topic)
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port =8080)

 