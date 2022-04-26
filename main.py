#Released By Aamer Issam, this script allow You to ping either hostnames or @ip and gives back as output thier hostname or @Ip
#put your @ip or hostnames in the 'hosts.txt' file then run the script, wait till it finishes then check 'result.xlsx'
#For those who actualy are using windwos, You would better to run ./main.py using powershell as administrator otherwise You may get the following messsage 'access denied'
#I wrote this script when my supervisor gaven me about 560 hostnames to ping on, so i thoudht that i could be helpful for those in need of doing a bulk ping
import subprocess
import xlsxwriter
#You may need to install xlsxwriter module (pip install xlsxwriter)
import socket
def ping(ip):
    #ping -c 2 172.25.10.217       or  ping -c 2 hostname  this is for linux
    ping_reply = subprocess.run(["ping","-c","2", ip],stderr=subprocess.PIPE, stdout=subprocess.PIPE)   # Linux
    # ping -n 2 172.25.10.217       or  ping -n 2 hostname  this is for Windows
    # ping_reply = subprocess.run(["ping","-n","2", ip],stderr=subprocess.PIPE, stdout=subprocess.PIPE) # Windwos
    # ping_reply.returncode = 0 or 1
    return ping_reply.returncode

file=open("hosts.txt", "r")
lines=file.readlines()

workbook = xlsxwriter.Workbook('result.xlsx')
worksheet = workbook.add_worksheet()

worksheet.write('A1', 'Hostname')
worksheet.write('B1', 'IP_Address')
i=1
for line in lines:
    i+=1
    res = ping(line.rstrip())
    if res == 0:
        statement=print('{:15s} ===>> '.format(line.rstrip()),socket.gethostbyname(line.rstrip()))
        worksheet.write('A'+str(i), line.rstrip())
        worksheet.write('B'+str(i), statement)
    else:
        statement=print('{:15s} ===>> NONE'.format(line.rstrip()))
        worksheet.write('A'+str(i), line.rstrip())
        worksheet.write('B'+str(i), 'NONE')
workbook.close()
