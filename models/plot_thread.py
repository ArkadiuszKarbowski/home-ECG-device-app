from PyQt5 import QtCore

class PlotThread(QtCore.QThread):
    def __init__(self, parent):
        super(PlotThread, self).__init__(parent)

    def run(self):
        while True:
                        
            self.parent().updatePlot()
            self.msleep(200)
            
            