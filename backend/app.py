from flask import Flask, Response
import json
from os import listdir
from os.path import isfile, join

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api', methods=['GET'])
def get_all_agreements():
    agreement_path = "./agreements/"
    files = [f for f in listdir(agreement_path) if isfile(join(agreement_path, f))]
    json_objects = []
    for file in files:
        s = open(agreement_path + file, 'r')
        x = {
            "name": file.split('.')[0],
            "agreement": s.read(),
            "accepted": True
        }
        json_objects.append(x)

    return Response(json.dumps(json_objects), mimetype='application/json')


if __name__ == '__main__':
    app.run()

# Supply and store markdown files.
