import json
import random
import os

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

    def to_dict(self):
        return {"prompt": self.prompt, "options": self.options, "answer": self.answer}

    @classmethod
    def from_dict(cls, data):
        return cls(data["prompt"], data["options"], data["answer"])

class QuizGame:
    def __init__(self):
        self.filename = "state.json"
        self.questions = []
        self.high_score = 0
        self.load_data()

    def load_data(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.questions = [Question.from_dict(q) for q in data.get("questions", [])]
                    self.high_score = data.get("high_score", 0)
            else:
                # 5개 이상의 기본 문제 세팅
                self.questions = [
                    Question("파이썬에서 리스트에 요소를 추가하는 함수는?", ["add()", "append()", "push()", "insert()"], 2),
                    Question("파이썬의 탄생 연도는?", ["1989", "1991", "1995", "2000"], 2),
                    Question("딕셔너리의 키-값 쌍을 모두 가져오는 메서드는?", ["keys()", "values()", "items()", "get()"], 3),
                    Question("출력 시 줄바꿈을 하지 않으려면 print(..., end='')에서 end에 무엇을 넣나?", ["' '", "''", "'\\n'", "'\\t'"], 2),
                    Question("파이썬에서 나머지를 구하는 연산자는?", ["/", "//", "%", "**"], 3)
                ]
                self.save_data()
        except Exception:
            self.questions = []
            self.high_score = 0

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            data_to_save = {
                "high_score": self.high_score,
                "questions": [q.to_dict() for q in self.questions]
            }
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)

    def run(self):
        while True:
            print(f"\n=== 파이썬 퀴즈 (최고 점수: {self.high_score}) ===")
            print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록 보기\n4. 종료")
            choice = input("선택: ")

            if choice == '1':
                if len(self.questions) < 3:
                    print("⚠️ 문제가 3개 이상이어야 시작 가능합니다.")
                    continue
                score = 0
                sample = random.sample(self.questions, 3)
                for q in sample:
                    print(f"\n[문제] {q.prompt}")
                    for i, opt in enumerate(q.options, 1): print(f"{i}. {opt}")
                    try:
                        if int(input("정답: ")) == q.answer:
                            print("✅ 정답!"); score += 1
                        else: print(f"❌ 오답! (정답: {q.answer})")
                    except: print("⚠️ 숫자만 입력!")
                
                print(f"\n이번 점수: {score}/3")
                if score > self.high_score:
                    print("🎊 최고 점수 갱신!")
                    self.high_score = score
                    self.save_data()

            elif choice == '2':
                p = input("문제: ")
                opts = [input(f"보기 {i}: ") for i in range(1, 5)]
                try:
                    ans = int(input("정답(1-4): "))
                    self.questions.append(Question(p, opts, ans))
                    self.save_data()
                except: print("❌ 저장 실패")

            elif choice == '3':
                for i, q in enumerate(self.questions, 1): print(f"{i}. {q.prompt}")

            elif choice == '4': break
            