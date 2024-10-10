from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '8c540c44e5318c71256e15fc1b15d61e'  # Replace with a secure random key

# Quiz data
QnA = [
    ["Which planet is known as the Red Planet?", "A) Earth B) Mars C) Jupiter D) Venus", "B"],
    ["What is the capital of India?", "A) Mumbai B) Delhi C) Kolkata D) Chennai", "B"],
    ["Which ocean is the largest?", "A) Atlantic B) Indian C) Arctic D) Pacific", "D"],
    ["What is the chemical symbol for water?", "A) H2O B) O2 C) CO2 D) HO", "A"],
    ["Which country is home to the Great Barrier Reef?", "A) USA B) Australia C) Canada D) India", "B"],
    ["Which is the longest river in the world?", "A) Amazon B) Nile C) Yangtze D) Mississippi", "B"],
    ["Who invented the telephone?", "A) Albert Einstein B) Thomas Edison C) Alexander Graham Bell D) Nikola Tesla", "C"],
    ["What is the tallest mountain in the world?", "A) Mount Kilimanjaro B) K2 C) Mount Everest D) Mount Fuji", "C"],
    ["Which continent is the Sahara Desert located in?", "A) Asia B) Africa C) South America D) Australia", "B"],
    ["Which bird is often associated with delivering babies in folklore?", "A) Owl B) Sparrow C) Eagle D) Stork", "D"],
    ["What is the national currency of Japan?", "A) Yen B) Won C) Dollar D) Rupee", "A"],
    ["Which country gifted the Statue of Liberty to the USA?", "A) Germany B) France C) Italy D) Spain", "B"],
    ["Which is the smallest country in the world by area?", "A) Monaco B) Vatican City C) Luxembourg D) San Marino", "B"],
    ["What is the freezing point of water?", "A) 0°C B) 50°C C) 100°C D) -10°C", "A"],
    ["Who was the first man to walk on the moon?", "A) Yuri Gagarin B) Neil Armstrong C) Buzz Aldrin D) Michael Collins", "B"]
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 30000, 50000, 100000, 1000000, 2500000, 5000000, 10000000, 20000000, 50000000, 10000000]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['GET', 'POST'])
def start():
    session['score'] = 0
    session['question_index'] = 0
    return redirect('/question')

@app.route('/question', methods=['GET', 'POST'])
def question():
    if 'question_index' not in session:
        return redirect('/')
    
    question_index = session['question_index']
    
    if question_index >= len(QnA):
        return redirect('/result')
    
    if request.method == 'POST':
        reply = request.form['reply']
        correct_answer = QnA[question_index][2]
        
        if reply.upper() == correct_answer:
            session['score'] = levels[question_index]
            session['question_index'] += 1
            
            if session['score'] == 10000000:
                return redirect('/jackpot')
            return redirect('/question')
        else:
            return redirect('/result')

    question = QnA[question_index]
    return render_template('question.html', question=question, level=levels[question_index])

@app.route('/result')
def result():
    score = session.get('score', 0)
    return render_template('result.html', score=score)

@app.route('/jackpot')
def jackpot():
    return render_template('jackpot.html')

if __name__ == '__main__':
    app.run(debug=True)
