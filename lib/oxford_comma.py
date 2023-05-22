def oxford_comma(items):
    if len(items) > 2:
        slice = ", ".join(items[0:len(items)-1])
        return ", and ".join([slice, items[-1]])
    else:
        return " and ".join(items)
    

