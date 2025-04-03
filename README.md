# AiChatCoder Agent

Agent for generating and applying AI-powered coding prompts in your repository via a web UI at [www.aichatcoder.com](https://aichatcoder.com).

The AiChatCoder Agent is a command-line tool that runs locally in your repository as part of the AiChatCoder system. 
It generates tailored AI prompts based on your codebase, which you can copy to a chat model (e.g., ChatGPT) via the web UI at [www.aichatcoder.com](https://aichatcoder.com). 
After receiving the chat response, the agent applies the suggested changes to your files, streamlining your coding workflow.

## Overview

AiChatCoder is a system designed for developers to integrate AI assistance into their coding process. The system consists of two main components:

- **AiChatCoder Agent** (this pip package): A local agent that runs in your repository to generate prompts and apply changes.
- **AiChatCoder Web UI** ([www.aichatcoder.com](https://aichatcoder.com)): A web interface for controlling the agent, generating prompts, and managing chat responses.

### Workflow (Prototype)

1. **Run the Agent Locally**:
   Use the `aichatcoder` CLI to start the agent in your repository.

2. **Control via Web UI**:
   Open the web UI at [www.aichatcoder.com](https://aichatcoder.com), write a prompt (or use the agent’s suggestions), and hit "Generate."

3. **Generate Prompts**:
   The agent analyzes your codebase and generates specific AI prompts, which are displayed in the web UI for you to copy.

4. **Interact with Chat Model**:
   Copy the generated prompt to a chat model (e.g., ChatGPT). The chat model responds with code or instructions in a specific format.

5. **Apply Changes**:
   Copy the chat response back to the web UI. The web UI sends the response to the agent, which applies the changes to your repository files.

## Installation

AiChatCoder requires Python 3.8+ to be installed on your system. Follow the steps below for your platform:

### Windows
1. Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/windows/).
2. Open a command prompt and install AiChatCoder:
   ```bash
   pip install aichatcoder
   ```

### Linux (e.g., Ubuntu)
1. Python 3 is usually pre-installed. Check with `python3 --version`.
2. If `pip` is not installed, run:
   ```bash
   sudo apt update
   sudo apt install python3-pip
   ```
3. Install AiChatCoder:
   ```bash
   pip install aichatcoder
   ```

### Mac (ARM/Intel)
1. macOS 12.3+ does not include Python by default. Download and install Python 3.8+ from [python.org](https://www.python.org/downloads/mac-osx/), or use Homebrew:
   ```bash
   brew install python
   ```
2. Install AiChatCoder:
   ```bash
   pip install aichatcoder
   ```

## Usage

This package provides a CLI for running the agent in your repository. The web UI at [www.aichatcoder.com](https://aichatcoder.com) is required to control the agent and manage the workflow.

### Global Configuration

AiChatCoder stores a global configuration file in YAML format at the following location:
- Linux/Mac: `~/.aichatcoder/config.yml`
- Windows: `C:\Users\<Username>\.aichatcoder\config.yml`

The configuration file stores your web auth token, which is required to connect to the AiChatCoder web UI.

### First Run Setup

The first time you run `aichatcoder init`, you’ll be prompted to provide a web auth token if it’s not already set in the configuration file. 
You can obtain your web auth token by logging in with your GitHub account at [www.aichatcoder.com](https://aichatcoder.com)

### Check for Updates

When you run `aichatcoder init` or `aichatcoder run`, the CLI will check for updates on PyPI. If a newer version is available, you’ll be prompted to update.

### Initialize the Agent

```bash
aichatcoder init
```

This sets up the agent in your current repository. If a web auth token is not set, you’ll be prompted to provide one.

### Run the Agent

```bash
aichatcoder run
```

This starts the agent, which will connect to the web UI and prepare to generate prompts and apply changes. If a web auth token is not set, you’ll be prompted to run `aichatcoder init` to set it up.

## License

The AiChatCoder Agent is licensed under a custom "No Usage" License. This package is made public for transparency and security review purposes only. 
Usage, modification, or distribution of this package by others is strictly prohibited. See the [LICENSE](https://github.com/aichatcoder/aichatcoder/blob/main/LICENSE) file for details.

## Credits

Created by [therceman](https://github.com/therceman).

## Links

- Website: [aichatcoder.com](https://aichatcoder.com)
- PyPI: [pypi.org/project/aichatcoder/](https://pypi.org/project/aichatcoder/)
- GitHub: [github.com/aichatcoder/aichatcoder](https://github.com/aichatcoder/aichatcoder)