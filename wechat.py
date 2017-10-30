#_*_ coding:utf-8 _*_
#! /usr/bin/env python
 
import requests
import json

def get_token():
 
  url='https://qyapi.weixin.qq.com/cgi-bin/gettoken'
  values = {'corpid' : 'ww6c9dd7fa7f100584' ,
      'corpsecret':'YR2bz9qMKbtOZx3cgujdqlv3eblvRytTozknXSZ9aJM',
       }
  req = requests.post(url, params=values, proxies={'http': '10.22.0.238:3128','https': '10.22.0.238:3128'})   #proxies为设置 代理服务器
  data = json.loads(req.text)
  #print(data)
  return data['access_token']


def send_msg(wechatmsg):
  url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="+get_token()
  values = """{"touser" : "LiuLei|smnrao|happy" ,
      "toparty":"",
      "totag":"",
      "msgtype":"text",
      "agentid":"1000003",
      "text":{
        "content": "%s"
      },
      "safe":"0"
      }""" %(str(wechatmsg))
  #print(url)
  
  data = json.loads(values) 
  req = requests.post(url, values,proxies={'http': '10.22.0.238:3128','https': '10.22.0.238:3128'})      #proxies为设置 代理服务器
  #print(req)
 
if __name__ == '__main__':
  send_msg("Test")