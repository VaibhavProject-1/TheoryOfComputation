import AutomaPy

from AutomaPy.examples import EndingWithOneZeroOne

dfa = EndingWithOneZeroOne()

print(dfa.check_string("101"))
