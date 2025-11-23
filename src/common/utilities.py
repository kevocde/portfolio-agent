import argparse
import os
from typing import Any
from dotenv import load_dotenv


def load_args() -> dict[Any, Any]:
    """Load command line arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--transport', help='Mode to run the server in', choices=['streamable', 'stdio'], default='stdio')
    parser.add_argument('--host', help='Host to bind the server to', default='0.0.0.0')
    parser.add_argument('--port', help='Port to bind the server to', type=int, default=8000)
    parser.add_argument('--session', help='Session Key for the history', type=str)

    return parser.parse_args().__dict__

def get_env(key: str, default: Any = "") -> str:
    """Get environment variable"""
    load_dotenv()
    return os.getenv(key, default)

def get_message_length() -> tuple[int, int]:
    """Returns the message length min max values"""
    message_length = get_env('MESSAGE_LENGTH', '10,500')
    if ',' in message_length:
        message_length = message_length.split(',')
        return int(message_length[0]), int(message_length[1])
    else:
        return int(message_length), 500
