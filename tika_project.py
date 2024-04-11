from flask import Flask, request, jsonify
from flask_cors import CORS
from tika import parser

app = Flask(__name__)
CORS(app)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Nenhum arquivo selecionado'}), 400

    try:
        parsed = parser.from_buffer(file.read())
        text = parsed['content']
        return jsonify({'text': text}), 200
    except Exception as e:
        print('Erro ao extrair texto:', e)
        return jsonify({'error': 'Erro ao extrair texto do arquivo'}), 500

if __name__ == '__main__':
    app.run(debug=True)
