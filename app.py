import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'LazyDeveloper'

os.system("git clone https://omkaranvekargaming-code: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@github.com/omkaranvekargaming-code/Moviekingzbot okk && cd okk && pip3 install -U -r requirements.txt && nohup python3 bot.py &")

