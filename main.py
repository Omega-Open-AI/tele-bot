#!/usr/bin/env python3
"""
Telegram AI Image Generator Bot - Main Entry Point

This is the main entry point for the Telegram bot application.
It initializes the bot and starts the polling process.

Author: AI Assistant
Version: 2.0.0
License: MIT
"""

import asyncio
import logging
import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from bot.core import TelegramImageBot
from config.settings import get_settings

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def main():
    """Main function to start the bot"""
    try:
        # Load configuration
        settings = get_settings()
        
        # Validate required environment variables
        if not settings.TELEGRAM_BOT_TOKEN:
            logger.error("TELEGRAM_BOT_TOKEN environment variable is required")
            sys.exit(1)
            
        if not settings.HUGGINGFACE_API_KEY:
            logger.error("HUGGINGFACE_API_KEY environment variable is required")
            sys.exit(1)
        
        # Initialize and start the bot
        logger.info("Starting Telegram AI Image Generator Bot...")
        bot = TelegramImageBot(settings)
        bot.run()
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()