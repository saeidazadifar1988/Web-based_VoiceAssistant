# AI Voice Assistant with Flask, OpenAI's GPT-3 & IBM Watson

A full-stack AI-powered voice assistant built with **Flask**, **OpenAI GPT**, **IBM Watson Speech-to-Text (STT)**, and **IBM Watson Text-to-Speech (TTS)**.

The application allows users to speak naturally through their microphone, converts speech into text, generates an AI response using OpenAI, converts the response back into speech, and returns both text and audio to the browser.

---

##  Features

- 🎤 Speech-to-Text using IBM Watson STT
- 🤖 AI-powered conversations using OpenAI GPT
- 🔊 Text-to-Speech using IBM Watson TTS
- 🌐 Flask backend with REST API
- 💻 Browser-based frontend
- 🐳 Dockerized application
- 🎯 Voice selection support
- 🔄 End-to-end speech conversation pipeline

---

# Project Architecture

```
User
 │
 │ Voice
 ▼
Browser (Frontend)
 │
 │ POST Audio
 ▼
Flask Server
 │
 ├──────────────► IBM Watson Speech-to-Text
 │                    │
 │                    ▼
 │            Transcribed Text
 │
 ├──────────────► OpenAI GPT
 │                    │
 │                    ▼
 │             AI Generated Response
 │
 ├──────────────► IBM Watson Text-to-Speech
 │                    │
 │                    ▼
 │               Audio Response
 │
 ▼
Browser
(Text + Voice)
```

---

# Project Structure

```
voice-chatapp/
│
├── server.py              # Flask backend
├── worker.py              # AI helper functions
├── templates/
│   └── index.html         # Frontend
├── static/
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

# Technologies Used

- Python
- Flask
- OpenAI API
- IBM Watson Speech-to-Text
- IBM Watson Text-to-Speech
- Docker
- HTML
- JavaScript

---

# Workflow

The application follows this pipeline:

1. User records speech.
2. Audio is sent to the Flask server.
3. Flask sends audio to IBM Watson Speech-to-Text.
4. Watson returns the recognized text.
5. The recognized text is sent to OpenAI GPT.
6. GPT generates a response.
7. The response is sent to IBM Watson Text-to-Speech.
8. Watson returns synthesized audio.
9. Flask sends both the response text and audio back to the browser.

---

# Flask API Endpoints

## GET /

Loads the frontend.

**Response**

```
index.html
```

---

## POST /speech-to-text

Converts recorded speech into text.

### Request

Binary audio data.

### Response

```json
{
  "text": "Hello, how are you?"
}
```

---

## POST /process-message

Processes the user's message using OpenAI and converts the response to speech.

### Request

```json
{
    "userMessage":"What is Artificial Intelligence?",
    "voice":"en-US_MichaelV3Voice"
}
```

### Response

```json
{
    "openaiResponseText":"Artificial Intelligence is...",
    "openaiResponseSpeech":"<base64 encoded wav>"
}
```

---

# Worker Functions

## speech_to_text(audio_binary)

- Sends audio to IBM Watson Speech-to-Text
- Returns transcribed text

---

## openai_process_message(user_message)

- Sends prompt to OpenAI GPT
- Returns AI-generated response

---

## text_to_speech(text, voice)

- Sends text to IBM Watson Text-to-Speech
- Returns WAV audio

---

# Running the Project

## 1. Clone Repository

```bash
git clone <repository-url>
cd voice-chatapp
```

---

## 2. Build Docker Image

```bash
docker build . -t voice-chatapp-powered-by-openai
```

---

## 3. Run Container

```bash
docker run -p 8000:8000 voice-chatapp-powered-by-openai
```

The application will be available at:

```
http://localhost:8000
```

---

# IBM Watson Services

## Speech-to-Text

Base URL

```
https://sn-watson-stt.labs.skills.network
```

Example API

```
POST /speech-to-text/api/v1/recognize
```

---

## Text-to-Speech

Base URL

```
https://sn-watson-tts.labs.skills.network
```

Example API

```
POST /text-to-speech/api/v1/synthesize
```

---

# OpenAI Configuration

The application uses the Chat Completions API.

Example configuration:

```python
model="gpt-5-nano"
```

System prompt:

```
Act like a personal assistant.
Respond to questions,
translate sentences,
summarize news,
and give recommendations.
Keep responses concise.
```

---

# Docker

The Dockerfile performs the following steps:

- Creates a Python environment
- Copies project files
- Installs dependencies
- Starts the Flask server

Build:

```bash
docker build . -t voice-chatapp-powered-by-openai
```

Run:

```bash
docker run -p 8000:8000 voice-chatapp-powered-by-openai
```

---

# Example Conversation

**User**

> Tell me about machine learning.

↓

**Speech-to-Text**

```
Tell me about machine learning.
```

↓

**OpenAI**

```
Machine learning is a branch of artificial intelligence that enables computers to learn patterns from data without being explicitly programmed.
```

↓

**Text-to-Speech**

```
Audio (.wav)
```

↓

**Browser**

Displays:

- Response text
- Spoken audio

---

# Testing

After starting the application:

- Open the application in your browser.
- Allow microphone permissions.
- Record your voice.
- Submit text messages.
- Select different voices.
- Verify both text and speech responses.

---

# Notes

- Ensure Docker is installed.
- Grant microphone permissions in your browser.
- Rebuild the Docker image after modifying the source code.
- Keep Python indentation consistent (use spaces instead of mixing tabs and spaces).

---

# Future Improvements

- Conversation history
- Streaming OpenAI responses
- Multiple language support
- User authentication
- Voice activity detection
- Real-time speech recognition
- Persistent chat sessions
- Better UI/UX
- Response caching
- Deployment on cloud platforms

---

# License

This project is intended for educational purposes and demonstrates how to integrate Flask, OpenAI GPT, IBM Watson Speech-to-Text, and IBM Watson Text-to-Speech into a complete AI voice assistant.