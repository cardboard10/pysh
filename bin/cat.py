import sys
import _shell as sh
sys.argv[1]
p=sh.cd
globals()["debug"]=[]
def print(*a):
  globals()["debug"].append(", ".join(a))
if len(sys.argv)>1:
  p=sys.argv[1]
p=sh.path(p)
#for i in range(1):
try:
  print(f"atempting to access file:{p}")
  f=open(p)
  fc=f.read()#f.read(sh.maxh)
  f.close()
  exit(fc)
except OSError:
  print("their was a problem accessing that file")
  exit(1)
