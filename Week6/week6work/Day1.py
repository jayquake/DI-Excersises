from flask import Flask
from flask import render_template
from datetime import *
# Flask
app = Flask(__name__)
class Resume:
    def __init__(self,name,age,job, history):
        self.name = name
        self.age = age
        self.job = job
        self.history = history
jason =Resume('Jason Quaicoo',30, '''After nine days I let the horse run free
'Cause the desert had turned to sea
There were plants and birds and rocks and things
there was sand and hills and rings
The ocean is a desert with it's life underground
And a perfect disguise above
Under the cities lies a heart made of ground
But the humans will give no love''',['On the first part of the journey' ,'I was looking at all the life' ,
'There were plants and birds and rocks and things',
'There was sand and hills and rings',
'The first thing I met was a fly with a buzz',
'And the sky with no clouds',
'The heat was hot and the ground was dry',
'But the air was full of sound'])

item_list = jason.history
@app.route('/')
def today():
    today = date.today()
    return str(today)

@app.route('/CV')
def cv():
    html = """<h1> {} , {} </h1>
    <h2> Accolades </h2>
    <p>{}</p>
    <ul>
    {% for item in {} %}
      <li> {} </li>

    </ul>
""".format(jason.name, jason.age, jason.job, item_list)
    return html
if __name__ == '__main__':

    app.run()
