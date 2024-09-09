import os
import ollama

def run(prompt):
    client = ollama.Client()
    response = client.generate(model="llama3.1:8b", prompt = prompt)
    return response


current_dir = os.path.dirname(os.path.abspath(__file__))
text_dir = os.path.join(current_dir)
file_path = os.path.join(text_dir,"text.txt")
with open(file_path, "r") as file:
    text = file.read()
    

response = run(text)
print(response)