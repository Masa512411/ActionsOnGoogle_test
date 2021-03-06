import json

import os 

from flask import Flask
from flask import request
from flask import jsonify
from flask import make_response

import random

app = Flask(__name__)

@app.route("/webhook",methods=['POST'])
def webhook():
    req = request.get_json()
    novels = req["result"]["parameters"]["novels"]
    quotations = json.load(open("quotations.json",encoding="utf-8_sig"))

    if novels == "羊をめぐる冒険":
        speech = random.choice(list(quotations.get("羊をめぐる冒険").values()))
    elif novels == "風の歌を聴け":
        speech = random.choice(list(quotations.get("風の歌を聴け").values())) 
    elif novels == "ダンスダンスダンス":
        speech = random.choice(list(quotations.get("ダンスダンスダンス").values()))
    elif novels == "ノルウェイの森":
        speech = random.choice(list(quotations.get("ノルウェイの森").values()))
    elif novels == "ねじ巻き鳥クロニクル":
        speech = random.choice(list(quotations.get("ねじ巻き鳥").values()))
    elif novels == "世界の終わりとハードボイルドワンダーランド":
        speech = random.choice(list(quotations.get("セカオワ").values()))

    res = make_response(jsonify({'speech':speech,'displayText':speech}))
    res.headers['Content-Type'] = 'application/json'    
    return res


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
