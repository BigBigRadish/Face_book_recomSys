# -*- coding: utf-8 -*-
'''
读取CSS用模块。
'''
from CustomTitlebar.framelesswindow import FramelessWindow
import sys, os

class CommonHelper :

    def __init__(self ) :
        pass
         
    @staticmethod    
    def readQss( style):
        with open( style , 'r') as f:
           return f.read()
           
    @staticmethod    
    def FrameCustomerTitle( ui, title="python", setparent=False):
        
        framelessWindow = FramelessWindow(title);
        
        from Styles.CommonHelper import CommonHelper
        styleFile = os.path.join(os.path.dirname(sys.argv[0]),'Styles/style.css')
        qssStyle = CommonHelper.readQss( styleFile )  
        framelessWindow.setStyleSheet( qssStyle )   
        
        framelessWindow.setContent(ui)
        
        if setparent:
            ui.setParent(framelessWindow)
            
        return framelessWindow
