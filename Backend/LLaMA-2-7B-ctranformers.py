from ctransformers import AutoModelForCausalLM
import gradio as gr
from flask_cors import CORS

# https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF
# Set gpu_layers to the number of layers to offload to GPU. Set to 0 if no GPU acceleration is available on your system.
llm = (AutoModelForCausalLM.from_pretrained(
    "TheBloke/Llama-2-7b-Chat-GGUF",
    model_file="llama-2-7b-chat.q4_K_M.gguf",
    model_type="llama",
    gpu_layers=0
))


def generate_text(prompt):
    response = llm(prompt)
    return response


# Create Gradio Interface
iface = gr.Interface(
    fn=generate_text,
    inputs="text",
    outputs="text",
    live=False,
    theme='Bandika/agyrem'
)
app = iface.launch(server_port=1782)
CORS(app)
