class Solution:
    def intToRoman(self, num: int) -> str:
        dic={
             "I":1,
             "IV":4,
             "V":5,
             "IX":9,
             "X":10,
             "IV":14,
             "XL":40,
             "L":50,
             "XC":90,
             "C":100,
             "XD":140,
             "D":500,
             "XM":900,
             "M":1000,
            }
        output=[]
        for k,v in reversed(dic.items()):
            while num>0:
                if v <= num:
                    output.append(k)
                    num-=v
                else:
                    break
        return"".join(output)            
                 
