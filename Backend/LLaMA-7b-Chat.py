from ctransformers import AutoModelForCausalLM
import gradio as gr
from flask_cors import CORS
# https://huggingface.co/TheBloke/LLaMA-7b-GGUF

llm = AutoModelForCausalLM.from_pretrained(
    "TheBloke/LLaMA-7b-GGUF",
    model_file="llama-7b.Q4_K_M.gguf",
    model_type="llama",
    gpu_layers=0)


def generate_text(prompt, history):
    response = llm(prompt)
    return response


# Create Gradio Interface
iface = gr.ChatInterface(
    fn=generate_text,
    theme='Bandika/agyrem'
)

app = iface.launch(server_port=1791)
CORS(app)
