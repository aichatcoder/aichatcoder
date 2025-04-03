# AiChatCoder Agent

Agent for generating and applying AI-powered coding prompts in your repository via a web UI.

The AiChatCoder Agent is a command-line tool that runs locally in your repository as part of the AiChatCoder system. It generates tailored AI prompts based on your codebase, which you can copy to a chat model (e.g., ChatGPT) via the web UI at [aichatcoder.com](https://aichatcoder.com). After receiving the chat response, the agent applies the suggested changes to your files, streamlining your coding workflow.

## Overview

AiChatCoder is a system designed for developers to integrate AI assistance into their coding process. The system consists of two main components:

- **AiChatCoder Agent** (this pip package): A local agent that runs in your repository to generate prompts and apply changes.
- **AiChatCoder Web UI** ([aichatcoder.com](https://aichatcoder.com)): A web interface for controlling the agent, generating prompts, and managing chat responses.

### Workflow

1. **Run the Agent Locally**:
   Use the `aichatcoder` CLI to start the agent in your repository.

2. **Control via Web UI**:
   Open the web UI at [aichatcoder.com](https://aichatcoder.com), write a prompt (or use the agent’s suggestions), and hit "Generate."

3. **Generate Prompts**:
   The agent analyzes your codebase and generates specific AI prompts, which are displayed in the web UI for you to copy.

4. **Interact with Chat Model**:
   Copy the generated prompt to a chat model (e.g., ChatGPT). The chat model responds with code or instructions in a specific format.

5. **Apply Changes**:
   Copy the chat response back to the web UI. The web UI sends the response to the agent, which applies the changes to your repository files.

## Installation

Install the AiChatCoder Agent using pip:

```bash
pip install aichatcoder
```

## Usage
This package provides a CLI for running the agent in your repository. The web UI at aichatcoder.com is required to control the agent and manage the workflow.
### Initialize the Agent
```bash
aichatcoder init
```

This sets up the agent in your current repository.
### Run the Agent
```bash
aichatcoder run
```

This starts the agent, which will connect to the web UI and prepare to generate prompts and apply changes.

## Status
This is a mockup version of the AiChatCoder Agent.

Future versions will include:

- Full integration with the web UI at aichatcoder.com.

- Prompt generation for AI chat models (e.g., ChatGPT).

- Applying changes to repository files based on chat responses.

- Custom alias support (e.g., `acc init` instead of `aichatcoder init`).

- Cross-platform functionality.

## License
The AiChatCoder Agent is licensed under the MIT License. See the [LICENSE](https://github.com/aichatcoder/aichatcoder/blob/main/LICENSE) file for details.

## Credits
Created by [therceman](https://www.therceman.dev)

## Links
- Website: [aichatcoder.com](https://aichatcoder.com)
- PyPI: [aichatcoder](https://pypi.org/project/aichatcoder/)

