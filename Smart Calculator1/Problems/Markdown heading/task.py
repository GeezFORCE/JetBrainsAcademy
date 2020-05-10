def heading(title, level=1):
    if 1 < level < 6:
        return "#" * level + " " + title
    elif level >= 6:
        return "#" * 6 + " " + title
    else:
        return "#" + " " + title
