import matplotlib as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.ticker as ticker
import ekg_app_window

class EkgDisplay(FigureCanvas):
  
    def __init__(self):
        self.buffer = []  # bufor na dane EKG


    def receive_data(self, data):
        self.buffer.append(data)  # Dodaj dane do bufora
        

    def display_data(self):
       pass
          # Przykładowe wyjście, można dostosować do swoich potrzeb

   