# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("IDEA-CCNL/Ziya-LLaMA-13B-v1")
model = AutoModelForCausalLM.from_pretrained("IDEA-CCNL/Ziya-LLaMA-13B-v1")