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
from PyQt5.Qt import QThreadPool
from call_k_means import Run_k_means
from sklearn import metrics

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
        self.fig_roc = MyFigure(self,width = 4, height = 5, dpi = 100)
        
        self.ui.verticalLayout.addWidget(self.mpl)
        self.ui.verticalLayout_2.addWidget(self.fig_roc)
        
        self.ui.pushButton.clicked.connect(self.pushButton_Click)  #隨機參數
        self.ui.pushButton_2.clicked.connect(self.pushButton_2_Click)  #畫圖
        self.ui.pushButton_3.clicked.connect(self.pushButton_3_Click)  #Bayes
        self.ui.pushButton_4.clicked.connect(self.pushButton_4_Click)  #K-means
        self.ui.checkBox.stateChanged.connect(self.checkBoxChangedAction)  #是否使用第3顆硬幣
        
        self.coin_dict = dict()
        self.coin_dict['toss_coin3'] = np.zeros(101)
        self.coin_dict['toss_coin3_count'] = np.zeros(101)
              
        self.show()
        
    def checkBoxChangedAction(self):  #是否使用第3顆硬幣
        if self.ui.checkBox.isChecked() == False:
            self.coin_dict['toss_coin3'] = np.zeros(101)
            self.coin_dict['toss_coin3_count'] = np.zeros(101)
    
    def close_mpl(self):
        self.mpl.axes.clear()
    
    def close_fig_roc(self):
        self.fig_roc.axes.clear()
    
    def pushButton_Click(self):  #random數據
        random_rounds = np.random.randint(1, 10000)
        random_rounds2 = np.random.randint(1, 10000)
        random_times = np.random.randint(1, 1000)        
        random_threshold = np.random.randint(300, 800)
        random_threshold2 = np.random.randint(300, 800)
        
        self.ui.spinBox.setValue(random_rounds)
        self.ui.spinBox_2.setValue(random_rounds2)
        self.ui.spinBox_4.setValue(random_times)
        self.ui.doubleSpinBox.setValue(random_threshold / 1000.0)
        self.ui.doubleSpinBox_2.setValue(random_threshold2 / 1000.0)
        
        if self.ui.checkBox.isChecked():
            random_rounds3 = np.random.randint(1, 10000)
            random_threshold3 = np.random.randint(300, 800)
            
            self.ui.spinBox_3.setValue(random_rounds3)
            self.ui.doubleSpinBox_3.setValue(random_threshold3 / 1000.0)
    
    def throw_coin(self, rounds, times, threshold):  #丟硬幣
        toss_coin = np.random.rand(rounds, times)
        toss_coin[toss_coin >= threshold] = 1
        toss_coin[toss_coin < threshold] = 0   #小於閥值就是反面
        
        toss_coin = 1 - toss_coin        
        toss_coin = np.sum(toss_coin, 1)
        return toss_coin        
    
    def calc_fitting_curve(self, toss_coin, toss_coin_count, times):  #計算擬合曲線
        mu = toss_coin.mean()
        sigma = toss_coin.std()
        y = stats.norm.pdf(range(times + 1), mu, sigma)
        max_n = np.max(toss_coin_count)
        max_y = np.max(y)
        factor = max_n/max_y
        return y, factor
        
    def pushButton_2_Click(self):  #畫直方圖和擬合曲線
        if self.ui.spinBox.value() == 0 \
        or self.ui.spinBox_2.value() == 0 \
        or self.ui.spinBox_4.value() == 0 \
        or self.ui.doubleSpinBox.value() == 0\
        or self.ui.doubleSpinBox_2.value() == 0:
            QMessageBox.about(self, 'Error', 'input parameter plz')
        else:
            #清空上一次的結果
            self.ui.label_8.setText('TP:')
            self.ui.label_9.setText('FN:')
            self.ui.label_10.setText('TN:')
            self.ui.label_11.setText('FP:')
            self.ui.label_12.setText('TPR:')
            self.ui.label_13.setText('FPR:')
            self.ui.label_14.setText('ACC:')
            self.ui.label_15.setText('AUC:')
            
            self.ui.label_16.setText('TP:')
            self.ui.label_17.setText('FN:')
            self.ui.label_18.setText('TN:')
            self.ui.label_19.setText('FP:')
            self.ui.label_20.setText('TPR:')
            self.ui.label_21.setText('FPR:')
            self.ui.label_22.setText('ACC:')
            self.ui.label_23.setText('AUC:')
            
            self.close_fig_roc()
            self.fig_roc.draw()          
            
            self.close_mpl()
            
            rounds1 = self.ui.spinBox.value()
            rounds2 = self.ui.spinBox_2.value()
            times = self.ui.spinBox_4.value()
            threshold1 = self.ui.doubleSpinBox.value()
            threshold2 = self.ui.doubleSpinBox_2.value()
                        
            #丟硬幣
            toss_coin1 = self.throw_coin(rounds1, times, threshold1)
            toss_coin2 = self.throw_coin(rounds2, times, threshold2)
            
            #統計硬幣在不同次數的回合數並補0到times的長度
            toss_coin1_count = self.appendzeros(np.bincount(toss_coin1.tolist()), times)
            toss_coin2_count = self.appendzeros(np.bincount(toss_coin2.tolist()), times)
                        
            #畫直方圖
            self.mpl.axes.bar(range(times + 1), toss_coin1_count, label = 'Coin1', edgecolor = 'black', alpha=.5)
            self.mpl.axes.bar(range(times + 1), toss_coin2_count, label = 'Coin2', edgecolor = 'black', alpha=.5)
            
            #畫擬合曲線
            y1, factor1 = self.calc_fitting_curve(toss_coin1, toss_coin1_count, times)
            y2, factor2 = self.calc_fitting_curve(toss_coin2, toss_coin2_count, times)
            
            self.mpl.axes.plot(range(times + 1), y1*factor1, 'm--', color = 'green', linewidth = 2)
            self.mpl.axes.plot(range(times + 1), y2*factor2, 'm--', color = 'red', linewidth = 2)
            
            self.mpl.axes.legend()
            self.mpl.draw()
            
            #存資料
            self.coin_dict = dict()
            self.coin_dict['rounds1'] = rounds1
            self.coin_dict['rounds2'] = rounds2
            self.coin_dict['times'] = times
            self.coin_dict['toss_coin1'] = toss_coin1
            self.coin_dict['toss_coin2'] = toss_coin2
            self.coin_dict['y1'] = y1
            self.coin_dict['y2'] = y2
            self.coin_dict['factor1'] = factor1
            self.coin_dict['factor2'] = factor2
            self.coin_dict['toss_coin1_count'] = toss_coin1_count
            self.coin_dict['toss_coin2_count'] = toss_coin2_count
            
            #存0陣列避免拿不出資料
            self.coin_dict['toss_coin3'] = np.zeros(101)
            self.coin_dict['toss_coin3_count'] = np.zeros(101)
            
            if self.ui.checkBox.isChecked():  #如果勾使用第3個硬幣
                if self.ui.spinBox_3.value() == 0 or self.ui.doubleSpinBox_3.value() == 0:
                    QMessageBox.about(self, 'Error', 'input parameter plz')            
                else:
                    rounds3 = self.ui.spinBox_3.value()
                    times = self.ui.spinBox_4.value()
                    threshold3 = self.ui.doubleSpinBox_3.value()
                    
                    #丟硬幣
                    toss_coin3 = self.throw_coin(rounds3, times, threshold3)
                    
                    #統計硬幣在不同次數的回合數並補0到times的長度
                    toss_coin3_count = self.appendzeros(np.bincount(toss_coin3.tolist()), times)
                    
                    #畫直方圖
                    self.mpl.axes.bar(range(times + 1), toss_coin3_count, label = 'Coin3', edgecolor = 'black', alpha=.5)
                    
                    #畫擬合曲線
                    y3, factor3 = self.calc_fitting_curve(toss_coin3, toss_coin3_count, times)
                    
                    self.mpl.axes.plot(range(times + 1), y3*factor3, 'm--', color = 'blue', linewidth = 2)
                    
                    self.mpl.axes.legend()
                    self.mpl.draw()
                    
                    #存資料
                    self.coin_dict['rounds3'] = rounds3
                    self.coin_dict['toss_coin3'] = toss_coin3
                    self.coin_dict['y3'] = y3
                    self.coin_dict['factor3'] = factor3
                    self.coin_dict['toss_coin3_count'] = toss_coin3_count
    
    def appendzeros(self, bincount, times):  #補0到補到 times+1 的長度
        appendlen = times - len(bincount) + 1  #看要補幾格0
        if appendlen > 0:
            appendarr = np.zeros(appendlen)
            bincount = np.hstack((bincount, appendarr))           
        return bincount
    
    def replot_now(self, coin_count = 2):  #因為刷新都會把畫布清空，所以我重畫原本的直方圖
        times = self.coin_dict['times']
        y1 = self.coin_dict['y1']
        y2 = self.coin_dict['y2']
        factor1 = self.coin_dict['factor1']
        factor2 = self.coin_dict['factor2'] 
        toss_coin1_count = self.coin_dict['toss_coin1_count']
        toss_coin2_count = self.coin_dict['toss_coin2_count']
        
        #畫直方圖
        self.mpl.axes.bar(range(times + 1), toss_coin1_count, label = 'Coin1', edgecolor = 'black', alpha=.5)
        self.mpl.axes.bar(range(times + 1), toss_coin2_count, label = 'Coin2', edgecolor = 'black', alpha=.5)
        
        #畫擬合曲線
        self.mpl.axes.plot(range(times + 1), y1*factor1, 'm--', color = 'green', linewidth = 2)       
        self.mpl.axes.plot(range(times + 1), y2*factor2, 'm--', color = 'red', linewidth = 2)
        
        if coin_count > 2:
            y3 = self.coin_dict['y3']
            factor3 = self.coin_dict['factor3'] 
            toss_coin3_count = self.coin_dict['toss_coin3_count']
            self.mpl.axes.bar(range(times + 1), toss_coin3_count, label = 'Coin3', edgecolor = 'black', alpha=.5)
            self.mpl.axes.plot(range(times + 1), y3*factor3, 'm--', color = 'blue', linewidth = 2)
        
        self.mpl.axes.legend()
        self.mpl.draw()
    
    def find_Bayes_line(self, coin_count, toss_coin_count_list, times, rounds_list, landa_list):
        #coin_count 硬幣數量 ex: 3
        #toss_coin_count_list 每顆硬幣在0~100的柱子高度，size是[3, 101]
        #rounds_list 每顆硬幣的rounds ex: [4000, 6000, 8000]
        #landa_list 每顆硬幣的landa ex: [1, 2, 1]
        tmp = np.zeros_like(toss_coin_count_list)
        total_rounds = np.sum(rounds_list)
        last_coin = -1  #前一次最高硬幣
        current_coin = -1  #當前最高硬幣
        ans = []
        
        for i in range(times + 1):
            for j in range(coin_count):
                tmp[j, i] = landa_list[j]*toss_coin_count_list[j, i]/total_rounds
            if np.sum(tmp[:, i]) == 0:
                continue
            last_coin = current_coin
            current_coin = np.argmax(tmp[:, i], 0)
            
            if current_coin != last_coin and last_coin != -1:
                ans.append(i)
        return ans
    
    def calc_classification_rate(self, toss_coin1, toss_coin2, divide_value):
        #Coin1固定在左邊，Coin2固定在左邊
        #toss_coin1_count是第一顆硬幣丟0~100次正面分別有幾個回合的array
        #divide_value是分割線的值
        
        if toss_coin1.min() <= toss_coin2.min():
            toss_coin1_copy = toss_coin1.copy()
            toss_coin2_copy = toss_coin2.copy()
        else:
            toss_coin1_copy = toss_coin2.copy()
            toss_coin2_copy = toss_coin1.copy()
            
        #計算線左邊是Coin1的有幾個(tp)，線右邊是Coin2的有幾個(tn)
        toss_coin1_copy[toss_coin1_copy <= divide_value] = 1
        toss_coin1_copy[toss_coin1_copy > divide_value] = 0
        toss_coin2_copy[toss_coin2_copy < divide_value] = 0
        toss_coin2_copy[toss_coin2_copy >= divide_value] = 1  
        
        tp = np.sum(toss_coin1_copy)
        fn = len(toss_coin1_copy) - tp
        tn = np.sum(toss_coin2_copy)
        fp = len(toss_coin2_copy) - tn
        
        tpr = tp/(tp + fn)
        fpr = fp/(fp + tn)
        
        acc = (tp + tn) / (tp + fn + tn + fp)
        auc = metrics.auc([0, fpr, 1], [0, tpr, 1])
        
        return tp, fn, tn, fp, tpr, fpr, acc, auc   
               
    def pushButton_3_Click(self):  #貝氏分類器
        rounds1 = self.coin_dict['rounds1']
        rounds2 = self.coin_dict['rounds2']
        toss_coin1 = self.coin_dict['toss_coin1']
        toss_coin2 = self.coin_dict['toss_coin2']
                
        times = self.coin_dict['times']
        
        toss_coin1_count = self.coin_dict['toss_coin1_count'].reshape([1, times + 1])
        toss_coin2_count = self.coin_dict['toss_coin2_count'].reshape([1, times + 1])   
        
        if self.ui.checkBox.isChecked() == False:  #如果沒有勾使用第3個硬幣
            #貝氏分類
            landa1 = self.ui.spinBox_5.value()
            landa2 = self.ui.spinBox_6.value()
            toss_coin_count_list = np.vstack((toss_coin1_count, toss_coin2_count))
            rounds_list = np.array([rounds1, rounds2])
            landa_list = np.array([landa1, landa2])
            
            ans = self.find_Bayes_line(2, toss_coin_count_list, times, rounds_list, landa_list)
            
            #畫分類線
            textheight = max(toss_coin1_count.max(), toss_coin2_count.max())  #文字的高度選柱子最高點
            
            self.close_mpl()
            self.replot_now()
            
            self.mpl.axes.axvline(x = ans[0], linewidth = 2, color = 'brown')
            self.mpl.axes.text(ans[0] + 2, textheight, str(ans[0]))
            
            self.mpl.draw()
                 
            #算分類率
            tp, fn, tn, fp, tpr, fpr, acc, auc = self.calc_classification_rate(toss_coin1, toss_coin2, ans)       
