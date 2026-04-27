from  flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def home():
    #connect to db , fetch data and pass it to the template
    return render_template('home.html', name='John Doe')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/submit', methods=['POST'])
def process_form_data():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    return f"Received data - Name: {name}, Email: {email}, Message: {message}"  
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000   , debug=True)    