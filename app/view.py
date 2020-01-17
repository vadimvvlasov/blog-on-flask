# View - template: отвечает за отображение пользователю данных
from app import app
from flask import render_template

@app.route('/')
def index():
    name = '[0.7:1,5] mm'
    return render_template('index.html', n=name)
