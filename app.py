from dotenv import load_dotenv
import gradio as gr
from openai import OpenAI
from agents import Agent, Runner, trace, function_tool
import os

def load_dotenv_file():
    load_dotenv(override=True)

# Function to explain the code using GPT
async def explain_code(code, level):
    load_dotenv_file()
    if not code:
        return "Please paste some code to explain."

    prompt = f"""
    Explain the following code to a {level} level programmer in simple terms.

    Code:
    {code}
    """

    try:
        messages = '{"role": "system", "content": "You are a helpful assistant that explains code clearly."},'
        messages += '{"role": "user", "content": {' + prompt +'}'

        tools = []
        agent = Agent(
            name="Code Explainer",
            model="gpt-4",
            instructions=messages,
            tools=tools
        )
        result = await Runner.run(agent, "")
        return result.final_output
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Gradio Interface
demo = gr.Interface(
    fn=explain_code,
    inputs=[
        gr.Textbox(label="Paste your code here", lines=10, placeholder="e.g. def add(a, b): return a + b"),
        gr.Radio(choices=["beginner", "intermediate", "advanced"], label="Target User Level", value="beginner")
    ],
    outputs=gr.Textbox(label="Explanation"),
    title="🧠 Code Explainer Bot",
    description="Paste your code and choose the level of explanation. The bot will explain it in simple language using AI."
)

demo.launch()
