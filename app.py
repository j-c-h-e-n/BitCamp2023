from flask import Flask, render_template
app = Flask(__name__)
import populartimes

@app.route('/')
def index():
  return render_template('webpage.html')

@app.route('/yahentamitsi')
def loadYahetamitsi():
  print("in yahentamitsi")
  return render_template('theYPage.html')

@app.route('/251north')
def load251North():
  return render_template('theNPage.html')

@app.route('/south')
def loadSouth():
  return render_template('theSPage.html')

if __name__ == '__main__':
    app.run(debug=True)