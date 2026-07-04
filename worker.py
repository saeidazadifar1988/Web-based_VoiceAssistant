from openai import OpenAI
import requests

openai_client = OpenAI()


def speech_to_text(audio_binary):

    # Set up Watson Speech-to-Text HTTP Api url
    base_url = "https://sn-watson-stt.labs.skills.network"
    api_url = base_url + "/speech-to-text/api/v1/recognize"

    # Set up parameters for our HTTP request
    params = {
        "model": "en-US_Multimedia",
    }

    # Set up the body of our HTTP request
    body = audio_binary

    try:
        # Send a HTTP Post request
        response = requests.post(
            api_url,
            params=params,
            data=body
        )

        response.raise_for_status()

        response = response.json()

        # Parse the response to get our transcribed text
        text = "null"

        if response.get("results"):
            print("speech to text response:", response)

            text = response["results"][0]["alternatives"][0]["transcript"]

            print("recognised text:", text)

        return text

    except Exception as e:
        print("Speech-to-Text Error:", e)
        return "null"


def text_to_speech(text, voice=""):

    # Set up Watson Text-to-Speech HTTP Api url
    base_url = "https://sn-watson-tts.labs.skills.network"
    api_url = (
        base_url
        + "/text-to-speech/api/v1/synthesize?output=output_text.wav"
    )

    # Adding voice parameter in api_url if the user has selected a preferred voice
    if voice != "" and voice != "default":
        api_url += "&voice=" + voice

    # Set the headers for our HTTP request
    headers = {
        "Accept": "audio/wav",
        "Content-Type": "application/json",
    }

    # Set the body of our HTTP request
    json_data = {
        "text": text,
    }

    try:
        # Send a HTTP Post request to Watson Text-to-Speech Service
        response = requests.post(
            api_url,
            headers=headers,
            json=json_data
        )

        response.raise_for_status()

        print("text to speech response:", response)

        return response.content

    except Exception as e:
        print("Text-to-Speech Error:", e)
        return b""


def openai_process_message(user_message):

    # Set the prompt for OpenAI Api
    prompt = (
        "Act like a personal assistant. "
        "You can respond to questions, translate sentences, "
        "summarize news, and give recommendations. "
        "Keep responses concise - 2 to 3 sentences maximum."
    )

    try:
        # Call the OpenAI Api to process our prompt
        openai_response = openai_client.chat.completions.create(
            model="gpt-5-nano",
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            max_completion_tokens=1000
        )

        print("openai response:", openai_response)

        # Parse the response to get the response message for our prompt
        response_text = openai_response.choices[0].message.content

        return response_text

    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I couldn't process your request."