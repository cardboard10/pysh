import sys
import _shell as sh

p1=sh.path(sys.argv[1])
p2=sh.path(sys.argv[2])
f1=open(p1,"r")
f2=open(p2,"w")
f2.write(f1.read())
f1.close()
f2.close()
f1=open(p1,"w")
f1.write("")
f1.close()



