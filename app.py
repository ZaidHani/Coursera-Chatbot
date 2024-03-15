# importing librareis
import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from pinecone import Pinecone as pc
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain_pinecone import PineconeVectorStore
import os

#loading apis
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

# Loading Pinecone
pinecone_environment = 'gcp-starter'
pc = pc()
index = pc.Index("mychatpot")

# function for getting the answer
def get_answer(query):

    model = 'models/embedding-001'
    embed = GoogleGenerativeAIEmbeddings(model=model)

    vstore = PineconeVectorStore(embedding=embed, index=index, text_key='text')
    retriever = vstore.as_retriever(k=10)

    llm = ChatGoogleGenerativeAI(model='gemini-pro', temperature=0.7 ,convert_system_message_to_human=True)

    template = """You play the role of an assistant who will help users to find courses suited to them.
A user is not related to the context, guide the student to ask you about Coursera's courses.
Your job is to speak to the user and answer their question if they had one.
Your creator is Zaid Hani from Jordan, and he is a Data Science student.\n\n
context: \n {context} \n
user input: \n {question} \n
Answer:"""

    QA_CHIAN_PROMPT = PromptTemplate.from_template(template)

    qa_chian = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type_kwargs={
            'prompt':QA_CHIAN_PROMPT
        }
    )
    response = qa_chian.invoke(query)
    return response['result']

st.title('Courses Chatbot')
st.markdown('This chatbot is a part of Mentorness AI Internship, this chatbot will answer your questions about Coursera website courses.')

# Accept user input
if prompt := st.chat_input("Talk with Coursera's Courses Bot"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
        
if prompt == None:
    prompt = 'Hello'
    
# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write(get_answer(prompt))