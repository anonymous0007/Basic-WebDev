from flask import Flask, render_template

app = Flask(__name__)  

JOBS = [
  {
    'id':1,
    'title':'Spoofing',
    'price':'50$'
  },
  {
    'id':2,
    'title':'Carding',
    'price':'70$'
  },
  {
    'id':3,
    'title':'Hijacking',
    'price':'410$'
  },
  {
    'id':4,
    'title':'Data-recovery',
    'price':'200$'
  }
]

@app.route("/")
def home():
  return render_template('home.html', jobs=JOBS)
    

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)