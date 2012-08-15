def print_badge(badge):
    print '%6d %s: %s' % (badge.award_count, badge.name, badge.description)


def print_badges(site, limit=10):
    for badge in sorted(site.all_nontag_badges(), reverse=True, key=lambda s: s.award_count)[:limit]:
        print_badge(badge)


# eof
