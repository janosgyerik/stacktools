from stackauth import StackAuth

all_sites = StackAuth().sites()
sites = filter(lambda x: not x.name.endswith('Meta'), all_sites)


def print_site(site):
    if site is None:
        return
    print '%s - %s' % (site.name, site.site_url)


def print_sites():
    for site in sites:
        print_site(site)


def find_site(keyword):
    for site in sites:
        if keyword.lower() in site.name.lower():
            return site


# eof
