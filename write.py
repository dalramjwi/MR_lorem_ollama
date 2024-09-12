import lorem
# 1. Lorem Ipsum 100개 생성
lorem_list = [lorem.sentence() for _ in range(10)]  # 100개의 문장 생성

# 2. text.txt 파일에 쓰기
with open("text.txt", "w") as file:
    for sentence in lorem_list:
        file.write(sentence + "\n")  # 각 문장을 줄바꿈하여 파일에 작성

print("text.txt 파일에 100개의 Lorem Ipsum 문장이 작성되었습니다.")