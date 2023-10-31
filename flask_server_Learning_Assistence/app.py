from flask import Flask, render_template, request, redirect, url_for , jsonify

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('login-email')
        password = request.form.get('login-password')

        # Do something with the form data (e.g., authentication)

        # Redirect to generate_qna.html
        return redirect(url_for('generate_qna'))

    return render_template('auth.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve form data
        email = request.form.get('signup-email')
        password = request.form.get('signup-password')
        password2 = request.form.get('confirm-signup-password')

        # Perform validation or other actions with the form data
       
        # Print form data (for demonstration purposes)
        print(f'Email: {email}, Password: {password} ,  password2 : { password2}')
        
        # Add your logic for user registration or other actions
        return redirect(url_for('login'))

    return render_template('auth.html')




@app.route('/create_post' , methods=['GET', 'POST'] )
def create_post():
    # Additional logic for generating Q&A or render a template
     if request.method == 'POST':
            # Retrieve form data
        new_post = request.form.get('post-input')
       

        # Perform validation or other actions with the form data
       
        # Print form data (for demonstration purposes)
        print(f'new_post: {new_post}')
        return redirect(url_for('forum'))
    



@app.route('/generate_qna' , methods=['GET', 'POST'])
def generate_qna():
    # Additional logic for generating Q&A or render a template
    question_data = [
    {"subject": "Math", "num_questions": 10},
    {"subject": "Science", "num_questions": 15},
    # Add more data as needed
]

    return render_template('generate_qna.html' , questions=question_data)


@app.route('/answer_evaluation')
def answer_evaluation():
    subjects_data = [
        {"subject": "Math", "score": 90},
        {"subject": "Science", "score": 85},
        {"subject": "History", "score": 78},
    ]

    return render_template('answer_evaluation.html', subjects_data=subjects_data)
    # Additional logic for generating Q&A or render a template
  


@app.route('/forum')
def forum():
    # Additional logic for generating Q&A or render a template
    return render_template('forum.html')


@app.route('/quiz' , methods=['GET', 'POST'])
def quiz():
    quiz_data = [

    {
        "question": "For Fiscal year 2021, what was your total GhG Carbon Emission for all scopes?",
        "answers": [
            "Scope 1 - Determine environmental impact levels.",
            "Scope 2 - Reduce carbon footprints.",
            "Scope 3 - Enhance environmental impacts on a larger scale.",
            "I do not know the answer to this question.",
        ],
    },
    {
        "question": "Another question?",
        "answers": [
            "Option 1",
            "Option 2",
            "Option 3",
            "I do not know the answer to this question.",
        ],
    },


    # Add more questions and answers as needed
    ]
    if request.method == 'POST':
            questionText = request.form.get('questionText')
            print(f"Launching quiz for subject: {questionText}")
            return redirect(url_for('quiz'))
    return render_template('quiz.html' , quiz_data=quiz_data)
            



@app.route('/quiz/respnse', methods=['GET', 'POST'])
def quiz_response():
    if request.method == 'POST':
        # Form data submitted, process it
        question = request.form.getlist('question')
        selected_answers = request.form.getlist('selected-answer')
        # Do something with selected_answers

        # For now, just print the selected answers
        print("Question:", question)
        print("Selected Answers:", selected_answers)
        result = "fail"
        # You can redirect to a different page or render a new template
        return render_template('quiz.html', result=result)

    # If it's a GET request, render the quiz form
    # return render_template('quiz.html', quiz_data=quiz_data)

        

@app.route('/logout')
def logout():
    # Additional logic for generating Q&A or render a template
    return redirect(url_for('login'))




if __name__ == '__main__':
    app.run(debug=True)
