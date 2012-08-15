#!/usr/bin/env python
#
# Purpose: list, find, print StackExchange sites
#

# todo: this is only to easy run as ./scripts/blah.py, remove it later
import sys
sys.path.append('.')

import optparse

from stacktools.sites import find_site, print_site, print_sites

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.set_usage('%prog [options]')
    parser.set_description('list, find, print StackExchange sites')
    parser.add_option('--list', '-l', dest='op_list', action='store_true')

    (options, args) = parser.parse_args()

    if options.op_list:
        print_sites()
    else:
        for keyword in args:
            print_site(find_site(keyword))

# eof
