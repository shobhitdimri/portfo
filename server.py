from flask import Flask, render_template,request,redirect
import csv
app = Flask(__name__)
print(__name__)

@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/works.html')
def works():
    return render_template('works.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/work.html')
def work():
    return render_template('work.html')

@app.route('/thank you.html')
def thank():
    return render_template('thank you.html')

def write_to_file(data):
    with open('database.txt', mode='a') as database:
       email =data["email"]
       subject =data["subject"]
       file=database.write('\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',mode='a',newline='') as database2:
       email=data["email"]
       subject=data["subject"]
       message=data["message"]
       csv_writer=csv.writer(database2,  quotechar='"', quoting=csv.QUOTE_MINIMAL)
       csv_writer.writerow([email,subject,message])



@app.route('/Submit_form', methods=['POST', 'GET'])
def Submit_form():
    if request.method=='POST':
        try:
         data=request.form.to_dict()
         write_to_csv(data)
         return redirect('/thank you.html')
        except:
            return'not saved on database'
    else:
        return  'something went wrong!'
