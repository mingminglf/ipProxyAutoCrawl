import requests

import time


def auth(proxy):
    response = None
    start_time = time.time()
    try:
        if (proxy.protol.lower().find("https") > -1) or (proxy.protol.lower().find("socks5") > -1) or (
                proxy.protol.lower().find("socks4") > -1):
            response = requests.get("https://baidu.com.com/",
                                    proxies={"http": proxy.getProxy(), "https": proxy.getProxy()}, timeout=10)
        elif proxy.protol.lower().find("http") > -1:
            response = requests.get("http://example.com/", proxies={"http": proxy.getProxy()}, timeout=10)
        if response.status_code == 200:
            end_time = time.time()
            proxy.elseInfo.update({"time": "::::time:::{:.2f}".format(end_time - start_time), "isTure": True})
            return True
    except Exception:

        return False
