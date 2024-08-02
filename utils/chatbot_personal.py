from langchain_community.document_loaders import PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import create_qa_with_sources_chain
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import streamlit as st
import os
# Define your system instruction
system_instruction = "The assistant should provide detailed explanations."

# Define your template with the system instruction
template = (
    f"{system_instruction} "
    "Combine the chat history and follow up question into "
    "a standalone question. Chat History: {chat_history}"
    "Follow up question: {question}"
)

# Create the prompt template
condense_question_prompt = PromptTemplate.from_template(template)

def chatbot(prompt):


    load_dotenv()

    # Step 1
    raw_documents = PDFMinerLoader("docs/guilherme.pdf").load()

    # Step 2
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100, chunk_overlap=20, length_function=len
    )
    documents = text_splitter.split_documents(raw_documents)

    # Step 3
    embeddings_model = OpenAIEmbeddings(api_key=st.secrets["OPENAI_API_KEY"])
    db = FAISS.from_documents(documents, embeddings_model)

    # Step 4
    retriever = db.as_retriever()

    # Step 5
    llm_src = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-16k",max_tokens= 300)

    # Define your system instruction
    system_instruction = """You are a personal RAG designed to intoduce Guilherme to recruiters.
                        You must answer using only data about Guilherme Alves de Oliveira
                        If you judge the question is not about the provided context respond with 'I don't have this information' in the respective asked language"""

# Define your template with the system instruction
    template = (
    f"{system_instruction} "
    "You must give your answers in the question language, for example, if the question is em portuguese, repond in portuguese"
    )

# Create the prompt template
    condense_question_prompt = PromptTemplate.from_template(template)

    qa_chain = create_qa_with_sources_chain(llm_src)
    retrieval_qa = ConversationalRetrievalChain.from_llm(
        llm_src,
        retriever,
        condense_question_prompt,
        return_source_documents=True,
    )

    # Output
    output = retrieval_qa({
        "question": f"{prompt}",
        "chat_history": []
    })

    return output['answer']