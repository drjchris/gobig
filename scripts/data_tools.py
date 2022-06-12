from datetime import datetime
from pandas import date_range

def listDates(sdate: str, edate: str, duration:str) -> list:
    # do the day thing
    if duration.lower()=='d':
        outlistr = date_range(start=sdate, end=edate)
        outlist = [str(x)[:10] for x in outlistr]
        return outlist
    # do the month thing
    elif duration.lower()=='m':
        outlistr = date_range(sdate[:7], edate, freq='MS')
        outlist = [str(x)[:10] for x in outlistr]
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