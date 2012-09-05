#!/usr/bin/env python
#
# Purpose: list, find, print StackExchange sites
#

# todo: this is only to easy run as ./scripts/blah.py, remove it later
import sys
sys.path.append('.')

import optparse

from stacktools.sites import find_site, print_site, print_sites
from stacktools.badges import print_badges

if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.set_usage('%prog [options]')
    parser.set_description('list, find, print StackExchange sites')
    parser.add_option('--site', '-s', dest='site_keyword')
    parser.add_option('--badges', '-b', dest='op_badges', action='store_true')

    (options, args) = parser.parse_args()

    if options.site_keyword:
        site = find_site(options.site_keyword)
    else:
        site = None

    if site:
        if options.op_badges:
            print_badges(site.get_site())
        else:
            print_site(site)
    else:
        print_sites()

# eof
