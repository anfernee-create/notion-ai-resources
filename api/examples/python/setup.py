# Python setup for Notion AI API
# Install required packages

from setuptools import setup, find_packages

setup(
    name="notion-ai-examples",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "notion-client>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
)

# Quick start:
# 1. pip install -e .
# 2. Create .env file with NOTION_TOKEN
# 3. Run examples
