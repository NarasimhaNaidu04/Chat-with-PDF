import streamlit as st
import google.generativeai as genai
import PyPDF2

genai.configure(api_key="AIzaSyAGsaFMI6fGTqZc2SxBGTrJAtRqyqKxAc4")
model = genai.GenerativeModel("gemini-2.5-flash")

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
        
        response = model.generate_content(prompt)
        st.write(response.text)