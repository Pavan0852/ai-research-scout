import yaml

def load_interests():

    with open(
        "app/config/interests.yaml",
        "r"
    ) as f:

        config = yaml.safe_load(f)

    return config["user"]["interests"]