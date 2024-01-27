# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)




# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# @app.route('/about')
# def about():
#     return 'This is the about page.'

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'

# class MyForm(FlaskForm):
#     name = StringField('Name')
#     submit = SubmitField('Submit')

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     form = MyForm()
#     if form.validate_on_submit():
#         return f'Hello, {form.name.data}!'
#     return render_template('form.html', form=form)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class MyForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')

@app.route('/form', methods=['GET', 'POST'])
def form():
    form = MyForm()
    if form.validate_on_submit():
        return f'Hello, {form.name.data}!'
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
