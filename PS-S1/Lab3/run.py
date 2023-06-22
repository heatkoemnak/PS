from flask import Flask,render_template,Response
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from num import Num
app = Flask(__name__)

@app.route('/')

def home():
    nm = Num()

    list_data=[1200,1300,2300,3200,3300,3800,4000,4100,4300,4800,5500,5700,5700,5800,6000,6300,6800,6800,6900,7700]
    mean = nm.mean(list_data)
    median = nm.median(list_data)
    return render_template('base.html',list_data=list_data,mean=mean,median=median)
@app.route('/plot.png')
def plot_png():
    list_data=[1200,1300,2300,3200,3300,3800,4000,4100,4300,4800,5500,5700,5700,5800,6000,6300,6800,6800,6900,7700]
    fig = create_figure(list_data)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')
def create_figure(list_data):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.boxplot(list_data)
    axis.set_title("Boxplot")
    axis.set_ylabel("Measurement")
    return fig

    
if __name__ == '__main__':

    app.run(host='localhost',port=5050,debug =True)

        