import os
from dotenv import load_dotenv
import streamlit as st

from src.pdf_processor import extract_text_from_pdf
from src.utils import chunk_text
from src.embeddings import embed_texts, embed_text
from src.rag_pipeline import FaissRAG

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI-Powered PDF Document Assistant", layout="wide")

def check_api_key():
    if not OPENAI_API_KEY or OPENAI_API_KEY == "your_api_key_here":
        st.error("Missing OpenAI API key. Add it to your .env file as OPENAI_API_KEY.")
        return False
    return True


def main():
    st.title("AI-Powered PDF Document Assistant")
    st.write("Upload a PDF, then ask questions about its content. Uses embeddings + FAISS + GPT.")

    if not check_api_key():
        return

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    if "rag" not in st.session_state:
        st.session_state.rag = None

    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file is not None:
        try:
            pages = extract_text_from_pdf(uploaded_file)
            st.success(f"Loaded: {uploaded_file.name}")
            st.write(f"Pages extracted: {len(pages)}")
            # Combine pages into a single text with page markers
            texts = []
            metadatas = []
            for pnum, text in pages:
                if text.strip():
                    texts.append(text)
                    metadatas.append({"page": pnum, "source": uploaded_file.name})

            if not texts:
                st.error("No extractable text found in the PDF.")
            else:
                # Chunk text into smaller passages for embeddings
                chunks, chunk_metas = chunk_text(texts, metadatas)
                st.write(f"Created {len(chunks)} chunks for embeddings")

                # Create RAG object and build FAISS index
                st.session_state.rag = FaissRAG()
                with st.spinner("Computing embeddings and building FAISS index..."):
                    embeddings = embed_texts(chunks)
                    st.session_state.rag.build_index(embeddings, chunks, chunk_metas)
                st.success("Index ready — ask questions below.")
        except Exception as e:
            st.error(f"Could not process the PDF: {e}")

    # Chat interface
    query = st.text_input("Ask a question about the document:")
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("Clear Chat"):
            st.session_state.chat_history = []

    if query:
        if not st.session_state.rag:
            st.error("Please upload a PDF and wait for the index to be created before asking questions.")
        else:
            try:
                with st.spinner("Searching and generating answer..."):
                    answer, sources = st.session_state.rag.answer_query(query)
                st.session_state.chat_history.append((query, answer, sources))
            except Exception as e:
                st.error(f"Error during question answering: {e}")

    # Display chat history
    if st.session_state.chat_history:
        for q, a, sources in reversed(st.session_state.chat_history):
            st.markdown(f"**User:** {q}")
            st.markdown(f"**AI:** {a}")
            if sources:
                src_lines = ", ".join([f"page {s['page']}" for s in sources])
                st.markdown(f"**Sources:** {src_lines}")


if __name__ == "__main__":
    main()
