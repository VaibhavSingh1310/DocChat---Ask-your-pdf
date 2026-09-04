import streamlit as st

from rag.extract import extract_text
from rag.chunk import chunk_text
from rag.embed_store import VectorStore
from rag.generate import generate_answer

st.set_page_config(page_title="DocChat", page_icon="📄")
st.title("📄 DocChat — Ask questions about your PDF")

if "store" not in st.session_state:
    st.session_state.store = None

uploaded = st.file_uploader("Upload a PDF", type="pdf")

if uploaded and st.session_state.store is None:
    with st.spinner("Reading and indexing your document..."):
        text = extract_text(uploaded)
        chunks = chunk_text(text)
        store = VectorStore()
        store.build(chunks)
        st.session_state.store = store
    st.success(f"Indexed {len(chunks)} chunks. Ask away!")

if st.session_state.store:
    query = st.text_input("Ask a question about the document")
    if query:
        with st.spinner("Thinking..."):
            relevant = st.session_state.store.search(query)
            answer = generate_answer(query, relevant)
        st.write(answer)
        with st.expander("Sources used"):
            for c in relevant:
                st.caption(c[:300] + "...")
