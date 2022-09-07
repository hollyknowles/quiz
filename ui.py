import tkinter as tk


class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Quiz Game")
        self.window.geometry("700x700")
        title_label = tk.Label(self.window, text="Quiz Game", font="bold 24", fg="blue")
        title_label.pack()

        question_number_label = tk.Label(self.window, text="How many questions?")
        question_number_label.pack()
        question_number_entry = tk.Spinbox(self.window, from_=5, to=50)
        question_number_entry.pack()

        category_label = tk.Label(self.window, text="What category?")
        category_label.pack()
        default_category = tk.StringVar(self.window)
        default_category.set("Any Category")  # initial value
        category_label_option = tk.OptionMenu(self.window, default_category, "General Knowledge",
                                              "Books",
                                              "Film",
                                              "Music",
                                              "Musicals and Theatre",
                                              "Television",
                                              "Video Games",
                                              "Board Games",
                                              "Science and Nature",
                                              "Computers",
                                              "Mathematics",
                                              "Mythology",
                                              "Sports",
                                              "Geography",
                                              "History",
                                              "Politics",
                                              "Art",
                                              "Celebrities",
                                              "Animals",
                                              "Vehicles",
                                              "Comics",
                                              "Gadgets",
                                              "Anime and Manga",
                                              "Cartoon and Animation")
        category_label_option.pack()

        difficulty_label = tk.Label(self.window, text="What difficulty level?")
        difficulty_label.pack()
        default_difficulty = tk.StringVar(self.window)
        default_difficulty.set("Easy")  # initial value
        difficulty_label_option = tk.OptionMenu(self.window, default_difficulty, "Medium", "Hard")
        difficulty_label_option.pack()

        type_label = tk.Label(self.window, text="Multiple choice or True/False?")
        type_label.pack()
        default_type = tk.StringVar(self.window)
        default_type.set("Multiple Choice")  # initial value
        type_label_option = tk.OptionMenu(self.window, default_type, "True or False")
        type_label_option.pack()

        start_button = tk.Button(self.window, text="GO!", command=self.start_quiz)
        start_button.pack()

        self.window.mainloop()

    def start_quiz(self):
        pass


test = UI()
