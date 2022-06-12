from datetime import datetime

def listDates(sdate: str, edate: str) -> list:
    start_date = datetime.strptime(sdate.strip(), '%Y-%m-%d')
    end_date = datetime.strptime(edate.strip(), '%Y-%m-%d')
    outlist = [datetime.strptime('%2.2d-%2.2d' % (y, m), '%Y-%m').strftime('%Y-%m-01')
        for y in range(start_date.year, end_date.year + 1)
        for m in range(start_date.month if y == start_date.year else 1, end_date.month + 1 if y == end_date.year else 13)]
    return outlist


def countValues(rawlist: list) -> list:
    interdict = {}
    for inval in sorted(list(set(rawlist))):
        interdict[inval] = 0
    for eval in rawlist:
        interdict[eval]+=1
    outlist = []
    for eent in interdict:
        outlist.append({'value': eent, 'count': interdict[eent]})
    return outlist