import asyncio
from copilot import CopilotClient

async def main():
    async with CopilotClient() as client:
        async with await client.create_session(
            model="gpt-4o"   # ✅ correct
        ) as session:

            response = await session.send_and_wait({
                "prompt": """ Review the repository for security vulnerabilities.
        Output a concise markdown report with severity levels.
        """
            })

            print(response["text"])

asyncio.run(main())