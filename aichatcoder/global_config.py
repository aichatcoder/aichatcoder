import yaml
from pathlib import Path
import click

# Define the config directory and file path based on the platform
CONFIG_DIR = Path.home() / ".aichatcoder"
CONFIG_FILE = CONFIG_DIR / "config.yml"

def ensure_config_exists():
    """Ensure the config directory and file exist, creating them if necessary."""
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True)
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w") as f:
            yaml.dump({"web_auth_token": ""}, f)

def load_config():
    """Load the configuration from the YAML file."""
    ensure_config_exists()
    with open(CONFIG_FILE, "r") as f:
        return yaml.safe_load(f)

def save_config(config):
    """Save the configuration to the YAML file."""
    with open(CONFIG_FILE, "w") as f:
        yaml.dump(config, f)

def get_web_auth_token():
    """Get the web auth token from the config file."""
    config = load_config()
    return config.get("web_auth_token", "")

def set_web_auth_token():
    """Prompt the user for a web auth token and save it to the config file."""
    click.echo("No web auth token found. Please provide your web auth token to connect to the AiChatCoder web UI.")
    click.echo("You can obtain your web auth token by logging in with your GitHub account at www.aichatcoder.com")
    token = click.prompt("Web Auth Token", type=str)
    config = load_config()
    config["web_auth_token"] = token
    save_config(config)
    click.echo(f"Web auth token saved to {CONFIG_FILE}.")