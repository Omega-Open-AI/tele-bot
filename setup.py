#!/usr/bin/env python3
"""Setup script for Telegram AI Image Generator Bot."""

import os
from setuptools import setup, find_packages

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Read requirements from requirements.txt
with open(os.path.join(this_directory, "requirements.txt"), encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

# Development requirements
dev_requirements = [
    "pytest>=7.0.0",
    "pytest-asyncio>=0.21.0",
    "pytest-cov>=4.0.0",
    "black>=23.0.0",
    "isort>=5.12.0",
    "flake8>=6.0.0",
    "mypy>=1.0.0",
    "pre-commit>=3.0.0",
    "sphinx>=6.0.0",
    "sphinx-rtd-theme>=1.2.0",
]

setup(
    name="telegram-draft-bot",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Telegram bot for AI-powered image generation using Hugging Face models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/telegram-draft-bot",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/telegram-draft-bot/issues",
        "Source": "https://github.com/yourusername/telegram-draft-bot",
        "Documentation": "https://github.com/yourusername/telegram-draft-bot/blob/main/docs/",
    },
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Communications :: Chat",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Framework :: AsyncIO",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": dev_requirements,
        "test": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "pytest-cov>=4.0.0",
        ],
        "docs": [
            "sphinx>=6.0.0",
            "sphinx-rtd-theme>=1.2.0",
            "myst-parser>=1.0.0",
        ],
        "monitoring": [
            "sentry-sdk>=1.20.0",
            "prometheus-client>=0.16.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "telegram-draft-bot=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "telegram-draft-bot": [
            "*.md",
            "*.txt",
            "*.yml",
            "*.yaml",
        ],
    },
    keywords=[
        "telegram",
        "bot",
        "ai",
        "image-generation",
        "huggingface",
        "stable-diffusion",
        "flux",
        "artificial-intelligence",
        "machine-learning",
        "text-to-image",
        "chatbot",
        "automation",
    ],
    zip_safe=False,
    platforms=["any"],
    license="MIT",
    # Additional metadata
    maintainer="Your Name",
    maintainer_email="your.email@example.com",
    download_url="https://github.com/yourusername/telegram-draft-bot/archive/v1.0.0.tar.gz",
    # Security
    options={
        "bdist_wheel": {
            "universal": False,
        },
    },
)