import csv
from flask import Flask, render_template, send_from_directory, request, redirect
app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
	return render_template ('index.html')

@app.route('/<string:page_name>')
def page(page_name=None):
	return render_template(page_name)

def write_to_file(data):
	with open('database.txt',mode = 'a') as database:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		file = database.write(f'\n{name},{email},{subject},{message}')
		
def write_to_csv(data):
	with open('database.csv', mode = 'a',newline = '\n') as database2:
		name = data["name"]
		email = data["email"]
		subject = data["subject"]
		message = data["message"]
		csv_file = csv.writer(database2,delimiter = ',',quotechar = ' ', quoting = csv.QUOTE_MINIMAL)
		csv_file.writerow([name,email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		data = request.form.to_dict()
		write_to_csv(data)
		return redirect('/thanks.html#contact')
	else:
		return 'Something went wrong,please try again.'

