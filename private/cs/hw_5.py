import re
class program(object):
    def __init__(self, codes):
        self.codes = codes

    def CFG(self):
        codes = self.codes
        """ codes=codes.replace("if("," if (")
        codes=codes.replace("while("," while (")
        codes=codes.replace(":if",": if ")
        codes=codes.replace(":while",": while ")
        codes=codes.replace(";fi","; fi ")
        codes=codes.replace("done\n"," done ")
        codes=codes.replace("fi\n"," fi ") """
        codes=re.sub(r"(?<=\;|\s)fi(?=((\d)+?\:))"," fi ",codes)
        codes=re.sub(r"(?<=\:|\s)while(?=\(|\s)"," while ",codes)
        codes=re.sub(r"(?<=\:|\s)if(?=\(|\s)"," if ",codes)
        codes=re.sub(r"(?<=\;|\s)done(?=((\d)+?\:))"," done ",codes)
        codes=re.sub(r"(?<=\:|\s)return(?=\s|\()"," return ",codes)

        a = [0 for i in range(100)]
        b = ["" for i in range(100)]
        index = 0
        n = 0
        for i in range(codes.count(";")+1):
            split = codes.split(";")[i]
            if "{" in split:
                start = i
        for i in range(codes.count(";")+1):
            split = codes.split(";")[i]
            if "}" in split:
                end = i
        for i in range(start, end):
            split = codes.split(";")[i]
            after = codes.split(";")[i+1]
            before = codes.split(";")[i-1]
            index += 1
            if i == start and (" if " not in split and " while " not in split)and "return" not in split:
                a[n] = index
                b[n] = "begin"
                n += 1
            if " if " in split:
                if i == start or (" fi "in split or " done "in split ):
                    a[n] = index
                    b[n] = "if"
                    n += 1
                index += 1
                if " return " not in split :
                    a[n] = index
                    b[n] = "if2"
                    n += 1
            if " fi " in split and " return " not in split:
                if i != end-1 and (" if " not in split and " while "not in split):
                    a[n] = index
                    b[n] = "fi"
                    n += 1
            if " while " in split:
                a[n] = index
                b[n] = "while"
                index += 1
                n+=1
                if  " return " not in split:
                    a[n] = index
                    b[n] = "while2"
                    n += 1
            if " done " in split and " return " not in split :
                if i != end-1 and (" if " not in split and " while "not in split):
                    a[n] = index
                    b[n] = "done"
                    n += 1
            if " return " in split:
                if (" done "not in after and" fi "  not in after):
                    a[n] = index
                    b[n] = "last return"
                    n += 1
                if " fi " in after:
                    a[n] = index
                    b[n] = "if return"
                    n += 1
                if " done " in after:
                    a[n] = index
                    b[n] = "while return"
                    n += 1

        matrix = [[0 for i in range(n)] for i in range(n)]
        for i in range(n-1):
            if b[i] == "if2":
                if b[i+1] == "if return":
                    matrix[i-1][i] = matrix[i][i+1] = matrix[i-1][i+2] = 1
                else:
                    matrix[i-1][i] = matrix[i][i+1] = matrix[i-1][i+1] = 1
            elif b[i] == "if return" and b[i-1] != "if2":
                matrix[i-1][i] = matrix[i-1][i+1] = 1
            elif b[i] == "while":
                if b[i+1] !="while return" and b[i+2]!="while return":
                    matrix[i][i+1] = matrix[i+1][i] = matrix[i][i+2] = 1
                    """ if b[i+2] == "last return":
                        matrix[i][i+2] = 1 """
                elif b[i+1]=="while return":
                    matrix[i][i+1]=matrix[i][i+2] = 1
                else:
                    matrix[i][i+1]=matrix[i+1][i+2] = matrix[i][i+3] = 1
                
            elif b[i] == "last return"and (b[i-1]=="fi"or b[i-1]=="done"):
                matrix[i-1][i] = 1
            elif b[i] == "begin" or (b[i] == "fi" or b[i] == "done"):
                matrix[i][i+1] = 1

        order = [str(a[i])for i in range(n)]
        order.sort()
        for i in range(n):
            for j in range(n):
                if a[j] == int(order[i]):
                    a[i], a[j] = a[j], a[i]
                    for k in range(n):
                        matrix[i][k], matrix[j][k] = matrix[j][k], matrix[i][k]
                    for l in range(n):
                        matrix[l][i], matrix[l][j] = matrix[l][j], matrix[l][i]
                    break

        if n>1:
            print("[", end="")
            for i in range(n):
                for j in range(n):
                    print(matrix[i][j], end="")
                    if j != (n-1):
                        print(",", end="")
                if i != n-1:
                    print(";", end="")
            print("]")
        else:
            print('[0]')

""" s = ""
while "}" not in s:
    s += input()
    s += ' ' """
s="main() { gs:if;}"
p = program(s)
p.CFG()
