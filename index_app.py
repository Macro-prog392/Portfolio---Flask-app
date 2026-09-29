from flask import Flask, render_template, request 

app = Flask(__name__,template_folder='template')

@app.route('/', methods=['GET','POST'])

def method_name():
    name = "naruto"
    result = 40000
   # return render_template('index.html')
    if request.method == 'POST':
        receipt_name = request.form.get('rname')
        email = request.form.get('rgmail')
        content = request.form.get('content-message')
        
        return f'<h4><u><b>Message</b></u></h6> {receipt_name}, your message has been received \n that is why message has been sent to this email: <p> {email}</p> \n <h4><u><b>Content of Message</b></u></h4> {content}'

@app.route('/<name>', methods=['GET','POST'])

def base_name(name):
    return render_template('base.html')

if __name__ == "__main__":
    app.run(debug = True,host='0.0.0.0')