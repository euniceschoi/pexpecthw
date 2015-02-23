import pexpect
process = pexpect.spawn("echo HELLO")
process.expect("HELLO")

pexpect.spawn("mb -i primates2.nex")
sumt primates2.nex
prim_run_1 = pexpect.run("mb primates.nex")
sump primates2.nex

quit 
