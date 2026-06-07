import os
from datetime import datetime
import uuid
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
import gradio as gr

from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

from langchain_tavily import TavilySearch

load_dotenv()

def get_date():
    """Get the current date"""
    print("Getting today's date...")
    return datetime.now().strftime("%Y-%m-%d")

web_search = TavilySearch()

conn = sqlite3.connect("agent_history.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)

llm = ChatOllama(model="qwen3.5:4b")

system_prompt = """
You are a helpful assistant.
Answer all user's questions to the best of your ability.
Use the get_date tool ONLY when the user is asking about the today's date.
Use the web_search tool for answering questions that require up-to-date information.
"""

agent = create_agent(
    model=llm, 
    tools=[get_date, web_search], 
    system_prompt=system_prompt, 
    checkpointer=checkpointer)

def handle_query(query, history, thread_id):
    config = {"configurable": {"thread_id": thread_id}}
    response = agent.invoke({"messages": [{"role": "user", "content": query}]}, config=config)
    return response["messages"][-1].content

with gr.Blocks() as demo:
    gr.Markdown("## AI Agent with Ollama and Gradio")
    thread_id = gr.State(value=lambda: str(uuid.uuid4()))
    gr.ChatInterface(fn=handle_query, title="AI Agent", additional_inputs=[thread_id])

if __name__ == "__main__":
    demo.launch()