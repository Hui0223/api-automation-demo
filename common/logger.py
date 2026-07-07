from __future__ import annotations

import json
import logging
from typing import Any


def get_logger(name: str = "project_a") -> logging.Logger:
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s - %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    logger.propagate = False
    return logger


def to_json_summary(value: Any, max_len: int = 300) -> str:
    try:
        text = json.dumps(value, ensure_ascii=False)
    except TypeError:
        text = str(value)
    if len(text) > max_len:
        return text[:max_len] + "..."
    return text

