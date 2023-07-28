class IpEntity:
    ip = ""
    protol = ""
    port = ""
    elseInfo = {}

    def getProxy(self):
        return self.protol + "://" + self.ip + ":" + self.port

    def __init__(self, ip, port, protol, elseInfo={}):
        self.ip = ip
        self.port = port
        self.protol = protol
        if self.elseInfo != {}:
            self.elseInfo.update(elseInfo)
        else:
            self.elseInfo = elseInfo

    def getelseInfo(self):
        return self.elseInfo
