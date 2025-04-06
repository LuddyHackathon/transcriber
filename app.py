from flask import request
import flask
import os
import subprocess
os.environ['MPLBACKEND'] = 'Agg'


app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def transcribe():
    args = request.args
    voice_file = args.get('voice_file')

    with open('batch.txt', 'w') as batch:
        batch.write(voice_file+'\n')
    subprocess.run([
        "Faster-Whisper-XXL/faster-whisper-xxl",
        "batch.txt",
        "-m", "turbo",
        "--task", "transcribe",
        "--diarize", "reverb_v2",
        "-br",
        "-o", "Transcripts",
        "-f", "txt", "srt"
    ])
