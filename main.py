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
    # 1. 테스트용 문제 생성
    test_quiz = Quiz("파이썬에서 리스트의 길이를 구하는 함수는?", ["size()", "len()", "count()", "length()"], 2)

    # 2. 문제 출력
    test_quiz.display()

    # 3. 사용자로부터 직접 입력 받기 (이 부분을 수정!)
    print("\n정답 번호를 입력하세요: ", end="")
    user_ans = int(input()) # 사용자가 입력한 글자를 숫자로 바꿉니다.

    if test_quiz.check_answer(user_ans):
        print("✅ 정답입니다!")
    else:
        print("❌ 틀렸습니다.")