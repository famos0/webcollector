#!/usr/bin/env python3

import sys
from lib.main import main
from lib.usage import usage   

if __name__ == "__main__":

    if not len(sys.argv[1:]):
        usage()
    main(sys.argv[1:])
