class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용
        self.choices = choices    # 4개의 선택지 (리스트)
        self.answer = answer      # 정답 번호 (1~4)

    def display(self):
        """문제를 화면에 예쁘게 출력합니다."""
        print(f"\n[문제] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")

    def check_answer(self, user_input):
        """사용자 입력이 정답인지 확인합니다."""
        return user_input == self.answer

# --- 테스트 코드 ---
if __name__ == "__main__":
    questions = [
        Quiz("파이썬에서 리스트의 길이를 구하는 함수는?", ["size()", "len()", "count()", "length()"], 2),
        Quiz("출력할 때 사용하는 함수는?", ["print()", "input()", "out()", "show()"], 1),
        Quiz("정수를 만드는 함수는?", ["str()", "float()", "int()", "list()"], 3)
    ]

    print("🚀 퀴즈 게임을 시작합니다!\n")
    
    # [추가] 점수를 저장할 변수 생성
    score = 0

    for q in questions:
        q.display()
        try:
            user_ans = int(input("정답 번호를 입력하세요: "))
            if q.check_answer(user_ans):
                print("✅ 정답입니다!\n")
                score += 1  # [추가] 정답일 때 점수 1점 증가
            else:
                print("❌ 틀렸습니다.\n")
        except ValueError:
            print("⚠️ 숫자만 입력해주세요! 다음 문제로 넘어갑니다.\n")

    # [추가] 최종 결과 출력
    print("=" * 30)
    print(f"🏁 게임 종료! 당신의 점수는 {score}/{len(questions)}입니다.")
    print("=" * 30)
    