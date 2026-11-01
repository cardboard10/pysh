
import _shell
import sys
args1=sys.argv
args2=_shell.lastcmd
if not args1==args2:
  if len(args1)==0:
    sys.argv.clear()
    sys.argv.extend(_shell.lastcmd)
p=sys.argv[1]
p=_shell.path(p)
_shell.cd=p
