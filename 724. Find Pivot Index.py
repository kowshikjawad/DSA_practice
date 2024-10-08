from sys import dllhandle


x = "foo"
y = "bar"


d = {}

for i in range(len(x)):
        char1,char2 = x[i],y[i]
        if char1 not in d:
                if char2 in d.values():
                        print("f")
                d[char1] = char2
        elif d[char1] != char2:
                print("f")
print("t")
        
                





                
                

                
        



        
        
        