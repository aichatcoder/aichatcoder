import click
from aichatcoder.updater import check_for_updates

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

    click.echo("Initializing AiChatCoder Agent...")

@main.command()
def run():
    """Run the agent to generate prompts and apply changes."""
    # Check for updates
    from aichatcoder import __version__
    check_for_updates(__version__)

    click.echo("Running AiChatCoder Agent...")

if __name__ == "__main__":
    main()