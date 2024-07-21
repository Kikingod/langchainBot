import asyncio
from flask import Flask, request, render_template
from help import ai  # Adjust this import based on your LangChain setup

app = Flask(__name__)


async def get_response(question):
    return await asyncio.to_thread(ai, question)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods = ['GET', 'POST'])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    return ai(input)

if __name__ == '__main__':
    app.run(debug=True)
