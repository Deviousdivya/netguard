"""Vercel serverless entry point: exposes the FastAPI backend (backend/main.py) under both /api/* and the original paths."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "backend"))

from fastapi import FastAPI  # noqa: E402
from main import app as backend  # noqa: E402
