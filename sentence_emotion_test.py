from pymood import EmotionPredict


class SimpleTester:
    def __init__(self, model_path, vectorizer_path, label_encoder_path):
        self.predictor = EmotionPredictor(
            model_path=model_path,
            vectorizer_path=vectorizer_path,
            label_encoder_path=label_encoder_path
        )

    def run_tests(self):
        # 테스트 케이스 정의
        test_cases = [
            "정말 화가 납니다.",  # 분노 예상
            "오늘은 최고의 날이에요! 정말 행복하고 기뻐요!",  # 기쁨 예상
            "기분이 불안하고 마음이 편하지 않아요.",  # 불안 예상
            "갑작스러운 상황에 너무 당황스러워요.",  # 당황 예상
            "너무 슬프고 눈물이 납니다."  # 슬픔 예상
        ]

        # 테스트 실행 및 결과 출력
        for text in test_cases:
            result = self.predictor.predict(text)
            print(f"테스트 입력: {text}")
            print(f"예측 결과: {result}")
            print()


if __name__ == "__main__":
    # 경로 설정
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
    model_path = os.path.join(base_path, 'emotion_mlp_model.sav')
    vectorizer_path = os.path.join(base_path, 'emotion_vectorizer.pkl')
    label_encoder_path = os.path.join(base_path, 'emotion_label_encoder.pkl')

    # SimpleTester 실행
    tester = SimpleTester(model_path, vectorizer_path, label_encoder_path)
    tester.run_tests()
