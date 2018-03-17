from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('user_name', '三上')
    return render_template('hello.html', title='flask test', name=name)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True)