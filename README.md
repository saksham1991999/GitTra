# MLH-Hackathon-1

Translation script for git

This branch is for 1) parsing comments and 2) writing scripts for clone, commit, and push

### Development Setup

### Setting up/Installing the CLI client
- In the root directory, cd into the cli directory using `cd cli`.
- Run the following command:
  - **Linux**: `python3 -m pip install --editable .`
  - **Windows & Mac**: `pip install -e .`
- Use any `gittra` command now!

#### Commands:
- `gittra clone [GITHUB URL] [LANGUAGE]` Clones a Github repository with translated comments with the following options:
    - `--rename -n [DIRECTORY NAME]`
