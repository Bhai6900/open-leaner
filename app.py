from flask import Flask, render_template, request,jsonify
app= Flask(__name__)
JOBS =[ 
  {
  'id': 1,
  'title': 'Data analyst',
  'location': 'Bengaluru, India',
  'salary': 'Rs. 10,00,000'},
  {
  'id': 2,
  'title': 'Data scientist',
  'location': 'delhi, India',
  'salary': 'Rs. 12,00,000'},
  {
  'id': 3,
  'title': 'frontend engineer',
  'location': 'San Francisco,USA',
  'salary': 'USD. 1,00,000'},
  {
  'id': 4,
  'title': 'backend engineer',
  'location': 'Remote',
 
   },

    
    
]
@app.route('/')
def hello_world():

  return render_template('hello.html', jobs=JOBS, company_name="OPEN LEARNER")
  
@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == '__main__':
  app.run(host='0.0.0',debug=True)