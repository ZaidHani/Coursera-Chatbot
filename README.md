# Coursera-Chatbot
This repo has the process of making a chatbot using langchain, I've used Gemini as an LLM and Pinecone as a vector database, this chatbot was built with 3 steps.

## step 1: preparing the data
The first step to build this chatbot was to get a data suitable for a chatbot. I've picked this dataset I've found on Kaggle: https://www.kaggle.com/datasets/khusheekapoor/coursera-courses-dataset-2021
After chosing this dataset I've cleaned it and normalized it so it can fit in the vector database.

## step 2: inserting into the vector database
After cleaning the data it was time to insert it into Pinecone, inserting the data was a little bit of a challenge since it was the first time I've used Gemini to make a chatbot, but I've figured it out and used 'models/embedding-001' as an embdding model

## step 3: making the chatbot
Building the chatbot was the most challenging part, I've used multiple langchain chains before I've finally choose the 'RetrievalQA' chain. It was the most fitting chain for the purpose of this bot. After glueing everything using langchain I've deployed the bot using stremlit.

### you can check the chatbot on this link:
https://zaid-mentorness.streamlit.app/
