from flask import Flask, render_template ,jsonify
from database import engine
from sqlalchemy import text


app=Flask(__name__)
Expertise=[
  {
    'id':1,
    'title':'Data Analyst',
    'language':'Python',
    'Packages':'Matplotlib, Pandas'
   },
  {
    'id':2,
    'title':'Machine Learning',
    'language':'Python',
    'Packages':'Scikit-learn, Pandas'
   },
  {
    'id':3,
    'title':'Deep Learning',
    'language':'Python',
    'Packages':'Pytorch, Pandas'
   },
{
    'id':4,
    'title':'Dashboard Designing',
    'language':'DAX',
    'Packages':'Powerbi'
   }
]

def load_from_database():
  with engine.connect() as conn:
   result=conn.execute(text("select * from exp"))
   result_all=result.all()
  #exp=[]
  d1=dict(enumerate(result_all))
  return d1


@app.route("/")
def hello_world():
  return render_template('home.html',
                          exp=d1,
                          page_name='Portfolio')
@app.route("/api/expertise")
def list_expertise():
  return jsonify(Expertise)
if __name__ =="__main__":
  app.run(host='0.0.0.0',debug=True)
