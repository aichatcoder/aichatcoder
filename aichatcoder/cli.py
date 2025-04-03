import click
from aichatcoder.updater import check_for_updates
from aichatcoder.global_config import get_web_auth_token, set_web_auth_token

@click.group()
def main():
    """AiChatCoder Agent: Generate and apply AI-powered coding prompts."""
    pass

@main.command()
def init():
    """Initialize the agent in your repository."""
    # Check for updates
    from aichatcoder import __version__
    check_for_updates(__version__)

    # Check for web auth token
    token = get_web_auth_token()
    if not token:
        set_web_auth_token()

    click.echo("Initializing AiChatCoder Agent...")

@main.command()
def run():
    """Run the agent to generate prompts and apply changes."""
    # Check for updates
    from aichatcoder import __version__
    check_for_updates(__version__)

    # Check for web auth token
    token = get_web_auth_token()
    if not token:
        click.echo("No web auth token found. Please run 'aichatcoder init' to set up your web auth token.")
        return

    click.echo("Running AiChatCoder Agent...")

if __name__ == "__main__":
    main()