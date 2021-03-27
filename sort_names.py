from operator import itemgetter

def sort_by_last(names):
    """ This function sorts a list of names by by last name, then first name. 
    One word names are treated as last names
    """
    if len(names) <= 1:
        return names
    # generate tuple for each name
    names_ls = [(x.split()[0], x.split()[-1]) if len(x.split())>1 else [x] for x in names]
    # sort list of tuples by last name then first name
    names_sorted = sorted(names_ls, key = itemgetter(-1, 0))
    # recreat name string from tuples
    f = [(x[0]+ ' ' +x[-1]) if len(x)>1 else x[0] for x in names_sorted]
    return f