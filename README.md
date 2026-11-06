# ⚡ EV — ENHANCED VIRTUAL INTELLIGENCE

![Platform: Windows](https://img.shields.io/badge/Platform-Windows_10_%2F_11-00f0ff.svg)
![Python](https://img.shields.io/badge/Python-3.10_%7C_3.11_%7C_3.12-blue.svg)
![UI: PySide6](https://img.shields.io/badge/UI-PySide6_%2F_Qt6-emerald.svg)
![Voice: SAPI5 + Google STT](https://img.shields.io/badge/Voice-WakeWord_%2B_SAPI5_%2B_STT-violet.svg)
![AI: Gemini + Local](https://img.shields.io/badge/AI-Google_Gemini_%2B_Offline_Core-amber.svg)

> **EV (Enhanced Virtual Intelligence)** is an autonomous, personal desktop AI assistant inspired by Tony Stark's **J.A.R.V.I.S.** from Iron Man. EV runs natively on your Windows laptop, listens for the wake word **"Hey EV"**, executes real Windows computer automation, answers complex programming and general questions, monitors your hardware in real time, and communicates through a natural voice.

---

## 🎛️ 1. Architecture Overview

```
EV/
├── main.py                  # Entry point, boots Qt event loop & assistant core
├── config.py                # Central configuration, app registries & prompts
├── requirements.txt         # Core Python dependencies
├── .env.example             # Example environment configuration
├── start.bat                # Windows 1-click launcher
├── README.md                # Documentation & instructions
│
├── core/
│   ├── assistant.py         # Main orchestrator & conversational manager
│   ├── ai_engine.py         # Google Gemini API & offline intelligence fallback
│   ├── command_router.py    # Allowlisted Windows automation dispatcher
│   ├── events.py            # Thread-safe Qt signal bus
│   └── memory.py            # User preference & context extraction
│
├── voice/
│   ├── listener.py          # Continuous ambient listening worker
│   ├── wake_word.py         # Wake-word detection engine ("Hey EV")
│   ├── speech_to_text.py    # Noise-filtering SpeechRecognition engine
│   └── text_to_speech.py    # Windows SAPI5 natural speech synthesis
│
├── automation/
│   ├── app_launcher.py      # Windows application launcher & process closer
│   ├── browser.py           # Web searches (Google & YouTube) & URL navigation
│   ├── file_manager.py      # Safe folder/file creation, reading, and listing
│   └── system_control.py    # Live psutil CPU, RAM, Battery, Volume, and Lock
│
├── ui/
│   ├── dashboard.py         # Primary futuristic frameless HUD window
│   ├── components.py        # Animated Arc Reactor Core & Telemetry gauges
│   ├── settings.py          # Configuration modal (API keys, voice, language)
│   └── styles.py            # Deep navy & neon electric cyan QSS stylesheet
│
├── database/
│   └── database.py          # Persistent SQLite conversation & memory database
│
└── tests/
    ├── test_database.py     # Database & memory tests
    ├── test_commands.py     # Command router & automation tests
    └── test_ai.py           # AI engine & offline fallback tests
```

---

## 🎙️ 2. Advanced Voice Interaction

EV is built around voice:

1. **Wake-Word Activation**: Say **"Hey EV"** (or *"EV"*, *"Jarvis"*). The central Arc Reactor transitions to glowing emerald, and EV acknowledges you.
2. **Continuous Ambient Listening**: Runs in a non-blocking background thread. It automatically detects speech while you work.
3. **Push-to-Talk / Manual Mic**: Toggle the microphone on or off via the HUD button or press `Enter` in the text command box.
4. **Echo-Loop Prevention**: When EV is speaking, the voice listener automatically mutes audio capture to prevent EV from responding to its own voice.
5. **Speech Cleanup**: Markdown asterisks, code fences, and URLs are cleaned before speech synthesis so EV sounds like a natural human rather than reading out code syntax.
6. **Bilingual Support**: Configurable for both **English** (`en-US`, `en-IN`) and **Hindi** (`hi-IN`).

---

## 🧠 3. EV Intelligence (AI Brain)

* **Google Gemini Integration**: Native HTTPS REST client communicating with Gemini 1.5 Flash or 2.0 Flash with system instructions and recent conversation context.
* **Offline Fallback Engine**: If your API key is not yet configured or internet drops, EV's internal rule-based and knowledge engine automatically handles:
  * Greetings, persona, and capability inquiries
  * Concepts (Artificial Intelligence, Machine Learning, Cloud Computing, OOP)
  * Programming assistance (Python, C, C++, JavaScript, algorithms, data structures)
  * Math calculations (`calculate 25 * 4 + 10`)
  * English to Hindi phrase translations
  * Helpful reminders to configure your Gemini API key in Settings

---

## 🖥️ 4. Windows Computer Automation

EV connects directly to Windows APIs to perform real tasks safely through an allowlisted command router:

### Applications
| Voice Command | Action |
| :--- | :--- |
| *"Hey EV, open Visual Studio Code"* | Launches VS Code (`code`) |
| *"Hey EV, open Google Chrome"* | Launches Chrome |
| *"Hey EV, open Notepad"* | Launches Notepad |
| *"Hey EV, open Calculator"* | Launches Windows Calculator |
| *"Hey EV, open File Explorer"* | Launches Windows Explorer |
| *"Hey EV, open Windows Settings"* | Opens Windows Settings (`ms-settings:`) |
| *"Hey EV, close Notepad"* | Safely closes active Notepad processes |

### Web & Searches
| Voice Command | Action |
| :--- | :--- |
| *"Hey EV, search google for Python tutorials"* | Opens default browser with Google search results |
| *"Hey EV, search YouTube for lofi hip hop"* | Opens YouTube search results |
| *"Hey EV, open GitHub"* | Navigates to github.com |
| *"Hey EV, open ChatGPT"* | Navigates to chat.openai.com |

### System Telemetry & Hardware Control
| Voice Command | Action |
| :--- | :--- |
| *"Hey EV, what time is it?"* | Spoken time report: *"The current time is 02:45 AM on Sunday, November 1."* |
| *"Hey EV, check battery status"* | Reports battery percentage and AC charging state |
| *"Hey EV, CPU usage"* | Reports real CPU load % and RAM usage from `psutil` |
| *"Hey EV, volume up"* / *"volume down"* | Adjusts Windows master volume |
| *"Hey EV, mute"* | Toggles master volume mute |
| *"Hey EV, lock screen"* | Instantly locks the Windows workstation session |

### File Operations
| Voice Command | Action |
| :--- | :--- |
| *"Hey EV, create folder named ProjectAlpha"* | Creates folder safely on Desktop |
| *"Hey EV, create file notes.txt"* | Creates file safely on Desktop |
| *"Hey EV, list files"* | Reads out directory contents |
| *"Hey EV, read file notes.txt"* | Reads content of target text file |

---

## 🌌 5. Futuristic J.A.R.V.I.S. HUD Interface

* **Central Arc Reactor Core**: High-performance custom-painted 60 FPS widget:
  * Concentric rotating dials with calibrated ticks
  * Pulsating energy core
  * Audio-reactive sine waveforms active during speaking/listening
  * Color state transitions: **Cyan** (Idle), **Emerald** (Listening), **Amber** (Thinking), **Blue** (Speaking), **Crimson** (Muted)
* **Left Panel**: Scrollable conversation audit tape with quick action directive chips.
* **Right Panel**: Real-time telemetry updating every second with CPU %, RAM %, Battery %, Network uplink status, Date, and Time.
* **Bottom Panel**: Mic toggle button, command input box, Send button, and Stop Speech button.

---

## 🚀 6. Installation & Quick Start

### Prerequisites
* Windows 10 or 11
* Python 3.10, 3.11, or 3.12 (Python 3.11 recommended)
* Working microphone and speakers / headphones

### Step 1: Install Dependencies
Open PowerShell or Command Prompt in the project folder and run:
```powershell
pip install -r requirements.txt
```

### Step 2: Configure Environment (Optional)
Copy `.env.example` to `.env`:
```powershell
copy .env.example .env
```
Add your free Google Gemini API key from [aistudio.google.com](https://aistudio.google.com/):
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```
*(You can also input your API key directly inside the running app via the **⚙ CONFIG** button in the top header).*

### Step 3: Launch EV
Double-click [`start.bat`](file:///c:/Users/rohit/Desktop/Ev/start.bat) or run:
```powershell
python main.py
```

---

## 💻 7. Running in VS Code

1. Open the `Ev` folder in Visual Studio Code (`File > Open Folder...`).
2. Select your Python interpreter (`Ctrl + Shift + P` -> `Python: Select Interpreter` -> choose Python 3.11).
3. Open `main.py` and press `F5` or click **Run Python File**.

---

## 🧪 8. Running Automated Tests

EV comes with a full unit test suite covering database operations, command routing, and AI fallback:
```powershell
python -m unittest discover tests
```

---

## 📦 9. Building a Windows Standalone Executable (.exe)

To bundle EV into a standalone Windows `.exe` application using PyInstaller:

1. Install PyInstaller:
   ```powershell
   pip install pyinstaller
   ```
2. Build the executable:
   ```powershell
   pyinstaller --noconsole --name "EV_Assistant" --add-data "config.py;." --add-data "database;database" --add-data "assets;assets" main.py
   ```
3. The executable will be generated in `dist/EV_Assistant/EV_Assistant.exe`.

---

## 🔒 10. Security & Privacy Guarantees

* **No Secret Audio Recording**: Audio is processed strictly when listening is active. The microphone state is visibly displayed on the HUD at all times.
* **No Arbitrary Shell Execution**: All voice inputs pass through strict allowlisted regex and function dispatchers. Voice commands cannot execute arbitrary PowerShell or Bash scripts.
* **Local SQLite Storage**: Conversation history and memories are kept locally on your machine in `database/ev_memory.db`. No data is sent to external servers other than AI queries to the official Gemini API.