#            print('\ntp:%d\nfn:%d\ntn:%d\nfp:%d\ntpr:%f\nfpr:%f\nacc:%f\nauc:%f\n' %(tp, fn, tn, fp, tpr, fpr, acc, auc))
             
            self.close_fig_roc()
            self.fig_roc.axes.plot([0, fpr, 1], [0, tpr, 1], color = 'green')
            self.fig_roc.axes.fill_between([0, fpr, 1], [0, tpr, 1], color = 'GreenYellow', alpha=0.5)
            self.fig_roc.axes.plot(fpr, tpr, '.', color = 'darkgreen')
            self.fig_roc.axes.plot([0, 1], [0, 1], color = 'blue', linestyle = '--')            
                        
            #左P 右N
            self.ui.label_8.setText('TP: %d' %(tp))
            self.ui.label_9.setText('FN: %d' %(fn))
            self.ui.label_10.setText('TN: %d' %(tn))
            self.ui.label_11.setText('FP: %d' %(fp))
            self.ui.label_12.setText('TPR: %.3f' %(tpr))
            self.ui.label_13.setText('FPR: %.3f' %(fpr))
            self.ui.label_14.setText('ACC: %.3f' %(acc))
            self.ui.label_15.setText('AUC: %.3f' %(auc))
            
            #左N 右P
            tpr = tn/(tn + fp)
            fpr = fp/(fn + tp)
            auc = metrics.auc([0, fpr, 1], [0, tpr, 1])
            
            self.fig_roc.axes.plot([0, fpr, 1], [0, tpr, 1], color = 'red')
            self.fig_roc.axes.fill_between([0, fpr, 1], [0, tpr, 1], color = 'Fuchsia', alpha=0.3)
            self.fig_roc.axes.plot(fpr, tpr, '.', color = 'darkred')
            
            self.fig_roc.draw()
                       
            self.ui.label_16.setText('TP: %d' %(tn))
            self.ui.label_17.setText('FN: %d' %(fp))
            self.ui.label_18.setText('TN: %d' %(tp))
            self.ui.label_19.setText('FP: %d' %(fn))
            self.ui.label_20.setText('TPR: %.3f' %(tpr))
            self.ui.label_21.setText('FPR: %.3f' %(fpr))
            self.ui.label_22.setText('ACC: %.3f' %(acc))
            self.ui.label_23.setText('AUC: %.3f' %(auc))
        else:  #有勾使用第3顆硬幣
            try:
                rounds3 = self.coin_dict['rounds3']
                toss_coin3_count = self.coin_dict['toss_coin3_count'].reshape([1, times + 1])              
                
                landa1 = self.ui.spinBox_5.value()
                landa2 = self.ui.spinBox_6.value()
                landa3 = self.ui.spinBox_7.value()
                
                toss_coin_count_list = np.vstack((toss_coin1_count, toss_coin2_count))
                toss_coin_count_list = np.vstack((toss_coin_count_list, toss_coin3_count))
                rounds_list = np.array([rounds1, rounds2, rounds3])
                landa_list = np.array([landa1, landa2, landa3])
                
                ans = self.find_Bayes_line(3, toss_coin_count_list, times, rounds_list, landa_list)
                
                textheight = max(toss_coin1_count.max(), toss_coin2_count.max(), toss_coin3_count.max())  #文字的高度選柱子最高點
                
                self.close_mpl()
                self.replot_now(3)
                
                self.mpl.axes.axvline(x = ans[0], linewidth = 2, color = 'brown')
                self.mpl.axes.text(ans[0] + 2, textheight, str(ans[0]))
                self.mpl.axes.axvline(x = ans[1], linewidth = 2, color = 'brown')
                self.mpl.axes.text(ans[1] + 2, textheight, str(ans[1]))
                
                self.mpl.draw()
                
            except Exception as e:
                QMessageBox.about(self, 'エラー', 'コイン3のデータがありません、Plotで新規作成してください。')
                print('貝氏分類 Coin3 錯誤')
        
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
        do_k_means.res.callback_signal.connect(self.show_k_means_result)  #回傳值連接func後續處理
        QThreadPool.globalInstance().start(do_k_means)  #執行多線程
            
    def show_k_means_result(self, msg, new_center1, new_center2):
        if msg == 'error':
            QMessageBox.about(self, '執行錯誤')
        else:
            toss_coin1_count = self.coin_dict['toss_coin1_count']
            toss_coin2_count = self.coin_dict['toss_coin2_count']
        
            print(msg)
            self.close_mpl()
            self.replot_now()
            
            mid = (new_center1 + new_center2)/2
            
            self.mpl.axes.axvline(x = new_center1, linewidth = 2, color = 'black')
            self.mpl.axes.axvline(x = new_center2, linewidth = 2, color = 'black')
            self.mpl.axes.axvline(x = mid, linewidth = 2, color = 'brown', linestyle = '--')
                      
            textheight = max(toss_coin1_count.max(), toss_coin2_count.max())  #文字的高度選柱子最高點
            self.mpl.axes.text(new_center1 + 2, textheight, str(np.round(new_center1, 1)))
            self.mpl.axes.text(new_center2 + 2, textheight, str(np.round(new_center2, 1)))
            self.mpl.axes.text(mid + 2, textheight, str(np.round(mid, 1))) 
            self.mpl.draw()
        
app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())