from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal
import threading
import socket
from time import strftime
from time import localtime
newmsg=[]
curr_time = None
class ReciveMsg(QtCore.QObject):
    pv =pyqtSignal()
    chatlist = pyqtSignal()
    def __init__(self):
        super(QtCore.QObject, self).__init__()

    def recive(self, conn):
        while True:
            message = conn.recv(1024)
            message = message.decode()
            print("recive :",message)
            global newmsg,curr_time
            curr_time = strftime("%H:%M:%S",  localtime())
            newmsg = message.split(';')
            if(newmsg[0] == "getChat"):
                self.chatlist.emit()
            if(newmsg[0] == "send" or newmsg[0] == "sendtochannel" or newmsg[0] ==  "sendtogroup"):
                self.pv.emit()
            # message = message.split(';')
            # if(message[0]=="getChat"):
            #     del message[0]
            #     for i in message:
            #         item = QtWidgets.QListWidgetItem(i)
            #         self.listWidget.addItem(item)
            #     print('recv:', message)
            #     print(message)
    
        

class Ui_MainWindow(object):
    uname=None
    currentChat=None
    recivemsg = ReciveMsg()
    thread=None
    connection = None
    channels= []
    groups=[]
    myChats={}
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.page)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(240, 150, 301, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.username = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.username.setMaximumSize(QtCore.QSize(16777215, 30))
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.login = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.login.setObjectName("login")
        self.horizontalLayout.addWidget(self.login)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.page_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(90, 0, 521, 341))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.back = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.back.setObjectName("back")
        self.horizontalLayout_2.addWidget(self.back)
        self.searchbox = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.searchbox.setObjectName("searchbox")
        self.horizontalLayout_2.addWidget(self.searchbox)
        self.search = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.search.setObjectName("search")
        self.horizontalLayout_2.addWidget(self.search)
        self.addnew = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.addnew.setObjectName("addnew")
        self.horizontalLayout_2.addWidget(self.addnew)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 303))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.msglist = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.msglist.setObjectName("msglist")
        self.verticalLayout.addWidget(self.msglist)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.chattitle = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.chattitle.setObjectName("chattitle")
        self.gridLayout_2.addWidget(self.chattitle, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.chatlist = QtWidgets.QListWidget(self.verticalLayoutWidget_2)
        self.chatlist.setMaximumSize(QtCore.QSize(200, 16777215))
        self.chatlist.setObjectName("chatlist")
        self.horizontalLayout_3.addWidget(self.chatlist)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.page_2)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(90, 340, 311, 61))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.horizontalLayoutWidget_6)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.send = QtWidgets.QPushButton(self.page_3)
        self.send.setMinimumSize(QtCore.QSize(0, 40))
        self.send.setObjectName("send")
        self.horizontalLayout_5.addWidget(self.send)
        self.msginp = QtWidgets.QTextEdit(self.page_3)
        self.msginp.setMinimumSize(QtCore.QSize(200, 0))
        self.msginp.setObjectName("msginp")
        self.horizontalLayout_5.addWidget(self.msginp)
        self.gridLayout_3.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.gridLayout_4.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget_2.addWidget(self.page_5)
        self.horizontalLayout_7.addWidget(self.stackedWidget_2)
        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.page_6)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(130, 170, 491, 71))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.backtomain = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.backtomain.setObjectName("backtomain")
        self.horizontalLayout_8.addWidget(self.backtomain)
        self.chatname = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.chatname.setObjectName("chatname")
        self.horizontalLayout_8.addWidget(self.chatname)
        self.addchanel = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.addchanel.setObjectName("addchanel")
        self.horizontalLayout_8.addWidget(self.addchanel)
        self.addgroup = QtWidgets.QPushButton(self.horizontalLayoutWidget_7)
        self.addgroup.setObjectName("addgroup")
        self.horizontalLayout_8.addWidget(self.addgroup)
        self.stackedWidget.addWidget(self.page_6)
        self.gridLayout.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        host = '127.0.0.1'
        port = 12345
        self.connection= socket.socket()
        self.connection.connect((host, port))
        self.thread = threading.Thread(target=self.recivemsg.recive, args=(self.connection,))
        self.send.clicked.connect(self.sendMSG)
        self.login.clicked.connect(self.loginfunc)
        self.search.clicked.connect(self.searchAll)
        self.chatlist.itemClicked.connect(self.switchChat)
        self.recivemsg.chatlist.connect(self.showSearchResult)
        self.recivemsg.pv.connect(self.PVMessage)
        self.back.clicked.connect(self.showChatList)
        self.addnew.clicked.connect(self.page6)
        self.addchanel.clicked.connect(self.addChanel)
        self.backtomain.clicked.connect(self.backtoMain)
        self.pushButton_6.clicked.connect(self.jointoChannel)
        self.addgroup.clicked.connect(self.addGroup)
        self.back.clicked.connect(self.showChatList)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def showSearchResult(self):
        self.chatlist.clear()
        global newmsg
        del newmsg[0]
       
        for i in newmsg:
            
            item = QtWidgets.QListWidgetItem(i)
            self.chatlist.addItem(item)
        print('recv:', newmsg)
        print(newmsg)

    def addGroup(self):
        c = self.chatname.text()
        if(c != ""):
            c+= ':group'
            self.chatname.clear()
            cname = "creategroup;" + c  
            print(cname)
            self.connection.send(cname.encode())
            self.myChats[c] = ""
            self.groups.append(c)
    

    def backtoMain(self):
        self.stackedWidget.setCurrentIndex(1)
        self.showChatList()
    def jointoChannel(self):
        if(self.currentChat.split(':')[-1] == 'channel'):
            msg = "joinchannel;"+self.currentChat+';'+ self.uname
        else:
            msg = "joingroup;"+self.currentChat+';'+ self.uname
            self.stackedWidget_2.setCurrentIndex(0)
        self.msglist.setText("")
        self.myChats[self.currentChat] = ""
        self.connection.send(msg.encode())
        self.showChatList()

        
    def addChanel(self):
        c = self.chatname.text()
        if(c != ""):
            c+= ':channel'
            self.chatname.clear()
            cname = "createchannel;" + c  
            print(cname)
            self.connection.send(cname.encode())
            self.myChats[c] = ""
            self.channels.append(c)

    def page6(self):
        self.stackedWidget.setCurrentIndex(2)
    def addToChatList(self):
        if(newmsg[1] not in self.myChats):
            self.myChats[newmsg[1]] = ""
            item = QtWidgets.QListWidgetItem(newmsg[1])
            self.chatlist.addItem(item)
            

    def PVMessage(self):
            
            global newmsg,curr_time
            if(newmsg[0] == "sendtogroup"):
                if(self.currentChat == newmsg[1]):
                    self.msglist.append(newmsg[2]+':'+newmsg[3]+'['+curr_time+']')
                    self.myChats[newmsg[1]] = self.msglist.toPlainText()
                else:
                    self.myChats[newmsg[1]] = self.myChats[newmsg[1]]+newmsg[2]+':'+ newmsg[3]+'['+curr_time+']'
            if(newmsg[0] == "sendtochannel"):
                print("kkk")
                if(self.currentChat == newmsg[1]):
                    self.msglist.append(newmsg[3]+'['+curr_time+']')

                    self.myChats[newmsg[1]] = self.msglist.toPlainText()
                else:
                    self.myChats[newmsg[1]] = self.myChats[newmsg[1]] + newmsg[3]+'['+curr_time+']'
            if(newmsg[0] == "send"):
                del newmsg[0]
                self.addToChatList()
                if(self.currentChat == newmsg[1]):
                    self.msglist.append(newmsg[1]+":"+newmsg[2]+'['+curr_time+']')
                    self.myChats[newmsg[1]] = self.msglist.toPlainText()
                else:
                    self.myChats[newmsg[1]] = self.myChats[newmsg[1]]+newmsg[1]+":" + newmsg[2]+'['+curr_time+']'
    def sendMSG(self):
        msg:str = self.msginp.toPlainText()
        txt = None
        if(self.currentChat != None and msg != "" ):
            if(self.currentChat.split(':')[-1] == 'channel'):
                txt = self.uname+':'+msg+'['+curr_time+']'+'\n'
                msg = "sendtochannel;"+self.currentChat+";"+self.uname +";"+msg+'\n'

            elif(self.currentChat.split(':')[-1] == 'group'):
                txt = self.uname+':'+msg+'['+curr_time+']'+'\n'
                msg = "sendtogroup;"+self.currentChat+";"+self.uname +";"+msg+'\n'
            else:    
                txt = self.uname+':'+msg+'['+curr_time+']'+'\n'
                msg = "send;"+self.currentChat+";"+self.uname +";"+msg+'\n'
                self.msglist.append(txt)
            #self.User_Chat[self.currentchat].append(self.username +":"+message)
            self.connection.send(msg.encode())
            
            self.myChats[self.currentChat] = self.myChats[self.currentChat] + txt

            self.msginp.clear()
    def switchChat(self):
        
        self.currentChat = self.chatlist.currentItem().text()
        self.chattitle.setText(self.currentChat)
        if(':' in self.currentChat):
            cname = self.currentChat.split(':') 
            if(cname[-1] == "channel"):
                if(self.currentChat in self.channels):
                    self.msglist.setText(self.myChats[self.currentChat])
                    self.stackedWidget_2.setCurrentIndex(0)
                if(self.currentChat in self.myChats):
                    self.msglist.setText(self.myChats[self.currentChat])

                else:
                    self.stackedWidget_2.setCurrentIndex(1)
            if(cname[-1] == "group"):
                if(self.currentChat in self.myChats):
                    self.msglist.setText(self.myChats[self.currentChat])
                    self.stackedWidget_2.setCurrentIndex(0)
                else:
                    self.stackedWidget_2.setCurrentIndex(1)
        
        elif(self.currentChat not in self.myChats):
            self.myChats[self.currentChat] = ""
            self.chatlist.clear()
            self.msglist.setText("")
            self.stackedWidget_2.setCurrentIndex(0)
            for i in self.myChats:
            
                item = QtWidgets.QListWidgetItem(i)
                self.chatlist.addItem(item)
        else:
            self.msglist.setText(self.myChats[self.currentChat])

    def showChatList(self):
        self.chatlist.clear()
        for i in self.myChats:
            item = QtWidgets.QListWidgetItem(i)
            self.chatlist.addItem(item)

    def loginfunc(self):
        self.uname = self.username.text()
        message = "chatinfo;"+self.uname
        print('send:' , message)
        message = message.encode()
        self.connection.send(message)
        self.stackedWidget.setCurrentIndex(1)
        self.thread.start()
    def searchAll(self):
        query = self.searchbox.text()
        message = "getChat;" + query
        print('send search:', message)
        message = message.encode()
        self.connection.send(message)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login.setText(_translate("MainWindow", "login"))
        self.back.setText(_translate("MainWindow", "back"))
        self.search.setText(_translate("MainWindow", "search"))
        self.addnew.setText(_translate("MainWindow", "add new"))
        self.chattitle.setText(_translate("MainWindow", "TextLabel"))
        self.send.setText(_translate("MainWindow", "send"))
        self.pushButton_6.setText(_translate("MainWindow", "join"))
        self.backtomain.setText(_translate("MainWindow", "back"))
        self.addchanel.setText(_translate("MainWindow", "add chanel"))
        self.addgroup.setText(_translate("MainWindow", "add group"))
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

from PyQt5.QtWidgets import QLabel, QSizePolicy, QMenu

import sys
app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()