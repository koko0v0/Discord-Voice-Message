# Discord Voice Message API Wrapper

## Overview
This Python script enables the automatic uploading and sending of voice messages in Discord channels. It provides a convenient way to handle voice messages through Discord's API.

## Preview
![demo](images/demo.png)

## Features
- Upload voice messages to Discord channels.
- Send voice messages with audio attachments.
- Automatic handling of audio file uploading and message sending.

## Requirements
- Python 3.7 or higher
- `requests` library

## Installation
1. Clone this repository or download the script.
2. Install the required Python libraries:
``` bash
pip install requests
```

## Setup
Before using the script, you need to set your Discord bot token:
1. Obtain a Discord bot token from the Discord Developer Portal.
2. In the script, replace TOKEN = None [line 4] with your bot token, like this:
```python
TOKEN = "your_discord_bot_token_here"
```

## Usage
To use the script, simply run it with Python and provide the necessary parameters:
``` bash
python voice_message.py
```

## Functions
- upload_voice_message(channel_id, audio_file_path): Uploads a voice message to the specified Discord channel.
- send_voice_message(channel_id, audio_file_path, audio_duration): Sends a voice message to the specified Discord channel.

## Parameters
- channel_id: The ID of the Discord channel where the message will be sent.
- audio_file_path: The file path of the audio message.
- audio_duration: The duration of the audio message in seconds (optional).

## Contributing
Contributions to this project are welcome. Please open an issue or pull request on the project's GitHub page.

The original idea for this project was contributed by a member @LostMyInfo<lostmyinfo> from the official Discord Developers server. We are grateful for his innovative idea and encourage similar contributions from the community.

## License
---
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
