from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {
    "id": 1,
    "title": "Software Engineer",
    "location": "Lahore",
    "salery": ""
  },
  {
    "id": 2,
    "title": "WebDeveloper",
    "location": "India",
    "salery": "RS 3000000"
  },
  {
    "id": 3,
    "title": "Data Scientists",
    "location": "USA",
    "salery": "USD 200000"
  },
  {
    "id": 4,
    "title": "Human Resources",
    "location": "Lahore",
    "salery": "Rs 150000"
  },
  {
    "id": 5,
    "title": "Backend Developer",
    "location": "UAE",
    "salery": "AED 200000"
  },
]


@app.route("/")
def hello_world():
  return render_template('home.html', data=JOBS, company="Usman")


@app.route('/api/jobs')
def list_job():
  return jsonify(JOBS)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
