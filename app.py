from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('html1.html')

if __name__ =='__main':
    app.debug = True
    app.run()
