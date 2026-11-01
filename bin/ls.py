import sys
import _shell as sh
p=sh.cd
if len(sys.argv)>1:
  p=sys.argv[1]
p=sh.path(p)

try:
  lsf=open(p+"ls.json")
  import json
  lsd=json.loads(lsf.read())
  lsf.close()
  exit("\n".join(lsd["files"]))
except OSError:
  print("directory not compatible")
  exit(1)

