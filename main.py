import datetime
import os
import urllib.parse

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from src.ics_util import export_ics

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root():
    return RedirectResponse(url="https://github.com/minna-de-hack/schedule-api")

@app.get("/api")
async def make_schedule(request: Request, title: str = "", description: str = "", dates: str = ""):
    context = {"request": request, "title": title, "description": description, "dates":dates}

    if dates != "":
        try:
            start, end = dates.split("/")
            start = datetime.datetime.strptime(start, '%Y%m%dT%H%M%S')
            end = datetime.datetime.strptime(end, '%Y%m%dT%H%M%S')
            context["start"] = start.strftime('%Y/%m/%d %H:%M')
            context["end"] = end.strftime('%Y/%m/%d %H:%M')
        except:
            dates = ""
            context["start"], context["end"] = "", ""

    baseurl = "https://www.google.com/calendar/render?"
    d = {"action" : "TEMPLATE", "text" : title,
         "details" : description, "dates" : dates}
    d_qs = urllib.parse.urlencode(d)
    context["url"] = baseurl + d_qs
    context["export_url"] = "/api/export?" + urllib.parse.urlencode({"title" : title, "description" : description, "dates" : dates})

    return templates.TemplateResponse("index.html", context)

# http://localhost/api/export?title=sample+title&description=Today+is+Friday+in+California&dates=20201201T120000/20201201T121000
@app.get("/api/export")
async def export_schedule(title: str = "", description: str = "", dates: str = ""):
    try:
        fpath = export_ics(title, description, dates)
    except:
        pass

    response = FileResponse(
        path=fpath,
        filename=os.path.split(fpath)[-1])

    return response

# http://localhost/sample/
@app.get("/sample", response_class=HTMLResponse)
async def sample():
    return """
    <html>
        <head>
            <title>sample HTML</title>
        </head>
        <body>
            <iframe style="border:0" width="400" src="http://localhost/api?title=sample+title&description=Today+is+Friday+in+California&dates=20201201T120000/20201201T121000"></iframe>
        </body>
    </html>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)