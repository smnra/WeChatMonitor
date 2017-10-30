# -*- coding: UTF-8 -*-
import datetime
import ssh
import wechat

now = datetime.datetime.now()   #获取当前时间
#print("Today is %s." % now.strftime('%Y%m%d')) 

def mrServerStatus(host,serverName):        #参数为IP地址 和 mr服务器名称
    sshmr_1 = ssh.sshOpen() 
    ftpStr = sshmr_1.sshcon(host,22,'richuser','richr00t',"netstat -an|awk '{print $4}' | grep ':21$'")     #执行查看ftp端口是否打开
    mrStr = sshmr_1.sshcon(host,22,'richuser','richr00t',"ps -ef|awk '{print $10,$9}' | grep l3fw")     #检查mr进程是否打开
    mrNum = sshmr_1.sshcon(host,22,'richuser','richr00t',"ls l3fw_mr/kpi_import/" + now.strftime('%Y%m%d') + "| wc -w")     #统计mr基站数
    traceNum = sshmr_1.sshcon(host,22,'richuser','richr00t',"ls l3fw_mr/import/" + now.strftime('%Y%m%d') + "| wc -w")      #统计trace基站数
    if ftpStr.find(':::21') == -1:
        ftpStatus = "Faild"
    else:
        ftpStatus = "OK"

    if mrStr.find('watchdog.sh') == -1:
        mrStatus = "Faild"
    else:
        mrStatus = "OK"
    return [serverName,ftpStatus,mrStatus,str(mrNum.strip()),str(traceNum.strip())]     #函数返回一个mr服务器的以上状态的列表 
   
 

#massage_info = "Server\\tFTP\\tMR\\teNodeB\\tTrace\\n Server\\tFTP\\tMR\\teNodeB\\tTrace"

#wechat.send_msg(massage_info) 


mr1 = mrServerStatus("10.100.162.112","MR_1")
mr2 = mrServerStatus("10.100.162.111","MR_2")
mr3 = mrServerStatus("10.100.162.110","MR_3")
mr4 = mrServerStatus("10.100.162.109","MR_4")
mr5 = mrServerStatus("10.100.162.108","MR_5")
mr6 = mrServerStatus("10.100.162.115","MR_6")
mr7 = mrServerStatus("10.100.162.117","MR_7")

'''
mr1 = ["MR_1","OK","OK",193,601]
mr2 = ["MR_2","OK","OK",193,602]
mr3 = ["MR_3","OK","OK",193,603]
mr4 = ["MR_4","OK","OK",193,604]
mr5 = ["MR_5","OK","OK",193,605]
mr6 = ["MR_6","OK","OK",193,606]
mr7 = ["MR_7","OK","OK",193,607]
'''






title = ("%s MR Server Status:\\n" % now.strftime('%Y-%m-%d'))
message_wx0 = "Server FTP  MR   eNodeB Trace\\n"
message_wx1 = "%s  %s    %s    %s        %s\\n" % (mr1[0],mr1[1],mr1[2],mr1[3],mr1[4])
message_wx2 = "%s  %s    %s    %s        %s\\n" % (mr2[0],mr2[1],mr2[2],mr2[3],mr2[4])
message_wx3 = "%s  %s    %s    %s        %s\\n" % (mr3[0],mr3[1],mr3[2],mr3[3],mr3[4])
message_wx4 = "%s  %s    %s    %s        %s\\n" % (mr4[0],mr4[1],mr4[2],mr4[3],mr4[4])
message_wx5 = "%s  %s    %s    %s        %s\\n" % (mr5[0],mr5[1],mr5[2],mr5[3],mr5[4])
message_wx6 = "%s  %s    %s    %s        %s\\n" % (mr6[0],mr6[1],mr6[2],mr6[3],mr6[4])
message_wx7 = "%s  %s    %s    %s        %s" % (mr7[0],mr7[1],mr7[2],mr7[3],mr7[4])

print(title + message_wx0 + message_wx1 + message_wx2 + message_wx3 + message_wx4 + message_wx5 + message_wx6 + message_wx7)

wechat.send_msg(title + message_wx0 + message_wx1 + message_wx2 + message_wx3 + message_wx4 + message_wx5 + message_wx6 + message_wx7)  #调用微信发送消息模块 发送检查结果
