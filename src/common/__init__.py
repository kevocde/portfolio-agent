import argparse, os
from dotenv import load_dotenv

def load_args() -> dict:
    """Load command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--transport', help='Mode to run the server in', choices=['streamable', 'stdio'], default='stdio')
    parser.add_argument('--host', help='Host to bind the server to', default='0.0.0.0')
    parser.add_argument('--port', help='Port to bind the server to', type=int, default=8000)
    parser.add_argument('--session', help='Session Key for the history', type=str)

    return parser.parse_args().__dict__

def load_env() -> None:
    """Load environment variables from .env file if it exists"""
    load_dotenv()

def get_env(key: str, default: str = "") -> str:
    """Get environment variable"""
    return os.getenv(key) or default
