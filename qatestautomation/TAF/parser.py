import re
from rewriter import configrewrite

def decifer():
    command ="teststand2unit1;SSSFW10.2.10;NWSSFW10.2.1;test_power;"
    splitcommand = re.findall(r'(.*?);', command)

    print(splitcommand)

    configrewrite(splitcommand[0])

decifer()