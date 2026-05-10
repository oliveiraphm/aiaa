import asyncio
import os
from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")


async def main():

    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini",
        api_key=api_key,
    )

    engineer = AssistantAgent(
        name="Engineer",
        model_client=model_client,
        system_message="""
        You are a professional Python engineer, known for your expertise in software development.
        You create clean, efficient, well-structured code.
        """,
    )

    reviewer = AssistantAgent(
        name="Reviewer",
        model_client=model_client,
        system_message="""
        You are a strict code reviewer.
        You analyze code for bugs, inefficiencies, and bad practices.
        Return a structured list of issues and improvements.
        """,
    )

    team = RoundRobinGroupChat(
        participants=[engineer, reviewer],
        max_turns=6,
    )

    task = "Write a snake game using Pygame."

    await Console(
        team.run_stream(task=task)
    )

    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())