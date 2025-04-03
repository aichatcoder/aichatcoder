import click

@click.group()
def main():
    """AiChatCoder Agent: Generate and apply AI-powered coding prompts."""
    pass

@main.command()
def init():
    """Initialize the agent in your repository."""
    click.echo("Initializing AiChatCoder Agent...")

@main.command()
def run():
    """Run the agent to generate prompts and apply changes."""
    click.echo("Running AiChatCoder Agent...")

if __name__ == "__main__":
    main()