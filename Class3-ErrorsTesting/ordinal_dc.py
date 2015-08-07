def ordinal(n):
    try:
        n = int(n)
    except:
        return "Not a valid input"
    n=str(n)
    endings = {'1':'st', '2':'nd', '3':'rd'}
    if n[-2:-1] == '1': return n+'th'
    elif n[-1] in endings.keys(): return n+ endings[n[-1]]
    else: return n+'th'
