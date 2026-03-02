"""
Assistente RAG de Políticas Internas (RH)
- Streamlit (interface)
- LangChain com LCEL (orquestração)
- FAISS (banco vetorial)
- OpenAI (embeddings + LLM)
"""

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Lógica do agente do RAG

def carregar_pdf(): # Ler o pdf e extrair o texto do pdf
    pdf_loader = PyPDFLoader("politica_rh.pdf")
    texto = pdf_loader.load()
    return texto

texto_pdf = carregar_pdf()

def separar_em_blocos(texto_pdf):
    separador = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200)
    lista_blocos = separador.split_documents(texto_pdf)
    return lista_blocos

lista_blocos = separar_em_blocos(texto_pdf)

# Embedding

def criar_banco_vetores(lista_blocos):
    ferramenta_embedding = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
    banco_vetores = FAISS.from_documents(lista_blocos, ferramenta_embedding)
    return banco_vetores

banco_vetores = criar_banco_vetores(lista_blocos)

# Lógica do agente de IA

def criar_chain_agente():

    prompt_template = ChatPromptTemplate.from_template("""Você é um assistente de RH que responde perguntas sobre políticas internas da empresa.
    Use APENAS as informações do contexto abaixo para responder.
    Se não encontrar a resposta diga claramente que não sabe responder.
    Responda em português do Brasil, de forma clara e objetiva. 
    
    Contexto: {context} 
    
    A pergunta: {question}
    Resposta:""")

    buscador_contexto = banco_vetores.as_retriever()

    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

    chain = ({"context": buscador_contexto, "question": RunnablePassthrough()} 
             | prompt_template 
             | llm 
             | StrOutputParser())
    
    return chain