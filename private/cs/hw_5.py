class program(object):
    def __init__(self, codes):
        self.codes = codes
    def CFG(self):
        codes = self.codes
        a = [0 for i in range(100)]
        b = ["" for i in range(100)]
        index = 0
        n = 0
        for i in range(codes.count("\n", 0, len(codes))):
            split = codes.split("\n")[i]
            if "{" in split:
                start = i+1
        for i in range(codes.count("\n", 0, len(codes))):
            split = codes.split("\n")[i]
            if "}" in split:
                end = i
        for i in range(start, end):
            split = codes.split("\n")[i]
            after = codes.split("\n")[i+1]
            before = codes.split("\n")[i-1]
            if "fi" not in split and "done" not in split:
                index += 1
            if i == start:
                a[n] = index
                b[n] = "begin"
                n += 1
            if "if" in split:
                if i==start or "fi" or "done" in before:
                    a[n]=index
                    b[n]="if"
                    n+=1
                elif "return" not in after:
                    a[n] = index+1
                    b[n] = "if"
                    n += 1
            if "while" in split:
                a[n] = index
                b[n] = "while"
                a[n+1] = index+1
                n += 2
            if "fi" in split and "return" not in after:
                a[n] = index+1
                b[n] = "fi"
                n += 1
            if "done" in split and "return" not in after:
                a[n] = index+1
                n += 1
            if "return" in split:
                a[n] = index
                b[n] = "return"
                n += 1
        matrix = [[0 for i in range(n)] for i in range(n)]
        for i in range(n-1):
            if b[i] == "if":
                matrix[i-1][i] = 1
                matrix[i][i+1] = 1
                matrix[i-1][i+1] = 1
            elif b[i] == "while":
                matrix[i][i+1] = matrix[i+1][i] = 1
                if b[i+2] == "return":
                    matrix[i][i+2] = 1
            elif b[i] == "return":
                matrix[i-1][i] = 1
            elif b[i] == "begin" or b[i] == "fi":
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
        print("[", end="")
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end="")
                if j != (n-1):
                    print(",", end="")
            if i != n-1:
                print(";", end="")
        print("]")
s = ""
while "}" not in s:
    s += input()
    s += '\n'
""" stopword = '    } '
for line in iter(input, stopword): # 输入为空行，表示输入结束
  s += line + '\n'
  s+='    } ' """
p = program(s)
p.CFG()
