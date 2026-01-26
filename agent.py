import asyncio
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import google, noise_cancellation
from ai_prompts import behavior_prompts, reply_prompts

load_dotenv()

async def entrypoint(ctx: agents.JobContext):
    print(f"\n--- AURA AI BY MUHAMMAD SHAYAN IS ONLINE ---")
    
    # Hum 'Puck' voice use kar rahe hain jo bohot natural lagti hai
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(voice="Puck")
    )
    
    await session.start(
        room=ctx.room,
        agent=Agent(instructions=behavior_prompts),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
            video_enabled=True 
        )
    )

    await ctx.connect()
    await session.generate_reply(instructions=reply_prompts)

if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))