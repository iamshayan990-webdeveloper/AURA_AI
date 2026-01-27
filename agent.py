# agent.py
import asyncio
from dotenv import load_dotenv
from livekit.agents import JobContext, WorkerOptions, cli, AgentSession, Agent, RoomInputOptions
from livekit.plugins import google, noise_cancellation
from ai_prompts import behavior_prompts, reply_prompts

load_dotenv()

async def entrypoint(ctx: JobContext):
    print(f"\n--- AURA AI (MALE) BY MUHAMMAD SHAYAN IS ONLINE ---")

    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(voice="Puck"), 
    )

    await session.start(
        room=ctx.room,
        agent=Agent(instructions=behavior_prompts),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
            video_enabled=True
        )
    )

    # Updated Male Greeting
    await session.say(reply_prompts, allow_interruptions=True)

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))