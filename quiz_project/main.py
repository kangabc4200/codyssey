import json
import random
import os

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

class QuizGame:
    def __init__(self):
        # 현재 파일(main.py) 위치를 기준으로 quiz_project 폴더 내 state.json 경로 설정
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(self.base_path, 'state.json')
        
        self.questions = []
        self.high_score = 0
        self.load_data()

    def load_data(self):
        """파일에서 데이터를 불러오거나, 형식이 맞지 않으면 기본 문제를 생성합니다."""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 데이터가 딕셔너리 형태일 때만 읽기 (AttributeError 방지)
                    if isinstance(data, dict):
                        self.high_score = data.get('high_score', 0)
                        self.questions = [
                            Question(q['prompt'], q['options'], q['answer']) 
                            for q in data.get('questions', [])
                        ]
                        if self.questions: return # 성공적으로 읽었으면 종료
            
            # 파일이 없거나 형식이 다르면 기본 문제 로드
            self.set_default_questions()
        except Exception:
            self.set_default_questions()

    def set_default_questions(self):
        """기본 문제 8개를 설정하고 저장합니다."""
        self.questions = [
            Question("파이썬에서 리스트에 요소를 추가하는 함수는?", ["1. add()", "2. append()", "3. insert()", "4. push()"], 2),
            Question("파이썬의 주석 기호는?", ["1. //", "2. /* */", "3. #", "4. <!-- -->"], 3),
            Question("다음 중 정수형 타입은?", ["1. str", "2. float", "3. int", "4. bool"], 3),
            Question("출력할 때 사용하는 함수는?", ["1. input()", "2. print()", "3. output()", "4. write()"], 2),
            Question("문자열 길이를 구하는 함수는?", ["1. size()", "2. length()", "3. count()", "4. len()"], 4),
            Question("조건문을 시작하는 키워드는?", ["1. for", "2. while", "3. if", "4. def"], 3),
            Question("함수를 정의할 때 사용하는 키워드는?", ["1. func", "2. define", "3. def", "4. function"], 3),
            Question("나머지를 구하는 연산자는?", ["1. /", "2. //", "3. %", "4. **"], 3)
        ]
        self.save_data()

    def save_data(self):
        """현재 상태를 state.json 파일에 저장합니다."""
        data = {
            'high_score': self.high_score,
            'questions': [
                {'prompt': q.prompt, 'options': q.options, 'answer': q.answer}
                for q in self.questions
            ]
        }
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def play_quiz(self):
        if len(self.questions) < 3:
            print("\n⚠️ 문제가 부족합니다. 3개 이상의 문제를 등록해주세요.")
            return

        random_questions = random.sample(self.questions, 3)
        score = 0

        for i, q in enumerate(random_questions, 1):
            print(f"\n[문제 {i}] {q.prompt}")
            for opt in q.options:
                print(opt)
            
            try:
                ans = int(input("정답 번호 입력: "))
                if ans == q.answer:
                    print("✅ 정답입니다!")
                    score += 1
                else:
                    print(f"❌ 틀렸습니다. 정답은 {q.answer}번입니다.")
            except ValueError:
                print("⚠️ 숫자만 입력 가능합니다.")

        print(f"\n결과: {score} / 3 점")
        if score > self.high_score:
            print("🎊 최고 점수를 경신했습니다!")
            self.high_score = score
            self.save_data()

    def add_quiz(self):
        print("\n[새 문제 추가]")
        try:
            prompt = input("문제 내용: ")
            opts = [f"{i}. {input(f'보기 {i} 내용: ')}" for i in range(1, 5)]
            ans = int(input("정답 번호(1-4): "))
            
            if 1 <= ans <= 4:
                self.questions.append(Question(prompt, opts, ans))
                self.save_data()
                print("✅ 문제가 성공적으로 추가되었습니다!")
            else:
                print("❌ 정답 번호는 1~4 사이여야 합니다.")
        except ValueError:
            print("❌ 올바른 숫자를 입력해 주세요.")

    def show_list(self):
        print("\n=== 전체 문제 목록 ===")
        if not self.questions:
            print("등록된 문제가 없습니다.")
        for i, q in enumerate(self.questions, 1):
            print(f"{i}. {q.prompt}")

    def run(self):
        while True:
            # 메뉴를 세로로 출력하도록 수정
            print(f"\n============================")
            print(f" 파이썬 퀴즈 게임 (최고점: {self.high_score})")
            print(f"============================")
            print("1. 퀴즈 시작")
            print("2. 문제 추가")
            print("3. 문제 목록 보기")
            print("4. 게임 종료")
            print(f"----------------------------")
            
            choice = input("선택: ")
            
            if choice == '1':
                self.play_quiz()
            elif choice == '2':
                self.add_quiz()
            elif choice == '3':
                self.show_list()
            elif choice == '4':
                print("게임을 종료합니다. 수고하셨습니다!")
                break
            else:
                print("⚠️ 잘못된 입력입니다. 1~4번 중 선택해주세요.")

if __name__ == "__main__":
    game = QuizGame()
    game.run()