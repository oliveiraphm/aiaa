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
You create clean, efficient, well-structured code for games and applications.
""",
    )

    critic = AssistantAgent(
        name="Critic",
        model_client=model_client,
        system_message="""
Critic. You are a game engineer and expert evaluator of game code.

Evaluate across:
- bugs (must be < 5 if any bug exists)
- gameplay quality
- goal compliance
- aesthetics

Return structured scores:
{bugs: 0, gameplay: 0, compliance: 0, aesthetics: 0}

Do NOT suggest code.
Only critique and provide improvement actions.
""",
    )

    team = RoundRobinGroupChat(
        participants=[engineer, critic],
        max_turns=10,
    )

    task = "Write a snake game using Pygame."

    await Console(
        team.run_stream(task=task)
    )

    await model_client.close()


if __name__ == "__main__":
    asyncio.run(main())