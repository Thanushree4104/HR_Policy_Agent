""" Step 3: turn text into numbers (vectors) using JINA"""

from langchain_community.embeddings import JinaEmbeddings
from hr_assistant import config

def get_embedding_model():
    """ Returns a Jina embedding model.
    Reads JINA key from the environment"""
    return JinaEmbeddings(model_name = config.EMBEDDING_MODEL_NAME)
