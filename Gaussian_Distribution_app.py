# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:23:51 2020

@author: Yuchi
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QMessageBox, QAction
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5 import QtGui
from Gaussian_Distribution import Ui_MainWindow
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.mlab as mlab
import scipy.stats as stats

class MyFigure(FigureCanvas):
    def __init__(self,parent=None,width = 5, height = 4, dpi = 100):
        self.fig = Figure(figsize = (width, height), dpi = dpi)
        self.axes = self.fig.add_subplot(111)
        self.axes.hold(True)
        FigureCanvas.__init__(self,self.fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(self,QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class AppWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.mpl = MyFigure(self,width = 4, height = 5, dpi = 100)
        
        self.ui.verticalLayout.addWidget(self.mpl)
        
        self.ui.pushButton.clicked.connect(self.pushButton_Click)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_Click)
        
        self.ui.horizontalSlider.valueChanged.connect(self.SetSliderValue)
        self.ui.horizontalSlider_2.valueChanged.connect(self.SetSliderValue)
        self.ui.horizontalSlider_3.valueChanged.connect(self.SetSliderValue)
        self.ui.horizontalSlider_4.valueChanged.connect(self.SetSliderValue)
        self.ui.horizontalSlider_5.valueChanged.connect(self.SetSliderValue)
        self.ui.horizontalSlider_6.valueChanged.connect(self.SetSliderValue)
              
        self.show()
    
    def close_mpl(self):
        self.mpl.axes.clear()
        self.mpl.close()
    
    def pushButton_Click(self):
        random_rounds1 = np.random.randint(1, 10000)
        random_rounds2 = np.random.randint(1, 10000)
        self.ui.horizontalSlider.setValue(random_rounds1)
        self.ui.horizontalSlider_4.setValue(random_rounds2)
        
        random_times = np.random.randint(1, 1000)
        self.ui.horizontalSlider_2.setValue(random_times)
        self.ui.horizontalSlider_5.setValue(random_times)
        
        random_threshold = np.random.randint(300, 800)
        random_threshold2 = np.random.randint(300, 800)
        self.ui.horizontalSlider_3.setValue(random_threshold)
        self.ui.horizontalSlider_6.setValue(random_threshold2)
    
    def SetSliderValue(self, value):
        self.ui.spinBox.setValue(self.ui.horizontalSlider.value())
        self.ui.spinBox_2.setValue(self.ui.horizontalSlider_2.value())
        self.ui.doubleSpinBox.setValue(self.ui.horizontalSlider_3.value() / 1000.0)
        
        self.ui.spinBox_3.setValue(self.ui.horizontalSlider_4.value())
        self.ui.spinBox_4.setValue(self.ui.horizontalSlider_5.value())
        self.ui.doubleSpinBox_2.setValue(self.ui.horizontalSlider_6.value() / 1000.0)
        
    def pushButton_2_Click(self):
        if self.ui.spinBox.value() == 0 \
        or self.ui.spinBox_2.value() == 0 \
        or self.ui.spinBox_3.value() == 0 \
        or self.ui.spinBox_4.value() == 0 \
        or self.ui.doubleSpinBox.value() == 0\
        or self.ui.doubleSpinBox_2.value() == 0:
            QMessageBox.about(self, 'Error', 'input parameter plz')
        else:
            self.close_mpl()
            
            rounds1 = self.ui.spinBox.value()
            times1 = self.ui.spinBox_2.value()
            threshold1 = self.ui.doubleSpinBox.value()
            
            toss_coin1 = np.random.rand(rounds1, times1)  #丟第一個硬幣
            toss_coin1[toss_coin1 >= threshold1] = 1
            toss_coin1[toss_coin1 < threshold1] = 0   #小於閥值就是反面
            
            toss_coin1 = 1 - toss_coin1
            
            toss_coin1 = np.sum(toss_coin1, 1)
            
            rounds2 = self.ui.spinBox_3.value()
            times2 = self.ui.spinBox_4.value()
            threshold2 = self.ui.doubleSpinBox_2.value()
            
            toss_coin2 = np.random.rand(rounds2, times2)
            toss_coin2[toss_coin2 >= threshold2] = 1
            toss_coin2[toss_coin2 <  threshold2] = 0
            
            toss_coin2 = 1 - toss_coin2
            
            toss_coin2 = np.sum(toss_coin2, 1)

            self.mpl = MyFigure(self, width = 4, height = 5, dpi = 100)
            
            
#            hist_val1 = np.zeros(times1 + 1)
#            
#            for i in range(toss_coin1.shape[0]):
#                hist_val1[np.int(toss_coin1[i])] = hist_val1[np.int(toss_coin1[i])] + 1
#            
#            hist_index1 = np.argwhere(hist_val1 > 0)
#            hist_val1 = hist_val1[np.int(hist_index1[0]):np.int(hist_index1[-1])+1]
#            
#            hist_val2 = np.zeros(times2 + 1)
#            
#            for i in range(toss_coin2.shape[0]):
#                hist_val2[np.int(toss_coin2[i])] = hist_val2[np.int(toss_coin2[i])] + 1
#            
#            hist_index2 = np.argwhere(hist_val2 > 0)
#            hist_val2 = hist_val2[np.int(hist_index2[0]):np.int(hist_index2[-1])+1]                     
            
            n, bins, patches = self.mpl.axes.hist(toss_coin1, bins = 30, edgecolor = 'black')
            mu = toss_coin1.mean()
            sigma = toss_coin1.std()
            y = stats.norm.pdf(bins, mu, sigma)
            max_n = np.max(n)
            max_y = np.max(y)
            self.mpl.axes.plot(bins, y*(max_n/max_y), 'm--', color = 'green', linewidth = 3)
                      
            n, bins, patches = self.mpl.axes.hist(toss_coin2, bins = 30, edgecolor = 'black')
            mu = toss_coin2.mean()
            sigma = toss_coin2.std()
            y = stats.norm.pdf(bins, mu, sigma)
            max_n = np.max(n)
            max_y = np.max(y)
            self.mpl.axes.plot(bins, y*(max_n/max_y), 'm--', color = 'red', linewidth = 3)
           
            self.mpl.axes.legend(('Coin1', 'Coin2'), fontsize = 12)
            self.ui.verticalLayout.addWidget(self.mpl)
                             
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())