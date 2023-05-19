import datetime
import urllib.parse

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/api")
async def makeschedule(request: Request, title: str = "", description: str = "", dates: str = ""):
    context = {"request": request, "title": title, "description": description}

    if dates != "":
        try:
            start, stop = dates.split("/")
            start = datetime.datetime.strptime(start, '%Y%m%dT%H%M%S')
            stop = datetime.datetime.strptime(stop, '%Y%m%dT%H%M%S')
            context["start"] = start.strftime('%Y/%m/%d %H:%M')
            context["stop"] = stop.strftime('%Y/%m/%d %H:%M')
        except:
            dates = ""
            context["start"], context["stop"] = "", ""

    baseurl = "https://www.google.com/calendar/render?"
    d = {"action" : "TEMPLATE", "text" : title,
         "details" : description, "dates" : dates}
    d_qs = urllib.parse.urlencode(d)
    context["url"] = baseurl + d_qs

    return templates.TemplateResponse("index.html", context)
    # ie. 
    # http://localhost/api?title=sample+title&description=Today+is+Friday+in+California&dates=20201201T120000/20201201T121000

@app.get("/")
async def root():
    return RedirectResponse(url="https://github.com/minna-de-hack/schedule-api")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)