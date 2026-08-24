""" Step 4: Store chunk embedding in FAISS so that we can search them"""
import os 
from langchain_community.vectorstores import FAISS
from hr_assistant import config
from hr_assistant.embeddings import get_embedding_model


# build_vector_store

def build_vector_store(chunks):
    """ Embed every chunk and build a searchable FAISS index in memory."""
    embeddings_model = get_embedding_model()
    return FAISS.from_documents(chunks, embeddings_model)

## save vector store 

def save_vector_store(vector_store , path : str = config.VECTORE_STORE_PATH)-> None:
    """ Save the FAISS index to disk so we don't have to rebuils it every time"""
    vector_store.save_local(path)

def load_vector_store(path: str =config.VECTORE_STORE_PATH):
    """ Load a previously saved FAISS index from disk"""
    embeddings_model = get_embedding_model()
    return FAISS.load_local(path, embeddings_model, allow_dangerous_deserialization=True)

def vector_store_exists(path: str = config.VECTORE_STORE_PATH)-> bool:
    """ Check if a saved FAISS index already exists on disk."""
    return os.path.exists(os.path.join(path, "index.faiss"))

def get_retriever(vector_store, k: int = config.TOP_K_RESULTS):
    """ Turn a vector store into a retriever that returns the top-k matching chunks."""
    return vector_store.as_retriever(search_kwargs={"k": k})
