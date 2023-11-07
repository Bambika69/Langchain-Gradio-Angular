from ctransformers import AutoModelForCausalLM
import gradio as gr
from flask_cors import CORS

# https://huggingface.co/TheBloke/LLaMA-7b-GGUF
# Initialize the model
llm = AutoModelForCausalLM.from_pretrained(
    "TheBloke/LLaMA-7b-GGUF",
    model_file="llama-7b.Q4_K_M.gguf",
    model_type="llama",
    gpu_layers=0
)


def generate_text(prompt, history):
    # Ensure all elements in history are strings
    history = [str(item) if not isinstance(item, str) else item for item in history]

    # Combine the history and the current prompt into a single string.
    combined_prompt = "\n".join(history + [prompt])
    response = llm(combined_prompt)
    response_text = response

    # Return the response text.
    return response_text


# Create Gradio Chat Interface
iface = gr.ChatInterface(
    fn=generate_text,
    theme='Bandika/agyrem'
)

# Launch the Gradio app
app = iface.launch(server_port=1791)
CORS(app)
