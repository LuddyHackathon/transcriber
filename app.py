from flask import request
import flask
import os
import sys
import subprocess
os.environ['MPLBACKEND'] = 'Agg'


app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
def transcribe():
    args = request.args
    voice_file = args.get('voice_file')
    transcribed_text = ''

    with open('batch.txt', 'w') as batch:
        batch.write('/voice/'+voice_file+'\n')
    process = subprocess.run(
        [
            "Faster-Whisper-XXL/faster-whisper-xxl",
            "batch.txt",
            "-m", "turbo",
            "--task", "transcribe",
            "--diarize", "reverb_v2",
            "-br",
            "-o", "/voice",
            "-f", "txt", "srt"
        ],
        capture_output=True)
    print(process.stdout, file=sys.stderr)
    with open(f'/voice/{voice_file.split(".")[0]}.txt') as transcribed:
        for line in transcribed.readline():
            transcribed_text += line
    return {"transcribed_text": transcribed_text}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=65535)
