#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

__author__ = "bibow"

import logging
from typing import Any, Dict, List, Tuple


def hello(
    logger: logging.Logger, setting: Dict[str, Any], **arguments: Dict[str, Any]
) -> str:
    return f"Hello, {arguments.get('name', 'World')}!"


def add_numbers(
    logger: logging.Logger, setting: Dict[str, Any], **arguments: Dict[str, Any]
) -> str:
    return str(float(arguments.get("a", 0)) + float(arguments.get("b", 0)))


def read_resource(logger: logging.Logger, setting: Dict[str, Any], uri: str) -> str:
    if uri == "status://server":
        return "Server is operational."
    raise ValueError(f"Unknown resource: {uri}")


def get_prompt(
    logger: logging.Logger,
    setting: Dict[str, Any],
    name: str,
    **arguments: Dict[str, Any],
) -> str:
    if name != "example-prompt":
        raise ValueError(f"Unknown prompt: {name}")

    return "Example prompt text"
