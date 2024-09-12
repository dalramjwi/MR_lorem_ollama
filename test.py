import os
from transformers import AutoTokenizer, AutoModelForCausalLM
def run (prompt):
    print("모델 로딩 중...")
    tokenizer = AutoTokenizer.from_pretrained("gpt2")
    model = AutoModelForCausalLM.from_pretrained("gpt2")
    inputs = tokenizer(prompt, return_tensors = "pt",truncation=True, max_length=1024)
    print("모델에서 응답 생성 중...")
    outputs = model.generate(**inputs, max_new_tokens=100)  # 최대 100개의 새 토큰 생성

    print("응답 디코딩 중...")
    response = tokenizer.decode(outputs[0], skip_special_tokens=True, clean_up_tokenization_spaces=True)

    
    return response
  
current_dir = os.path.dirname(os.path.abspath(__file__))  # 현재 파일의 디렉토리 경로
text_dir = os.path.join(current_dir)
file_path = os.path.join(text_dir, "text.txt")
# 텍스트 파일에서 내용을 읽어옴
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# 사용자에게 프롬프트 입력을 받음
user_prompt = input("Prompt를 입력하세요: ")

# 사용자 입력 프롬프트와 텍스트 파일의 내용을 결합하여 최종 프롬프트 생성
combined_prompt = f"{user_prompt}: {text}"

# 프롬프트의 길이가 1024 토큰을 넘지 않도록 자름
tokenizer = AutoTokenizer.from_pretrained("gpt2")
combined_prompt_tokens = tokenizer.encode(combined_prompt, add_special_tokens=False)

if len(combined_prompt_tokens) > 1024:
    # 프롬프트가 1024 토큰을 넘는 경우 자름
    combined_prompt_tokens = combined_prompt_tokens[:1024]
    combined_prompt = tokenizer.decode(combined_prompt_tokens, skip_special_tokens=True)

# 결합된 프롬프트를 GPT-2 모델에 전달하여 응답 생성
response = run(combined_prompt)

# 응답을 파일로 저장할 경로 설정 (UTF-8 인코딩 지정)
output_file_path = os.path.join(text_dir, "response.txt")

# 생성된 응답을 텍스트 파일로 저장
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write(response)  # 응답 텍스트 저장

print(f"응답이 '{output_file_path}' 파일에 저장되었습니다.")
