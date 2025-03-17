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
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tasks.logintask import task
from controller.stockcontroller import controller

load_dotenv()


async def siteValidation():
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
    history = await agent.run()
    test_result = history.final_result
    print(test_result)

asyncio.run(siteValidation())