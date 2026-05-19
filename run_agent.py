import asyncio
from copilot import CopilotClient

async def main():
    client = CopilotClient()

    # Start Copilot session
    await client.start()

    # ✅ Select Claude Opus 4.7
    session = await client.create_session({
        "model": "gpt-4o",
        "streaming": False
    })

    # Send prompt
    response = await session.send_and_wait({
        "prompt": """
        Review the repository for security vulnerabilities.
        Output a concise markdown report with severity levels.
        """
    })

    print(response["text"])

if __name__ == "__main__":
    asyncio.run(main())