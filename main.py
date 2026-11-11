import json
import random
import os

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    # JSON 저장을 위해 객체를 딕셔너리로 변환하는 함수
    def to_dict(self):
        return {
            "prompt": self.prompt,
            "options": self.options,
            "answer": self.answer
        }

class QuizGame:
    def __init__(self):
        self.questions = []
        self.filename = "state.json"
        self.load_data()  # 시작하자마자 데이터 불러오기

    def load_data(self):
        """파일에서 퀴즈 데이터를 불러옵니다."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    # 딕셔너리 리스트를 Question 객체 리스트로 변환
                    self.questions = [Question(q['prompt'], q['options'], q['answer']) for q in data]
            except Exception as e:
                print(f"데이터 로드 중 오류 발생: {e}")
                self.questions = []
        else:
            # 파일이 없으면 기본 문제 세팅 (처음에만 실행됨)
            self.questions = [
                Question("파이썬의 탄생 연도는?", ["1989", "1991", "1995", "2000"], 2),
                Question("리스트에 요소를 추가하는 함수는?", ["add()", "push()", "append()", "insert()"], 3)
            ]
            self.save_data()

    def save_data(self):
        """현재 퀴즈 목록을 파일에 저장합니다."""
        with open(self.filename, "w", encoding="utf-8") as f:
            # 객체들을 딕셔너리 형태로 변환하여 저장
            json_data = [q.to_dict() for q in self.questions]
            json.dump(json_data, f, ensure_ascii=False, indent=4)

    def run(self):
        """메뉴를 출력하고 사용자 입력을 처리합니다."""
        while True:
            print("\n=== 파이썬 퀴즈 프로그램 ===")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 종료")
            
            choice = input("원하는 메뉴 번호를 입력하세요: ")
            
            if choice == '1':
                print("\n(퀴즈 풀기 기능을 곧 구현할 예정입니다!)")
            elif choice == '2':
                print("\n(퀴즈 추가 기능을 곧 구현할 예정입니다!)")
            elif choice == '3':
                print("\n--- 전체 퀴즈 목록 ---")
                for i, q in enumerate(self.questions, 1):
                    print(f"{i}. {q.prompt}")
            elif choice == '4':
                print("프로그램을 종료합니다. 안녕히 가세요!")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")

# 프로그램 실행
if __name__ == "__main__":
    game = QuizGame()
    game.run()