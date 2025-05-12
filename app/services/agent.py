import os
import datetime
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

system_message = """
You are an agent designed to interact with a SQL database.
Today's date is {today}.
Given an input question, create a syntactically correct {dialect} query to run, 
then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, 
always limit your query to at most {top_k} results.

If a date is required for the query and the user does not specify one, assume today's date: {today}.

You can order the results by a relevant column to return the most interesting 
examples in the database. Never query for all the columns from a specific table, 
only ask for the relevant columns given the question.

You have access to tools for interacting with the database.

Only use the below tools. Only use the information returned by the below tools to construct 
your final answer.

You MUST double-check your query before executing it. If you get an error while executing a query,
rewrite the query and try again.

The only DML statements allowed are INSERT and UPDATE for a single record.
DO NOT insert or update multiple records.
DO NOT make any other DML statements (e.g., DELETE, DROP) to the database.

If the question does not seem related to the database, just return "I don't know" as the answer.

If you are showing available DESKS, show notes along with them
""".format(
    dialect="mywql",
    top_k=10,
    today=datetime.date.today().isoformat(),
)

class Agent:
    def __init__(self):
        #langchain.debug = True
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
                verbose=bool(settings.DEBUG),
                prefix=system_message,
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