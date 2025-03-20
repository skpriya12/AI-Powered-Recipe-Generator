import openai
import os
import gradio as gr

# Load OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_recipe(ingredients, temperature=0.7):
    """Generate a recipe using OpenAI's GPT-3.5 Turbo model."""
    if not ingredients.strip():
        return "Please enter at least one ingredient."

    prompt = f"Create a short and simple recipe using the following ingredients:\n{ingredients}\n"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,  # Controls creativity (0 = strict, 1 = creative)
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"Error: {str(e)}"

# Gradio UI
iface = gr.Interface(
    fn=generate_recipe,
    inputs=[
        gr.Textbox(label="Enter Ingredients (comma-separated)"),
        gr.Slider(0, 1, value=0.7, label="Creativity Level (Temperature)")
    ],
    outputs=gr.Textbox(label="Generated Recipe"),
    title="AI-Powered Recipe Generator",
    description="Enter ingredients and let AI generate a quick recipe for you!",
)

# Launch UI
iface.launch()
