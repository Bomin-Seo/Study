import pandas
import pandas as pd

class RemoteControl:
    def __init__(self):
        self.__enabledChannelList = []
        self.currentchannel = 0
        self.blockchannel = []
        self.favorchannel = []
        self.blocked_favor = []

    def powerOnRemoteControl(self, input_list):
        for i in range(len(input_list)):
            self.__enabledChannelList.append(input_list[i])
            self.favorchannel.append(0)
        self.currentchannel = self.__enabledChannelList[0]
        return len(self.__enabledChannelList)

    def gotoChannel(self, num):
        for i in range(len(self.__enabledChannelList)):
            if num == self.__enabledChannelList[i][0]:
                self.currentchannel = self.__enabledChannelList[i]
        return self.currentchannel[0]

    def nextChannel(self):
        channelindex = self.__enabledChannelList.index(self.currentchannel)
        if len(self.__enabledChannelList) == channelindex + 1:
            self.currentchannel = self.__enabledChannelList[0]
        else:
            self.currentchannel = self.__enabledChannelList[channelindex + 1]
        return self.currentchannel[1]

    def previousChannel(self):
        channelindex = self.__enabledChannelList.index(self.currentchannel)
        if channelindex == 0:
            self.currentchannel = self.__enabledChannelList[len(self.__enabledChannelList) - 1]
        else:
            self.currentchannel = self.__enabledChannelList[channelindex - 1]
        return self.currentchannel[1]

    def blockChannel(self):
        temp_chan = self.currentchannel
        channelindex = self.__enabledChannelList.index(self.currentchannel)
        if channelindex == len(self.__enabledChannelList) - 1:
            self.currentchannel = self.__enabledChannelList[0]
        else:
            self.currentchannel = self.__enabledChannelList[channelindex + 1]
        self.blockchannel.append(self.__enabledChannelList[channelindex])
        self.blocked_favor.append(self.favorchannel[channelindex])
        del self.__enabledChannelList[channelindex]
        del self.favorchannel[channelindex]
        return self.currentchannel[1]

    def unblockChannel(self, num):
        blocked = False
        for i in range(len(self.blockchannel)):
            if num == self.blockchannel[i][0]:
                blocked = True
                blockedchannelindex = i
        if blocked:
            self.currentchannel = self.blockchannel[blockedchannelindex]
            self.__enabledChannelList.append(self.currentchannel)
            self.__enabledChannelList.sort()
            blockedindex = self.__enabledChannelList.index(self.currentchannel)
            self.favorchannel.insert(blockedindex, self.blocked_favor[blockedchannelindex])
            return 1
        else:
            return -1

    def powerOffRemoteControl(self):
        df = pd.DataFrame(self.__enabledChannelList)
        df.to_csv("output.csv", index= False, header=False)

    def favorChannel(self):
        if self.currentchannel not in self.__enabledChannelList:
            return -1
        else:
            channelindex = self.__enabledChannelList.index(self.currentchannel)
            self.favorchannel[channelindex] += 1
            return 1

    def aiNextChannel(self):
        channelindex = self.__enabledChannelList.index(self.currentchannel)
        temp_favor = self.favorchannel[:]
        nextfavorlist = []
        if self.favorchannel[channelindex] == min(self.favorchannel):
            mostfavor = self.favorchannel.index(max(self.favorchannel))
            self.currentchannel = self.__enabledChannelList[mostfavor]
        else:
            for i in range(len(self.favorchannel)):
                temp_favor[i] -= self.favorchannel[channelindex]
                if temp_favor[i] >= 0:
                    temp_favor[i] = 9999
                temp_favor[i] = abs(temp_favor[i])
            nextval = min(temp_favor)
            for j in range(len(temp_favor)):
                if temp_favor[j] == nextval:
                    nextfavorlist.append(j)
            self.currentchannel = self.__enabledChannelList[nextfavorlist[0]]
        return self.currentchannel[0]

    def aiPreviousChannel(self):
        channelindex = self.__enabledChannelList.index(self.currentchannel)
        temp_favor = self.favorchannel[:]
        nextfavorlist = []
        if self.favorchannel[channelindex] == max(self.favorchannel):
            leastfavor = self.favorchannel.index(min(self.favorchannel))
            self.currentchannel = self.__enabledChannelList[leastfavor]
        else:
            for i in range(len(self.favorchannel)):
                temp_favor[i] -= self.favorchannel[channelindex]
                if temp_favor[i] <= 0:
                    temp_favor[i] = 9999
                temp_favor[i] = abs(temp_favor[i])
            nextval = min(temp_favor)
            for j in range(len(temp_favor)):
                if temp_favor[j] == nextval:
                    nextfavorlist.append(j)
            self.currentchannel = self.__enabledChannelList[nextfavorlist[0]]
        return self.currentchannel[0]

    def getenable(self):
        return self.__enabledChannelList