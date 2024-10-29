# Penguin Bot

**Penguin Bot** is a versatile Discord bot designed for community management, moderation, and interactive fun. Fully customizable through the [Penguin Bot Dashboard](#on-dev), this bot is ideal for server owners looking for a powerful tool that handles everything from user engagement to server moderation.

## Features
- **Command Prefix**: Customize the command prefix to match your server’s style.
- **Welcome Message**: Automatically welcome new members in a designated channel.
- **Vent Channel**: Allow users to vent or share thoughts anonymously.
- **Fun and Moderation Commands**: Built-in commands for games, moderation tools, and more.
- **User-Friendly Dashboard**: Configure all bot settings easily through the dashboard.

## Tech Stack

- **Bot Framework**: [discord.py](https://discordpy.readthedocs.io/)
- **Backend API**: [Flask](https://flask.palletsprojects.com/) with MongoDB for data storage.
- **Database**: [MongoDB](https://www.mongodb.com/) to store server-specific configurations.

## Setup

### Prerequisites

- Python 3.8+
- MongoDB (local or hosted on MongoDB Atlas)
- Discord Developer Bot Token (from the [Discord Developer Portal](https://discord.com/developers/applications))

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mikeharrison32/penguin.git
   cd Penguin
   ```

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   Create a `.env` file with your bot token and MongoDB URI:

   ```plaintext
   TOKEN=<YOUR_DISCORD_BOT_TOKEN>
   MONGO_URI=<YOUR_MONGODB_CONNECTION_STRING>
   ```

### Running the Bot

Start the bot with the following command:

```bash
python app.py
```

