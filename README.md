---
title: code-explainer
app_file: app.py
sdk: gradio
sdk_version: 5.38.1
---
# 🧠 Code Explainer Bot

Code Explainer Bot is an AI-powered web application that explains code snippets at different expertise levels (beginner, intermediate, advanced) using OpenAI's GPT-4 model. The app features a simple Gradio interface for easy interaction.

## Features

- **Code Explanation:** Paste any code snippet and receive a clear explanation.
- **Expertise Levels:** Choose the explanation level: beginner, intermediate, or advanced.
- **OpenAI GPT-4:** Uses the `openai-agents` library to interact with GPT-4.
- **Web Interface:** Built with Gradio for a user-friendly experience.

## Getting Started

### Prerequisites

- Python 3.8+
- An OpenAI API key

### Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/summarize-youtube-video.git
   cd summarize-youtube-video
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

### Running the Application

```sh
python app.py
```

- The Gradio web interface will launch in your browser.
- Paste your code, select the target user level, and get an explanation.

## Project Structure

- [`app.py`](app.py): Main application code. Contains the Gradio interface and the code explanation logic.
- [`requirements.txt`](requirements.txt): Python dependencies.
- [`LICENSE`](LICENSE): GNU GPL v3 license.
- `.env`: Environment variables (not included, create your own).
- `.gitignore`: Standard Python and editor ignores.

## How It Works

- The app loads your OpenAI API key from `.env` using `dotenv`.
- When you submit code and select a level, the app sends a prompt to GPT-4 via the `openai-agents` library.
- GPT-4 returns a code explanation tailored to the selected expertise level.
- The explanation is displayed in the Gradio interface.

## Example Usage

1. Paste your code:
   ```python
   def add(a, b):
       return a + b
   ```
2. Select "beginner" as the target user level.
3. Click submit.
4. Receive a simple explanation of the code.

## License

This project is licensed under the GNU General Public License v3.0. See [`LICENSE`](LICENSE) for details.

## Acknowledgements

- [Gradio](https://gradio.app/)
- [OpenAI](https://openai.com/)
- [openai-agents](https://github.com/openai/openai-agents)
- [dotenv](https://pypi.org/project/python-dotenv/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For questions or support, please open an issue