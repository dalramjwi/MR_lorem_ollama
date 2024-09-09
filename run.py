import os
import ollama

# LLaMA 모델을 호출하는 함수
def run(prompt):
    client = ollama.Client()
    response = client.generate(model="llama3.1:8b", prompt=prompt)
    return response

# 파일 경로 설정 및 텍스트 읽기 (UTF-8 인코딩 지정)
current_dir = os.path.dirname(os.path.abspath(__file__))
text_dir = os.path.join(current_dir)
file_path = os.path.join(text_dir, "text.txt")
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 사용자에게 파일 내용에 대한 지시를 입력받음
user_prompt = input("Prompt를 입력하세요: ")

# 사용자가 입력한 지시와 파일의 내용을 결합하여 prompt 생성
combined_prompt = f"{user_prompt}: {text}"

# 결합된 prompt를 LLaMA 모델에 전달하여 응답 받기
response = run(combined_prompt)

# 응답을 파일로 저장할 경로 설정 (UTF-8 인코딩 지정)
output_file_path = os.path.join(text_dir, "response.txt")

# 응답을 파일로 저장
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(response['response'])  # 응답의 'response' 키에 있는 텍스트 저장

print(f"응답이 '{output_file_path}' 파일에 저장되었습니다.")
