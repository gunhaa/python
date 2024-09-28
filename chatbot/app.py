from flask import Flask, render_template,jsonify,request
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import redis


GOOGLE_API_KEY="AIzaSyD-4TZyQsJgNA8hIvQKEOOG5bVlpKzZHws"

r = redis.StrictRedis(
    host='localhost',
    port=6379,
    db=0,
    password='1234',
    decode_responses=True
)

def langChain():
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

    data = request.get_json()
    chat = data.get('chat', 'error')
    
    result = model.generate_content(chat)
    
    return result

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('main.html')

@app.route("/question", methods=["POST"])
def question():
    
    response = langChain()

    generated_text = response.text
    
    print(generated_text)
    
    return jsonify({'text': generated_text})

if __name__ == '__main__':
    app.run(debug=True)