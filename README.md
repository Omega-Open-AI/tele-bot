# 🤖 Telegram AI Image Generator Bot

A powerful Telegram bot that generates high-quality images using state-of-the-art AI models from Hugging Face. Create stunning visuals with simple text prompts, enhance your creativity with AI-powered prompt suggestions, and analyze images with advanced computer vision.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/docker-supported-blue.svg)](docker-compose.yml)
[![CI/CD](https://github.com/yourusername/telegram-draft-bot/workflows/Python%20Application%20CI/CD/badge.svg)](https://github.com/yourusername/telegram-draft-bot/actions)
[![Code Coverage](https://codecov.io/gh/yourusername/telegram-draft-bot/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/telegram-draft-bot)

## ✨ Features

### 🎨 Image Generation
- **Multiple AI Models**: Support for Flux, Stable Diffusion, Kolors, and more
- **Smart Model Selection**: Automatically chooses the best model based on your prompt
- **High-Quality Output**: Generate images up to 1024x1024 resolution
- **Fast Processing**: Optimized for quick response times

### 🧠 AI-Powered Enhancements
- **Prompt Enhancement**: AI improves your prompts for better results
- **Image Analysis**: Describe any image with advanced computer vision
- **Content Filtering**: Built-in safety measures for appropriate content

### ⚙️ Advanced Features
- **Rate Limiting**: Prevents abuse with configurable limits
- **User Preferences**: Remember your favorite models and settings
- **Caching**: Redis-powered caching for improved performance
- **Comprehensive Logging**: Detailed logs for monitoring and debugging

### 🛠️ Developer-Friendly
- **Modular Architecture**: Clean, maintainable code structure
- **Comprehensive Tests**: Full test suite with high coverage
- **Docker Support**: Easy deployment with Docker Compose
- **CI/CD Pipeline**: Automated testing and deployment

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Redis server
- Telegram Bot Token ([Get from @BotFather](https://t.me/botfather))
- Hugging Face API Key ([Get from Hugging Face](https://huggingface.co/settings/tokens))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/telegram-draft-bot.git
   cd telegram-draft-bot
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your API keys and configuration
   ```

5. **Start Redis** (if not already running)
   ```bash
   redis-server
   ```

6. **Run the bot**
   ```bash
   python main.py
   ```

### Docker Deployment

For a quick setup with Docker:

```bash
# Copy and configure environment
cp .env.example .env
# Edit .env with your configuration

# Start the bot with Redis
docker-compose up -d
```

## 📖 Usage

### Basic Commands

- `/start` - Welcome message and basic instructions
- `/help` - Detailed usage guide and tips
- `/models` - View all available AI models
- `/setmodel <model_name>` - Set your preferred model
- `/enhance <prompt>` - Improve your prompt with AI
- `/generate <prompt>` - Generate an image

### Image Generation

Simply send any text message to generate an image:

```
A majestic mountain landscape at sunset
```

```
A cute robot reading a book in a library, digital art
```

### Advanced Prompting

For better results, use descriptive prompts:

```
A photorealistic portrait of a wise old wizard with a long white beard, wearing a blue robe, standing in a magical forest, high quality, detailed, 4K
```

### Image Analysis

Send any photo to get an AI-powered description:

1. Send a photo to the bot
2. Receive a detailed analysis
3. Use the description as inspiration for new images

## 🏗️ Architecture

```
src/
├── bot/                 # Bot implementation
│   ├── core.py          # Main bot orchestrator
│   ├── handlers.py      # Command and message handlers
│   └── utils.py         # Utility functions
├── models/              # AI model configurations
│   └── model_config.py  # Model definitions and selection
└── config/              # Configuration management
    └── settings.py      # Environment and settings
```

### Key Components

- **TelegramImageBot**: Main bot class that orchestrates all components
- **BotHandlers**: Manages all Telegram command and message handlers
- **BotUtils**: Utility functions for image processing, API calls, and caching
- **Settings**: Configuration management with environment variables
- **ModelConfig**: AI model definitions and selection logic

## 🤖 Supported Models

### Text-to-Image Models

| Model | Quality | Speed | Best For |
|-------|---------|-------|----------|
| **Flux Pro** | Premium | Slow | Professional artwork, high detail |
| **Flux Dev** | High | Medium | Balanced quality and speed |
| **Flux Schnell** | Good | Fast | Quick generations, iterations |
| **Kolors** | High | Medium | Artistic styles, creative content |
| **Stable Diffusion** | Good | Fast | General purpose, reliable |

### Text-to-Text Models
- **Llama 3.1**: Advanced prompt enhancement
- **Qwen 2.5**: Creative writing assistance

### Image-to-Text Models
- **LLaVA**: Detailed image analysis
- **BLIP**: Quick image descriptions

## ⚙️ Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `TELEGRAM_BOT_TOKEN` | ✅ | - | Your Telegram bot token |
| `HUGGINGFACE_API_KEY` | ✅ | - | Your Hugging Face API key |
| `REDIS_URL` | ✅ | - | Redis connection URL |
| `MAX_PROMPT_LENGTH` | ❌ | 500 | Maximum prompt length |
| `RATE_LIMIT_PER_USER` | ❌ | 10 | Requests per user per hour |
| `MAX_IMAGE_SIZE` | ❌ | 1024 | Maximum image dimension |
| `IMAGE_QUALITY` | ❌ | 85 | JPEG compression quality |
| `LOG_LEVEL` | ❌ | INFO | Logging level |

See [.env.example](.env.example) for all available configuration options.

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_handlers.py
```

## 📚 Documentation

- **[Setup Guide](docs/setup.md)** - Detailed installation and configuration
- **[Usage Guide](docs/usage.md)** - Complete user manual with examples
- **[Development Guide](docs/development.md)** - Contributing and development setup

## 🤝 Contributing

We welcome contributions! Please see our [Development Guide](docs/development.md) for details.

### Quick Contribution Steps

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes and add tests
4. Run tests: `pytest`
5. Commit your changes: `git commit -m 'Add amazing feature'`
6. Push to the branch: `git push origin feature/amazing-feature`
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for providing amazing AI models
- [python-telegram-bot](https://python-telegram-bot.org/) for the excellent Telegram bot framework
- [Redis](https://redis.io/) for fast caching and session storage
- All the amazing AI researchers and developers who created the models we use

## 📞 Support

- 📖 Check the [documentation](docs/)
- 🐛 Report bugs via [GitHub Issues](https://github.com/yourusername/telegram-draft-bot/issues)
- 💡 Request features via [GitHub Issues](https://github.com/yourusername/telegram-draft-bot/issues)
- 💬 Join our [GitHub Discussions](https://github.com/yourusername/telegram-draft-bot/discussions)

## 🔮 Roadmap

- [ ] **Batch Generation**: Generate multiple images at once
- [ ] **Style Presets**: Pre-configured artistic styles
- [ ] **Image Editing**: Modify existing images with AI
- [ ] **Video Generation**: Support for AI video models
- [ ] **Custom Models**: Support for user-uploaded models
- [ ] **Web Interface**: Optional web dashboard
- [ ] **Multi-language**: Support for multiple languages
- [ ] **Advanced Analytics**: Usage statistics and insights

---

<div align="center">
  <strong>Made with ❤️ for the AI community</strong>
  <br>
  <sub>Star ⭐ this repo if you find it useful!</sub>
</div>
