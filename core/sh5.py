
import __main__
import keymap as keymap
from time import sleep,time
from gint import getkey,dtext,dclear,dupdate,KEY_SHIFT,KEY_ALPHA,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,clearevents,keypressed,\
KEY_DEL,pollevent,KEYEV_DOWN,KEY_F1,KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT,KEY_EXIT,KEY_EXE,KEY_OPTN,KEY_ON,clearevents,keypressed

globals()["scroll_lock"]=True
globals()["history"]=__main__.sh_history
alpha=False
shift=False
curstr=">>>"
scroll=0
import sys
__main__.scroll=globals()["scroll"]




def logic():
  e=pollevent()
  if e.type==KEYEV_DOWN:
    key(e)
  if globals()["cursor"]>len(globals()["history"][globals()["curstr"]]):
    globals()["cursor"]=len(globals()["history"][globals()["curstr"]])
  elif globals()["cursor"]<0:
    globals()["cursor"]=0
globals()["cursorshown"]=True
globals()["lastflip"]=time()
def draw():
  dclear(0)
  thisframe=time()
  cs=globals()["prompt"]+globals()["history"][globals()["curstr"]]
  if thisframe-globals()["lastflip"]>=1:
    globals()["lastflip"]=thisframe
    globals()["cursorshown"]=not globals()["cursorshown"]
  if globals()["cursorshown"]:
    cs+=" "
    cs=list(cs)
    if cs[globals()["cursor"]+len(globals()["prompt"])]=="\n":
      cs.insert(globals()["cursor"]+len(globals()["prompt"]),"_")
    else:
      cs[globals()["cursor"]+len(globals()["prompt"])]="_"
    cs="".join(cs)
  cs0=cs.split("\n")
  cs=[]
  for line in cs0:
    if len(line)<19:
      cs.append(line)
    else:
      i=0
      lin=""
      for c in line:
        if i<=19:
          lin+=c
        if i==19:
          cs.append(lin+"\\")
          lin=""
          i=0
        else:i+=1
      cs.append(lin)
  if globals()["scroll_lock"]:
    globals()["scroll"]=-((len(cs)-6)*10)
  for line,i in zip(cs,range(len(cs))):
    dtext(0,(i*10)+globals()["scroll"],3,line)
  if globals()["alpha"] and globals()["shift"]:
    dtext(120,50,3,"A")
  elif globals()["alpha"]:dtext(120,50,3,"a")
  elif globals()["shift"]:dtext(120,50,3,"s")
  else:dtext(120,50,3,"1")
  dupdate()
def key(key):
  if key.key==KEY_OPTN:
    globals()["scroll_lock"]=not globals()["scroll_lock"]
  if globals()["scroll_lock"]:
    if key.key==KEY_UP:
      globals()["curstr"]-=1
    if key.key==KEY_DOWN:
      globals()["curstr"]+=1
    if key.key==KEY_UP or key.key==KEY_DOWN:
      if globals()["curstr"]>=len(globals()["history"]):
        globals()["curstr"]=0
      elif globals()["curstr"]<0:
        globals()["curstr"]=len(globals()["history"])-1
  else:
    if key.key==KEY_UP:
      globals()["scroll"]+=10
    if key.key==KEY_DOWN:
      globals()["scroll"]-=10
  if keypressed(KEY_ON):globals()["history"][globals()["curstr"]]=""
  if key.key==KEY_LEFT:
    globals()["cursor"]-=1
    if globals()["cursor"]<0:globals()["cursor"]=0
  if key.key==KEY_RIGHT:
    globals()["cursor"]+=1
    if globals()["cursor"]>len(globals()["curstr"]):globals()["cursor"]=len(globals()["curstr"])
  #if key.key==KEY_EXIT:
  #  globals()["running"]=0
  if key.key==KEY_ALPHA:
    globals()["alpha"]=not globals()["alpha"]
    #print("alpha")
  if key.key==KEY_SHIFT:
    globals()["shift"]=not globals()["shift"]
    #print("shift")
  if key.key==KEY_DEL and globals()["cursor"]>0:
    new=list(globals()["history"][globals()["curstr"]])
    r1=new.pop(globals()["cursor"]-1)
    #if r1=="\n" and globals()["curstr"][globals()["cursor"]-1]=="\r":
    #  new.pop(globals()["cursor"]-1)
    #  globals()["cursor"]-=1
    globals()["cursor"]-=1
    globals()["history"][globals()["curstr"]]="".join(new)
  if key.key==KEY_EXE:
    exe()
  k=key.key
  m=""
  if globals()["alpha"]:m+="a"
  if globals()["shift"]:m+="s"
  try:
    cs=list(globals()["history"][globals()["curstr"]])
    cs.insert(globals()["cursor"],keymap.keymap[(k,m)])
    globals()["history"][globals()["curstr"]]="".join(cs)
    globals()["cursor"]+=1
  except KeyError:
    pass
  clearevents()


def exe():
  globals()["running"]=0
globals()["prompt"]=""
def Input(prompt=":",default=""):#,scroll=0):
  globals()["scroll"]=__main__.scroll
  globals()["prompt"]=prompt.replace("\r\n","\n")
  globals()["curstr"]=len(globals()["history"])
  globals()["history"].append(default)
  globals()["running"]=1
  globals()["cursor"]=len(globals()["history"][globals()["curstr"]])
  while globals()["running"]==1:
    logic()
    draw()
  __main__.scroll=globals()["scroll"]
  if globals()["history"][globals()["curstr"]].endswith("\n"):
    return globals()["history"][globals()["curstr"]][:-1]
  else:
    return globals()["history"][globals()["curstr"]]



