from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib
import pandas as pd
matplotlib.use('Qt5Agg')

class EKGplot(FigureCanvas):
	def __init__(self, parent=None, width=5, height=4, dpi=100):
		fig = Figure(figsize=(width, height), dpi=dpi)
		self.axes = fig.add_subplot(111)
		fig.patch.set_alpha(.5)
		
		super(EKGplot, self).__init__(fig)
		fig.tight_layout()
		
		