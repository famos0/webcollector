#!/usr/bin/env python3

import sys
from lib.main import *
from lib.usage import usage   

if __name__ == "__main__":

    if not len(sys.argv[1:]):
        usage()
    program = Program()
    program.main(sys.argv[1:])
