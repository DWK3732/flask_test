from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__) 

@app.route('/')
#@app.route('/<int:num>')
def inputTest(num=None):
    return render_template('main.html', num=num)

@app.route('/<string:k>')
def insputTest(k=None):
    return render_template('main.html', k=k)

@app.route('/calculate',methods=['POST'])
def calculate(k=None):
    if request.method == 'POST':
        temp = request.form['k']
    else:
        temp = None
    return redirect(url_for('insputTest',k=temp))

if __name__ == '__main__':
    app.run()