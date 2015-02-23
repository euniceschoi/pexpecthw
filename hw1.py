newprimates = open("primates2.nex", "w")
oldprimates = open("primates.nex").read()

for line in oldprimates:
    newprimates.write(line.replace("mcmc", "mcmcp"))
newprimates.close()


child = pexpect.spawn("mb -i primates2.nex") 
#tells mrbayes to run in interactive mode
#send the string "mcmc" to the process
child.sendline(r"mcmc") 
#tells mrbayes to stop the analysis
child.sendline("no") 
child.expect("MrBayes >") 
# wait for the mrbayes prompt
print child.before 
# child.before shows all of the screen output
quit
