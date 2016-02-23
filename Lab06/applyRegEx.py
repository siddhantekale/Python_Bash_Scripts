#! /usr/bin/envpython3.4
#
#$Author: ee364a09 $
#$Date: 2016-02-23 15:22:12 -0500 (Tue, 23 Feb 2016) $
#$HeadURL: svn+ssh://ece364sv@ecegrid-thin1/home/ecegrid/a/ece364sv/svn/S16/students/ee364a09/Lab06/applyRegEx.py $
#$Revision: 88776 $

import os
import glob
import re
import sys

def getRejectedUsers():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    pattern6 = re.compile(r"((\w+)$|(\w+ \w+)$)")

    list_rejected = []
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)
            match5 = re.search(pattern5, line)
            match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match2 is None and match3 is None and match4 is None and match5 is None and match6 is None:
                #print(match.group(1))
                if(str[-1]==' '):
                    str = str[0:-1]
                list_rejected.append(str)

    #for i in list_rejected:
     #   print(i)
    return sorted(list_rejected)

def getUsersWithEmails():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            #match3 = re.search(pattern3, line)
            #match4 = re.search(pattern4, line)
            #match5 = re.search(pattern5, line)
            #match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match2 is not None:
                #print(match.group(1))
                if(str[-1]==' '):
                    str = str[0:-1]
                dict_users[str] = match2.group(0)

    return dict_users


def getUsersWithPhones():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    #pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            #match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)
            match5 = re.search(pattern5, line)
            #match6 = re.search(pattern6, line)

            if match is not None:
                #print(match)
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None:
                #print(match.group(1))

                if(str[-1]==' '):
                    str = str[0:-1]
                if match3 is not None:
                    #print("here")
                    print(match3.group)
                    dict_users[str] = match3.group(0)
                elif match4 is not None:
                    #print("here")
                    print(match4.group)
                    dict_users[str] = match3.group(0)
                elif match5 is not None:
                    #print("here")
                    print(match5.group)
                    dict_users[str] = match3.group(0)

    return dict_users

def getUsersWithStates():
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    #pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    pattern6 = re.compile(r"((\w+)$|(\w+ \w+)$)")
    dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            #match2 = re.search(pattern2, line)
           # match3 = re.search(pattern3, line)
            #match4 = re.search(pattern4, line)
            #match5 = re.search(pattern5, line)
            match6 = re.search(pattern6, line)

            if match is not None:
                #print(match)
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None:
                #print(match.group(1))

                if(str[-1]==' '):
                    str = str[0:-1]
                if match6 is not None:
                    dict_users[str] = match6.group(0)

    return dict_users

def getUsersWithoutEmails():
    list_rejected = getRejectedUsers()
    list_users = []
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    #dict_users = {}
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            #match3 = re.search(pattern3, line)
            #match4 = re.search(pattern4, line)
            #match5 = re.search(pattern5, line)
            #match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                #print(match.group(2))
                #print(match.group(3))
                #print(match.group(4))
                #print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match2 is None:
                #print(match.group(1))
                if(str[-1]==' '):
                    str = str[0:-1]
                if str not in list_rejected:
                    list_users.append(str)

    return sorted(list_users)

def getUsersWithoutStates():
    list_rejected = getRejectedUsers()
    list_users = []
    pattern = re.compile(r"(([A-Za-z]+)(,?)([\s]{1,2})((\w)+))")
    pattern2 = re.compile(r"([\w.-]+@[\w.-]+)")
    pattern3 = re.compile(r"([\d]){10}")
    pattern4 = re.compile(r"([\d]{3})(-)([\d]{3})(-)([\d]{4})")
    pattern5 = re.compile(r"\(([\d]{3})\) ([\d]{3})(-)([\d]{4})")
    pattern6 = re.compile(r"((\w+)$|(\w+ \w+)$)")
    with open("SiteRegistration.txt","r") as input:
        for line in input:
            match = re.match(pattern, line)

            match2 = re.search(pattern2, line)
            match3 = re.search(pattern3, line)
            match4 = re.search(pattern4, line)
            match5 = re.search(pattern5, line)
            match6 = re.search(pattern6, line)

            if match is not None:
                #print(match.group(0))
                #print (match.groups())
                #print(match.group(1))
                print(match.group(2))
                print(match.group(3))
                print(match.group(4))
                print(match.group(5))
                if(match.group(3) != ''):
                    str = match.group(5).strip() + ' ' + match.group(2).strip()
                    #print(str)
                else:
                    #print(match.group(4))
                    str = match.group(1).strip() + ' ' + match.group(4).strip()

            if match is not None and match6 is None:
                if match2 is not None or match3 is not None or match4 is not None or match5 is not None:
                #print(match.group(1))
                    if(str[-1]==' '):
                        str = str[0:-1]
                    if str not in list_rejected:
                        list_users.append(str)

    return sorted(list_users)



















if __name__ == "__main__" :
    getUsersWithPhones()