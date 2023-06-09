from flask import Flask, render_template
app = Flask(__name__)
import source

@app.route('/')
def index():
  return render_template('webpage.html')

@app.route('/yahentamitsi')
def loadYahetamitsi():
  percentage = source.get_busyness_percentage("Yahentamitsi", 1000)
  return render_template('theYPage.html', percentage = percentage)

@app.route('/251north')
def load251North():
  percentage = source.get_busyness_percentage("251North", 500)
  return render_template('theNPage.html', percentage = percentage)

@app.route('/south')
def loadSouth():
  percentage = source.get_busyness_percentage("South", 1000)
  return render_template('theSPage.html', percentage = percentage)

if __name__ == '__main__':
    app.run(debug=True)