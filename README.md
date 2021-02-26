[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<p align="center">
  <a href="www.gittra.com">
    <img src="https://gittra.herokuapp.com/static/images/gittralogo.png" alt="Logo" height="80">
  </a>

  <h3 align="center">GitTra</h3>

  <p align="center">
    Git add-on for translating comments on open-source project. 
    <br />
    Helps people work on inter-language collaboration.
  </p>
</p>



## Development Setup

### Prerequisites
- Ensure that you have the Github CLI client installed. If not, follow the instructions [here](https://github.com/cli/cli) to set it up.
- Ensure that you have pip and python installed.
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
