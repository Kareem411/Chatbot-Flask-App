from flask import Flask, render_template, request

app = Flask(__name__)

# Chatbot function
def get_chatbot_response(message):
    # Your chatbot code here
    return "Chatbot response for: " + message

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Chatbot page
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.form['user_message']
    chatbot_response = get_chatbot_response(user_message)
    return render_template('chatbot.html', user_message=user_message, chatbot_response=chatbot_response)

if __name__ == '__main__':
    app.run(debug=True)