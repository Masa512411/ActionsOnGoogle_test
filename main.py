import json

import os 

from flask import Flask
from flask import request
from flask import jsonify

import ramdom

app = Flask(__name__)

@app.route("/webhook",methods=['POST'])
def webhook():
    req = request.get_json()
    novels = req["parameters"]["novels"]
    quotations = json.load(open("quotations.json",encoding="utf-8_sig"))

    if novels == "羊をめぐる冒険":
        speech = random.choice(quotations.get("羊をめぐる冒険"))
    else if novels == "風の歌を聞け":
        speech = random.choice(quotations.get("風の歌を聴け")) 
    else if novels == "ダンスダンスダンス":
        speech = random.choice(quotations.get("ダンスダンスダンス")) 
    else if novels == "ノルウェイの森":
        speech = random.choice(quotations.get("ノルウェイの森")) 
    else if novels == "ねじ巻き鳥クロニクル":
        speech = random.choice(quotations.get("ねじ巻き鳥")) 
    else if novels == "世界の終わりとハードボイルドワンダーランド":
        speech = random.choice(quotations.get("セカオワ"))

     req["result"]["fulfillment"]["speech"] = speech

     return jsonify(req)
        
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)
    app.run(debug=False,port=port,host='0.0.0.0')
