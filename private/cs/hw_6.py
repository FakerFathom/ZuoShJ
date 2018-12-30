import re


class program:
    def __init__(self, codes):
        self.codes=codes
        
    def evaluate(self):
        codes=self.codes
        codes=re.sub(r"!"," not ",codes)
        codes=re.sub(r"\|"," or ",codes)
        codes=re.sub(r"\&"," and ",codes)
        codes=re.sub(r"(?<=\:|\s)if(?=\(|\s)"," if ",codes)
        codes=re.sub(r"(?<=\;|\s)fi(?=\s)"," fi ",codes)
        codes=re.sub(r"(?<=\:|\s)while(?=\(|\s)"," while ",codes)
        codes=re.sub(r"(?<=\;|\s)done(?=\s)"," done ",codes)
        codes=re.sub(r"(?<=\:|\s)return(?=\s|\()"," return ",codes)
        r=""
        for i in range(codes.count(";")):
            split=codes.split(";")[i]
            split=re.sub(r"(\s)*\{(\s)*","",split)
            split=re.sub(r"(\s)*\}(\s)*","",split)
            split=re.sub(r"(\s)*bool(\s)+","",split)
            split=re.sub(r"(\s)*(\S)+\:(\s)*","",split)
            split=re.sub(r"(\s)*main(\s)*\((\s)*\)(\s)*?","",split)
            r=r+split+";"
        print(r) 
        
            



s = ""
while "}" not in s:
    s += input()
    s += '' 
p = program(s)
p.evaluate()