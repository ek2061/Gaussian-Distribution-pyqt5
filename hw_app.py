# -*- coding: utf-8 -*-
"""
Created on Tue May  5 19:15:54 2020

@author: Yuchi
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QMessageBox, QAction
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap, QIcon, QMovie
from PyQt5 import QtGui
from hw import Ui_MainWindow
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.mlab as mlab
import scipy.stats as stats
from random import choice
import time
from PyQt5.Qt import QThreadPool
from call_k_means import Run_k_means

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
        
        self.ui.pushButton.clicked.connect(self.pushButton_Click)  #隨機參數
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_Click)  #畫圖
        self.ui.pushButton_3.clicked.connect(self.pushButton_3_Click)  #Bays
        self.ui.pushButton_4.clicked.connect(self.pushButton_4_Click)  #K-means
              
        self.show()
    
    def close_mpl(self):
        self.mpl.axes.clear()
#        self.mpl.close()
    
    def pushButton_Click(self):
        random_rounds = np.random.randint(1, 10000)
        random_rounds2 = np.random.randint(1, 10000)
        random_times = np.random.randint(1, 1000)        
        random_threshold = np.random.randint(300, 800)
        random_threshold2 = np.random.randint(300, 800)
        
        self.ui.spinBox.setValue(random_rounds)
        self.ui.spinBox_2.setValue(random_rounds2)
        self.ui.spinBox_3.setValue(random_times)
        self.ui.doubleSpinBox.setValue(random_threshold / 1000.0)
        self.ui.doubleSpinBox_2.setValue(random_threshold2 / 1000.0)
        
    def pushButton_2_Click(self):
        if self.ui.spinBox.value() == 0 \
        or self.ui.spinBox_2.value() == 0 \
        or self.ui.spinBox_3.value() == 0 \
        or self.ui.doubleSpinBox.value() == 0\
        or self.ui.doubleSpinBox_2.value() == 0:
            QMessageBox.about(self, 'Error', 'input parameter plz')
        else:
            self.close_mpl()
            
            rounds1 = self.ui.spinBox.value()
            times1 = self.ui.spinBox_3.value()
            threshold1 = self.ui.doubleSpinBox.value()
            
            toss_coin1 = np.random.rand(rounds1, times1)  #丟第一個硬幣
            toss_coin1[toss_coin1 >= threshold1] = 1
            toss_coin1[toss_coin1 < threshold1] = 0   #小於閥值就是反面
            
            toss_coin1 = 1 - toss_coin1
            
            toss_coin1 = np.sum(toss_coin1, 1)
            
            rounds2 = self.ui.spinBox_2.value()
            times2 = self.ui.spinBox_3.value()
            threshold2 = self.ui.doubleSpinBox_2.value()
            
            toss_coin2 = np.random.rand(rounds2, times2)
            toss_coin2[toss_coin2 >= threshold2] = 1
            toss_coin2[toss_coin2 <  threshold2] = 0
            
            toss_coin2 = 1 - toss_coin2
            
            toss_coin2 = np.sum(toss_coin2, 1)

            #####以下畫直方圖
            
            n1, bins1, patches = self.mpl.axes.hist(toss_coin1, bins = 50, edgecolor = 'black')
            mu = toss_coin1.mean()
            sigma = toss_coin1.std()
            y1 = stats.norm.pdf(range(times1 + 1), mu, sigma)
            max_n1 = np.max(n1)
            max_y1 = np.max(y1)
            factor = max_n1/max_y1
            self.mpl.axes.plot(range(times1 + 1), y1*factor, 'm--', color = 'green', linewidth = 3)
                      
            n2, bins2, patches = self.mpl.axes.hist(toss_coin2, bins = 50, edgecolor = 'black')
            mu = toss_coin2.mean()
            sigma = toss_coin2.std()
            y2 = stats.norm.pdf(range(times2 + 1), mu, sigma)
            max_n2 = np.max(n2)
            max_y2 = np.max(y2)
            factor = max_n2/max_y2  #放大倍數
            self.mpl.axes.plot(range(times2 + 1), y2*factor, 'm--', color = 'red', linewidth = 3)
           
            self.mpl.axes.legend(('Coin1', 'Coin2'), fontsize = 12)
                                   
            self.coin_dict = dict()
            self.coin_dict['times'] = times1
            self.coin_dict['n1'] = n1
            self.coin_dict['bins1'] = bins1
            self.coin_dict['n2'] = n2
            self.coin_dict['bins2'] = bins2
            self.coin_dict['toss_coin1'] = toss_coin1
            self.coin_dict['toss_coin2'] = toss_coin2
            self.coin_dict['y1'] = y1
            self.coin_dict['y2'] = y2
            self.coin_dict['factor'] = factor
            
            self.mpl.draw()
    
    def replot_now(self):  #因為刷新都會把畫布清空，所以我重畫原本的直方圖
        toss_coin1 = self.coin_dict['toss_coin1']
        toss_coin2 = self.coin_dict['toss_coin2']
        y1 = self.coin_dict['y1']
        y2 = self.coin_dict['y2']
        factor = self.coin_dict['factor']
        times = self.coin_dict['times']
        
        n, bins, patches = self.mpl.axes.hist(toss_coin1, bins = 50, edgecolor = 'black')
        n, bins, patches = self.mpl.axes.hist(toss_coin2, bins = 50, edgecolor = 'black')
        
        self.mpl.axes.plot(range(times + 1), y1*factor, 'm--', color = 'green', linewidth = 3)
        self.mpl.axes.plot(range(times + 1), y2*factor, 'm--', color = 'red', linewidth = 3)
        
    
    def pushButton_3_Click(self):
        n1 = self.coin_dict['n1']
        n2 = self.coin_dict['n2']
        bins1 = self.coin_dict['bins1']
        bins2 = self.coin_dict['bins2']
                
        self.close_mpl()
        self.replot_now()
        
        n1_list = n1.tolist()
        n1_max_index = n1_list.index(max(n1))  #柱子最高值
        
        n2_list = n2.tolist()
        n2_max_index = n2_list.index(max(n2))
        
        ans = np.ceil((bins1[n1_max_index] + bins2[n2_max_index])/2)
        
        self.mpl.axes.axvline(x = ans, linewidth = 3, color = 'brown')
        self.mpl.axes.text(ans+2, max(n1), str(ans))
        
        self.mpl.draw()
        
    def pushButton_4_Click(self):
        self.close_mpl()
        self.replot_now()
        
        V1 = self.coin_dict['toss_coin1']
        V2 = self.coin_dict['toss_coin2']
        D = np.hstack((V1, V2))
        D.tolist().sort()
        k1 = choice(D)  #隨機選2個不重複的中心k1, k2
        k2 = choice(D)
        while(k1 == k2):
            k2 = choice(D)
            
        do_k_means = Run_k_means(D, k1, k2)  #把 D, k1, k2 傳入多線程
        do_k_means.res.callback_signal.connect(self.show_k_means_result)  #結果連接後續func
        QThreadPool.globalInstance().start(do_k_means)  #執行多線程
            
    def show_k_means_result(self, msg, new_center1, new_center2):
        n1 = self.coin_dict['n1']
        if msg == 'error':
            QMessageBox.about(self, '執行錯誤')
        else:
            print(msg)
            self.close_mpl()
            self.replot_now()
            
            mid = (new_center1 + new_center2)/2
            
            self.mpl.axes.axvline(x = new_center1, linewidth = 3, color = 'black')
            self.mpl.axes.axvline(x = new_center2, linewidth = 3, color = 'black')
            self.mpl.axes.axvline(x = mid, linewidth = 3, color = 'brown', linestyle="--")
            
            self.mpl.axes.text(new_center1 + 2, max(n1), str(np.round(new_center1, 1)))
            self.mpl.axes.text(new_center2 + 2, max(n1), str(np.round(new_center2, 1)))
            self.mpl.axes.text(mid + 2, max(n1), str(np.round(mid, 1))) 
            self.mpl.draw()
        
        
        
        
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())