from flask import Flask, render_template, jsonify
 

from data import generate_jobs
 


 

app = Flask(__name__)
 

jobs = generate_jobs(20)  # Generate 20 jobs
 


 

@app.route('/')
 

def job_listings():
 

    return render_template('jobs.html', jobs=jobs)
 


 

@app.route('/api/jobs')
 

def api_jobs():
 

    return jsonify({"jobs": jobs})
 


 

if __name__ == '__main__':
 

    app.run(port=5002, debug=True)