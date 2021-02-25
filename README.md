# Gittra

## About
Scrolling through Chinese Github repositories and wishing you spoke the language? Yep, us too. Introducing Gittra - the new way to collaborate on projects written in different spoken languages. As a coder, you're well-versed in all sorts of programming languages, and spoken languages shouldn't be a barrier either!

Through our CLI client, we let users fork, clone, and push to a repository written in a different language, which will then be translated to their language of choice. Using a Python translation module, we've taken care of translating comments for you so that you can focus on understanding the code and collboarating with other coders around the world.

## How it works
When the user forks or clones a foreign repository, we take care of translating all the comments and pushing this version into a new 'translated' branch. As the user pushes changes onto the translated branch in their own languages, we'll automatically update these changes in the 'main' branch. This way, all contributors can work in their own languages while making seamless pull requests in the original repository language. 

## Development Setup

### Prerequisites
- Ensure that you have the Github CLI client installed. If not, follow the instructions [here](https://github.com/cli/cli) to set it up.
- Ensure that you have pip and Python installed properly.
- Optional: Set up a virtual environment by following the instructions [here](https://docs.python.org/3/library/venv.html)
- Install the required dependencies using `pip install -r requirements.txt`

### Installing the CLI client
- In the root directory, run the following command:
  - **Linux**: `python3 -m pip install --editable .`
  - **Windows & Mac**: `pip install -e .`
- Use any `gittra` command now to fork, clone and push repos in different languages!

### Usage Commands
- `gittra fork [GITHUB URL] [LANGUAGE]` Forks a Github repository and translates comments into a given language on a new 'translated' branch
- `gittra clone [GITHUB URL] [LANGUAGE]` Clones a Github repository and translates comments into a given language on a new 'translated' branch
- `gittra push` Pushes into the 'translated' branch of the respository and automatically updates the 'main' branch as well
