# -*- coding: utf-8 -*-
"""
Created on Wed May  6 13:30:43 2020

@author: Yuchi
"""

from PyQt5.QtCore import QRunnable, QObject, pyqtSignal
import numpy as np
import time

class ResponseSignals(QObject):
    callback_signal = pyqtSignal(str, float, float)  #要回傳的結果 msg,new_center1,2
    
class Run_k_means(QRunnable):
    def __init__(self, D, k1, k2):  #主程式傳入的參數
        super(QRunnable,self).__init__()
        self.D = D
        self.k1 = k1
        self.k2 = k2
        self.res = ResponseSignals()  #回傳結果
        
    def k_means(self, D, k1, k2):
        Dis1 = np.abs(D-k1)  #分別算到k1, k2的距離
        Dis2 = np.abs(D-k2)
        classes = np.zeros(len(D))  #到k1距離短就代表第1類，k2同
        new_center1_list = []
        new_center2_list = []
        for i in range(len(D)):
            if Dis1[i] <= Dis2[i]:
                classes[i] = 1
                new_center1_list.append(D[i])
            else:
                classes[i] = 2
                new_center2_list.append(D[i])
        new_center1 = np.mean(new_center1_list)  #平均這些同是第一類的值得到一個新的中心
        new_center2 = np.mean(new_center2_list)
        print('[%f, %f]' %(new_center1, new_center2))
        return new_center1, new_center2

    def run(self):
        try:
            new_center1, new_center2 = self.k_means(self.D, self.k1, self.k2)  
            
            while(new_center1 != self.k1 or new_center2 != self.k2):  #新中心和舊中心都相同才能停下來
                self.res.callback_signal.emit('doing', new_center1, new_center2)
                time.sleep(1)
                self.k1 = new_center1
                self.k2 = new_center2
                new_center1, new_center2 = self.k_means(self.D, self.k1, self.k2)
            else:
                self.res.callback_signal.emit('complete', new_center1, new_center2)
        except Exception as e:
            self.res.callback_signal.emit('error', 0.0, 0.0)