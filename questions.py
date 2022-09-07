import requests


class Questions:
    def __init__(self, question_number, category, difficulty, question_mode):
        self.question_number = question_number
        self.category = category
        self.difficulty = difficulty
        self.question_mode = question_mode

    def get_question_data(self):
        parameters = {
            "amount": self.question_number,
            "category": self.category,
            "difficulty": self.difficulty,
            "type": self.question_mode
        }
        response = requests.get(url="https://opentdb.com/api.php", params=parameters)
        question_data = response.json()["results"]

        return question_data

# variable = Questions("10", "12", "easy", "multiple")
# print(variable.get_question_data())
