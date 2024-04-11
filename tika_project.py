from flask import Flask, request, jsonify
from tika import parser

app = Flask(__name__)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    # Verifica se um arquivo foi enviado na solicitação
    if 'file' not in request.files:
        return jsonify({'error': 'Nenhum arquivo enviado'}), 400

    file = request.files['file']

    # Extrai texto do arquivo usando o Apache Tika
    raw_text = parser.from_buffer(file).get('content')

    return jsonify({'text': raw_text})

if __name__ == '__main__':
    app.run(debug=True)
