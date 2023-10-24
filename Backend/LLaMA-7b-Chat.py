import gradio as gr
from flask_cors import CORS
from transformers import AutoModelForCausalLM

# Load pre-trained LLaMa model
model = AutoModelForCausalLM.from_pretrained("TheBloke/LLaMA-7b-GGUF", model_file="llama-7b.Q4_K_M.gguf", model_type="llama", gpu_layers=0)

# Define a list to store the history of questions
question_history = []

def get_last_question():
    """Returns the last question asked."""
    return question_history[-1] if question_history else None

def set_last_question(question):
    """Stores the given question as the last question."""
    question_history.append(question)

# Define a function to generate text given a prompt
def generate_text(prompt):
    # Get the last question asked (if any)
    last_question = get_last_question()

    # Generate text based on the prompt and last question
    response = model(prompt, last_question)

    # Store the current question as the last question
    set_last_question(prompt)

    return response




gr.ChatInterface(generate_text).launch(server_port=1791)
# Launch the Gradio app with CORS enabled

