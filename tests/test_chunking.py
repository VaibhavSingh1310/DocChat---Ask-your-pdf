import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from rag.chunk import chunk_text


def test_chunk_count():
    text = " ".join(["word"] * 1000)
    chunks = chunk_text(text, chunk_size=500, overlap=50)
    assert len(chunks) == 3


def test_chunk_overlap():
    text = " ".join([str(i) for i in range(100)])
    chunks = chunk_text(text, chunk_size=50, overlap=10)
    first_chunk_words = chunks[0].split()
    second_chunk_words = chunks[1].split()
    assert first_chunk_words[-10:] == second_chunk_words[:10]


def test_empty_text():
    assert chunk_text("") == []
