from llama_cpp import Llama
import time
import json
import re

start_time = time.time()

prompts_dir = "prompts/"
prompt_file = "prompt_2.txt"
with open(file=f"{prompts_dir}{prompt_file}", mode="r", encoding="utf8") as infile:
    prompt_template = infile.read()

seo_data_dir = "data/"
seo_data_file = "data_2.json"
with open(file=f"{seo_data_dir}{seo_data_file}", mode="r", encoding="utf8") as infile:     
    seo_data_json = json.load(infile)               
    seo_data = json.dumps(seo_data_json)
    seo_data = re.sub(r'\s+', '', seo_data) 
    seo_data = re.sub(r'\r?\n', '', seo_data) 


# Path to your quantized model
MODEL_PATH  = "models/mistral-7b-instruct-v0.2.Q6_K.gguf"

# Initialize the model (you can tweak n_ctx for larger input)
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=32768,
    n_threads=40,
    n_gpu_layers=-1,  # 👉 runs first 20 layers on GPU, rest on CPU
    n_batch=700,           # adjust if running into memory issues
    verbose=True
)

print(llm.context_params.n_ctx)

prompt = f"""
    {prompt_template}    
    {seo_data}
"""


ressponse_dir = "response/"

output = llm(
    prompt,
    max_tokens=32768,  # allow full completion
    temperature=1.2,  # high creativity
    top_p=0.9,        # nucleus sampling, balanced creativity
    typical_p=0.95,   # prefer typical next tokens
    repeat_penalty=1.2,   # discourages repeating phrases
    presence_penalty=0.8, # encourages introducing new ideas
    stop=None,        # don't stop generation early
    echo=False,
    stream=False,
    seed=None        
)
end_time = time.time()
file_name = int(time.time())
response_file = f"{ressponse_dir}{file_name}.json"
output["model"] = MODEL_PATH
output["total_time"] = f"{end_time - start_time:.2f}"
    
print("🔍 Suggestions:")
print(output)

with open(file=response_file,mode="w",encoding="utf8") as outfile:
    ouput_json = json.dumps(output,indent=4)
    outfile.write(ouput_json)


# Print total time taken
print(f"Total time taken: {end_time - start_time:.2f} seconds")