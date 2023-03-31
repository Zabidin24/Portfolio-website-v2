from flask import Flask, render_template ,jsonify
from database import engine
from sqlalchemy import text


app=Flask(__name__)


def load_from_database():
  with engine.connect() as conn:
   result=conn.execute(text("select * from exp"))
   result_all=result.all()
   exp=[]
   d1=dict(enumerate((result_all)))
   exp.append(d1)
   return exp


@app.route("/")
def hello_world():
  exp=load_from_database()
  return render_template('home.html',
                          exp=exp,
                          page_name='Portfolio')
@app.route("/api/expertise")
def list_expertise():
  return jsonify(Expertise)
if __name__ =="__main__":
  app.run(host='0.0.0.0',debug=True)
