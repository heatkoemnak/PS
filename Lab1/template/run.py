from flask import Flask ,render_template
app = Flask(__name__)
def home():
    return render_template('m5.html')
if __name__ =='__main__':
    app.run('localhost',port=5050)



