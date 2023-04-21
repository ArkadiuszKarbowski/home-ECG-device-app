from PyQt5 import QtCore, QtGui, QtWidgets
from models.ekg_reader import EkgReader
from models.worker import Worker
from models.ekg_plot import EKGplot
from PyQt5 import uic
import queue
import numpy as np
import matplotlib.ticker as ticker
import matplotlib

matplotlib.use('Qt5Agg')

class EkgApp(QtWidgets.QMainWindow):
    
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('ekg_app_front.ui', self)
        self.setFixedSize(self.size())
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("static/background_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.threadpool = QtCore.QThreadPool()

        self.canvas = EKGplot(self, width=4, height=3, dpi=100)
        self.ui.gridLayout.addWidget(self.canvas, 3, 1, 1, 3)
        self.reference_plot = None
        self.q = queue.Queue(maxsize=20)

        self.plotdata = np.zeros((1,200))
        self.ekg_reader = EkgReader(self)

        self.interval = 30 

        
        self.update_plot()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(self.interval) #msec
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()
        self.start_worker()
    
    def update_plot(self):
        try:
            data=[0]
            
            while True:
                try: 
                    data = self.q.get_nowait()
                except queue.Empty:
                    break
                shift = len(data)
                self.plotdata = np.roll(self.plotdata, -shift,axis = 0)
                self.plotdata[-shift:,:] = data
                self.ydata = self.plotdata[:]
                self.canvas.axes.set_facecolor((0,0,0))
                
        
                if self.reference_plot is None:
                    plot_refs = self.canvas.axes.plot( self.ydata, color=(0,1,0.29))
                    self.reference_plot = plot_refs[0]				
                else:
                    self.reference_plot.set_ydata(self.ydata)

            
            self.canvas.axes.yaxis.grid(True,linestyle='--')
            start, end = self.canvas.axes.get_ylim()
            self.canvas.axes.yaxis.set_ticks(np.arange(start, end, 0.1))
            self.canvas.axes.yaxis.set_major_formatter(ticker.FormatStrFormatter('%0.1f'))
            self.canvas.axes.set_ylim( ymin=-0.5, ymax=0.5)		
            self.canvas.draw()
        except:
            pass
    def start_worker(self):
        worker = Worker(self.ekg_reader.read)
        self.threadpool.start(worker)
    
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = EkgApp()
    mainWindow.show()
    sys.exit(app.exec_())