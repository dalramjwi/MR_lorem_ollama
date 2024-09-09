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
    
# 사용자에게 파일 내용에 대한 지시를 입력받음
user_prompt = input("Prompt를 입력하세요 : ")

# 사용자가 입력한 지시와 파일의 내용을 결합하여 prompt 생성
combined_prompt = f"{user_prompt}: {text}"

# 결합된 prompt를 LLaMA 모델에 전달
response = run(combined_prompt)
print(response)
