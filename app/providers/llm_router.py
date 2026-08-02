"""
LLM Router

Routes AI tasks to the appropriate LLM provider and model
based on the configuration defined in:

    app/config/llm_routing.yaml

The router is provider-agnostic.

Example:

    response = invoke(
        task="summarization",
        prompt=paper_text
    )
"""

from functools import lru_cache
from pathlib import Path
from pyexpat import model
from typing import Any

import yaml

from app.providers.openrouter_provider import invoke as openrouter_invoke


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

CONFIG_PATH = (
    Path(__file__)
    .resolve()
    .parent.parent
    / "config"
    / "llm_routing.yaml"
)


# -------------------------------------------------------------------
# Exceptions
# -------------------------------------------------------------------

class LLMRouterError(Exception):
    """Base exception for LLM Router."""


class TaskNotFoundError(LLMRouterError):
    """Raised when a task is missing."""


class ProviderNotSupportedError(LLMRouterError):
    """Raised when provider is unsupported."""


# -------------------------------------------------------------------
# Configuration Loader
# -------------------------------------------------------------------

@lru_cache(maxsize=1)
def load_config() -> dict[str, Any]:
    """
    Load routing configuration.

    Cached after first load.
    """

    if not CONFIG_PATH.exists():
        raise FileNotFoundError(
            f"Configuration not found:\n{CONFIG_PATH}"
        )

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    if config is None:
        raise LLMRouterError(
            "llm_routing.yaml is empty."
        )

    validate_config(config)

    return config


def reload_config() -> None:
    """
    Clear cached configuration.

    Useful while developing.
    """

    load_config.cache_clear()


# -------------------------------------------------------------------
# Validation
# -------------------------------------------------------------------

def validate_config(config: dict[str, Any]) -> None:

    if "provider" not in config:
        raise LLMRouterError(
            "Missing 'provider' in llm_routing.yaml"
        )

    if "tasks" not in config:
        raise LLMRouterError(
            "Missing 'tasks' section in llm_routing.yaml"
        )

    for task, settings in config["tasks"].items():

        if "model" not in settings:
            raise LLMRouterError(
                f"Task '{task}' missing model."
            )


# -------------------------------------------------------------------
# Task Utilities
# -------------------------------------------------------------------

def get_provider() -> str:
    return load_config()["provider"]


def get_task_config(task: str) -> dict[str, Any]:

    tasks = load_config()["tasks"]

    if task not in tasks:

        available = ", ".join(tasks.keys())

        raise TaskNotFoundError(
            f"Unknown task '{task}'.\n"
            f"Available tasks: {available}"
        )

    return tasks[task]


def available_tasks() -> list[str]:
    return list(load_config()["tasks"].keys())


# -------------------------------------------------------------------
# Router
# -------------------------------------------------------------------

def invoke_for_task(
    task: str,
    prompt: str,
    system_prompt: str | None = None,
) -> str:
    """
    Route prompt to the configured provider.

    Parameters
    ----------
    task:
        Task name defined in llm_routing.yaml

    prompt:
        User prompt

    system_prompt:
        Optional system prompt

    Returns
    -------
    str
        LLM response
    """

    provider = get_provider()

    task_config = get_task_config(task)

    model = task_config["model"]

    temperature = task_config.get(
        "temperature",
        0.3,
    )

    max_tokens = task_config.get(
        "max_tokens",
        6048,
    )

    if provider == "openrouter":

        return openrouter_invoke(
            model=model,
            prompt=prompt,
            system_prompt=system_prompt,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    raise ProviderNotSupportedError(
        f"Provider '{provider}' is not supported."
    )


# -------------------------------------------------------------------
# Development Test
# -------------------------------------------------------------------

if __name__ == "__main__":

    print(f"[LLM Router] Task: {task} | Model: {model}")

    print("Provider :", get_provider())

    print("Tasks :")

    for task in available_tasks():
        print(" -", task)