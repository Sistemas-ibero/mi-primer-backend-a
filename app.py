from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

usuario = {
    'email': 'ejemplo@gmail.com',
    'password': '123456'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/success', methods=['POST'])
def success():
    email = request.form['email']
    password = request.form['password']
    print(email, password)
    if email == usuario['email'] and password == usuario['password']:
        return render_template('success.html')
    else:
        print("Llegale >:(")
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)