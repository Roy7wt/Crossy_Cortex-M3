#-*- coding:gbk -*-
#-------------------------------------------------------------------------------
# Name:        ??1
# Purpose:
#
# Author:      lenovo
#
# Created:     27/05/2015
# Copyright:   (c) lenovo 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import requests
import json
import os
import webbrowser

crossyWebPrefix = "http://tq5124.dy.tongqu.me/crossy"

def getScoreCookie(url):
    result = requests.get(url)
    sessionID = result.cookies.get("ASP.NET_SessionId", "none")
    return sessionID

def scoreQueryFunc():
    print "����ִ�в�ѯ���ɼ���..."

    sessionID = getScoreCookie("http://electsys.sjtu.edu.cn/edu/student/sdtMain.aspx")
    print sessionID
    postData = {'cookie':'ASP.NET_SessionId=' + sessionID}
    result = requests.post(crossyWebPrefix + "/api/1/elect/info", params=postData)
    print result.text

    '''if result.status_code == 400:
        print "Sessionδ���棬�����µ�¼"
        os.system("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
        webbrowser.open("http://electsys.sjtu.edu.cn/edu/login.aspx")
    print("��ɵ�¼ʱ������\"login complete\"")

    while (True):
        a = raw_input()
        if a == "login complete":
            break

    sessionID = getScoreCookie("http://electsys.sjtu.edu.cn/edu/student/sdtMain.aspx")
    if sessionID != "none":
        postData = {'cookie':'ASP.NET_SessionId=' + sessionID}
        result = requests.post(crossyWebPrefix + "/api/1/elect/info", params=postData)
        print result.text'''



def booksQueryFunc():
    print "����ִ�в�ѯ���鼮��..."
def busQueryFunc():
    print "����ִ�в�ѯ��У��ʱ�̱�..."
def ecardQueryFunc():
    print "����ִ�в�ѯ��У԰����Ϣ��..."

def main():
    print "---------Crossy Server---------"
    queryType = "scoreQuery"

    if queryType == "scoreQuery":
        scoreQueryFunc()
    elif queryType == "booksQuery":
        booksQueryFunc()
    elif queryType == "busQuery":
        busQueryFunc()
    elif queryType == "ecardQuery":
        ecardQueryFunc();
    else: print "Unavailable Type. Please Check."


if __name__ == '__main__':
    main()
