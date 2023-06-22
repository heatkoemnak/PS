from flask import Flask,render_template


from num import Num
app = Flask(__name__)

@app.route('/')

def home():
    nm = Num()

    list_data=[1200,1300,2300,3200,3300,3800,4000,4100,4300,4800,5500,5700,5700,5800,6000,6300,6800,6800,6900,7700]
    mean = nm.mean(list_data)
    median = nm.median(list_data)
    return render_template('base.html',list_data=list_data,mean=mean,median=median)
if __name__ == '__main__':

    app.run(host='localhost',port=5050,debug =True)
        