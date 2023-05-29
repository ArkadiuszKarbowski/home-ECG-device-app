from PyQt5 import QtCore, QtGui, QtWidgets
from models.ekg_reader import EkgReader
from models.worker import Worker
from models.ekg_plot import EKGplot
import queue
import pandas as pd
import matplotlib
from glowing_buttons.custom_buttons import *
from ekg_app_gui import *
from models.plot_thread import PlotThread
matplotlib.use('Qt5Agg')

class EkgApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_EKGApp()
        self.ui.setupUi(self)
        self.setFixedSize(self.size())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/background_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.threadpool = QtCore.QThreadPool()

        self.canvas = EKGplot(self, width=4, height=3, dpi=100)
        self.canvas.setStyleSheet("background-color: transparent;")
        self.ui.gridLayout.addWidget(self.canvas, 3, 0, 1, 3)
        self.reference_plot = None
        self.q = queue.Queue(maxsize=20)
        
        self.ui.ekg_button.setObjectTheme(13)
        self.ui.spo2_button.setObjectTheme(3)
        self.ui.ekg_button.clicked.connect(self.ekg_btn_clicked)
          
        self.initializePlot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(100) #msec
        self.timer.timeout.connect(self.updatePlot)
        # self.start_workers()
        # self.ekg_reader = EkgReader(self)


    def initializePlot(self):
        self.canvas.axes.clear()
        self.canvas.axes.set_xlabel('Sample')
        self.canvas.axes.set_ylabel('Data')
        self.canvas.axes.set_facecolor((1, 1, 1, 0.1))
        self.canvas.axes.legend(loc='upper left')
        self.canvas.show()

    def updatePlot(self):
        data = pd.read_csv('data.csv')

        if len(data) >= 200:
            data = data.tail(200)  # Wybieramy ostatnie 200 próbek

        x = data['sample']
        y = data['data']
        
        self.canvas.axes.clear()
        self.canvas.axes.plot(x, y, label='Ekg signal')
        self.canvas.draw()
        self.canvas.show()

    def start_plot(self):
        plot_thread = PlotThread(self)
        plot_thread.start()
        
    
    
    def ekg_btn_clicked(self):
        self.start_plot()
        self.ekg_reader = EkgReader(self)
        self.start_workers()
        
    def start_workers(self):
        saver = Worker(self.ekg_reader.save_to_csv, 'data.csv')
        reader = Worker(self.ekg_reader.read)

        self.threadpool.start(reader)
        self.threadpool.start(saver)
        
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = EkgApp()
    mainWindow.show()
    sys.exit(app.exec_())