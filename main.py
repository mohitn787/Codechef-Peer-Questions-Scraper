# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 18:29:52 2020

@author: mohit
"""

from bs4 import BeautifulSoup
import requests
import re
#give your codechef id
my_id=""
def findAnswer(a,id):
  final=[]
  for i in range(len(a)):
    m=""
    n=""
    p=""
    a[i]=str(a[i])
    z=a[i]
    check=id+"$"
    x = re.findall(check, z)
    ss="status/"
    s_len=len(ss)
    if(x):
      m=z.split(",")
      n=m[0]
      p=n[n.index(ss)+s_len:]
      final.append(p)
  return final
def questionSeparator(id):
    url="https://www.codechef.com/users/"+id
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    answer_id=id
    momo=[]
    for link in soup.find_all("a"):
        momo.append(link.get("href"))
    return findAnswer(momo,answer_id)
def differ(a,b):
    new=[]
    for i in b:
        if i not in a:
            new.append(i)
    return new
#give the id of codechef for your friend
new_id=input("Enter the Id with which you need to know the Question Diffferences\n")
m_1=questionSeparator(my_id)
m_2=questionSeparator(new_id)
m_3=differ(m_1,m_2)
m_4=differ(m_2,m_1)
print("FOLLOWING ARE THE QUESTIONS SOLVED BY "+new_id+" AND NOT BY "+my_id)
for i in m_3:
    print(i)
print("FOLLOWING ARE THE QUESTIONS SOLVED BY "+my_id+" AND NOT BY "+new_id)
for i in m_4:
    print(i)
