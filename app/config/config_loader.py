from pathlib import Path
import yaml


CONFIG_PATH = (
    Path(__file__)
    .parent
    / "interests.yaml"
)


def load_config():

    with open(CONFIG_PATH, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def get_user_interests():

    config = load_config()

    return config["user"]["interests"]


def get_enabled_sources():

    config = load_config()

    return config["sources"]


def get_llm_provider():

    config = load_config()

    return config["llm"]["provider"]