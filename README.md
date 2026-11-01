# pysh
pysh is something like a mini-unix user space? for the casio monochrome fx-9750Giii, requires the gint lib which is provded by the pythonExtra addin




This is A Mini Unix-like Shell & Script Runner for Python on Casio fx-9750Giii calculators with the pythonExtra add-in

relative path syntax support:
../
./
/

other syntax support:
cmd >> filepath
! special note: I for some reason didn't include syntax for separating commands with ';'

when you run a cmd it takes the file at that position with the cmd name + ".py" and executes it. the script being executed is sandboxed and has special print and exit cmds to give support to the pysh shell, it also provides a _shell library to interact with the shell for things like changing the current working directory

download the pysh-core.zip for the runner
and if you want some basic commands to use with it you can download the pysh-basic-cmds.zip file and extract it into the /bin/ dir of your casio's filesystem

enjoy!
P.S. I currently do not have access to my calculator as it has been misplaced so unless I setup a VM for testing stuff, or find it, it is unlikely I will be upgrading this project
