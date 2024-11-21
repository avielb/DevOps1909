import datetime
from mydep import test as mydep_test, test
from my_other_dep import test as my_other_dep_test
mydep_test()
my_other_dep_test()

# fifi
def wait_for_print():
    from time import sleepd
    sleep(3)
    print("Hello World")

wait_for_print()
print(datetime.datetime.now())
