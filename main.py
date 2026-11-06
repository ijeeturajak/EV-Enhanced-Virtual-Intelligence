"""
EV — ENHANCED VIRTUAL INTELLIGENCE
Main Application Entry Point
"""

import sys
import os
import logging
from pathlib import Path

# Ensure logs directory exists before configuring logging FileHandler
log_dir = Path(__file__).resolve().parent / "logs"
log_dir.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (%(name)s) %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_dir / "ev.log", encoding="utf-8")
    ]
)
logger = logging.getLogger("EV.Main")

from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from ui.dashboard import EVDashboard
from core.assistant import assistant
from voice.listener import listener
from voice.text_to_speech import tts

def main():
    logger.info("Initializing EV Application Architecture...")

    # Enable High DPI Scaling for crisp futuristic graphics
    if hasattr(Qt, "AA_EnableHighDpiScaling"):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, "AA_UseHighDpiPixmaps"):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    app.setApplicationName("EV - Enhanced Virtual Intelligence")
    app.setOrganizationName("EV Industries")

    # Launch Futuristic Dashboard
    dashboard = EVDashboard()
    dashboard.show()

    # Start Background Assistant Core (Wake-word listener & speech dispatch)
    assistant.start()

    logger.info("EV Desktop Workstation loaded successfully.")
    
    # Run application event loop
    exit_code = app.exec()

    # Graceful shutdown
    logger.info("Shutting down EV Subsystems...")
    listener.stop()
    tts.stop()
    sys.exit(exit_code)

if __name__ == "__main__":
    main()

