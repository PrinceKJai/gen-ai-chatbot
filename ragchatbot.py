import pdfplumber
import streamlit as st
from langchain_text_splitters import RecursiveCharacterTextSplitter

st.header("Gen AI Chatbot")

st.sidebar.header("AI Chatbot")

with st.sidebar:
    st.title("Your documents")
    file = st.file_uploader("Upload your pdf documents and start asking questions", type="pdf")

#Extract content from PDF and chuck it
if file is not None:
    #extract text from the PDF
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text = text + page.extract_text() + "\n"
    #st.write(text)

    #Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ". ", " ", ""],
        chunk_size=1000,
        chunk_overlap = 200
    )
    chunks = text_splitter.split_text(text)
    st.write(chunks)
