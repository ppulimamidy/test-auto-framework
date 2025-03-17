import os
from langchain_openai import ChatOpenAI
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
from pydantic import BaseModel
from browser_use import Controller, ActionResult
from typing import List
from tasks.logintask import task
from controller.logincontroller import controller   

load_dotenv()

# Configure Gemini
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
agent = Agent(
        task=task,
        # llm=ChatOpenAI(model="gpt-4o"),
        llm=ChatGoogleGenerativeAI(
            model="gemini-2.0-flash",  # Using pro instead of flash
            temperature=0,
            google_api_key=os.environ.get("GEMINI_API_KEY")
        ),
        use_vision=True,
        controller=controller
    )