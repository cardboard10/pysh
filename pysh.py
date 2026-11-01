import __main__
__main__.sh_history=[]
globals()["outs"]=""
def print(arg):
  globals()["outs"]+=str(arg)+"\n"
class pysh:
  def __init__(sh,cd="/bin/",maxh=222):
    sh.history=[]
    sh.maxh=maxh
    sh.cd=cd
    sh.vars={}
    sh.ps1="{cd}$"
    sh.finaloutput=0
    sh.PATH=["bin"]
    sh.lastcmd=[]
    sh.enter()
  def path(sh,p):
    if p.startswith("./"):
      p1=sh.cd
      p2=p[2:]
      if p1.endswith("/"):
        p=p1+p2
      else:
        p=p1+"/"+p2
    elif p.startswith("../"):
      print("going up")
      p1=sh.cd
      p2=p[3:]
      if p1.endswith("/"):
        p1=p1[:-1]
      p1=p1.split("/")
      p1.pop(-1)
      p1="/".join(p1)
      if not p1.startswith("/"):
        p1="/"+p1
      if p1.endswith("/"):
        p=p1+p2
      else:
        p=p1+"/"+p2
    elif not (p.startswith("/") and p.startswith(".")):
      p1=sh.cd
      p2=p
      if p1.endswith("/"):
        p=p1+p2
      else:
        p=p1+"/"+p2
    return p
  def enter(sh):
    import sh5 as SH
    globals()["outs"]=""
    while True:
      if len(globals()["outs"])>sh.maxh:
        globals()["outs"]=globals()["outs"][len(globals()["outs"])-sh.maxh:]
      __main__.sh_history=sh.history
      cmd=SH.Input(globals()["outs"]+"\n"+sh.ps1.replace("{cd}",sh.cd))
      sh.history.append(cmd)
      if cmd in ["exit","exit()","quit","quit()"]:
        break
      elif cmd!="":
        out=sh.exe(cmd.split(" "))
        if type(out)==int:
          print(f"{cmd.split(" ")[0]} exited with exitcode:{out}")
        else:print(out)
  def oenter(sh,grabcmd=input):
    while True:
      cmd=grabcmd(sh.ps1.replace("{cd}",sh.cd))
      if cmd in ["exit","exit()","quit","quit()"]:
        break
      elif cmd!="":
        out=sh.exe(cmd.split(" "))
        if type(out)==int:
          print(f"{cmd.split(" ")[0]} exited with exitcode:{out}")
        else:print(out)
  def exe(sh,cmd):
    sh.lastcmd=cmd.copy()
    print(f"${cmd}")
    sh.finaloutput=0
    try:
      pi=cmd.index(">>")
      if len(cmd)==pi+2:
        pipefile=cmd.pop(-1)
        pipefile=sh.path(pipefile)
        cmd.pop(-1)
    except ValueError:pipefile=None
    fp=cmd[0].replace("./",sh.cd)
    if not fp.endswith(".py"):
      fp+=".py"
    if not (fp.startswith("/") and fp.startswith(".")):
      found=False
      for d in sh.PATH:
        if not d.startswith("/"):
          d="/"+d
        if not d.endswith("/"):
          d=d+"/"
        try:
          open(d+fp).close()
          found=True
          fp=d+fp
          break
        except OSError:pass
      if not found:
        sh.finaloutput=6
        print(f"cmd '{fp}' not found")
        return 1
    else:
      fp=sh.path(fp)
    file=open(fp)
    fc=file.read()
    file.close()
    cmd[0]=fp
    initcode="""
import sys
#print(sys.argv)
sys.argv.clear()
sys.argv.extend(params)
sys.modules["_shell"]=sh
def exit(code=0):
  import _shell as sh
  sh.finaloutput=code
try:del fp
except:pass
try:del params
except:pass
try:del sys
except:pass
import _shell
import sys
args1=sys.argv
args2=_shell.lastcmd
if not args1==args2:
  if len(args1)==0:
    sys.argv.clear()
    sys.argv.extend(_shell.lastcmd)
"""
    code=initcode+fc
    exec(code,dict(fp=cmd[0],params=cmd,sh=sh))
    out=sh.finaloutput
    if pipefile==None:
      return out
    else:
      with open(pipefile,"a") as file:
        file.write(out)
      return f"output rerouted to {pipefile}"


pysh()

