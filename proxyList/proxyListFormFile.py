
import re
from entity import ipEntity

ipPattern = re.compile(r"^(((25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))")
protPattern = re.compile(r'(https)|(socks5)|(socks4)|(http)|(HTTPS)|(SOCKS5)|(SOCKS4)|(HTTP)')
portPattern = re.compile("^([0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$")


def getProxyList():
    proxyList = []
    with open(r"C:\Users\admin\Desktop\ff.txt", mode='r') as f:
        list = f.readlines()
        portFlag = 0
        protFlag = 0
        ipStr = portStr = protStr = ""
        for str in list:
            # print(str)
            tempList = str.split()
            for singstr in tempList:
                # print(singstr)
                ipMatchObj = ipPattern.search(singstr)
                if ipMatchObj:
                    if ipStr != "":
                        proxyList.append(ipEntity.IpEntity(ipStr, portStr, protStr))
                        ipStr = portStr = protStr = ""
                    portFlag = 1
                    protFlag = 1
                    ipStr = ipMatchObj.group()
                    # print("search --> ip.group() : " + ipMatchObj.group())

                portMatchObj = portPattern.search(singstr)
                if portMatchObj:
                    if portFlag == 1:
                        portFlag = 0
                        portStr = portMatchObj.group()
                        # print("search --> port.group() : " + portMatchObj.group())
                protMatchObj = protPattern.search(singstr)
                if protMatchObj:
                    if protFlag == 1:
                        protFlag = 0
                        protStr = protMatchObj.group().lower()
                        # print("search --> protocol.group() : " + protMatchObj.group())
    # print(proxyList)
    return proxyList
