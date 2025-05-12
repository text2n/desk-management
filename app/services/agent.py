import os
from typing import Annotated
# from datetime import date, timedelta # Not strictly needed if using SQL date functions
from fastapi import Depends
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_core.exceptions import OutputParserException
from app.core.config import settings
from app.core.logger import logger

class Agent:
    def __init__(self):
        langchain.debug = True
        try:
            self.db = SQLDatabase.from_uri(settings.DATABASE_URI, include_tables=["desks", "desk_bookings"])
            settings.DEBUG and print("Database connection successful.")
            # print(db.get_table_info()) # Uncomment to see the schema LangChain sees
        except Exception as e:
            logger.error(f"Error connecting to database: {e}")
            exit()

        # Initialize the Gemini LLM
        try:
            self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0)
            settings.DEBUG and print("Gemini LLM initialized.")
        except Exception as e:
            settings.DEBUG and print(f"Error initializing Gemini LLM: {e}")
            logger.error(f"Error initializing Gemini LLM: {e}")
            exit()
        #agent executor
        try:
            self.agent_executor = create_sql_agent(
                llm=self.llm,
                db=self.db,
                agent_type="openai-tools",
                verbose=bool(settings.DEBUG)
            )
            settings.DEBUG and print("SQL Agent created.")
        except Exception as e:
            logger.error(f"Error creating SQL agent: {e}")
            exit()

    def ask_question(self, question: str):
        """
        Generate SQL queries for the natural language question and return results in natural language
        """
        logger.info(f"Asking: '{question}'")

        try:
            response = self.agent_executor.invoke({"input": question})
            logger.info(f"Response: '{question}' \n {response['output']}")
        except OutputParserException as e:
            logger.error(f"Details: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
        return response["output"]


AgentDep = Annotated[Agent, Depends(Agent)]