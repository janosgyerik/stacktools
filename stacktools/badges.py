def print_badge(badge):
    print '%6d %s: %s' % (badge.award_count, badge.name, badge.description)


def print_badges(site, limit=0):
    badges_sorted = sorted(site.all_nontag_badges(), reverse=True, key=lambda s: s.award_count)
    if limit:
        badges = badges_sorted[:limit]
    else:
        badges = badges_sorted

    for badge in badges:
        print_badge(badge)


# eof
