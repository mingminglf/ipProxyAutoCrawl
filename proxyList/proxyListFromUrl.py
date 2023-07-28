#根据网地址来进行爬取
from bs4 import BeautifulSoup
import requests
from entity import ipEntity
def getProxyList():
    response = requests.get("https://www.freeproxy.world/?type=socks5&anonymity=&country=&speed=&port=&page=1")
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.find_all("tr")
    proxyList = []
    for row in rows:
        try:
            ip = row.find_all("td")[0].text
            port = row.find_all("td")[1].find("a").text
            city = row.find_all("td")[3].text
            protocol = row.find_all("td")[5].text
            temp=ipEntity.IpEntity(ip=ip.replace("\n", "").replace(" ", ""), port=port.replace("\n", "").replace(" ", ""),
                              protol=protocol.replace("\n", "").replace(" ", ""),elseInfo={"city":city})

            proxyList.append(temp)

        except Exception as e:
            pass
    return proxyList
