class program(object):
    codes="a"
    def __init__(self,codes):
        self.codes=codes
    
    def CFG(self):
        codes=self.codes;
        a=[0 for i in range(100)]
        b=["" for i in range(100)]
        index=0
        n=0
        for i in range(codes.count("\n",0,len(codes))):
            split=codes.split("\n")[i]
            if split.find("{",0,len(split))>0:
                start=i+1
        for i in range(codes.count("\n",0,len(codes))):
            split=codes.split("\n")[i]  
            if split.find("}",0,len(split))>0:
                end=i      
        for i in range(start,end):
            split=codes.split("\n")[i]
            subsplit=codes.split("\n")[i+1]
            if split.find("fi",0,len(split))<=0 and split.find("done",0,len(split))<=0:
                index+=1
            if i==start:
                a[n]=index
                b[n]="begin"
                n+=1
            if split.find("if",0,len(split))>0:
                if subsplit.find("return",0,len(subsplit)<0):
                    a[n]=index+1
                    b[n]="if"
                    n+=1
            if split.find("while",0,len(split))>0:
                a[n]=index
                b[n]="while"
                a[n+1]=index+1
                n+=2
            if split.find("if",0,len(split))>0 and subsplit.find("return",0,len(subsplit))<0:
                pass
            if split.find("done",0,len(split))>0 and subsplit.find("return",0,len(subsplit))<0:
                    a[n]=index+1
                    n+=1
            if split.find("return",0,len(split))>0:
                    a[n]=index
                    b[n]="return"
                    n+=1
        matrix=[[0 for i in range(n)] for i in range(n)]
        for i in range(n-1):
            if b[i]=="if":
                matrix[i-1][i]=1
                matrix[i][i+1]=1
                matrix[i-1][i+1]=1
            elif b[i]=="while":
                matrix[i-1][i]=1
                matrix[i][i-1]=1
            else :matrix[i][i+1]=1
        order=[str(a[i])for i in range(n)]
        order.sort()

        for j in range(n):
            matrix[2][j]=matrix[n-1][j]
        for i in range(2,n):
            for j in range(n):
                matrix[i][j]=matrix[i-1][j]
        print("[",end="")
        for i in range(n):
            for j in range(n):
                print(matrix[i][j],end="")
                if j!=(n-1):
                    print(",",end="")
            if i!=n-1:
                print(";",end="")
        print ("]")
        print(a)




s="""
    bool x = True;
    bool y = False;
    bool z = True;
    bool a = True;
    main()
    {
    1:  x= !y;
    2:  z= !x;
    3:  if ( (x & y) | (! z) )
    4:      y= !y;
    5:      pass;
        fi
    6:  x=!y;
    7:  z=!z;
    8:  while ( ( x | y) & (a | z) )
    9:      a=!y;
    10:     y=!z;
        done
    11: return x;
    } 
"""
p=program(s)
p.CFG()