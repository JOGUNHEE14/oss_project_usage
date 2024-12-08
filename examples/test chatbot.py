from pymoood.chatbot import Chatbot

# Cohere API 키 설정 (직접 입력)
API_KEY = "api"

# Chatbot 클래스 초기화
bot = Chatbot(API_KEY)

# 사용자 입력으로 실시간 대화
print("=== Chatbot 상담 시작 ===")
print("상담을 종료하려면 '종료'라고 입력하세요.")

while True:
    user_input = input("User: ")  # 사용자로부터 입력받기
    if user_input.strip() in ["종료", "exit", "quit"]:  # 종료 조건
        print("Chatbot: 상담을 종료합니다. 좋은 하루 되세요!")
        break
    chatbot_response = bot.Answer(user_input)  # Chatbot 답변 생성
    print(f"Chatbot: {chatbot_response}")
