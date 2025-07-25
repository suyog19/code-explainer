# 🧠 Code Explainer Bot

This project provides an AI-powered web app that explains code snippets at different expertise levels (beginner, intermediate, advanced) using OpenAI's GPT-4 model. The app is built with Gradio for the user interface.

## Features

- Paste any code snippet and get a clear explanation.
- Choose the explanation level: beginner, intermediate, or advanced.
- Powered by OpenAI GPT-4 via the `openai-agents` library.
- Simple Gradio web interface.

## Usage

1. **Install dependencies**  
   Run:
   ```sh
   pip install -r requirements.txt
   ```

2. **Set your OpenAI API key**  
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Run the app**  
   ```sh
   python app.py
   ```
   The Gradio interface will launch in your browser.

## Files

- [`app.py`](app.py): Main application code.
- [`requirements.txt`](requirements.txt): Python dependencies.
- `.env`: Environment variables (not included, create your own).

## License

This project is licensed under the GNU GPL v3. See