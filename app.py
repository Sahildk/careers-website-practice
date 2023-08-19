from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analyst',
        'location': 'Bengluru, India',
        'salary': '10,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location': 'Delhi, India',
        'salary': '15,00,000'
    },
    {
        'id':3,
        'title':'Front-end Engineer',
        'location': 'Remote',
        'salary': '12,00,000'
    },
    {
        'id':4,
        'title':'Back-end Engineer',
        'location': 'San Francisco, USA',
        'salary': '$12500'
    }
]

@app.route("/")
def hello_world():
    return render_template('home.html',jobs=JOBS, company_name="Career's")

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug= True)