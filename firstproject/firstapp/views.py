from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def index(request):
    template = "<html>" \
        "This is your first view" \
        "</html>"
    return HttpResponse(content=template)

def get_date(request):
    today = date.today()
    # template = "<html>" \
    #     "Today's date is {}" \
    #     "</html>".format(today)
    template = f'''
    <html>
        Today's date is {today}!!.
    </html>'''
    return HttpResponse(content=template)