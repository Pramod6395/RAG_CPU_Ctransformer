import streamlit as st
from langchain.prompts.prompt import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from ctransformers import AutoModelForCausalLM
import os



llm = AutoModelForCausalLM.from_pretrained('TheBloke/Llama-2-7B-Chat-GGML', model_file = '/home/pramodpatil/Desktop/GPU/Llama2-Medical-Chatbot/llama-2-7b-chat.ggmlv3.q2_K.bin')

st.title("Medical PDF Knowledge Based")


# loading main db
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L12-v2')

current_directory = os.getcwd()

# Define the relative path to the server_db_file folder
relative_path = "index_data"

# Construct the complete path
main_db_directory = os.path.join(current_directory, relative_path)

vector_store = FAISS.load_local(main_db_directory, embeddings)

template = """
[INST] <<SYS>>
Only provide answers using information from the context provided and if you do not the answer state that the data is not contained in your knowledge base and stop your response<</SYS>>
context:{context}
Question: {query}
[/INST]
"""

prompt_template = PromptTemplate(
    input_variables=["query","context"], template=template
)


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        docs=vector_store.similarity_search(prompt,k=3)
        prompt1=prompt_template.format(query=prompt,context=docs)
        for response in llm(prompt1 ,max_new_tokens=1000, stream=True):
            full_response += (response or "")
            message_placeholder.markdown(full_response + "▌")
        full_response = full_response.replace("</s>", "").strip()

        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})