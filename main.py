import random
class Quiz:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def display(self):
        print(f"\n[문제] {self.question}")
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def check_answer(self, user_input):
        return user_input == self.answer
    
# --- 테스트 코드 ---
if __name__ == "__main__":
    questions = [
        Quiz("파이썬에서 리스트의 길이를 구하는 함수는?", ["size()", "len()", "count()", "length()"], 2),
        Quiz("출력할 때 사용하는 함수는?", ["print()", "input()", "out()", "show()"], 1),
        Quiz("정수를 만드는 함수는?", ["str()", "float()", "int()", "list()"], 3),
        Quiz("파이썬 파일의 확장자는 무엇인가요?", [".txt", ".py", ".js", ".java"], 2),
        Quiz("주석(설명)을 달 때 사용하는 기호는?", ["//", "/* */", "#", "--"], 3),
        Quiz("리스트에 요소를 추가하는 함수는?", ["add()", "push()", "append()", "insert_end()"], 3),
        Quiz("파이썬에서 '참'을 나타내는 값은?", ["True", "true", "YES", "1"], 1),
        Quiz("문자열을 숫자로 바꾸는 함수는?", ["str()", "int()", "float()", "bool()"], 2)
        ]

    # [2. 위치] 리스트를 만든 직후, for문이 시작되기 전에 섞어줍니다!
    random.shuffle(questions) 

    print("🚀 퀴즈 게임을 시작합니다! (순서 랜덤)\n")
    
    score = 0
selected_questions = questions[:3]  # 1. 먼저 3개만 골라냅니다.

for q in selected_questions:        # 2. 고른 3개에 대해서만 반복합니다.
    q.display()
    try:
        user_ans = int(input("정답 번호를 입력하세요: "))
        if q.check_answer(user_ans):
            print("✅ 정답입니다!\n")
            score += 1
        else:
            print("❌ 틀렸습니다.\n")
    except ValueError:
        print("⚠️ 숫자만 입력해주세요!\n")

# 3. 마지막 결과 출력 (들여쓰기 밖으로!)
print(f"🏁 게임 종료! 최종 점수: {score} / {len(selected_questions)}")