from flask import Flask,render_template,request
from med import chat_with_chatgpt, extract_text

app = Flask(__name__)

file_path = '/uploaded/'

@app.route('/')
def home():
    return "welcome"

@app.route('/file',methods = ['GET'])
def file():
    return render_template('file.html')

@app.route('/report', methods=['POST'])
def report():
    if 'file' not in request.files:
        return 'No file uploaded.'
    
    file = request.files['file']
    if file :
        up_file = file_path + file.filename
        file.save(up_file)
    
    if file.filename == '':
        return 'No file selected.'

    content = extract_text(up_file)

    prompt = f'''Report : {content}
Convert the report in simple words that patient can understand easily and also mentioned the numeric values  and suggest a medicine from given Report data.'''
    report_data = chat_with_chatgpt(prompt)

    data = report_data.json()
    response_content = data['choices'][0]["message"]["content"]

    return render_template('report.html',response_content=response_content)

if __name__ == '__main__':
    app.run(debug=True)  
