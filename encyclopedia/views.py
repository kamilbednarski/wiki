from django.shortcuts import render
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse

from . import util


def index(request):
    """
    Renders page with list of all entries,
    as a hrefs to each of them.
    """
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def entry(request, title):
    """
    Renders page for matching entry.
    """
    return render(request, "encyclopedia/entry.html", {
        "entry": util.get_entry(title),
        "entry_title": util.get_filename(title)
    })

def search(request):
    """
    Searches for entries matching user's input submitted
    via POST method in HTML form.
    """
    if request.method == 'POST':
        
        # Saving query from HTML form submited via POST method.
        query = request.POST['query']

        # If util.get_entry() can't find entry with name equal to query string,
        # search function is trying to find entry with name containing the query,
        # as a substring.
        if not util.get_entry(query):
            list_of_entries = util.list_similar(query)
            return render(request, "encyclopedia/search.html", {
                "query": query,
                "list_of_entries": list_of_entries
            })

        # If util.get_entry() found entry with name equal to query string,
        # search function is rendering it's page.    
        else:
            title = query
            return render(request, "encyclopedia/entry.html", {
                "entry": util.get_entry(title),
                "entry_title": util.get_filename(title)
            })

    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })

def new_page(request):
    """
    Redirects to page with possibility to add new entry.
    """
    return render(request, "encyclopedia/new_page.html")