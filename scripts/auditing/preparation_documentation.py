# auditing/preparation_documentation.py

import os
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

def prepare_documentation(contract_path):
    loader = TextLoader(contract_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)
    
    embeddings = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(docs, embeddings)
    
    return vectordb

# Usage
contract_path = "path/to/smart_contract.sol"
vectordb = prepare_documentation(contract_path)