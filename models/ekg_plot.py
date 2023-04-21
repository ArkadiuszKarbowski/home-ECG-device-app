from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
from cycler import cycler
matplotlib.use('Qt5Agg')

class EKGplot(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		super(EKGplot, self).__init__(fig)
		fig.tight_layout()
		fig.set(facecolor=None)
		fig.set_alpha(0)
		
		self.setWindowOpacity(1.0)
		self.setStyleSheet("border-image: none;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-radius:15px;")