import os
import requests

TOKEN = None # <--PUT YOUR DISCORD BOT TOKEN HERE-->

def upload_voice_message(channel_id, audio_file_path):
    """
    Uploads a voice message to Discord and returns the filename. This is useful for uploading files that are part of a voice message.
    
    @param channel_id - The ID of the channel to upload to.
    @param audio_file_path - The path to the audio file.
    
    @return The filename of the uploaded file. Note that it is important to check the return value of this function
    """

    with open(audio_file_path, "rb") as file:
        voicemessage = file.read()

    upload_url = f"https://discord.com/api/v10/channels/{channel_id}/attachments"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bot {TOKEN}",
    }
    data = {
        "files": [
            {
                "file_size": len(voicemessage),
                "filename": os.path.basename(audio_file_path),
                "id": "2",
            }
        ]
    }

    response = requests.post(
        upload_url, json=data, headers=headers, timeout=10
    )

    response_json = response.json()

    # upload the voice message data to upload_url
    put_url = response_json["attachments"][0]["upload_url"]
    requests.put(put_url, data=voicemessage, timeout=10)

    return response_json["attachments"][0]["upload_filename"]


def send_voice_message(channel_id, audio_file_path, audio_duration):
    """
    Sends a voice message with an audio attachment. This is a wrapper around the discord api/v10/attachments endpoint
    
    @param channel_id - The channel to send the voice message with
    @param audio_file_path - The path to the audio file that will be uploaded to the discord channel.
    @param audio_duration [optional] - The duration of the audio in seconds, any value will works
    
    @return The filename of the uploaded
    """
    
    if TOKEN is None:
        print("Empty discord bot token")
        exit(-1)

    upload_filename = upload_voice_message(channel_id, audio_file_path)

    # Send the message with the attachment
    message_url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
    headers = {
        "Authorization": f"Bot {TOKEN}",
        "content-type": "application/json",
    }
    
    """
    Voice Messages - https://discord.com/developers/docs/resources/channel#attachment-object

    Voice messages are messages with the IS_VOICE_MESSAGE flag. They have the following properties.

        They cannot be edited.
        Only a single audio attachment is allowed. No content, stickers, etc...
        The attachment has additional fields: duration_secs and waveform.

    The waveform is intended to be a preview of the entire voice message, with 1 byte per datapoint encoded in base64. Clients sample the recording at most once per 100 milliseconds, but will downsample so that no more than 256 datapoints are in the waveform.

    As of 2023-04-14, clients upload a 1 channel, 48000 Hz, 32kbps Opus stream in an OGG container. The encoding, and the waveform details, are an implementation detail and may change without warning or documentation.
    """
    
    data = {
        "flags": 8192,
        "attachments": [
            {
                "id": "0",
                "filename": os.path.basename(audio_file_path),
                "uploaded_filename": upload_filename,
                "duration_secs": audio_duration,  # [optional] any value will works
                "waveform": "FzYACgAAAAAAACQAAAAAAAA=",  # Replace with actual waveform but you can just use this one
            }
        ],
    }

    req = requests.post(
        message_url, json=data, headers=headers, timeout=10
    )

    return req


if __name__ == "__main__":
    send_voice_message(channel_id="", audio_file_path="audio.wav", audio_duration=10)