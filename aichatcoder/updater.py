import requests
from packaging import version
import os
import click


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
                os.system("pip install --upgrade aichatcoder")
                click.echo("Please restart the CLI to use the updated version.")
                return True
        else:
            click.echo(" [OK]")
            click.echo(f"You are using the latest version {current_version}.")
        return False
    except (requests.RequestException, KeyError, ValueError):
        click.echo(" [FAILED]")
        click.echo("Could not check for updates. Proceeding with current version.")
        return False