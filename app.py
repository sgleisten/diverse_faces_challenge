from flask import Flask, request, render_template, jsonify
import openai
import os

app = Flask(__name__)

# Get the OpenAI API key from environment variables
openai.api_key = os.getenv('sk-7WRKdAUdse02Cbb7l_FvWug9Wn1BySlhIC-fS_xcm6T3BlbkFJu0UqC9hvgG6qAZat9t1K-fgKcrQlQRmt2phhJS_RIA')

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][4]['url']
    return image_url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.json['prompt']
    image_url = generate_image(prompt)
    return jsonify({'image_url': image_url, 'reflective_question': generate_reflective_question(prompt)})

def generate_reflective_question(prompt):
    questions = [
        "Do the images accurately reflect the diversity within the characteristic or role you requested? Why or why not?",
        "Are there any aspects of diversity that seem to be missing or overrepresented in the generated images?",
        "Do you notice any biases in the images generated? If so, what kind of biases?",
        "How could the AI improve to better represent the requested characteristic or role?",
        "Do the images include a wide range of backgrounds, ages, and other characteristics within the requested group?",
        "How well do these images promote inclusivity and diversity?",
        "How do these images make you feel about the group you requested? Are there any stereotypes being reinforced or challenged?",
        "What are the social implications of the AI generating these particular images?",
        "What ethical considerations should be taken into account when generating and using these images?",
        "How can we ensure that the AI respects the dignity and diversity of all individuals in its image generation?"
    ]
    return questions[4]  # Simplified for demo, can add logic to choose based on prompt

if __name__ == '__main__':
    app.run(debug=True, port=5001)
