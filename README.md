# Projeto_Agente_IA_Python

<center>
  <img width="900" height="589" alt="image"
       src="https://github.com/user-attachments/assets/0467b7a7-217a-4027-8436-2dd6222e7bf5" />
</center>


## 📌 Descrição

Este projeto é baseado em um projeto de um aulão e visa criar um **agente de IA**, capaz de ler os dados de um arquivo PDF com politicas de Recursos Humanos da empresa, para poder responder duvidas referentes à Recursos Humanos, baseado no arquivo PDF lido. Em tecnologia, esta operação é chamada de RAG (Retrieval Augmented Generation).

Para realizar o RAG foram utilizadas as seguintes bibliotecas Python:
  - Streamlit: Utilizado para criar a interface do usuário, simulando um chatbot;
  - Langchain: Utilizado para instalar o langchain_core, este com bibliotecas auxiliares;
  - Langchain-community: Utilizado para ler arquivos em PDF e para criar o banco vetorial FAISS;
  - Langchain-google-genai: Utilizado para trabalhar com o Google Gemini;
  - Langchain-text-splitters: Utilizado para repartir, criando blocos de texto; 
  - Faiss-cpu: Utilizado como auxiliar para o banco vetorial FAISS;
  - Pypdf: Utilizado como auxiliar a leitura de arquivos em PDF;
  - Python-dotenv: Utilizado para trabalhar com ambientes dotenv, isolando dados sensiveis do Gemini.




Como executar a aplicação:

- Execute o comando de instalação das **bibliotecas Python** em seu terminal: pip install -r requirements.txt
- Crie um arquivo .env com a sua chave Gemini, seguindo o padrão: GEMINI_API_KEY=chave
- Inicialize o **Streamlit** através do comando em seu terminal: streamlit run app_basic.py.
- Faça perguntas relacionadas à politica de Recursos Humanos, por exemplo: "Com quantas horas de antecedência preciso comunicar a minha falta?" ou "A empresa oferece plano de saúde?"

---

## 🗂 Estrutura do Projeto

```bash
Projeto_Agente_IA_Python/
├── .env                      # Arquivo com a chave do Gemini
├── app_basic.py              # Arquivo com o agente de IA e todo o seu funcionamento
├── interface.py              # Arquivo com a interface da aplicação
├── politica_rh.pdf           # Arquivo pdf com as politicas de recursos humanos da empresa
├── requirements.txt          # Arquivo com as bibliotecas Python utilizadas
```
