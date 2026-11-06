"""
EV - Enhanced Virtual Intelligence
Configuration & Environment Settings
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Base Directory Paths
BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "database" / "ev_memory.db"
ASSETS_DIR = BASE_DIR / "assets"
LOGS_DIR = BASE_DIR / "logs"

# Ensure directories exist
(BASE_DIR / "database").mkdir(exist_ok=True)
(BASE_DIR / "logs").mkdir(exist_ok=True)
ASSETS_DIR.mkdir(exist_ok=True)

# Load environment variables
load_dotenv(BASE_DIR / ".env")

class Config:
    # Assistant Identity
    NAME = "EV"
    FULL_NAME = "Enhanced Virtual Intelligence"
    VERSION = "2.0.0 PRO"
    USER_NAME = os.getenv("EV_USER_NAME", "Sir")
    
    # AI Engine Configuration (Official Google Gen AI SDK)
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    AI_PROVIDER = os.getenv("AI_PROVIDER", "gemini")  # 'gemini', 'offline'
    AI_MODEL = os.getenv("AI_MODEL", "gemini-3-flash-preview")
    
    # Voice Settings (Microsoft Jenny Neural primary with local Windows SAPI5 fallback)
    AZURE_SPEECH_KEY = os.getenv("AZURE_SPEECH_KEY", "")
    AZURE_SPEECH_REGION = os.getenv("AZURE_SPEECH_REGION", "eastus")
    VOICE_NAME = os.getenv("VOICE_NAME", "en-US-JennyNeural")
    WAKE_WORD = os.getenv("WAKE_WORD", "hey ev").lower().strip()
    ALT_WAKE_WORDS = ["ev", "hey ev", "hello ev", "ok ev", "jarvis"]
    VOICE_RATE = int(os.getenv("VOICE_RATE", "175"))  # Moderate speaking speed (WPM)
    VOICE_VOLUME = float(os.getenv("VOICE_VOLUME", "1.0"))  # 0.0 to 1.0 (comfortable volume)
    VOICE_GENDER = os.getenv("VOICE_GENDER", "female")  # 'female' for Jenny Neural
    LANGUAGE = os.getenv("LANGUAGE", "en-US")  # English (United States) only
    
    # Behavior Settings
    CONTINUOUS_LISTENING = os.getenv("CONTINUOUS_LISTENING", "true").lower() == "true"
    AUDIO_FEEDBACK = os.getenv("AUDIO_FEEDBACK", "true").lower() == "true"
    SILENCE_THRESHOLD = float(os.getenv("SILENCE_THRESHOLD", "1.5"))  # Seconds
    ENERGY_THRESHOLD = int(os.getenv("ENERGY_THRESHOLD", "300"))
    
    # System Prompt for EV
    SYSTEM_PROMPT = f"""You are EV (Enhanced Virtual Intelligence), an advanced personal desktop AI assistant inspired by the conversational style of an intelligent, friendly, calm, confident, and futuristic superhero AI assistant.
You assist {USER_NAME} on their Windows desktop.

STRICT LANGUAGE REQUIREMENT:
- All responses must be in clear, natural English (United States) ONLY.
- Even if the user communicates or asks questions in other languages, you must always reply in fluent English.

Personality & Voice Persona:
- Tone: Helpful, intelligent, warm, friendly, calm, and confident.
- Conversational Delivery: Your responses will be spoken aloud by Microsoft Jenny Neural or Windows text-to-speech. Keep speech natural, fluid, and engaging. Avoid awkward markdown formatting such as tables, long raw ASCII lists, or repetitive symbols that do not sound good when spoken aloud.
- Capability & Guidance: You provide expert guidance across software engineering (Python, C, C++, JavaScript, web, algorithms), system architecture, computer automation, mathematics, and daily productivity.
- Conciseness: Give clear, articulate, and direct answers by default. Offer thoughtful in-depth explanations when the user asks for detail.
- Identity: You are EV. Address the user respectfully as "{USER_NAME}".
- Action Acknowledgments: When performing actions (launching an app, searching the web, system checks), acknowledge them clearly and naturally.
"""

    # Windows Application Registry for Voice Launching
    APP_REGISTRY = {
        "visual studio code": ["code", "code.exe"],
        "vscode": ["code", "code.exe"],
        "code": ["code", "code.exe"],
        "google chrome": ["chrome", "chrome.exe"],
        "chrome": ["chrome", "chrome.exe"],
        "browser": ["chrome", "msedge"],
        "notepad": ["notepad", "notepad.exe"],
        "calculator": ["calc", "calc.exe"],
        "file explorer": ["explorer", "explorer.exe"],
        "explorer": ["explorer", "explorer.exe"],
        "settings": ["ms-settings:"],
        "windows settings": ["ms-settings:"],
        "command prompt": ["cmd", "cmd.exe"],
        "cmd": ["cmd", "cmd.exe"],
        "terminal": ["wt", "powershell"],
        "powershell": ["powershell"],
        "task manager": ["taskmgr", "taskmgr.exe"],
        "paint": ["mspaint", "mspaint.exe"],
        "spotify": ["spotify", "spotify.exe"]
    }

    # Web URL Registry
    WEB_REGISTRY = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "reddit": "https://www.reddit.com",
        "stackoverflow": "https://stackoverflow.com",
        "wikipedia": "https://www.wikipedia.org"
    }

    @classmethod
    def update_setting(cls, key: str, value: str):
        """Update runtime config and optionally persist to .env"""
        if hasattr(cls, key):
            setattr(cls, key, value)
            # Update .env file
            env_file = BASE_DIR / ".env"
            lines = []
            if env_file.exists():
                with open(env_file, "r", encoding="utf-8") as f:
                    lines = f.readlines()
            
            key_found = False
            new_lines = []
            for line in lines:
                if line.startswith(f"{key}="):
                    new_lines.append(f"{key}={value}\n")
                    key_found = True
                else:
                    new_lines.append(line)
            
            if not key_found:
                new_lines.append(f"{key}={value}\n")
                
            with open(env_file, "w", encoding="utf-8") as f:
                f.writelines(new_lines)

