from homework_app import app

from flask import render_template,request

from homework_app.forms import UserInfoForm



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = UserInfoForm()
    if request.method == 'POST' and form.validate():
        name = form.name.data 
        phone_number = form.phone_number.data
        email = form.email.data
        password = form.password.data
    
        print(name,phone_number,email,password)

    return render_template('register.html',user_form = form)