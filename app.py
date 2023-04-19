from flask import Flask, request, jsonify
import base64
import pytesseract
from langcodes import Language

app = Flask(__name__)


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    return 'OK'

# OCR for single image given as base64 string
@app.route('/ocr/single', methods=['POST'])
def single_ocr():
    data = request.get_json()
    if 'image' not in data:
        return jsonify({'error': 'no image specified'}), 400

    with open("image.png", "wb") as fh:
        fh.write(base64.b64decode(data['image']))

    langs_str = ''
    if 'langs' in data:
        supported_langs = pytesseract.get_languages()
        for lang in data['langs']:
            lang_a3= Language.get(lang).to_alpha3()
            if lang_a3 in supported_langs:
                langs_str += lang_a3 + '+'
    if langs_str == '':
        langs_str = 'eng'

    ocr = pytesseract.image_to_string('image.png', lang=langs_str)
    return ocr.strip().replace('\n', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
