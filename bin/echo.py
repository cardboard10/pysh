import sys
#import _shell as sh

args=sys.argv
args.pop(0)
if len(args)>0:
  out=" ".join(args)
  if out.startswith("\"") and out.endswith("\""):
    out=out[1:-1]
  exit(out)

