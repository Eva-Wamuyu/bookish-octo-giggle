from flask import Flask
import json

app = Flask(__name__)



@app.route('/api/wamuyu',methods = ['GET'])
def endpoint():
    data = {
        "slackUsername": "rutheve.eva",
        "backend": True,
        "age": 22,
        "bio": "Backend dev,Game dev,skater and biker peng"
        }
    data_as_json = json.dumps(data)
    return data_as_json


if __name__ == '__main__':
    app.run()
