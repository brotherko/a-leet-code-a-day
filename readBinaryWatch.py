#V1: use bin then count using reduce
class Solution1(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                time = bin(h)[2:]+bin(m)[2:]
                countBit = reduce(lambda x,y: int(x)+int(y), time)
                if(countBit == num):
                    res.append("{:d}:{:0>2d}".format(h,m))
        return res       


#V2: bin then count using the count()
class Solution2(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        for h in range(12):
            for m in range(60):
                if(bin(h).count("1") + bin(m).count("1") == num):
                    res.append("{:d}:{:0>2d}".format(h,m))
        return res            

#V3: Store all binary combination of minutes, then directly retrieve the list by using num-led of h
# Runtime no too much different?
from collections import defaultdict
class Solution3(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        res = []
        memo = defaultdict(list)
        for m in range(60):
            memo[bin(m).count("1")].append(m)
        for h in range(12):
            for m in memo[num - bin(h).count("1")]:
                res.append("{:d}:{:0>2d}".format(h,m))
        return res     