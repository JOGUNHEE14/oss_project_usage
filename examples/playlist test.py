from pymoood import EmotionPredictor, YouTubeRecommender
import webbrowser

def test_pymoood():
    # 감정 예측 모델 초기화
    try:
        predictor = EmotionPredictor()
        print("EmotionPredictor 로드 성공!")
    except Exception as e:
        print(f"EmotionPredictor 로드 실패: {e}")
        return

    # 유튜브 추천 시스템 초기화
    api_key = "api"  # YouTube API 키를 여기에 입력
    try:
        recommender = YouTubeRecommender(api_key)
        print("YouTubeRecommender 로드 성공!")
    except Exception as e:
        print(f"YouTubeRecommender 로드 실패: {e}")
        return

    # 사용자 입력
    user_input = input("당신의 감정을 표현하는 문장을 입력하세요: ")

    # 감정 예측
    try:
        emotion = predictor.predict_emotion(user_input)
        print(f"예측된 감정: {emotion}")
    except Exception as e:
        print(f"감정 예측 실패: {e}")
        return

    # 추천 영상 검색
    try:
        recommendations = recommender.get_recommendations(emotion)
        if recommendations:
            print("\n추천 노래:")
            for i, (title, url) in enumerate(recommendations, start=1):
                print(f"{i}. {title} - {url}")
            print("\n첫 번째 추천 노래를 브라우저에서 엽니다.")
            webbrowser.open(recommendations[0][1])
        else:
            print("추천 결과가 없습니다.")
    except Exception as e:
        print(f"YouTube 추천 실패: {e}")

if __name__ == "__main__":
    test_pymoood()
