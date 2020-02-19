from flask import Flask
# from . import pizza

app = Flask(__name__)
@app.route('/')

def hello_world():
    return "Hello World!!! you owe me money!!!\n Pay what you owe"

@app.route('/home', defaults={'name':'Stranger'})
@app.route('/home/<string:name>')
def home(name):
    html = f"<h1 style= 'color :goldenrod;'> Welcome Home {name} </h1>"
    return html

@app.route('/user_info', methods=['GET'])
def get_info():
    age = request.args.get('age')




if __name__ == '__main__':
    app.run()