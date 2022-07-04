#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in my_list:
        biggest = list(max(i))
        print("{:d}".format(biggest))
