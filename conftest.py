"""Pytest configuration helpers.

Ensure the repository root is on sys.path so tests can import the `src` package
when running `pytest` from the project root.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
