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

def scoreQueryFunc():
    print "����ִ�в�ѯ���ɼ���..."
    result = requests.get("http://electsys.sjtu.edu.cn/edu/login.aspx")
    sessionID = result.cookies.get("ASP.NET_SessionId", "none")
    if sessionID == "none":
        print "Sessionδ���棬�����µ�¼"


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
