from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import Image
from kivy.properties import ListProperty, StringProperty
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.core.window import Window

class FirstScreen(Screen):
    def enter_button_pressed(self):
        app = MDApp.get_running_app()
        input_name = self.ids.name_input.text
        app.root.transition.direction = 'left'
        app.root.current = 'second'
        app.root.get_screen('second').update_welcome_label(input_name)
class SecondScreen(Screen):
    def on_enter(self):
        self.add_logos()

    def update_welcome_label(self, name):
        self.ids.welcome_label.text = f'Welcome {name}!\n Choose your battleground of knowledge!\n' \
                                      f' Select subject and embark on the\n' \
                                      f' quiz challenge to test your intellect!'
    def add_logos(self):
        logos_layout = MDFloatLayout()
        logos = [
            "common.png",
            "lfs.png",
            "command.png",
            "Navy.png",
        ]
        for i, logo_path in enumerate(logos):
            logo_button = Image(
                source=logo_path,
                size_hint=(0.4, 0.4),
                pos_hint={'x': 0.06 + (i % 2) * 0.49, 'y': 0.29 - (i // 2) * 0.23},
            )
            logos_layout.add_widget(logo_button)

        self.ids.logos_container.add_widget(logos_layout)

    def start_quiz(self):
        quiz_screen = self.manager.get_screen('quiz')
        quiz_screen.reset_quiz_state()
        self.manager.current = 'quiz'
        quiz_screen.load_question()

    def start_quiz2(self):
        quiz_screen2 = self.manager.get_screen('quiz2')
        quiz_screen2.reset_quiz_state()
        self.manager.current = 'quiz2'
        quiz_screen2.load_question()

    def assess_all_quiz(self):
        # Access the ScreenManager and change to the 'enter_code' screen
        self.manager.current = 'enter_code'

class QuizScreen(Screen):
    current_question = 0
    score = 0

    questions = [
        {"question": "1. The Pacific is the ......\n ocean in the world",
         "options": ["large", "Larger", "Largest", "more large"], "correct_answer": 2},
        {"question": "2. Mr. Mensah has ..... \nmoney than Mr. Abu.", "options": ["more", "Much", "Most", "Mucher"],
         "correct_answer": 0},
        {"question": "3. He was looking sad, now he is ......",
         "options": ["happier", "happy", "more happy", "more happier"], "correct_answer": 1},
        {"question": "4. Bananas are not as ......\nas pineapples",
         "options": ["sweetest", "Sweet", "Sweeter", "much sweet"], "correct_answer": 1},
        {"question": "5. The sun gives a\n..... light than the moon.",
         "options": ["brightest", "Brighter", "more brighter", "Bright"], "correct_answer": 1},
        {"question": "6. I have seen mine; have\n you seen ..... ?",
         "options": ["your", "Yours", "your's", "yours'"], "correct_answer": 1},
        {"question": "7. Roni is a good friend of.....", "options": ["hers", "he's", "She", "We"],
         "correct_answer": 0},
        {"question": "8. Show me the boy ....\n slapped you without just cause.",
         "options": ["which", "Who", "Whom", "Whose"], "correct_answer": 1},
        {"question": "9. Is that the man ..... \ncar was stolen last week.?",
         "options": ["who's", "Whose", "Whom", "Which"], "correct_answer": 1},
        {"question": "10. The pencil ...... was broken\n belongs to her.",
         "options": ["who", "Whom", "Whose", "which"], "correct_answer": 3},
        {"question": "11. To ..... it may concern", "options": ["whom", "who", "who's", "Who"],
         "correct_answer": 0},
        {
            "question": "12. The passive form of the \nstatement, 'The boy broke the ruler'\n is, ' The ruler ......... broken by the boy.",
            "options": ["has been", "was", "Is", "was being"], "correct_answer": 1},
        {
            "question": "13. The statement, 'Mr. Bako \nis killing a ram', is best\n written in the passive form as,\n ' A ram ...........by Mr. Bako.",
            "options": ["is being killed", "was being killed", "has been killed", "had been killed"],
            "correct_answer": 0},
        {"question": "14. 'My mother cooks rice' when \nwritten in passive form will be ",
         "options": ["Rice is cooked by my mother", "Rice is being cooked by my mother", "Rice was cooked by my mother",
                     "Rice was being cooked by my mother"], "correct_answer": 0},
        {"question": "15. 'The girl opened the door'\n is written in passive form as .........",
         "options": ["The door is opened by the girl", "The door was being opened by the girl",
                     "The door was opened by the girl", "The door has been opened by the girl"], "correct_answer": 2},
        {"question": "CHOOSE THE WORD WHICH IS\n ALMOST OPPOSITE IN MEANING\n TO THE WORD IN QUESTION 16-20.\n16. The clerk is on (permanent)\nappointment.",
         "options": ["attractive", "Lasting", "Fixed", "temporary"], "correct_answer": 3},
        {"question": "17. Our team (won) the match.", "options": ["lost", "played", "watched", "Abandoned"],
         "correct_answer": 0},
        {"question": "18. I do not think that ship will ( float).", "options": ["capsize", "Leak", "sink", "Wreck"],
         "correct_answer": 2},
        {"question": "19. His cocoa farm brought him \ngreat (profit).",
         "options": ["discomfort", "Disturbance", "loss", "Problem"], "correct_answer": 2},
        {"question": "20. My friends (praised) me \nfor paying them a visit.",
         "options": ["attacked", "blamed", "disturb", "Worried"], "correct_answer": 1},
        {"question": "21.The water in the fridge has .........",
         "options": ["freezer", "Frozen", "Froze", "Freeze"], "correct_answer": 1},
        {"question": "22. The thieves have ..... away.", "options": ["run", "Ran", "Running", "runs"],
         "correct_answer": 0},
        {"question": "23. The money was ..... under the bed.", "options": ["hide", "hidden", "Hiding", "Hid"],
         "correct_answer": 1},
        {"question": "24. Why have you .... the red biro?","options": ["choose", "Chose", "chosen", "Choice"],
         "correct_answer": 2},
        {"question": "25. A dog ..... Mary yesterday","options": ["bite", "Bitting", "bitten", "Bit"],
         "correct_answer": 3}
    ]
    def on_pre_enter(self):
        self.load_question()
    def load_question(self):
        question = self.questions[self.current_question]
        self.ids.question_label.text = question["question"]
        for i, option in enumerate(question["options"]):
            self.ids[f'option_{i + 1}'].text = option

    def __init__(self, **kwargs):
        super(QuizScreen, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()
    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False
    def show_result(self):
        result_label = self.manager.get_screen("result_screen").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen"
    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0
        self.load_question()
        self.clear_buttons()

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreen(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"

class CorrectionScreen1(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreen.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)
class QuizScreen2(Screen):
    current_question = 0
    score = 0

    questions = [
        {
            "question": "1. Express eighty three million,\neight hundred and thirteen thousand\n in figures.",
            "options": ["80380013", "83800013", "8300013", "800380013"], "correct_answer": 1},
        {"question": "2. Covert DXIV to Arabic numerals.",
         "options": ["545", "514", "404", "245"], "correct_answer": 1},
        {"question": "3. Divide 625.75 by 5",
         "options": ["125.15", "121.55", "15.15", "109.5"], "correct_answer": 0},
        {"question": "4. Find the H.C.F of 13 and 33", "options": ["64", "3", "13", "33"],
         "correct_answer": 2},
        {"question": "5. What is the quotient of \n576 and 12?",
         "options": ["12", "49", "48", "60"], "correct_answer": 2},
        {
            "question": "6. What is the place value \nof 7 in 5,670,038?",
            "options": ["Million", "Hundred of thousand", "Tens", "Tens of thousand"], "correct_answer": 3},
        {"question": "7. State the common factors\n of 15, 30 and 60",
         "options": ["15, 30, 60", "3, 5, 10", "3, 5, 15", "5, 15, 20"], "correct_answer": 1},
        {"question": "8. If x + 17 = 27. What is x?", "options": ["9", "0", "10", "17"],
         "correct_answer": 2},
        {"question": "9. Calculate the value of x\n in the equation x/4 =42/4",
         "options": ["42", "8", "52", "168"], "correct_answer": 0},
        {"question": "10. Find the difference \nbetween 13 2/3 and 2 1/3 ",
         "options": ["15 11/15", "11 3/2", "11 6/15", "11 1/15"], "correct_answer": 3},
        {"question": "11. Find the L.C.M of 18, 27 and 36", "options": ["3", "9", "108", "54"],
         "correct_answer": 2},
        {
            "question": "12. The prime numbers \nbetween 50 and 60 are ..... and ....",
            "options": ["51, 53", "51, 57", "53, 59", "53, 57"], "correct_answer": 2},
        {"question": "13. What is the place value \nof 1 in 1476.25?",
         "options": ["thousandths", "Hundredths", "Tens", "thousands"], "correct_answer": 3},
        {"question": "14. Find the product of 52 and 13",
         "options": ["676", "767", "776", "667"], "correct_answer": 0},
        {"question": "15. What is the 6th multiple of 7 ?",
         "options": ["24", "42", "55", "44"], "correct_answer": 1},
        {"question": "16. Simplify 2½- ¼", "options": ["2 1/3", "2 1/2", "2 1/4", "2 1/9"],
         "correct_answer": 2},
        {
            "question": "17. Write 5065 in words",
            "options": ["Five hundred and sixty five", "Fifty and sixty five five", "Five thousand and sixty five",
                        "Five hundred and sixty five"], "correct_answer": 2},
        {"question": "18. If a - 5 =3. What is y² ?", "options": ["64", "45", "8", "4"],
         "correct_answer": 0},
        {
            "question": "19. What is the 6th multiple of 10 ",
            "options": ["16", "600", "60", "61"], "correct_answer": 2},
        {
            "question": "20. How many prime numbers are\nthere in the set of numbers below?\n 12,13,14,15,16,17,18,19,20 ",
            "options": ["2", "3", "4", "5"], "correct_answer": 1},
        {
            "question": "21. What is the smallest number\n which when  divided by  15 and 24,\n leave a remainder of 1? ",
            "options": ["120", "121", "122", "124"], "correct_answer": 1},
        {
            "question": "22. Find the largest number which\n when divided by 9 and 27, \nleave s no remainder.",
            "options": ["3", "6", "9", "18"], "correct_answer": 2},
        {"question": "23. Write CMLXXXII In Arabic numerals",
         "options": ["1532", "1182", "982", "778"], "correct_answer": 2},
        {"question": "24. Covert 2023 to Roman numerals ",
         "options": ["MMXXIII", "CCXXIII", "MCXII", "MDCIII"], "correct_answer": 0},
        {"question": "25. Arrange 2/3,5/6,1/2,1/4\n in ascending order ",
         "options": ["1/4,5/6,2/3,1/2", "1/4,2/3,1/2,5/6", "1/2,2/3,1/4,5/6", "1/4,1/2,2/3,5/6"], "correct_answer": 3},
    ]

    def on_pre_enter(self):
        self.load_question()

    def load_question(self):
        question = self.questions[self.current_question]
        self.ids.question_label.text = question["question"]
        for i, option in enumerate(question["options"]):
            self.ids[f'option_{i + 1}'].text = option

    def __init__(self, **kwargs):
        super(QuizScreen2, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button
        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()
    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen2").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen2"

    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0
        self.load_question()
        self.clear_buttons()
        self.manager.current = "second"

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreen2(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz2')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"
class CorrectionScreen2(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreen2.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)

class EnterCode(Screen):
    def enter_button_pressed(self):
        app = MDApp.get_running_app()
        entered_code = self.ids.name_input.text.lower()  # Convert to lowercase for case-insensitive comparison

        # Check if the entered code is "dock"
        if entered_code == "dock":
            # Transition to SchoolExam screen
            app.root.transition.direction = 'left'
            app.root.current = 'school_name'
        else:
            # Handle incorrect code by showing a popup
            self.show_invalid_code_popup()

    def show_get_code_popup(self):
        content = MDFlatButton(text='Close', on_release=self.close_popup)
        self.dialog = MDDialog(
            title="             Get Code!",
            text="Call/Chat 08062942039 or go to www.surewayy.ng to get the code.",
            buttons=[content]
        )
        self.dialog.open()

    def close_popup(self, instance):
        self.dialog.dismiss()

    def show_invalid_code_popup(self):
        content = MDFlatButton(text='Close', on_release=self.close_popup)
        self.dialog = MDDialog(
            title="Invalid Code",
            text="The entered code is incorrect. Please try again.",
            buttons=[content]
        )
        self.dialog.open()

    def close_popup(self, *args):
        self.dialog.dismiss()

class SchoolExam(Screen):
    def on_enter(self):
        pass  # Your existing code...

    def switch_to_quiz_screen_n(self):
        self.manager.transition.direction = 'left'
        self.manager.current = 'quiz_screen_n'

class QuizScreenN(Screen):
    current_question = 0
    score = 0

    questions = [
        {
            "question": "1. Choose from the options lettered A to D\n the one that is nearest in meaning\n to the CAPITALIZED word.\n (1) Our AILING sister is at home.",
            "options": ["beautiful", "caring", "hostile", "sick"],
            "correct_answer": 3
        },
        {
            "question": "2. The match was POSTPONED\n because of the heavy rain.",
            "options": ["cancelled", "deferred", "prolonged", "suspended"],
            "correct_answer": 1
        },
        {
            "question": "3. The government is working hard to\n CONTROL malaria in our society.",
            "options": ["eradicate", "eliminate", "prevent", "transmit"],
            "correct_answer": 2
        },
        {
            "question": "4. Drinking DIRTY water \nwill make you sick.",
            "options": ["clean", "contaminated", "distilled", "filtered"],
            "correct_answer": 1
        },
        {
            "question": "5. The head teacher REBUKED Adamu\n for always coming late to school.",
            "options": ["advised", "criticized", "hated", "scolded"],
            "correct_answer": 3
        },
        {
            "question": "6. Choose from the options lettered\n A to D in question 6-10 the one that\n is most nearly opposite in meaning\n to the capitalized word.\n (6) I like meeting INTERESTING people.",
            "options": ["absoring", "boring", "fascinating", "happy"],
            "correct_answer": 1
        },
        {
            "question": "7. The boy was EXCITED when he saw \nhis mother.",
            "options": ["annoyed", "frightened", "happy", "joyous"],
            "correct_answer": 0
        },
        {
            "question": "8. The weather suddenly became HAZY.",
            "options": ["bright", "cold", "dry", "stormy"],
            "correct_answer": 0
        },
        {
            "question": "9. Youths nowadays are EAGER\n to be rich.",
            "options": ["keen", "longing", "quick", "reluctant"],
            "correct_answer": 3
        },
        {
            "question": "10. The stadium was EMPTY during\n the match.",
            "options": ["bare", "deserted", "free", "full"],
            "correct_answer": 3
        },
        {
            "question": "SECTION C STRUCTURE\n Complete each of the following\nStatement, with the most appropriate of the\n options lettered A- D\n11. The newly opened ice cream shop is _____\n my street.",
            "options": ["at", "by", "in", "on"],
            "correct_answer": 3
        },
        {
            "question": "12. The prefix ________ will combine with\n the word 'direct' to form a new word.",
            "options": ["dis-", "im-", "pre-", "re"],
            "correct_answer": 3
        },
        {
            "question": "13. My mother bought a cute shoe \nduring our ________.",
            "options": ["vacasion", "vacation", "vacattion", "varcattion"],
            "correct_answer": 1
        },
        {
            "question": "14. The golden wrist watch belongs \nto my father. It is ________.",
            "options": ["hers", "his", "mine", "ours"],
            "correct_answer": 1
        },
        {
            "question": "15. Victor was born with a silver spoon. \nThis means that he was ________.",
            "options": ["born into a poor family", "born into a wealthy family", "born into an influential family",
                        "fed with a silver Spoon"],
            "correct_answer": 1
        },
        {
            "question": "16. It has been raining for some \ndays now ________ it?",
            "options": ["hadn’t", "has", "hasn't", "isn't"],
            "correct_answer": 2
        },
        {
            "question": "17. Funmi was given the ________ \nportion, out of the people eating the meal.",
            "options": ["more smallest", "small", "smaller", "smallest"],
            "correct_answer": 3
        },
        {
            "question": "18. Which of the following words\n contains the /f/ sound?",
            "options": ["path", "phone", "sigh", "thing"],
            "correct_answer": 1
        },
        {
            "question": "19. My mother ________ to the \nhouse early yesterday.",
            "options": ["have returned", "is returning", "returned", "returns"],
            "correct_answer": 2
        },
        {
            "question": "20. There will be a conference\n of governors’ ________ at the \ngovernment house.",
            "options": ["wife", "wifes", "wive's", "wives"],
            "correct_answer": 3
        },
        {
            "question": "21. The children always ________ to \nschool although their father is rich.",
            "options": ["Are trekking", "have trekked", "trek", "trekked"],
            "correct_answer": 2
        },
        {
            "question": "22. Neither Joy nor her sisters\n ________ fruits.",
            "options": ["are liking", "is liking", "like", "liked"],
            "correct_answer": 2
        },
        {
            "question": "23. The ________ are waiting for her\n across the road.",
            "options": ["child", "children", "children’s", "childrens"],
            "correct_answer": 1
        },
        {
            "question": "24. The pupils must all keep quiet\n ________ they?",
            "options": ["aren't", "hadn't", "isn't", "mustn't"],
            "correct_answer": 3
        },
        {
            "question": "25. He was ________ from playing football.",
            "options": ["descouraged", "descoraged", "discoueraged", "discouraged"],
            "correct_answer": 3
        },
        {
            "question": "26. Which of the following suffixes can\n combine with the word 'employ' to form\n a new word?",
            "options": ["-al", "-ism", "-ly", "ment"],
            "correct_answer": 3
        },
        {
            "question": "27. Which of the following groups defines\n a nuclear family?",
            "options": ["father, mother and children", "father, mother and grand-children",
                        "father, mother and grand-father", "father, mother and nieces"],
            "correct_answer": 0
        },
        {
            "question": "28. The famous groundnut pyramids were\n built in ________ State.",
            "options": ["Adamawa", "Kaduna", "Kano", "Katsina"],
            "correct_answer": 2
        },
        {
            "question": "29. Monarch in Yoruba land is titled ________.",
            "options": ["Attah", "Eze", "Oba", "Obong"],
            "correct_answer": 2
        },
        {
            "question": "30. Yorubas inhabit the ________\n part of Nigeria.",
            "options": ["North Central", "North East", "South East", "South West"],
            "correct_answer": 3
        },
        {
            "question": "31. Nigeria is divided into ________ \ngeopolitical zones.",
            "options": ["2", "3", "4", "6"],
            "correct_answer": 3
        },
        {
            "question": "32. People related by birth and \nmarriage define ________.",
            "options": ["age grade", "family", "friendship", "kinship"],
            "correct_answer": 3
        },
        {
            "question": "33. Which of the following is an \nexample of material culture?",
            "options": ["art", "folklore", "language", "music"],
            "correct_answer": 0
        },
        {
            "question": "34. The leading cause of drug abuse\n in schools is ________.",
            "options": ["absenteeism", "expensive living", "high crime rate", "Peer pressure"],
            "correct_answer": 3
        },
        {
            "question": "35. Female genital mutilation is an example \nof ________.",
            "options": ["adverse traditional practice", "age-grade initiation", "ethnic cleansing",
                        "gender discrimination"],
            "correct_answer": 0
        },
        {
            "question": "36. Children who obey school rules and \nregulations exhibit ________.",
            "options": ["commitment", "devotion", "discipline", "selflessness"],
            "correct_answer": 2
        },
        {
            "question": "37. The ________ government is \nthe closest to the people.",
            "options": ["federal", "local", "national", "regional"],
            "correct_answer": 1
        },
        {
            "question": "38. June 12 is regarded as ________\n day in Nigeria.",
            "options": ["boxing", "children's", "democracy", "independence"],
            "correct_answer": 2
        },
        {
            "question": "39. Which of the following behaviors is \nnot acceptable in our schools?",
            "options": ["equity", "falsehood", "loyalty", "obedience"],
            "correct_answer": 1
        },
        {
            "question": "40. A natural occurrence that causes great \ndamage to life and property is ________.",
            "options": ["commotion", "disaster", "hardship", "poverty"],
            "correct_answer": 1
        },
        {
            "question": "41. Unfair treatment of an individual is\n usually motivated by ________.",
            "options": ["bias", "freedom", "friendship", "love"],
            "correct_answer": 0
        },
        {
            "question": "42. The penalty for murder in Nigeria\n is ________.",
            "options": ["banishment", "death", "exile", "imprisonment"],
            "correct_answer": 1
        },
        {
            "question": "43. FRSC stands for Federal Road\n Safety ________.",
            "options": ["Command", "Commission", "Committee", "Corps"],
            "correct_answer": 1
        },
        {
            "question": "44. An effectively secured home \nensures the following except ________.",
            "options": ["co-operation", "peace", "selfishness", "tolerance"],
            "correct_answer": 2
        },
        {
            "question": "45. Each of the following questions 45-50\n consists of five words lettered A to D. \nFour of them have at least something\n in common while one is odd. Pick the\n one that does not belong to the group.\n (a) barley (b) oat (c) rice (d) yam",
            "options": ["barley", "oat", "rice", "yam"],
            "correct_answer": 3
        },
        {
            "question": "46. .",
            "options": ["chair", "chalkboard", "desk", "swing"],
            "correct_answer": 3
        },
        {
            "question": "47. .",
            "options": ["bat", "crocodile", "dolphin", "shark"],
            "correct_answer": 1
        },
        {
            "question": "48. .",
            "options": ["ear", "eye", "liver", "skin"],
            "correct_answer": 2
        },
        {
            "question": "49. .",
            "options": ["Cabbage", "cucumber", "lettuce", "pawpaw"],
            "correct_answer": 3
        },
        {
            "question": "50. . ",
            "options": ["Clinic", "Dispensary", "Hospital", "supermarket"],
            "correct_answer": 3
        },
    ]

    def on_pre_enter(self):
        self.reset_quiz_state()
        self.load_question()

    def load_question(self):
        if 0 <= self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.ids.question_label.text = question["question"]
            for i, option in enumerate(question["options"]):
                self.ids[f'option_{i + 1}'].text = option
        else:
            # Handle the case where all questions are answered
            self.manager.current = 'result_screen_n'

    def __init__(self, **kwargs):
        super(QuizScreenN, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()

    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen_n").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen_n"

    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreenN(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz_screen_n')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"
class CorrectionN(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreenN.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)
class QuizScreenE(Screen):
    current_question = 0
    score = 0

    questions = [
    {
      "question": "PASSAGE A\nSpeech is great blessings but it can also be great curse,\n for while it helps us to make our intentions and desires\n known to our fellows, it can also if we use it carelessly,\nmake our attitude completely misunderstood. A slip of\nthe tongue, the use of unusual word, or of an\nambiguous word, and so on, may create an enemy where\nwe had hoped to win a friend.Again, different classes\n of people use different vocabularies, and the ordinary\n Speech of an educated may strike an uneducated \nlistener as pompous. Unwittingly, we may use a word \nwhich bears a different meaning to our listener from \nwhat It does to men of our own class. Thus, \nspeech is not a gift to use lightly without thought, buy\n one which demands careful handling, Only a fool will \nexpress himself alike to all kinds and conditions to men\n(1) The best way to win a friend is to avoid",
      "options": ["irony in speech", "pomposity in speech", "verbosity in speech", "ambiguity in speech"],
      "correct_answer": 3
    },
    {
      "question": "2. While talking to an uneducated person,\n we should use ……………..",
      "options": ["ordinary speech", "his vocabulary", "simple words", "polite language"],
      "correct_answer": 2
    },
    {
      "question": "3. If one used the same style of language\n with everyone, one would Sound ………………. ",
      "options": ["flat", "boring", "foolish", "democratic"],
      "correct_answer": 1
    },
    {
      "question": "4. A “slip of the tongue” means; something said ---------.",
      "options": ["wrongly by choice", "unintentionally", "without giving Proper thought", "to hurt another person"],
      "correct_answer": 0
    },
    {
      "question": "5. Speech can be a curse, because it",
      "options": ["hurt others", "lead to carelessness", "create misunderstanding", "reveal our intentions"],
      "correct_answer": 2
    },
    {
      "question": "Instruction: From the options lettered A to D.\n(6-10) choose the antonyms to the capitalized\n words in the sentences.\n6. At first, we found life in the town\n EXCITING but soon it became rather",
      "options": ["tiring", "disturbing", "burdensome", "boring"],
      "correct_answer": 3
    },
    {
      "question": "7. It is necessary to develop THRIFT \nhabits to be able to lead a comfortable life.",
      "options": ["expensive", "extravagant", "economical", "good"],
      "correct_answer": 1
    },
    {
      "question": "8. He hates these CONTINUAL arguments with friends",
      "options": ["repeat", "irrational", "occasional", "regular"],
      "correct_answer": 2
    },
    {
      "question": "9. He was CONSPICUOUS because of his colourful shirt",
      "options": ["charming", "ugly", "small", "unnoticeable"],
      "correct_answer": 3
    },
    {
      "question": "10. CUMULATIVELY, the effect of these drugs is quite bad.",
      "options": ["individually", "obviously", "clearly", "collectively"],
      "correct_answer": 0
    },
    {
      "question": "Instruction:  From the options lettered A to D,\n(11-15)choose the synonyms to the \n CAPITALIZED words in the sentence.\n11. The hunter retired to his ABODE at the end of the day.",
      "options": ["camp", "cubicle", "family", "home"],
      "correct_answer": 3
    },
    {
      "question": "12. The man was SLUGGISH.",
      "options": ["fast", "hasty", "quick", "slow"],
      "correct_answer": 3
    },
    {
      "question": "13. The girl asked for a SLICE of bread.",
      "options": ["loaf", "peace", "piece", "quantity"],
      "correct_answer": 2
    },
    {
      "question": "14. This class Is UNCLEAN, We cannot have our lesson here.",
      "options": ["clean", "dark", "dirty", "noisy"],
      "correct_answer": 2
    },
    {
      "question": "15. I BORROWED this ruler from her.",
      "options": ["lent", "loaned", "received", "snatched"],
      "correct_answer": 1
    },
    {
      "question": "Instruction: Choose the correctly spelt word for each\n list of words lettered A to D(16-20).\n16. Choose the correctly spelt word for\n each list of words lettered A to D.",
      "options": ["benefeted", "benefitted", "benifitted", "benifited"],
      "correct_answer": 1
    },
    {
      "question": "17. Choose the correctly spelt word for\n each list of words lettered A to D.",
      "options": ["fahrenheit", "farenhiet", "farenheit", "fahrenhiet"],
      "correct_answer": 0
    },
    {
      "question": "18. Choose the correctly spelt word\n for each list of words lettered A to D.",
      "options": ["skilful", "skilful", "skillfull", "skillful"],
      "correct_answer": 3
    },
    {
      "question": "19. Choose the correctly spelt word for \neach list of words lettered A to D.",
      "options": ["comandar", "commandor", "commander", "comander"],
      "correct_answer": 2
    },
    {
      "question": "20. Choose the correctly spelt word for\n each list of words lettered A to D.",
      "options": ["parallelogram", "parallellogram", "paralellogram", "parallelogramm"],
      "correct_answer": 0
    },
    {
      "question": " Instruction: Choose the options which best \ncompletes the following sentence(21-25).\n21. The university set up a ……………\ncommittee to oversee the examinations.",
      "options": ["forty-men", "forty-man", "forty-man's", "_ forty-men's"],
      "correct_answer": 1
    },
    {
      "question": "22. A terrible disaster was …….\nwhen the villagers sleeping in their huts \nwoke up in time to discover the fire.",
      "options": ["evicted", "evaded", "averted", "diverted"],
      "correct_answer": 2
    },
    {
      "question": "23. The man who was accused of theft was ……………….\n and released from prison.",
      "options": ["judged", "acquitted", "convicted", "sentenced"],
      "correct_answer": 1
    },
    {
      "question": "24. This event is held annually to…………………..\n the founder of the school.",
      "options": ["commentate", "commiserate", "commemorate", "commensurate"],
      "correct_answer": 2
    },
    {
      "question": "25. Everybody makes mistakes and nobody is ………….",
      "options": ["infallible", "immortal", "invincibie", "insuperable"],
      "correct_answer": 0
    },
    {
      "question": "Instruction: in each of the following words,\npick out the word that does\nnot belong to the group(26-30).\n26. In each of the following words, pick \nout the word that does not belong to the group.",
      "options": ["dollar", "naira", "ounce", "euro"],
      "correct_answer": 2
    },
    {
      "question": "27. In each of the following words, pick out \nthe word that does not belong to the group.",
      "options": ["square", "triangle", "rectangle", "cuboid"],
      "correct_answer": 3
    },
    {
      "question": "28. In each of the following words, pick out the\n word that does not belong to the group.",
      "options": ["fish", "snake", "crocodile", "whale"],
      "correct_answer": 1
    },
    {
      "question": "29. In each of the following words, pick \nout the word that does not belong to the group.",
      "options": ["spoon", "sword", "knife", "fork"],
      "correct_answer": 1
    },
    {
      "question": "Instruction: In each of the following questions,\n there are three sentences.\n Read them carefully and decide\n which one should come first,\nwhich second and which third(30-35).\n30. In each of the following words, pick out \nthe word that does not belong to the group.",
      "options": ["cat", "dog", "fox", "rabbit"],
      "correct_answer": 2
    },
    {
      "question": "31. Arrange the following sentences in the correct order:",
      "options": [ "3,2,1", "2,3,1", "3,1,2", "2,1,3"], "correct_answer": 2
    },
    {
      "question": "32. Arrange the following sentences in the\n correct order:",
      "options": [ "1,2,3", "2,1,3", "3,1,2", "2,3,1" ], "correct_answer": 1
    },
    {
      "question": "33. Arrange the following sentences in the \ncorrect order:",
      "options": ["1,2,3", "2,1,3", "3,2,1", "3,1,2"], "correct_answer": 0
    },
    {
      "question": "34. Arrange the following sentences in the \ncorrect order:",
      "options": [ "2,1,3", "1,2,3", "3,2,1", "3,1,2" ], "correct_answer": 2
    },
    {
      "question": "35. Arrange the following sentences in the\n correct order:",
      "options": ["1,2,3", "1,3,2", "2,1,3", "3,2,1"], "correct_answer": 1
    },
    {
      "question": "Choose the correct part of speech to the capitalized \n words in each of the following sentences.\n(36) She was wearing BEAUTIFUL ear-rings",
      "options": [ "Adjective", "Adverb", "Noun", "Pronoun"],"correct_answer": 0
    },
    {
      "question": "37. WOW, you have got a great score.",
      "options": ["Conjunction", "Interjection", "Pronoun", "Noun"], "correct_answer": 1
    },
    {
      "question": "38. The baby crawled UNDER the bed",
      "options": ["Preposition", "Conjunction", "Adverb", "Interjection"], "correct_answer": 0
    },
    {
      "question": "39.  She QUICKLY packed her bag and left.",
      "options": [ "Noun", "Adjective", "Adverb", "Verb" ], "correct_answer": 2
    },
    {
      "question": "40. This is a DEPRESSING time to be living \nin London as people are arguing over the election.",
      "options": [ "Interjection", "Adjective", "Adverb", "Preposition"],"correct_answer": 1
    },
    {
      "question": "41. TAKE your first left then go over the bridge",
      "options": [
        "Noun", "Preposition", "Verb","Adverb"], "correct_answer": 2
    },
    {
      "question": "42. There is a party next week THOUGH I don't think\n i can go.",
      "options": ["Preposition", "Conjunction", "Adverb", "Interjection" ], "correct_answer": 1
    },
    {
      "question": "43. He thinks WE will arrive at roughly 5pm.",
      "options": [ "Pronoun", "Preposition", "Conjunction", "Noun" ], "correct_answer": 0
    },
    {
      "question": "44. The music is VERY loud.",
      "options": ["Adjective", "Interjection", "Noun", "Adverb"
      ], "correct_answer": 0
    },
    {
      "question": "45.  He goes to Spain often NOT ONLY for the sun\n but also for the food.",
      "options": [ "Conjunction", "Adverb", "Preposition", "Verb"], "correct_answer": 0
    },
    {
      "question": "46. What is the synonym of 'huge'?",
      "options": [ "tiny", "large", "little", "small" ], "correct_answer": 1
    },
    {
      "question": "47. What is the antonym of 'brave'?",
      "options": [ "fearless",  "courageous", "cowardly", "bold" ], "correct_answer": 2
    },
    {
      "question": "48. Which word means 'to make something right'?",
      "options": [ "destroy", "fix", "ruin", "break"], "correct_answer": 1
    },
    {
      "question": "49. What is the synonym of 'happy'?",
      "options": [ "sad", "joyful", "angry", "miserable"], "correct_answer": 1
    },
    {
      "question": "50. What is the antonym of 'dark'?",
      "options": ["dim", "gloomy", "bright", "shadowy"], "correct_answer": 2
    }
  ]

    def on_pre_enter(self):
        self.reset_quiz_state()
        self.load_question()

    def load_question(self):
        if 0 <= self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.ids.question_label.text = question["question"]
            for i, option in enumerate(question["options"]):
                self.ids[f'option_{i + 1}'].text = option
        else:
            # Handle the case where all questions are answered
            self.manager.current = 'result_screen_e'

    def __init__(self, **kwargs):
        super(QuizScreenE, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()

    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen_e").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen_e"

    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreenE(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz_screen_e')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"
class CorrectionE(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreenE.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)

class QuizScreenV(Screen):
    current_question = 0
    score = 0

    questions = [
    {
     "question": "SECTION A:\nRead the passage below and answer the questions that \nfollow.The following day was a market day at Anikoro\n village. As soon as the market was full the dreadful\nleopard jumped from a nearby bush into the market.At\n once hell broke loose. There was a general stampede.\n Market women and men screamed and ran away in\n panic leaving their own children behind. Even animals\n (dogs and goats) joined in the mad race. People collided\n with one another Goods like pepper, salt, fish, garri,\n meat and groundnuts were trampled upon and scattered.\nTanigoro was nearby when the leopard jumped into the\n market. At once he jumped onto the top of the leopard\n and grabbed it by the neck with his bare hands.\n The leopard kicked about wildly but Tanigoro tightened his\n grip more and more. It was a tough battle which ended\n in a victory for Tanigoro. 1. According to the passage\n the leopard appeared when the market was ______",
     "options": ["Half fitted", " Empty", "fully filled", "Was deserted"],
     "correct_answer": 2
    },
    {
      "question": "In each of the following choose\nfrom the options the one which is\nnearest in meaning to the capitalized words\n1. There was a football competition\namong the schools in the area",
      "options": ["game", "play", "match", "contest"],
      "correct_answer": 2
    },
    {
      "question": "2. The pupils received gifts from Father Christmas",
      "options": ["parcels", "jewels", "presents", "rations"],
      "correct_answer": 2
    },
    {
      "question": "3. The width of the hall is ten metres",
      "options": ["breadth", "length", "size", "track"],
      "correct_answer": 0
    },
    {
      "question": "4. The supporters of the party applauded\n the speaker",
      "options": ["cheered", "boycotted", "carried", "shouted at"],
      "correct_answer": 3
    },
    {
      "question": "5. My mother advised me to be industrious \nif I want to pass my examination",
      "options": ["clever", "courageous", "hardworking", "brilliant"],
      "correct_answer": 2
    },
    {
      "question": " In each of the following choose from \nthe options the one which is nearly\n opposite in meaning to the capitalized words.\n6. Most Nigerians buy more local \nproducts than ____ ones",
      "options": ["atari", "indigenous", "universal", "foreign"],
      "correct_answer": 3
    },
    {
      "question": "7. The coach of the national team invited \nonly professional players for the match",
      "options": ["star", "excellent", "prolific", "amateur"],
      "correct_answer": 3
    },
    {
      "question": "8. Some politicians preach virtues \nbut practice _______",
      "options": ["vices", "sense", "vanity", "success"],
      "correct_answer": 0
    },
    {
      "question": "9. The river is very deep in the middle",
      "options": ["shallow", "broad", "wide", "hollow"],
      "correct_answer": 0
    },
    {
      "question": "10. My father rarely travels on Sundays",
      "options": ["surely", "nearly", "never", "often"],
      "correct_answer": 3
    },
    {
      "question": " Fill in the gap with appropriate \nanswers chosen from the options\n11. We saw the police ______ after\n the thief",
      "options": ["to run", "ran", "was running", "running"],
      "correct_answer": 3
    },
    {
      "question": "12. Teachers always have ______ to do",
      "options": ["works", "much work", "many works", "plenty works"],
      "correct_answer": 1
    },
    {
      "question": "13. Mr. Baffour has lived in Terna ______ 1990",
      "options": ["for", "since", "almost", "nearly"],
      "correct_answer": 1
    },
    {
      "question": "14. My father will travel to London _______",
      "options": ["next tomorrow", "yesterday", "tomorrow's next day", "by nail tomorrow"],
      "correct_answer": 0
    },
    {
      "question": "15. When l saw my friend I asked\n for______ to drink",
      "options": ["some water", "a water", "waters", "a small water"],
      "correct_answer": 0
    },
    {
      "question": "16. Since there was no vehicle we travelled\nto the village _______",
      "options": ["on foot", "by foot", "by feet", "on feet"],
      "correct_answer": 0
    },
    {
      "question": "17. It is obvious that the man cannot\n do _______ about your problem",
      "options": ["something", "nothing", "anything", "many"],
      "correct_answer": 2
    },
    {
      "question": "18. Musa didn't remember to bring his biro \nto school. This means that______",
      "options": ["Musa didn't come to school", "someone stole Musa's biro", "Musa didn't buy a biro", "Musa left his biro at home"],
      "correct_answer": 3
    },
    {
      "question": "19. If my father had travelled today, \nI would have attended Goke's birthday party.\n This means that ______",
      "options": ["I did not attend Goke's birthday party", "I attended Goke's birthday party", "my father travelled", "my father asked me to travel with him"],
      "correct_answer": 1
    },
    {
      "question": "Choose the word which has almost the same\n meaning to the underlined words \nfrom the options given below\n20. The fact could no longer be concealed.",
      "options": ["contained", "hidden", "revealed", "doubted"],
      "correct_answer": 1
    },
    {
      "question": "21. Mrs. Oladipo is such a severe woman that\n we all fear her.",
      "options": ["strict", "indulgent", "tolerant", "lenient"],
      "correct_answer": 0
    },
    {
      "question": "22. Abdulsalam likes paying his father a \nnocturnal visit.",
      "options": ["quiet", "lonely", "night", "natural"],
      "correct_answer": 2
    },
    {
      "question": "VERBAL APTITUDE INSTRUCTION:\n there are three sentences in each of\n the questions below. Read the sentences\n carefully and choose which one should come first,\n second and third.\n23.(1)Her mother bought her a new Dress.\n(2) Dunni’s birthday is next week.\n(3) Bisi loves her new dress.",
      "options": ["1, 2, 3", "3, 2, 1", "2, 3, 1", "2, 1, 3 "],
      "correct_answer": 3
    },
    {
      "question": "24. (1)We have just been promoted to a new class.\n(2) He is a very kind person.\n(3) Our new class teacher is Mr. Adebowale.",
      "options": ["1, 3, 2 ", "3, 2, 1 ", "1, 2, 3 ", "2, 1, 3 "],
      "correct_answer": 0
    },
    {
      "question": "25. (1)She is a very smart girl.\n(2)Folake is just five years old.\n(3) She is already in Primary Two. ",
      "options": [ "3, 2, 1","1, 2, 3 ","2, 3, 1 ", "3, 1, 2"],
      "correct_answer": 2
    },
    {
      "question": "GENERAL PAPER 26.\n What are the three arm of government in Nigeria?",
      "options": ["president, senator and honourable", "judiciary, presidency and executive", "legislature, judiciary and executive", "legislature, presidency and politician"],
      "correct_answer": 2
    },
    {
      "question": "27. A piece of land surrounded by water is",
      "options": ["ocean", "riverside", "island", "waterfall"],
      "correct_answer": 2
    },
    {
      "question": "28. COVID-19 originated from............",
      "options": ["new york", "new delhi", "tokyo", "wuhan, china"],
      "correct_answer": 3
    },
    {
      "question": "29. River Niger and River Benue meet in",
      "options": ["lagos", "kano", "ewekoro", "lokoja"],
      "correct_answer": 3
    },
    {
      "question": "30. The major source of government revenue in \nNigeria is............",
      "options": ["cocoa", "petroleum", "cocoa", "rubber"],
      "correct_answer": 1
    },
    {
      "question": "31. Which part of speech is the word 'quickly'?",
      "options": ["Adjective", "Adverb", "Noun", "Verb"],
      "correct_answer": 1
    },
    {
      "question": "32. What is the plural form of 'child'?",
      "options": ["childs", "children", "childes", "childen"],
      "correct_answer": 1
    },
    {
      "question": "33. If 'cat' is to 'feline', then 'dog' is to ________.",
      "options": ["bark", "puppy", "canine", "fido"],
      "correct_answer": 2
    },
    {
      "question": "34. What is the past tense of 'eat'?",
      "options": ["eated", "ate", "eated", "eating"],
      "correct_answer": 1
    },
    {
      "question": "35. 'She ____ to school every day.'",
      "options": ["goes", "go", "going", "gone"],
      "correct_answer": 0
    },
    {
      "question": "36. What is the opposite of 'happy'?",
      "options": ["joyful", "cheerful", "sad", "excited"],
      "correct_answer": 2
    },
    {
      "question": "37. What is the synonym of 'big'?",
      "options": ["large", "tiny", "huge", "small"],
      "correct_answer": 0
    },
    {
      "question": "38. Which word means 'to make something dirty'?",
      "options": ["clean", "scrub", "purify", "soil"],
      "correct_answer": 3
    },
    {
      "question": "39. If 'cat' is to 'kitten', then 'dog' is to ________.",
      "options": ["puppy", "kitten", "canine", "pup"],
      "correct_answer": 0
    },
    {
      "question": "40. What is the plural form of 'mouse'?",
      "options": ["mouses", "mice", "mousees", "micees"],
      "correct_answer": 1
    },
    {
      "question": "41. What is the comparative form of 'good'?",
      "options": ["better", "best", "gooder", "well"],
      "correct_answer": 0
    },
    {
      "question": "42. What is the past tense of 'drink'?",
      "options": ["drank", "drunk", "drunked", "drunken"],
      "correct_answer": 0
    },
    {
      "question": "43. 'He ____ a book yesterday.'",
      "options": ["read", "reading", "reads", "readed"],
      "correct_answer": 0
    },
    {
      "question": "44. What is the opposite of 'fast'?",
      "options": ["slow", "quick", "rapid", "speedy"],
      "correct_answer": 0
    },
    {
      "question": "45. 'The _______ car was parked in front.'",
      "options": ["red", "redder", "reddest", "more red"],
      "correct_answer": 0
    },
    {
      "question": "46. What is the synonym of 'angry'?",
      "options": ["mad", "happy", "upset", "joyful"],
      "correct_answer": 0
    },
    {
      "question": "47. Which word means 'to make something clean'?",
      "options": ["dirty", "cleanse", "sully", "pollute"],
      "correct_answer": 1
    },
    {
      "question": "48. What is the plural form of 'leaf'?",
      "options": ["leafs", "leaves", "leafes", "leafen"],
      "correct_answer": 1
    },
    {
      "question": "49. What is the comparative form of 'far'?",
      "options": ["farrer", "farest", "farther", "further"],
      "correct_answer": 2
    },
    {
      "question": "50. What is the past tense of 'take'?",
      "options": ["took", "taken", "take", "tooken"],
      "correct_answer": 0
    }
  ]

    def on_pre_enter(self):
        self.reset_quiz_state()
        self.load_question()

    def load_question(self):
        if 0 <= self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.ids.question_label.text = question["question"]
            for i, option in enumerate(question["options"]):
                self.ids[f'option_{i + 1}'].text = option
        else:
            # Handle the case where all questions are answered
            self.manager.current = 'result_screen_v'

    def __init__(self, **kwargs):
        super(QuizScreenV, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()

    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen_v").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen_v"

    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreenV(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz_screen_v')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"
class CorrectionV(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreenV.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)
class QuizScreenQ(Screen):
    current_question = 0
    score = 0

    questions = [
    {
      "question": "From the words or group of words lettered A to D,\nchoose the one which is nearest In \nmeaning to the word underlined in\n each of the following sentences.\n1. Your daddy needs a lucrative \njob to pay your school \nfees and care for your mummy.",
      "options": ["major", "minor", "profitable", "superior"],
      "correct_answer": 2
    },
    {
      "question": "2. The materials you brought for the programme\n were obsolete.",
      "options": ["beautiful", "ugly", "archaic", "extraordinary"],
      "correct_answer": 2
    },
    {
      "question": "3. My attempt to change the line of \ndiscussion was abortive.",
      "options": ["unsuccessful", "entertaining", "exceptional", "amusing"],
      "correct_answer": 0
    },
    {
      "question": "4. My friend and I were compelled to \nsleep in the petrol station.",
      "options": ["allowed", "forced", "encouraged", "ushered"],
      "correct_answer": 1
    },
    {
      "question": "5. You are too careless with the school uniforms.",
      "options": ["unconcerned", "uncelebrated", "prefatory", "exempted"],
      "correct_answer": 0
    },
    {
      "question": "From the words or group of words \nlettered A to D, choose the\n one which is opposite \nin meaning to the words underlined\n in each of the following sentences.\n6. The clothing material used by \nmy tailor is superior to yours.",
      "options": ["superb", "interior", "senior", "inferior"],
      "correct_answer": 3
    },
    {
      "question": "7. Mr. Kumangari is a famous person \nin our community.",
      "options": ["popular", "noise maker", "talkative", "unpopular"],
      "correct_answer": 3
    },
    {
      "question": "8. My grandmother is an experienced \nlawyer in Nigeria.",
      "options": ["clever", "humorous", "amateur", "good"],
      "correct_answer": 2
    },
    {
      "question": "9. The Secretary is arrogant and unprofessional \nin the discharge of his duty.",
      "options": ["authoritative", "humble", "playful", "tough"],
      "correct_answer": 1
    },
    {
      "question": "10. My best friend is the fastest \nstudent in our school.",
      "options": ["slowest", "commonest", "laziest", "slimmest"],
      "correct_answer": 0
    },
    {
      "question": "From the options lettered A to D,\nchoose the best interpretation\n for Questions 11 to 13.\n11. Chukwuemeka set his face against\n the decision of the committee.\nThis means that Chukwuemeka\n ______ the decision.",
      "options": ["did not respect", "welcomed", "appraised", "opposed"],
      "correct_answer": 3
    },
    {
      "question": "12. Alhaji Usman got to the airport at the\n nick of time. This means that\n Alhaji Usman got to the airport ______.",
      "options": ["very late", "too early", "just a little late", "at the exact time"],
      "correct_answer": 3
    },
    {
      "question": "13. Anduna is the black sheep of the family.\n This means that Anduna is ______.",
      "options": ["dark complexioned", "having a black sheep", "a disgrace", "the dark member of the family"],
      "correct_answer": 2
    },
    {
      "question": "14. The fact could no longer be concealed.",
      "options": ["contained", "hidden", "revealed", "doubted"],
      "correct_answer": 1
    },
    {
      "question": "15. Mrs. Oladipo is such a severe woman \nthat we all fear her.",
      "options": ["strict", "indulgent", "tolerant", "lenient"],
      "correct_answer": 0
    },
    {
      "question": "16. Abdulsalam likes paying his father \na nocturnal visit.",
      "options": ["quiet", "lonely", "night", "natural"],
      "correct_answer": 2
    },
    {
      "question": "17. Her mother bought her a new dress.",
      "options": ["some water", "a water", "waters", "a small water"],
      "correct_answer": 0
    },
    {
      "question": "18. Since there was no vehicle we \ntravelled to the village ______.",
      "options": ["on foot", "by foot", "by feet", "on feet"],
      "correct_answer": 0
    },
    {
      "question": "19. It is obvious that the man \ncannot do ______ about your problem.",
      "options": ["something", "nothing", "anything", "many"],
      "correct_answer": 2
    },
    {
      "question": "20. Musa didn't remember to bring his\n biro to school. This means that ______.",
      "options": ["Musa didn't come to school", "Someone stole Musa's biro", "Musa didn't buy a biro", "D. Musa left his biro at home"],
      "correct_answer": 3
    },
    {
      "question": "21. If my father had travelled today, \nI would have attended Goke's birthday party.\n This means that ______.",
      "options": ["I did not attend Goke's birthday party", "I attended Goke's birthday party", "My father travelled", "My father asked me to travel with him"],
      "correct_answer": 1
    },
    {
      "question": "In each of the Questions,\n choose the word that cannot\nbe formed by an arrangement of\n some or all the letters of the word\n printed in capital letters.\nNo letter may be used more times\n than the number of times It \nappeared in the capitalized word.\n 22.CELEBRATION",
      "options": ["mate", "later", "lemon", "trim"],
      "correct_answer": 3
    },
    {
      "question": "23. CELEBRATION.",
      "options": ["tile", "smile", "brat", "clear"],
      "correct_answer": 0
    },
    {
      "question": "24. HALLUCINATION.",
      "options": ["hall", "lunatic", "nation", "lucid"],
      "correct_answer": 3
    },
    {
      "question": "Choose from the list of words \nor group of words lettered A to D,\n the one which correctly and most\n suitably fills the gap in the sentence.\n25. The robbers gained access into\n the house ______ the window.",
      "options": ["about", "for", "by", "through"],
      "correct_answer": 2
    },
    {
      "question": "26. My father's farmland is located ______ \nthe king's palace and the market square.",
      "options": ["inside", "among", "between", "across"],
      "correct_answer": 2
    },
    {
      "question": "27. Mrs. Alubusa is responsible for the ______ \nof the conference room.",
      "options": ["to clean", "cleaning", "cleaned", "have cleaned"],
      "correct_answer": 1
    },
    {
      "question": "28. John and his friend fell ______\n because of an argument over a piece of land.",
      "options": ["in", "out", "over", "through"],
      "correct_answer": 1
    },
    {
      "question": "29.Choose from the list of words lettered A to D,\n the one which is correctly spelt. ",
      "options": ["operational", "oprassional", "operassional", "philorsophy"],
      "correct_answer": 0
    },
    {
      "question": "30. ",
      "options": ["philorsophy", "filosophy", "phylosophy", "philosophy"],
      "correct_answer": 3
    },
    {
      "question": "31. ",
      "options": ["celibration", "selebration", "celebration", "celeberation"],
      "correct_answer": 2
    },
    {
      "question": "GENERAL KNOWLEDGE \n32. The officer that controls the\n sailing of a Ship is called ______.",
      "options": ["lieutenant commander of the ship", "sailor of the ship", "pilot of the ship", "captain of the ship"],
      "correct_answer": 3
    },
    {
      "question": "33. Which of the following countries is\n currently being invaded by Russia?",
      "options": ["United States of America", "Canada", "United Kingdom", "Ukraine"],
      "correct_answer": 3
    },
    {
      "question": "34. The highest court in Nigeria is the ______\n court?",
      "options": ["supreme", "high", "magistrate", "customary"],
      "correct_answer": 0
    },
    {
      "question": "35. Which of the following cannot be regarded\n as a national symbol?",
      "options": ["Naira", "coat of arms", "amusement park", "national flag"],
      "correct_answer": 2
    },
    {
      "question": "36. A land area that is surrounded by water \nis called a/an ______?",
      "options": ["water body", "island", "ocean", "Mediterranean"],
      "correct_answer": 1
    },
    {
      "question": "37. Which of the following is a cash \ncrop in Nigeria?",
      "options": ["apple", "blueberry", "pumpkin", "cocoa"],
      "correct_answer": 3
    },
    {
      "question": "38. The counting of people in a particular area \nat a particular time in order to adequately\n plan for them and their environment is known\n as ______.",
      "options": ["census", "election", "democracy", "oligarchy"],
      "correct_answer": 0
    },
    {
      "question": "39. The journey to holy lands for religious \npurpose is called ______.",
      "options": ["religious holiday", "holy journey", "pilgrimage", "excursion"],
      "correct_answer": 2
    },
    {
      "question": "40. The eagle on Nigeria's Coat of Arms\n represents the nation’s ______.",
      "options": ["unity", "dignity", "wealth", "strength"],
      "correct_answer": 3
    },
    {
      "question": "41. The culture of a people refers to ______.",
      "options": ["their development level", "their way of life", "their level of education", "their ability to produce farm products"],
      "correct_answer": 1
    },
    {
      "question": "42. From the options lettered A to D, choose the word that cannot be formed by an arrangement of some or all the letters of the word printed in capital letters. INTELLIGENCE",
      "options": ["GENETIC", "CLEANING", "CITIZEN", "GENTLE"],
      "correct_answer": 1
    },
    {
      "question": "43. From the words or group of words lettered A to D, choose the one which correctly and most suitably fills the gap in the sentence. We decided to visit the park ______ the morning.",
      "options": ["in", "on", "at", "by"],
      "correct_answer": 0
    },
    {
      "question": "44. Choose from the list of words lettered A to D, the one which is correctly spelt. RESIDENCE",
      "options": ["RESEDENCE", "RECIDENCE", "REZIDENCE", "RESIDANT"],
      "correct_answer": 3
    },
    {
      "question": "45. GENERAL KNOWLEDGE: What is the currency of Japan?",
      "options": ["Yuan", "Euro", "Yen", "Dollar"],
      "correct_answer": 2
    },
    {
      "question": "46. What is the study of weather called?",
      "options": ["Zoology", "Botany", "Meteorology", "Geology"],
      "correct_answer": 2
    },
    {
      "question": "47. In which part of the body would you find the femur?",
      "options": ["Arm", "Leg", "Head", "Chest"],
      "correct_answer": 1
    },
    {
      "question": "48. What is the capital city of Australia?",
      "options": ["Melbourne", "Sydney", "Perth", "Canberra"],
      "correct_answer": 3
    },
    {
      "question": "49. Which planet is known as the Red Planet?",
      "options": ["Venus", "Mars", "Jupiter", "Mercury"],
      "correct_answer": 1
    },
    {
      "question": "50. What is the tallest mammal in the world?",
      "options": ["Elephant", "Giraffe", "Horse", "Kangaroo"],
      "correct_answer": 1
    }
  ]

    def on_pre_enter(self):
        self.reset_quiz_state()
        self.load_question()

    def load_question(self):
        if 0 <= self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.ids.question_label.text = question["question"]
            for i, option in enumerate(question["options"]):
                self.ids[f'option_{i + 1}'].text = option
        else:
            # Handle the case where all questions are answered
            self.manager.current = 'result_screen_q'

    def __init__(self, **kwargs):
        super(QuizScreenQ, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()

    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen_q").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen_q"

    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreenQ(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz_screen_q')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"

class CorrectionQ(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreenQ.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)
class QuizScreenG0(Screen):
    current_question = 0
    score = 0

    questions = [
    {
        "question": "1. What is MCMXCII in Hindu Arabic\n numerals system?",
        "options": ["1192", "1902", "1009", "1992"],
        "correct_answer": 3
    },
    {
        "question": "2. Which of these numbers: \n1, 3, 6, 11 and 12 are prime numbers?",
        "options": ["1 and 3", "1 and 11", "3 and 11", "1, 3, and 11"],
        "correct_answer": 2
    },
    {
        "question": "3. Change 120 seconds to minute(s)",
        "options": ["1", "2", "6", "12"],
        "correct_answer": 1
    },
    {
        "question": "4. If a cup costs 2 pounds and the \nrate of exchange is a pound to six\n hundred and forty naira,\n find its cost in Naira.",
        "options": ["320.00", "638.00", "642.00", "1,280"],
        "correct_answer": 3
    },
    {
        "question": "5. Find the even number between 19 and\n 41 that is multiple of 7.",
        "options": ["26", "28", "34", "36"],
        "correct_answer": 1
    },
    {
        "question": "6. Find the square root of 2 ¼",
        "options": ["1/4", "1/8", "1/2", "1 ½"],
        "correct_answer": 3
    },
    {
        "question": "7. Calculate the simple interest on N800.00\n for 4 years at the rate of \n6% per annum",
        "options": ["N186.00", "N192.00", "N196.00", "N220.00"],
        "correct_answer": 1
    },
    {
        "question": "8. If two-third of a number is 60, what is\n one-sixth of that same number?",
        "options": ["75", "60", "45", "15"],
        "correct_answer": 3
    },
    {
        "question": "9. The H.C.F of two numbers is 3. Which of \nthe following pairs represents \nthe two numbers in the options below?",
        "options": ["12 and 17", "10 and 20", "9 and 15", "8 and 12"],
        "correct_answer": 2
    },
    {
        "question": "10. 25% of N500.00 is less than one of the\n following by N80.00",
        "options": ["N195.00", "N205.00", "N225.00", "N230.00"],
        "correct_answer": 1
    },
    {
        "question": "11. Change N32.08 to kobo.",
        "options": ["320", "328", "330", "3,208"],
        "correct_answer": 3
    },
    {
        "question": "12. How many N10.00 added up to \nmake N1,000.00?",
        "options": ["10", "50", "100", "110"],
        "correct_answer": 2
    },
    {
        "question": "13. Change 7 1/2% to fraction in its\n lowest term.",
        "options": ["1/2", "3/20", "1/20", "3/40"],
        "correct_answer": 3
    },
    {
        "question": "14. Convert 8 weeks 8 days to days.",
        "options": ["64", "56", "48", "39"],
        "correct_answer": 0
    },
    {
        "question": "15. The marked price of an article is \nN8,200.00. If a customer receives N410.00\n as a discount on the article.\n What percentage\n is the discount?",
        "options": ["4", "5", "6", "8"],
        "correct_answer": 1
    },
    {
        "question": "16. Subtract 8cm 7mm from 42cm 5mm.",
        "options": ["34cm8mm", "34cm13mm", "33cm98mm", "33cm8mm"],
        "correct_answer": 3
    },
    {
        "question": "17. A man drives his car at an average \nspeed of 76km/h. Calculate the distance \ncovered in 3 hours.",
        "options": ["22km", "76km", "228km", "266km"],
        "correct_answer": 3
    },
    {
        "question": "18. Three boys shared certain numbers \nof mangoes in the ratio 5:3:2. If the one\n with the smallest ratio received \n40 mangoes, find the number of mangoes\n shared.",
        "options": ["80", "100", "120", "200"],
        "correct_answer": 3
    },
    {
        "question": "19. Bola bought six books at N45.00 each\n and sold them for N230.00. \nHow much does she lose?",
        "options": ["N50.00", "N45.00", "N40.00", "N30.00"],
        "correct_answer": 2
    },
    {
        "question": "20. If -2x = 6, find the value of x.",
        "options": ["12", "-3", "3", "6"],
        "correct_answer": 1
    },
    {
        "question": "21. Solve for x if 3 = 15x-2.",
        "options": ["1/5", "1/3", "2/5", "1/2"],
        "correct_answer": 1
    },
    {
        "question": "22. Given that the area of a rectangle \nis 42cm² and its breadth is 6 cm. \nFind its length.",
        "options": ["3cm", "5cm", "7cm", "9cm"],
        "correct_answer": 2
    },
    {
        "question": "23. Solve the equation: 2x = 30 - 3x.",
        "options": ["5", "6", "9", "11"],
        "correct_answer": 1
    },
    {
        "question": "24. Find the circumference of a circle \nwhose radius is cm. (Take π=22/7)",
        "options": ["21cm", "32cm", "33cm", "66cm"],
        "correct_answer": 2
    },
    {
        "question": "25. If [y] – 8 = 12, what is the value of y?",
        "options": ["4", "6", "8", "20"],
        "correct_answer": 3
    },
    {
        "question": "26. How many faces does a cube have?",
        "options": ["2", "4", "5", "6"],
        "correct_answer": 3
    },
    {
        "question": "27. Find the area of a rectangle whose \nlength is 8cm and breadth is 4cm.",
        "options": ["32cm²", "30cm²", "24cm²", "18cm²"],
        "correct_answer": 0
    },
    {
        "question": "28. What is a five-shaded polygon called?",
        "options": ["decagon", "heptagon", "hexagon", "pentagon"],
        "correct_answer": 3
    },
    {
        "question": "29. A rectangle has how many lines\n of symmetry?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": 1
    },
    {
        "question": "30. Find the volume of a cylinder whose \nbase area is 84cm² and height is 6cm.\n (Take π = 22/7)",
        "options": ["78cm²", "90cm²", "240cm²", "504cm²"],
        "correct_answer": 3
    },
    {
        "question": "31. Find the area of a circle whose\n diameter is 7cm.",
        "options": ["154.0cm²", "77.0cm²", "58.5cm²", "38.5cm²"],
        "correct_answer": 3
    },
    {
        "question": "32. What is the height of a triangle whose\n area is 144cm² and base is 16cm?",
        "options": ["10cm", "12cm", "14cm", "18cm"],
        "correct_answer": 3
    },
    {
        "question": "33. Ese is 24 years old and her younger \nsister is 18 years old. What was the\n sum of their ages 12 years ago?",
        "options": ["14 years", "15 years", "16 years", "18 years"],
        "correct_answer": 3
    },
    {
        "question": "34. What is the average of the following \nset of numbers: 6, 3, 2, 5, 5, 6, 8.",
        "options": ["2", "3", "5", "6"],
        "correct_answer": 2
    },
    {
        "question": "35. Find the mode of the following set of \nnumbers: 3, 2, 1, 0, 2, 3, 4, 2, 4",
        "options": ["0", "3", "2", "6"],
        "correct_answer": 2
    },
    {
        "question": "36. Which of the following is not an effect \nof air pollution?",
        "options": ["eye irritation", "lung disease", "running nose", "severe dysentery"],
        "correct_answer": 3
    },
    {
        "question": "37. Which of the following is a function\n of the canines?",
        "options": ["biting", "chewing", "grinding", "tearing"],
        "correct_answer": 3
    },
    {
        "question": "38. The reaction between oil and caustic\n potash during soap production is —",
        "options": ["condensation", "purification", "saponification", "separation"],
        "correct_answer": 2
    },
    {
        "question": "39. The force that pulls an object from a \nheight to the ground is",
        "options": ["electrical", "frictional", "gravitational", "magnetic"],
        "correct_answer": 2
    },
    {
        "question": "40. Which of the following is a \nshort distance race?",
        "options": ["400 metres", "1,500 metres", "3,000 metres", "5,000 metres"],
        "correct_answer": 0
    },
    {
        "question": "41. Which of these is an example of a \nthird class lever?",
        "options": ["crowbar", "hammer", "pliers", "shovel"],
        "correct_answer": 3
    },
    {
        "question": "42. Which of the following is a\n rhythmic movement?",
        "options": ["crawling", "lifting", "marching", "pulling"],
        "correct_answer": 3
    },
    {
        "question": "43. Forward roll is an activity \nperformed in",
        "options": ["aquatics", "athletics", "gymnastics", "soccer"],
        "correct_answer": 2
    },
    {
        "question": "44. Strength is measured by pull-up\n while balance is",
        "options": ["beam walk", "minute run", "press up", "sit up"],
        "correct_answer": 0
    },
    {
        "question": "45. How many players make a team in a\n game of football?",
        "options": ["10", "11", "13", "20"],
        "correct_answer": 1
    },
    {
        "question": "46. Latex is obtained from the",
        "options": ["bark", "branch", "flower", "leaf"],
        "correct_answer": 0
    },
    {
        "question": "47. The process of starting up a computer",
        "options": ["booting", "computing", "hibernating", "loading"],
        "correct_answer": 0
    },
    {
        "question": "48. Which of the following is not a\n computer hardware?",
        "options": ["cursor", "keyboard", "monitor", "mouse"],
        "correct_answer": 0
    },
    {
        "question": "49. Which of the following is a \nmagnetic material?'",
        "options": ["Coin", "Paper", "Plastic", "Wood"],
        "correct_answer": 0
    },
    {
        "question": "50. Which of the following is not a \nsense organ?",
        "options": ["Ear", "Eye", "Heart", "Skin"],
        "correct_answer": 2
    }
]

    def on_pre_enter(self):
        self.reset_quiz_state()
        self.load_question()
    def load_question(self):
        if 0 <= self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.ids.question_label.text = question["question"]
            for i, option in enumerate(question["options"]):
                self.ids[f'option_{i + 1}'].text = option
        else:
            # Handle the case where all questions are answered
            self.manager.current = 'result_screen_g0'

    def __init__(self, **kwargs):
        super(QuizScreenG0, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()

    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen_g0").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen_g0"
    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreenG0(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz_screen_g0')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"

class CorrectionG0(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreenG0.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)
class QuizScreenG1(Screen):
    current_question = 0
    score = 0

    questions =  [
    {
      "question": "1. Add 2.04 + 0.78 + 56.23 + 0.07",
      "options": ["59.12", "59.02", "58.22", "59.13"],
      "correct_answer": 0
    },
    {
      "question": "2. What is the quotient of 50.00 and 4.00?",
      "options": ["200", "46.00", "12.50", "54.00"],
      "correct_answer": 2
    },
    {
      "question": "3. Simplify (6 - 5) ÷ (-4 + 9) – (16 – 14)",
      "options": ["10", "5", "2", "3"],
      "correct_answer": 3
    },
    {
      "question": "4. Mrs. Al-Mustapha bought 200 eggs for\n N5,000.00. Each of the eggs was sold at\n N30.00 each. How much did she gain?",
      "options": ["N600", "N6,000", "N1,000", "N500"],
      "correct_answer": 1
    },
    {
      "question": "5. Enitan borrowed N12,000.00 from Chiuzor\n and promised to pay the money back \nafter 2 years together with an\n interest of 7%. How much should \nEnitan pay back to Chiuzor altogether?",
      "options": ["N 1,680", "N13,680", "10,320", "84,000"],
      "correct_answer": 0
    },
    {
      "question": "6. The market price of a refrigerator is \nN275,000.00, what will be the selling\n price if a discount of 10% is allowed?",
      "options": ["N302,500", "N295,000", "N303,500", "N247,500"],
      "correct_answer": 2
    },
    {
      "question": "7. If 12 women clean a building in 10 days,\n how long will it take 30 women to finish \nthe same piece of job if they work \nat the same rate?",
      "options": ["10 days", "6 days", "5 days", "4 days"],
      "correct_answer": 2
    },
    {
      "question": "8. Mr. Gunat's take-home pay for the month \nof November 2020 was reduced by 5%.\n If Mr. Gunat received N342,000.00\n after the reduction, how much was\n deducted from his salary?",
      "options": ["N360,000", "N36,000", "N18,000", "N9,000"],
      "correct_answer": 1
    },
    {
      "question": "9. Mr. Abidemi was born in the year 1953 and \ngave birth to his daughter in the\n year 1979. How old will Mr. Abidemi\n be when his daughter will be\n celebrating her 47th birthday?",
      "options": ["76 years", "69 years", "64 years", "73 years"],
      "correct_answer": 2
    },
    {
      "question": "10. Find the average of \n211, 568, 281, 189, 67, and 99?",
      "options": ["263", "362", "136", "236"],
      "correct_answer": 2
    },
    {
      "question": "11. What number will be divided by \n8 to give you a value that is\n 3 times 24?",
      "options": ["576", "567", "636", "720"],
      "correct_answer": 0
    },
    {
      "question": "12. What is the distance covered by a\n moving vehicle that traveled\n at a speed of 90 km/h in 30 minutes?",
      "options": ["120 km", "60 km", "90 km", "45 km"],
      "correct_answer": 2
    },
    {
      "question": "13. Adaobi and Chinelo were standing on\n point A, which was at the edge\n of a rectangular block. If Adaobi\n alone had to move round the rectangular\n block until she met with Chinelo at point A,\n what is the distance covered assuming the\n rectangular block had a length of 24m \nand a breadth of 36m?",
      "options": ["126m", "120m", "432m", "128m"],
      "correct_answer": 1
    },
    {
      "question": "14. A circle is divided into 12 equal sectors.\n What is the angle of each of the sectors?",
      "options": ["120°", "60°", "30°", "12°"],
      "correct_answer": 1
    },
    {
      "question": "15. A man arrived at a meeting venue 37 minutes\n late.If he finally spent 1 hour 23 minutes\n in the meeting and the meeting ended at \n2:33 p.m. At what time did the meeting\n start?",
      "options": ["12:30 p.m.", "11:30 a.m.", "11:33 a.m.", "12:33 p.m."],
      "correct_answer": 2
    },
    {
      "question": "16. A total of 756 oranges were shared among \nHussaina, Abeke, and Ifeyinwa in the ratio\n 2:3:4. How much did Ifeyinwa get?",
      "options": ["336", "168", "252", "172"],
      "correct_answer": 0
    },
    {
      "question": "17. Find the circumference of a circle with \na diameter of 7cm. Assume that pi is",
      "options": ["42cm", "32cm", "54cm", "22cm"],
      "correct_answer": 2
    },
    {
      "question": "18. In a class of 40 pupils, 15 of the pupils \nlove Mathematics, 7 love English, 28 love \nGeneral Studies while 23 love \nVerbal Reasoning. What percentage of \nthe class loves Mathematics?",
      "options": ["15%", "40%", "37.5%", "45.5%"],
      "correct_answer": 1
    },
    {
      "question": "19. What is the product of the sum of all\n the even numbers from 1 to 9 and \nall the odd numbers from 1 to 9?",
      "options": ["320", "500", "550", "450"],
      "correct_answer": 0
    },
    {
      "question": "20. What is the next number in the series \n237, 231, 226, 222, 219, 217, ………?",
      "options": ["215", "216", "214", "218"],
      "correct_answer": 0
    },
    {
      "question": "21. When half of 3,680 is Subtracted from \na quarter of 2,800 the \nanswer is …………………….?",
      "options": ["1,140", "1,840", "949", "1240"],
      "correct_answer": 0
    },
    {
      "question": "22. What is the ratio of boys to girls in a \nClass if there are 18 boys and 36 girls in \nthe class?",
      "options": ["1:3", "9:14", "3:1", "1:2"],
      "correct_answer": 2
    },
    {
      "question": "23. If the value of \ny = 4, x = 2 and z = 3. \nFind the value of (3y-9x) + 3xyz.",
      "options": ["66", "72", "78", "48"],
      "correct_answer": 0
    },
    {
      "question": "24. How many prime numbers are there in\n the set of numbers below?\n 12, 13, 14, 15, 16, 17, 18, 19, 20.",
      "options": ["2", "3", "4", "5"],
      "correct_answer":1
    },
    {
      "question": "25. Write in roman numerals one thousand,\n five hundred and eighty-four.",
      "options": ["MMDLXXIV", "MDLXXXVII" "MDLXXXIV" "DLXXIV"],
      "correct_answer": 2
    },
    {
      "question": "26. What is the HCF of 9, 12, and 15?",
      "options": ["2", "3", "4", "5"],
      "correct_answer": 1
    },
    {
      "question": "27. 2 years ago, a girl was 7 years old,\n how old will she be in 5 years time?",
      "options": ["7", "9", "10", "14"],
      "correct_answer": 3
    },
    {
      "question": "28. Express 5/8 as a decimal fraction",
      "options": ["0.652", "0.625", "0.605", "0.265"],
      "correct_answer": 1
    },
    {
      "question": "29 Solve the equation 3y + 4y =49",
      "options": ["7", "10", "5", "14"],
      "correct_answer": 0
    },
    {
      "question": "30. What is the place value \nof 7 in 5,670,038?",
      "options": ["Million", "Hundred of thousand", "Tens", "Tens of thousand"],
      "correct_answer": 3},
    {
      "question": "31. What is the meaning of www \nin computer studies?",
      "options": ["wide world web", "world wide web", "web wide world", "world web wide"],
      "correct_answer": 1
    },
    {
      "question": "32. A person who studies the weather\n of a place and predicts the \npossible change in weather is called ……",
      "options": ["weathertologist", "climate expert", "technocrat", "meteorologist"],
      "correct_answer": 3
    },
    {
      "question": "33. A medical doctor that specializes in \nthe study and treatment of medical\n conditions or issues related \nto children is called....",
      "options": ["neurologist", "paediatrician", "psychologist", "dermatologist"],
      "correct_answer": 1
    },
    {
      "question": "34. Which of the following classes of food \nis best for proving energy to the body?",
      "options": ["carbohydrates", "fat and oil", "vitamin", "mineral"],
      "correct_answer": 0
    },
    {
      "question": "35. Which of the following methods is most\n appropriate for the preservation of\n vegetables?",
      "options": ["smoking", "evaporation", "refrigeration", "grinding"],
      "correct_answer": 2
    },
    {
      "question": "36.What is the freezing point of clean \nand pure water?",
      "options": ["100°C", "0", "10°C", "5°C"],
      "correct_answer": 1
    },
    {
      "question": "37. The washing away of topsoil moving\n water or air is called",
      "options": ["washing", "evaporation", "movement", "erosion"],
      "correct_answer": 3
    },
    {
      "question": "38. Which of the following types of \nsoil is best for agriculture?",
      "options": ["sandy soil", "clay soil", "muddy soil", "loamy soil"],
      "correct_answer": 3
    },
    {
      "question": "39. The instrument used to measure \ntemperature is called.......",
      "options": ["barometer", "thermometer", "hygrometer", "potentiometer"],
      "correct_answer": 1
    },
    {
      "question": "40. Which of the following substances will\n float on water?",
      "options": ["stone", "metal", "palm oil", "hammer"],
      "correct_answer": 2
    },
    {
      "question": "41. Which of the following is not a\n computer hardware?",
      "options": ["cursor", "keyboard", "monitor", "mouse"],
      "correct_answer": "0"
    },
    {
      "question": "42. Toad and frog are generally called_______",
      "options": ["amphibians", "aves", "mammals", "pisces"],
      "correct_answer": "0"
    },
    {
      "question": "43. The instrument used for measuring\n the speed of the wind is a/an",
      "options": ["anemometer", "barometer", "hygometer", "wind vane"],
      "correct_answer": "0"
    },
    {
      "question": "44. Football matches are officiated by _____",
      "options": ["coaches", "commentators", "games master", "referees"],
      "correct_answer": "3"
    },
    {
      "question": "45. Swimming competition usually takes\n place in the _______",
      "options": ["arena", "court", "field", "pool"],
      "correct_answer": "3"
    },
    {
      "question": "46. Who among the following is regarded\n as the father of computer?",
      "options": ["Bill Gates", "Charles Babbage", "Steve Jobs", "Mark Zuckerberg"],
      "correct_answer": "0"
    },
    {
      "question": "47.The device used to monitor activites in \nschools, offices, home and business \npremises is _______ ",
      "options": ["ACTV", "CCTV", "DSTV", "GOTV"],
      "correct_answer": "1"
    },
    {
      "question": "48. A by-product of wood is________",
      "options": ["ceramic", "paper", "plastic", "polythene"],
      "correct_answer": "1"
    },
    {
      "question": "49. The following are examples of \naquatic animals except",
      "options": ["crab", "rat", "fish", "lobster"],
      "correct_answer": "1"
    },
    {
      "question": "50. Drilling is a process of\n making_____ in a material",
      "options": ["holes", "steps", "marks", "stems"],
      "correct_answer": "0"
    },
  ]

    def on_pre_enter(self):
        self.reset_quiz_state()
        self.load_question()
    def load_question(self):
        if 0 <= self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.ids.question_label.text = question["question"]
            for i, option in enumerate(question["options"]):
                self.ids[f'option_{i + 1}'].text = option
        else:
            # Handle the case where all questions are answered
            self.manager.current = 'result_screen_g1'

    def __init__(self, **kwargs):
        super(QuizScreenG1, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()

    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen_g1").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen_g1"

    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreenG1(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz_screen_g1')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"
class CorrectionG1(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreenG1.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)
class QuizScreenG2(Screen):
    current_question = 0
    score = 0

    questions = [
    {
        "question": "1. Find the sum of 1576,\n 125 and 64.",
        "options": ["1665", "1701", "1765", "2341"],
        "correct_answer": 2
    },
    {
        "question": "2. There are 34 mangoes on a tree, \nif only 9 of them are ripe, \nhow many unripe mangoes are there?",
        "options": ["43", "41", "26", "25"],
        "correct_answer": 3
    },
    {
        "question": "3. Find the least common multiple \nof 3, 4 and 5.",
        "options": ["120", "60", "30", "24"],
        "correct_answer": 1
    },
    {
        "question": "4. Express 17/20 as a decimal.",
        "options": ["0.085", "0.175", "0.85", "1.75"],
        "correct_answer": 2
    },
    {
        "question": "5. The length of a rectangular table\n is 40cm and its breadth is 25cm.\n Find its perimeter.",
        "options": ["1000cm", "130cm", "105cm", "90cm"],
        "correct_answer": 1
    },
    {
        "question": "6. If 4x—3 = 21,\n what is x?",
        "options": ["21", "7", "6", "5"],
        "correct_answer": 2
    },
    {
        "question": "7. What is the value of \n4³ x 3?",
        "options": ["192", "126", "64", "36"],
        "correct_answer": 0
    },
    {
        "question": "8. Express 72 as a product\n of its prime factors.",
        "options": ["2 x 2 x 2 x 3 x 3", "2 x 2 x 3 x 3 x 3", "2 x 2 x 2 x 2 x 3 x 3 x 3", "2 x 2 x 2 x 3 x 3 x 3"],
        "correct_answer": 0
    },
    {
        "question": "9. Write in figure: Sixty \nfour thousand, six hundred and four.",
        "options": ["6,464", "64,064", "60,604", "64,604"],
        "correct_answer": 3
    },
    {
        "question": "10. Write 48 in Roman Numerals.",
        "options": ["LXVIII", "XLIIX", "LVIII", "XLVIII"],
        "correct_answer": 3
    },
    {
        "question": "11. Ali and Yemi are to share N17.00\n such that Yemi takes N3.50 more\n than Ali, how much is Ali's share?",
        "options": ["N14.50", "N13.50", "N10.25", "N6.75"],
        "correct_answer": 2
    },
    {
        "question": "12. if 5/9 = x/36 \nWhat is x?",
        "options": ["45", "27", "20", "9"],
        "correct_answer": 2
    },
    {
        "question": "13. Find the average of \n6, 2, 5, 3,2.",
        "options": ["43", "2", "3", "25"],
        "correct_answer": 2
    },
    {
        "question": "14. Which of the following is/are odd?\n 1, 2, 3, 4, 6, 9, 24",
        "options": ["1 only", "9 only", "1 and 9 only", "1, 3 and 9 only"],
        "correct_answer": 3
    },
    {
        "question": "15. Find the simple interest on N360.00\n for 2 years at 5% per annum.",
        "options": ["N3.60", "N9.00", "N18.00", "N36.00"],
        "correct_answer": 3
    },
    {
        "question": " Use the following to answer\n questions 16 to 18\nX = 3, Y = 9 and Z = 12.\n16. Let the product of x, Y and Z\n be 3P, find P.",
        "options": ["11664", "972", "324", "108"],
        "correct_answer": 3
    },
    {
        "question": "X = 3, Y = 9 and Z = 12.\n17. Let Q be quotient of \nY and X therefore, 4Q is ………",
        "options": ["3", "12", "27", "16"],
        "correct_answer": 1
    },
    {
        "question": "X = 3, Y = 9 and Z = 12.\n18. Which of the following is \nnot true about X, Y & Z",
        "options": ["X + Y = Z", "Y = 3X", "Z - Y = X", "Y = Z"],
        "correct_answer": 3
    },
    {
        "question": "19. Fuel is sold at N26.00 per \nlitre. If my father fills his\n tank with N1,300.00.\n How many litres did he buy?",
        "options": ["126 litres", "130 litres", "100 litres", "50 litres"],
        "correct_answer": 3
    },
    {
        "question": "20. Express in figures: \nOne hundred and seven thousand \nand forty six.",
        "options": ["100,700,046", "10,745", "107,046", "10,746"],
        "correct_answer": 2
    },
    {
        "question": "21. What is the sum of \n1/2, 1/8, 1/4 and 1/3?",
        "options": ["1", "1", "2", "2"],
        "correct_answer": 2
    },
    {
        "question": "22. Find the least common multiple\n of 3, 4 and 5.",
        "options": ["120", "60", "30", "24"],
        "correct_answer": 1
    },
    {
        "question": "23. An isosceles triangle has\n ...... lines of symmetry.",
        "options": ["2", "5", "3", "1"],
        "correct_answer": 3
    },
    {
        "question": "24. A rectangular tank 6m by 4m\n by 5m is half full, \nwhat is the volume of water in \nthe tank?",
        "options": ["12m³", "120m³", "30m³", "60m³"],
        "correct_answer": 3
    },
    {
        "question": "25. Divide 240.06 by 6.",
        "options": ["4.1", "4.01", "40.01", "40.1"],
        "correct_answer": 2
    },
    {
        "question": "26. Change 0.55 kilograms\n to grams.",
        "options": ["5.5 grams", "55 grams", "500 grams", "550 grams"],
        "correct_answer": 3
    },
    {
        "question": "27. A car travels at 80km \nper hour, it drove for 2 hours,\n rested for 1 hour and continued\n the journey for another hour. \nOn the whole, how many kilometers\n did the car travel?",
        "options": ["240km", "320 km", "400km", "480 km"],
        "correct_answer": 0
    },
    {
        "question": "28. Write CXLVI in figures.",
        "options": ["164", "156", "146", "136"],
        "correct_answer": 2
    },
    {
        "question": "29. What is HCF of \n2 x 3x5; 2² x 3; 2 x 3² x5³?",
        "options": ["2² x 3", "2 x 3", "2 x 3 x 5²", "2² x 3²"],
        "correct_answer": 1
    },
    {
        "question": "30. If 25p = 625, \nwhat is 55p?",
        "options": ["1375", "1360", "1350", "1345"],
        "correct_answer": 0
    },
    {
        "question": "31. 391+ 21*... = 605,\n find the missing digit.",
        "options": ["8", "6", "4", "2"],
        "correct_answer": 2
    },
    {
        "question": "32. What must be added to \n112.6 to make 172.40",
        "options": ["285.46", "255.00", "60.34", "59.80"],
        "correct_answer": 3
    },
    {
        "question": "33. Approximate 1999 to 2 \nsignificant figures",
        "options": ["19", "20", "190", "2000"],
        "correct_answer": 3
    },
    {
        "question": "34. The sum of a prime number \nbetween 1 and 12 is ________",
        "options": ["25", "28", "29", "24"],
        "correct_answer": 1
    },
    {
        "question": "35. A line that divides a circle into \ntwo equal parts is called a/an",
        "options": ["diameter", "arc", "perimeter", "radius"],
        "correct_answer": 0
    },
    {
        "question": "36. A line from the center of a circle to \nany point on a circumference is called_____",
        "options": ["circumference", "arc", "perimeter", "radius"],
        "correct_answer": 3
    },
    {
        "question": "37. What number divided by 6 equals 20?",
        "options": ["105", "100", "25", "120"],
        "correct_answer": 3
    },
    {
        "question": "38. What percentage of 0.75 is 0.45?",
        "options": ["60%", "30%", "36%", "50%"],
        "correct_answer": 0
    },
    {
        "question": "39. Correct 71.3 to the nearest ten.",
        "options": ["72", "71", "70", "73"],
        "correct_answer": 1
    },
    {
        "question": "40. Approximate 87751 to the nearest hundred.",
        "options": ["88000", "90000", "87800", "80000"],
        "correct_answer": 2
    },
    {
        "question": "41. Which of the following protects \nthe brain from damage.",
        "options": ["muscle", "skull", "rub cage", "backbone"],
        "correct_answer": 1
    },
    {
        "question": "42. Aeroplanes are kept in _______",
        "options": ["free ways", "airport", "parking lot", "hangar"],
        "correct_answer": 3
    },
    {
        "question": "43. During cooking ______ energy is used.",
        "options": ["electrical", "chemical", "solar", "heat"],
        "correct_answer": 3
    },
    {
        "question": "44. Which of these is an output\n device of computer?",
        "options": ["CPU", "printer", "mouse", "keyboard"],
        "correct_answer": 1
    },
    {
        "question": "45. Growing crops with _____ \ngives improved yields.",
        "options": ["sand", "manure", "charcoal", "dust"],
        "correct_answer": 1
    },
    {
        "question": "46. Petrol, diesel and kerosene \nare products of _______",
        "options": ["wax", "coal", "iron ore", "crude oil"],
        "correct_answer": 3
    },
    {
        "question": "47. food containing all the classes \nof food is called________. ",
        "options": ["balanced diet", "good food", "balance food", "energy food"],
        "correct_answer": 1
    },
    {
        "question": "48. A dentist is tooth as \nan oculist is to __________.",
        "options": ["brain", "blood", "bone", "eye"],
        "correct_answer": 3
    },
    {
        "question": "49. The process whereby water\n is changed to steam is ______",
        "options": ["evaporation", "freezing", "condensation", "melting"],
        "correct_answer": 0
    },
    {
        "question": "50. The person who installs water system \nin a building is called______",
        "options": ["carpenter", "plumber", "engineer", "pilot"],
        "correct_answer": 1
    }
]
    def on_pre_enter(self):
        self.reset_quiz_state()
        self.load_question()

    def load_question(self):
        if 0 <= self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.ids.question_label.text = question["question"]
            for i, option in enumerate(question["options"]):
                self.ids[f'option_{i + 1}'].text = option
        else:
            # Handle the case where all questions are answered
            self.manager.current = 'result_screen_g2'

    def __init__(self, **kwargs):
        super(QuizScreenG2, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()

    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen_g2").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen_g2"

    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreenG2(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz_screen_g2')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"
class CorrectionG2(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreenG2.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)
class QuizScreenG3(Screen):
    current_question = 0
    score = 0

    questions = [
    {
        "question": "1. Add 2.04 + 0.78 + 56.23 + 0.07",
        "options": ["59.12", "59.02", "58.22", "59.13"],
        "correct_answer": 0
    },
    {
        "question": "2. what is the quotient of 50.00 and 4.00?",
        "options": ["200", "46.00", "12.50", "54.00"],
        "correct_answer": 2
    },
    {
        "question": "3. simplify \n1/2+1/8 + ( -4 + 9) – (16 – 14)",
        "options": ["10 3/8", "5 3/8", "2 3/8", "3 5/8"],
        "correct_answer": 3
    },
    {
        "question": "4. Mrs. Al-Mustapha bought 200 eggs\n for N5,000.00. Each of the eggs\n were sold at N30.00 each.\n How much did she gain?",
        "options": ["N600", "N6,000", "N1,000", "N500"],
        "correct_answer": 1
    },
    {
        "question": "5. Enitan borrowed N12,000.00 from\n Chiuzor and promised to pay the money\n back after 2 years together with\n an interest of 7%. How much\n should Enitan pay back to Chiuzor \naltogether?",
        "options": ["N 1,680", "N13,680", "10, 320", "84, 000"],
        "correct_answer": 0
    },
    {
        "question": "6. The market price of a refrigerator,\n is N275,000.00, what will be the \nselling price of a discount of 10%\n is allowed?",
        "options": ["N302,500", "N295,000", "N303,500", "N247,500"],
        "correct_answer": 3
    },
    {
        "question": "7. If 12 women clean a building in \n10 days, how long will it take 30\n women to finish the same piece of \njob if they work at the same rate?",
        "options": ["10 days", "6 days", "5 days", "4 days"],
        "correct_answer": 3
    },
    {
        "question": "8. Mr. Gunat take home pay for the month \nof November 2020 was reduced by 5%.\n If Mr. Gunat received N342, 000.00 \nafter the reduction, how much\n was deducted from his salary.",
        "options": ["N360,000", "N36,000", "N18,000", "N9,000"],
        "correct_answer": 1
    },
    {
        "question": "9. Mr. Abidemi was born in year 1953 and\n gave birth to his daughter in year 1979.\n How old will Mr. Abidemi be when \nhis daughter will be celebrating her\n 47th birthday?",
        "options": ["76years", "69years", "64years", "73years"],
        "correct_answer": 2
    },
    {
        "question": "10. Find the average of \n211, 568, 281, 189, 67 and 99?",
        "options": ["263", "362", "136", "236"],
        "correct_answer": 2
    },
    {
        "question": "11. What number will be divided by\n 8 to give you a value that is\n 3 times 24?",
        "options": ["576", "567", "636", "720"],
        "correct_answer": 0
    },
    {
        "question": "12. What is the distance covered by\n a moving vehicle that travelled \nat a speed of 90km/h in 30 minutes?",
        "options": ["120km", "60km", "90km", "45km"],
        "correct_answer": 2
    },
    {
        "question": "13. Adaobi and Chinelo were standing \non point A which was at the edge\n of rectangular block. If Adaobi \nalone had to move round the rectangular\n block until she met with Chinelo \nat point A, what is the distance covered\n assuming the rectangular block had a \nlength of 24m and a breadth of 36m",
        "options": ["126m", "120m", "432m", "128m"],
        "correct_answer": 1
    },
    {
        "question": "14. Express 160cm as a fraction of 4m.",
        "options": ["2/5", "1/5", "3/5", "1/4"],
        "correct_answer": 0
    },
    {
        "question": "15. A circle is divided into 12 equal\n sectors. What is the angle of each of the\n sectors?",
        "options": ["120°", "60°", "30°", "12°"],
        "correct_answer": 1
    },
    {
        "question": "16. A man arrived a meeting venue 37 \nminutes late. If he finally spent 1 hour 23\n minutes in the meeting and the meeting\n ended at 2.33p.m. At what time did the\n meeting start?",
        "options": ["12.30pm", "11.30am", "11.33am", "12.33pm"],
        "correct_answer": 2
    },
    {
        "question": "17. A total of 756 oranges were shared\n among Hussaina, Abeke and Ifeyinwa in\n the ration 2: 3:4. How much did Ifeyinwa\n get?",
        "options": ["336", "168", "252", "172"],
        "correct_answer": 0
    },
    {
        "question": "18. Find the circumference of a circle\n with diameter of 7cm. Assume that\n pie is 22/7",
        "options": ["42cm", "32cm", "54cm", "22cm"],
        "correct_answer": 3
    },
    {
        "question": "19. Simplify:\n (6 1/4 – 5 1/2 ) ÷ 1/4",
        "options": ["3/4", "1/4", "1/2", "3"],
        "correct_answer": 2
    },
    {
        "question": "20. In a class of 40 pupils, 15 \nof the pupils love Matheratics,7 \nlove English, 28 love General Studies \nwhile 23 love Verbal Reasoning. What \npercentage of the class love \nMathematics?",
        "options": ["15%", "40%", "37.5%", "45.5%"],
        "correct_answer": 1
    },
    {
        "question": "21. What is the product of the sum of \nall the even numbers from 1 to 9 \nand all the odd numbers from 1 to 9?",
        "options": ["320", "500", "550", "450"],
        "correct_answer": 0
    },
    {
        "question": "22. What is the next number in the series\n 237, 231,226, 222,219, 217,………….?",
        "options": ["215", "216", "214", "218"],
        "correct_answer": 0
    },
    {
        "question": "23. When half of 3,680 is Subtracted \nfrom a quarter of 2,800 the \nanswer is …………………….?",
        "options": ["1,140", "1,840", "949", "1240"],
        "correct_answer": 0
    },
    {
        "question": "24. What is the ratio of boys to girls in a\n Class if there are 18 boys and 36 girls\n in the class?",
        "options": ["1:3", "9:14", "3:1", "1:2"],
        "correct_answer": 2
    },
    {
        "question": "25. If the value of y = 4, x = 2 and z = 3. \nFind the value of (3y-9x) + 3xyz.",
        "options": ["66", "72", "78", "48"],
        "correct_answer": 0
    },
    {
        "question": "26. What is the meaning of www \nin computer studies?",
        "options": ["wide world web", "world wide web", "web wide world", "world web wide"],
        "correct_answer": 1
    },
    {
        "question": "27. A person who studies the weather of a \nplace and predicts the possible change in\n weather is called ……",
        "options": ["weathertologist", "climate expert", "technocrat", "meteorologist"],
        "correct_answer": 3
    },
    {
        "question": "28. A medical doctor that specializes in the\n study and treatment of medical conditions\n or issues related to children is called",
        "options": ["neurologist", "paediatrician", "psychologist", "dermatologist"],
        "correct_answer": 1
    },
    {
        "question": "29. Which of the following classes of food\n is best for proving energy to the body?",
        "options": ["carbohydrates", "fat and oil", "vitamin", "mineral"],
        "correct_answer": 0
    },
    {
        "question": "30. Which of the following methods is\n most appropriate for the preservation of\n vegetables?",
        "options": ["smoking", "evaporation", "refrigeration", "grinding"],
        "correct_answer": 2
    },
    {
        "question": "31. What is the freezing point of \nClean and pure water?",
        "options": ["100°C", "0", "10°C", "5 C"],
        "correct_answer": 1
    },
    {
        "question": "32. The washing away of top soil moving \nwater or air is called —__*",
        "options": ["washing", "evaporation", "movement", "erosion"],
        "correct_answer": 3
    },
    {
        "question": "33. Which of the following types of soil \nis best for agriculture?",
        "options": ["sandy soil", "clay soil", "muddy soil", "loamy soil"],
        "correct_answer": 3
    },
    {
        "question": "34. The instrument used to measure\n temperature is called.......",
        "options": ["barometer", "thermometer", "hygrometer", "potentiometer"],
        "correct_answer": 1
    },
    {
        "question": "35. Which of the following substances\n will float on water?",
        "options": ["stone", "metal", "palm oil", "hammer"],
        "correct_answer": 2
    },
    {
        "question": "36. What is the formula for the area of a rectangle?",
        "options": ["A = πr²", "A = lw", "A = 1/2 bh", "A = s²"],
        "correct_answer": 1
    },
    {
        "question": "37. What is the chemical symbol for gold?",
        "options": ["Au", "Ag", "Ge", "Gd"],
        "correct_answer": 0
    },
    {
        "question": "38. What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": 2
    },
    {
        "question": "39. Who is known as the father of modern physics?",
        "options": ["Albert Einstein", "Isaac Newton", "Galileo Galilei", "Niels Bohr"],
        "correct_answer": 0
    },
    {
        "question": "40. What is the chemical formula for water?",
        "options": ["CO₂", "H₂O", "NaCl", "H₂SO₄"],
        "correct_answer": 1
    },
    {
        "question": "41. What is the powerhouse of the cell?",
        "options": ["Ribosome", "Nucleus", "Mitochondria", "Golgi Apparatus"],
        "correct_answer": 2
    },
    {
        "question": "42. Who wrote 'To Kill a Mockingbird'?",
        "options": ["Ernest Hemingway", "Harper Lee", "J.K. Rowling", "Mark Twain"],
        "correct_answer": 1
    },
    {
        "question": "43. Who painted the Mona Lisa?",
        "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
        "correct_answer": 2
    },
    {
        "question": "44. What is the chemical symbol for iron?",
        "options": ["Fe", "Ir", "I", "In"],
        "correct_answer": 0
    },
    {
        "question": "45. Which planet is known as the Red Planet?",
        "options": ["Mars", "Jupiter", "Saturn", "Neptune"],
        "correct_answer": 0
    },
    {
        "question": "46. Who discovered penicillin?",
        "options": ["Alexander Fleming", "Louis Pasteur", "Robert Koch", "Joseph Lister"],
        "correct_answer": 0
    },
    {
        "question": "47. Who wrote 'Romeo and Juliet'?",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "correct_answer": 0
    },
    {
        "question": "48. What is the chemical symbol for potassium?",
        "options": ["Po", "K", "Pt", "P"],
        "correct_answer": 1
    },
    {
        "question": "49. Who was the first person to step on the moon?",
        "options": ["Buzz Aldrin", "Neil Armstrong", "Yuri Gagarin", "John Glenn"],
        "correct_answer": 1
    },
    {
        "question": "50. What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "correct_answer": 1
    }
]

    def on_pre_enter(self):
        self.reset_quiz_state()
        self.load_question()

    def load_question(self):
        if 0 <= self.current_question < len(self.questions):
            question = self.questions[self.current_question]
            self.ids.question_label.text = question["question"]
            for i, option in enumerate(question["options"]):
                self.ids[f'option_{i + 1}'].text = option
        else:
            # Handle the case where all questions are answered
            self.manager.current = 'result_screen_g3'

    def __init__(self, **kwargs):
        super(QuizScreenG3, self).__init__(**kwargs)
        self.selected_button = None

    def check_answer(self, button):
        if self.selected_button:
            self.selected_button.background_color = (1, 1, 1, 1)  # Set default background color

        button.background_color = (0, 1, 0, 1)  # Green background color
        self.selected_button = button

        # Check if the selected answer is correct
        question = self.questions[self.current_question]
        correct_answer_index = question["correct_answer"]
        if button == self.ids[f'option_{correct_answer_index + 1}']:
            self.score += 1

    def next_question(self):
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
            self.clear_buttons()
        else:
            self.manager.transition.direction = "up"  # Set transition direction
            self.show_result()

    def clear_buttons(self):
        for i in range(4):
            self.ids[f'option_{i + 1}'].background_color = (1, 1, 1, 1)  # Reset button color
            self.ids[f'option_{i + 1}'].disabled = False

    def show_result(self):
        result_label = self.manager.get_screen("result_screen_g3").ids.result_label
        result_label.text = f"Result: {self.score}/{len(self.questions)}"
        self.manager.current = "result_screen_g3"

    def reset_quiz_state(self):
        self.current_question = 0
        self.score = 0

    def try_again(self):
        self.reset_quiz_state()
        self.manager.current = 'second'

class ResultScreenG3(Screen):
    def on_enter(self, *args):
        # Display the total score on the ResultScreen
        quiz_screen = self.manager.get_screen('quiz_screen_g3')
        result_label = self.ids.result_label
        total_score = quiz_screen.score
        total_questions = len(quiz_screen.questions)
        comment = ""

        if total_score == total_questions:
            comment = "Excellent! You got all the questions right."
        elif total_score >= total_questions * 0.8:
            comment = "Great job! You scored well."
        elif total_score >= total_questions * 0.6:
            comment = "Good effort! Keep practicing."
        else:
            comment = "You need more practice. Keep trying!"

        result_label.text = f"Your score: {total_score}/{total_questions}\n{comment}"
class CorrectionG3(Screen):
    def on_pre_enter(self):
        self.populate_correction()
    def populate_correction(self):
        correction_grid = self.ids.correction_grid
        for question in QuizScreenG3.questions:
            question_text = question["question"]
            options = question["options"]
            correct_answer_index = question["correct_answer"]

            question_label = Label(text=question_text, size_hint_y=None, height=dp(50),color=(0, 0, 0, 1))
            correction_grid.add_widget(question_label)

            for i, option in enumerate(options):
                option_button = Button(text=option, size_hint_y=None, height=dp(50))
                if i == correct_answer_index:
                    option_button.background_color = (0, 1, 0, 1)  # Green for correct answer
                else:
                    option_button.background_color = (1, 0, 0, 1)  # Red for incorrect answer
                correction_grid.add_widget(option_button)
class LoginPage(MDApp):
    def build(self):
        return Builder.load_file("sure.kv")

if __name__ == '__main__':
    LoginPage().run()


