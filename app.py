import streamlit as st
from google import genai
import PyPDF2
import os
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def read_pdf(file):
    text = ""
    reader = PyPDF2.PdfReader(file)
    for page in reader.pages:
        text += page.extract_text()
    return text

st.title("Chat with PDF 🤖")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    pdf_text = read_pdf(uploaded_file)
    
    question = st.text_input("Ask something from PDF")

    if question:
        prompt = f"""
        Answer the question based only on this PDF content:
        
        {pdf_text}
        
        Question: {question}
        """
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        st.write(response.text)