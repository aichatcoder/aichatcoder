import requests
from packaging import version
import click
import sys
import subprocess


def check_for_updates(current_version):
    """Check for updates on PyPI."""
    click.echo("Checking for new version...", nl=False)

    try:
        response = requests.get("https://pypi.org/pypi/aichatcoder/json", timeout=5)
        response.raise_for_status()
        data = response.json()
        latest_version = data["info"]["version"]

        if version.parse(latest_version) > version.parse(current_version):
            click.echo(" [UPDATE AVAILABLE]")
            click.echo(f"New version {latest_version} is available! You are using {current_version}.")
            if click.confirm("Do you want to update now?"):
                # Use the current Python executable to ensure the correct environment is targeted
                python_executable = sys.executable
                # Run pip as a subprocess to upgrade the package
                subprocess.run([
                    python_executable, "-m", "pip", "install", "--upgrade", "--force-reinstall", "aichatcoder"
                ], check=True)
                click.echo("AiChatCoder Agent has been updated to the latest version.")
                click.echo("Exiting... Please rerun the agent command to use the updated version.")
                sys.exit(0)  # Exit the CLI to ensure the new version is loaded on the next run
        else:
            click.echo(" [OK]")
            click.echo(f"You are using the latest version {current_version}.")
        return False
    except (requests.RequestException, KeyError, ValueError):
        click.echo(" [FAILED]")
        click.echo("Could not check for updates. Proceeding with current version.")
        return False
    except subprocess.CalledProcessError:
        click.echo(" [FAILED]")
        click.echo(
            "Failed to update AiChatCoder Agent. Please update manually using 'pip install --upgrade aichatcoder'.")
        return False
