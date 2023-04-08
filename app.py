from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('webpage.html')

@app.route('/my-link/')
def my_link():
  print('I got clicked!')

  return render_template('theYPage.html')



if __name__ == '__main__':
    app.run(debug=True)