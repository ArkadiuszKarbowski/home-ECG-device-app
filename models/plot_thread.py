from PyQt5 import QtCore

class PlotThread(QtCore.QThread):
    def __init__(self, parent):
        super(PlotThread, self).__init__(parent)

    def run(self):
        while True:
            self.counter += 1
            if self.counter % 2 == 0:
                self.stop()
            
            self.parent().updatePlot()
            self.msleep(200)
            
            