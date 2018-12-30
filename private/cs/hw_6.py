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
            if " done "in split :
                if " return " not in split:
                    split=re.sub(r"(\s)*done(\s)*(\S)+\:(\s)*","",split)
                    r=r+"\n"+split+";"
                else:
                    split=re.sub(r"(\s)*done(\s)*(\S)+\:(\s)*","",split)
                    split=re.sub(r"^return","print(",split)
                    r=r+"\n"+split+")"

            elif " fi "in split :
                if " return " not in split:
                    split=re.sub(r"(\s)*fi(\s)*(\S)+\:(\s)*","",split)
                    r=r+"\n"+split+";"
                else:
                    split=re.sub(r"(\s)*fi(\s)*(\S)+\:(\s)*","",split)
                    split=re.sub(r"^return","print(",split)
                    r=r+"\n"+split+")"
            elif " if "in split :
                split=re.sub(r"(\s)*(\S)+?\:(\s)*",":",split)
                split=re.sub(r"^.","",split)
                r=r+"\n"+split+";"
            elif " while "in split :
                split=re.sub(r"(\s)*(\S)+?\:(\s)*",":",split)
                split=re.sub(r"^.","",split)
                r=r+"\n"+split+";"
            elif i==codes.count(";")-1:
                split=re.sub(r"(\s)*(\S)+\:(\s)*","",split)
                split=re.sub(r"^return","print(",split)
                r=r+split+")"
            else:
                split=re.sub(r"(\s)*\{(\s)*","",split)
                split=re.sub(r"(\s)*\}(\s)*","",split)
                split=re.sub(r"(\s)*bool(\s)+","",split)
                split=re.sub(r"(\s)*(\S)+\:(\s)*","",split)
                split=re.sub(r"(\s)*main(\s)*\((\s)*\)(\s)*","",split)
                r=r+split+";"
        exec(r)

s = ""
while "}" not in s:
    s += input()
    s += '' 
p = program(s)
p.evaluate()