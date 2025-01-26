from flask import Flask, render_template, url_for, request, jsonify, send_from_directory, redirect, Response, send_file
from backend.random_question import generate
from backend.predictor import predict
from backend.msfinder import scan
from backend.getcode import get_code_fun

import random
import os

app = Flask(__name__)

uid = random.randint(1000, 1000000000)

# Simulate a list of past paper questions
past_questions = [
    "What is the capital of France?",
    "Explain the theory of relativity.",
    "What is 2 + 2?",
    # Add more questions here...
]

# Route for solving a question
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/download')
def download_file():
    current_directory = os.getcwd()  # This gets the local directory path
    filename = 'mark_scheme.pdf'
    return send_from_directory(directory=current_directory, path=filename, as_attachment=True)



@app.route('/get_ms', methods=['POST'])
def get_ms():
    code = request.form.get('keyword')
    if code.index("/") != -1:
        scan(code)
        return redirect(url_for('download_file'))
    else:
        return "Invalid code, please try again."


@app.route('/finder')
def index_home():
    return render_template("msfinder.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/solver')
def solver():
    return render_template("solver.html")

@app.route('/generate_image', methods=['GET'])
def generate_image():
    syllabus_code = request.args.get('syllabus_code')
    if not syllabus_code:
        return "Syllabus code is required", 400

    try:
        generate(syllabus_code)

        # Path to the generated image
        image_path = os.path.join(os.getcwd(), 'question.png')

        # Check if the file exists
        if not os.path.exists(image_path):
            return "Image not found", 404

        # Open the image file and read its content
        with open(image_path, 'rb') as f:
            image_data = f.read()

        # Return the image data as a response with the appropriate content type
        return Response(image_data, mimetype='image/png')

    except Exception as e:
        return str(e), 500


@app.route('/random')
def random():
    return render_template("random.html")

@app.route('/keyterms')
def keyterms():
    return render_template("keyterms.html")

@app.route('/predictor')
def predictor():
    return render_template("predictor.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/predict', methods=['POST'])
def predict_grade():
    try:
        # Retrieve form data
        mock = request.form.get('mock', type=str)
        study = request.form.get('study-hours', type=int)
        interest = request.form.get('interest', type=int)
        average = request.form.get('pp-average', type=str)

        # Calculate predicted grade
        predicted_grade = predict(str(mock), int(study), int(interest), str(average))

        # Redirect back to form with predicted grade in query string
        return redirect(url_for('predictor', predicted_grade=predicted_grade))

    except Exception as e:
        print(f"Error: {e}")  # Log error to terminal
        return "An error occurred: " + str(e), 500

@app.route('/get_code', methods=['POST'])
def get_code_back():
    try:
        keyword = request.form.get('keyword', type=str)
        out = get_code_fun(str(keyword))
        return redirect(url_for('get_code', code=out))

    except Exception as e:
        print(f"Error: {e}")  # Log error to terminal
        return "An error occurred: " + str(e), 500


@app.route('/get_code')
def get_code():
    return render_template("getcode.html")

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    question = data.get('question')
    # Just echo the question for now
    return jsonify({'solution': f'This is a dummy solution for: {question}'})

# Route for getting a random question
@app.route('/random-question', methods=['GET'])
def random_question():
    generate("0478")
    return send_from_directory("question.png", "image.png")

# Serve past paper files
@app.route('/papers/<filename>')
def download_paper(filename):
    return send_from_directory('papers', filename)
