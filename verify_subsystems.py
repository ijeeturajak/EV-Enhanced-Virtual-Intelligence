"""
EV - Enhanced Virtual Intelligence
Subsystem Health & Integration Verification Script
Run directly: python verify_subsystems.py
"""

import sys
from pathlib import Path

# Ensure root directory is in sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

def run_health_check():
    print("==================================================")
    print("  EV SUBSYSTEM HARDWARE & INTEGRATION HEALTH CHECK")
    print("==================================================")

    # 1. Telemetry
    print("\n=== [1] SYSTEM HARDWARE TELEMETRY ===")
    try:
        from automation.system_control import system_control
        telemetry = system_control.get_system_telemetry()
        print(f"CPU Utilization: {telemetry['cpu_percent']}%")
        print(f"RAM Load: {telemetry['ram_percent']}% ({telemetry['ram_used_gb']} GB / {telemetry['ram_total_gb']} GB)")
        print(f"Battery: {telemetry['battery']['percent']}% (Charging: {telemetry['battery']['power_plugged']})")
        print(f"Network Reachable: {telemetry['online']}")
    except Exception as e:
        print(f"Telemetry check notice: {e}")

    # 2. Audio & Microphones
    print("\n=== [2] AUDIO & MICROPHONE HARDWARE ===")
    try:
        import speech_recognition as sr
        from voice.speech_to_text import stt
        mics = sr.Microphone.list_microphone_names()
        print(f"Detected Audio Input Devices: {len(mics)}")
        print(f"Default Microphone Active: {stt.microphone is not None}")
    except ImportError:
        print("Notice: SpeechRecognition or PyAudio not present in current environment.")
    except Exception as e:
        print(f"Audio check notice: {e}")

    # 3. Wake-Word Detection
    print("\n=== [3] WAKE-WORD PHONETIC DETECTION ===")
    try:
        from voice.wake_word import wake_detector
        for phrase in ["hey ev open chrome", "EV what time is it", "hey jarvis", "hello world"]:
            detected, cmd = wake_detector.check(phrase)
            print(f"Phrase: '{phrase}' -> Detected: {detected} | Extracted: '{cmd}'")
    except Exception as e:
        print(f"Wake word check notice: {e}")

    # 4. Command Router
    print("\n=== [4] COMMAND ROUTER (WINDOWS AUTOMATION) ===")
    try:
        from core.command_router import command_router
        for cmd in ["what time is it", "battery status", "cpu usage", "search google for python"]:
            handled, resp, action = command_router.route_command(cmd)
            print(f"Directive: '{cmd}' -> Handled: {handled} | Action: {action}")
    except Exception as e:
        print(f"Command router check notice: {e}")

    # 5. Database Persistence
    print("\n=== [5] DATABASE PERSISTENCE ===")
    try:
        from database.database import db
        msg_id = db.add_message("user", "Health check ping")
        recent = db.get_recent_conversation(limit=1)
        print(f"Database Write & Read OK: ID {msg_id} (Latest: '{recent[-1]['content']}')")
    except Exception as e:
        print(f"Database check notice: {e}")

    # 6. AI Reasoning Core & Google Gen AI SDK
    print("\n=== [6] AI REASONING CORE (GOOGLE GEMINI) ===")
    try:
        from core.ai_engine import ai_engine, GENAI_AVAILABLE
        print(f"Google Gen AI SDK Available: {GENAI_AVAILABLE}")
        print(f"Gemini API Key Configured: {'Yes' if ai_engine.is_configured() else 'No (Operating in local offline mode)'}")
        print(f"Target Model: {ai_engine.model}")
        success, reply = ai_engine.generate_response("Who are you?")
        print(f"AI Response OK: {success} | '{reply[:65]}...'")
    except Exception as e:
        print(f"AI engine check notice: {e}")

    print("\n>>> HEALTH CHECK ROUTINE COMPLETED! <<<")

if __name__ == "__main__":
    run_health_check()

