import os
import uuid
import datetime

import arrow
from ics import Calendar, Event

def export_ics(title: str, description: str, dates: str = "",):
    basedir = os.path.dirname(__file__)
    dir_name = "icsdata"
    os.makedirs(os.path.join(basedir, dir_name), exist_ok=True)

    if dates != "":
        try:
            start, end = dates.split("/")
            start = datetime.datetime.strptime(start, '%Y%m%dT%H%M%S')
            end = datetime.datetime.strptime(end, '%Y%m%dT%H%M%S')

        except:
            dates = ""
            start, end = "", ""

    calendar = Calendar()
    event = Event()
    event.name = title
    event.description = description
    event.begin = arrow.get(start).replace(tzinfo="Asia/Tokyo")
    event.end = arrow.get(end).replace(tzinfo="Asia/Tokyo")
    calendar.events.add(event)
    fname = str(uuid.uuid5(uuid.NAMESPACE_DNS, title+description+dates))
    fpath = os.path.join(basedir, dir_name, F"{fname}.ics")

    with open(fpath, 'w') as f:
        f.writelines(calendar.serialize_iter())

    return fpath

if __name__ == '__main__':
    export_ics()