from flask import Flask, render_template, jsonify


app=Flask(__name__)

Expertise=[
{
  'id': 1,
  'title': 'Data Analysis',
  'language': 'python',
  'Packages': 'Pandas, NumPy'
  },
{
  'id': 2,
  'title': 'Machine Learning',
  'language': 'python',
  'Packages': 'Pandas, Scikit-learn'
  },
{
  'id': 3,
  'title': 'Deep Learning',
  'language': 'python',
  'Packages': 'Pandas, Pytorch'
  },
{
  'id': 4,
  'title': 'Dashboard Designing',
  'language': 'DAX, Data modeling',
  'Application': 'PowerBI'
  }


  
]


@app.route("/")
def hello_world():
  return render_template('home.html',
                         exp=Expertise, 
                        page_name="portfolio")
@app.route("/api/expertise")
def list_jobs():
  return jsonify(Expertise)
  
if __name__ =="__main__":
  app.run(host='0.0.0.0',debug=True)
