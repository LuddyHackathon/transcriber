import os
import tempfile
import flask
from flask import request
import whisper

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def transcribe():
    if request.method == 'POST':
        args = request.args
        voice_file = args.get('voice_file')

        # there are no english models for large
        audio_model = whisper.load_model('small.en')

        save_path = os.path.join('/voice', voice_file)

        result = audio_model.transcribe(save_path, language='english')

        with open('/voice/voice.txt', 'w') as f:
            f.write(result)

        return result['text']
    else:
        return "This endpoint only processes POST wav blob"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65535)