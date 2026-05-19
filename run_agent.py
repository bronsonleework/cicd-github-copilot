import asyncio
from copilot import CopilotClient
from copilot.session import PermissionHandler

async def main():
    async with CopilotClient() as client:
        async with await client.create_session(
            model="gpt-4o",
            on_permission_request=PermissionHandler.approve_all
        ) as session:

            # must be STRING, not dict
            response = await session.send_and_wait(
                "Review the repository for security vulnerabilities. Output a concise markdown report with severity levels."
            )

            # print raw first
            print(response)

asyncio.run(main())
