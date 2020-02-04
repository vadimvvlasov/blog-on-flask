# View - template: отвечает за отображение пользователю данных
from app import app
from flask import render_template

@app.route('/')
def index():
    name = 'There'
    return render_template('index.html', n=name)
