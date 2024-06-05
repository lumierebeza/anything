import discord
import os
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

load_dotenv()

# Initialize the Discord bot with the necessary intents
intents = discord.Intents.default()
intents.messages = True

# Check if message_content intent is available
if hasattr(intents, 'message_content'):
    intents.message_content = True

client = discord.Client(intents=intents)

# Get the token from the environment variables
token = os.getenv('TOKEN')

print('This is my EC2 metadata region:', ec2_metadata.region)
print('This is my EC2 metadata instance ID:', ec2_metadata.instance_id)

@client.event
async def on_ready():
    # Print a message when the bot is logged in and ready
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    # Get the username, channel, and message content
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    # Log the message
    print(f'Message "{user_message}" by {username} on {channel}')

    # Prevent the bot from replying to itself
    if message.author == client.user:
        return

    # Check if the message is in the "random" channel
    if channel == "random":
        # Respond to greetings
        if user_message.lower() == "bangtan?":
            await message.channel.send(f'ARMY! {username} Your EC2 Data: {ec2_metadata.region}')
        elif user_message.lower() == "hello":
            await message.channel.send(f'Hello {username}')
        elif user_message.lower() == "ec2 data":
            await message.channel.send(f'Your instance data is: Region - {ec2_metadata.region}, Instance ID - {ec2_metadata.instance_id}')

# Run the bot with the token
client.run(token)
