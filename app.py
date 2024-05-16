from flask import Flask, render_template, request, jsonify
import spacy

app = Flask(__name__)

# Load your trained model
model_path = r"C:\Users\User\OneDrive\Desktop\NER\trained_model"
try:
    nlp = spacy.load(model_path)
except Exception as e:
    app.logger.error(f"Error loading model: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    try:
        input_text = request.json['inputText']

        # Process the input text using your trained model
        doc = nlp(input_text)

        # Extract skills recognized by the model
        skills = []
        for ent in doc.ents:
            if ent.label_ == "SKILL":
                skills.append(ent.text)

        return jsonify({'skills': skills})
    except Exception as e:
        app.logger.error(f"Error performing NER: {e}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
