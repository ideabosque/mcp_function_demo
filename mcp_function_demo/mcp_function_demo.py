#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

__author__ = "bibow"

import logging
from typing import Any, Dict, List, Tuple

MCP_CONFIGURATION = {
    "tools": [
        {
            "name": "hello",
            "description": "Greet someone",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name",
                        "default": "World",
                    }
                },
            },
            "annotations": None,
        },
        {
            "name": "add_numbers",
            "description": "Add two numbers",
            "inputSchema": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "First number"},
                    "b": {"type": "integer", "description": "Second number"},
                },
                "required": ["a", "b"],
            },
            "annotations": None,
        },
    ],
    "resources": [
        {
            "uri": "status://server",
            "name": "Server Status",
            "description": "Status info",
            "mimeType": "text/plain",
            "size": None,
            "annotations": None,
        }
    ],
    "prompts": [
        {
            "name": "example-prompt",
            "description": "An example prompt template",
            "arguments": [
                {"name": "arg1", "description": "Example argument", "required": True}
            ],
        }
    ],
    "module_links": [
        {
            "type": "tool",
            "name": "hello",
            "module_name": "mcp_function_demo",
            "class_name": "MCPFunctionDemo",
            "function_name": "hello",
            "return_type": "text",
        },
        {
            "type": "tool",
            "name": "add_numbers",
            "module_name": "mcp_function_demo",
            "class_name": "MCPFunctionDemo",
            "function_name": "add_numbers",
            "return_type": "text",
        },
        {
            "type": "resource",
            "name": "Server Status",
            "module_name": "mcp_function_demo",
            "class_name": "MCPFunctionDemo",
            "function_name": "read_resource",
        },
        {
            "type": "prompt",
            "name": "example-prompt",
            "module_name": "mcp_function_demo",
            "class_name": "MCPFunctionDemo",
            "function_name": "get_prompt",
        },
    ],
    "modules": [
        {
            "package_name": "mcp_function_demo",
            "module_name": "mcp_function_demo",
            "class_name": "MCPFunctionDemo",
            "setting": {},
        }
    ],
}


class MCPFunctionDemo:
    def __init__(self, logger: logging.Logger, **setting: Dict[str, Any]):
        self.logger = logger
        self.setting = setting

    def hello(self, **arguments: Dict[str, Any]) -> str:
        return f"Hello, {arguments.get('name', 'World')}!"

    def add_numbers(self, **arguments: Dict[str, Any]) -> str:
        return str(float(arguments.get("a", 0)) + float(arguments.get("b", 0)))

    def read_resource(self, uri: str) -> str:
        if uri == "status://server":
            return "Server is operational."
        raise ValueError(f"Unknown resource: {uri}")

    def get_prompt(self, name: str, **arguments: Dict[str, Any]) -> str:
        if name != "example-prompt":
            raise ValueError(f"Unknown prompt: {name}")

        return "Example prompt text"
