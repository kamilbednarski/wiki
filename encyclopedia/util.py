import re
import random

from markdown import markdown
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def contains(string, substring):
    """
    Checks if string contains substring.
    """
    string = string.lower()
    substring = substring.lower()
    return string.__contains__(substring)


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))

def get_random():
    """
    Returns random entry name.
    """
    list_of_entries = list_entries()
    random_entry = random.choice(list_of_entries)
    return random_entry


def list_similar(query):
    """
    Returns a list of names of encyclopedia entries
    that contains given query as a substring.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if contains(filename, query)))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        markdown_content = f.read().decode("utf-8")
        converted_content = markdown(markdown_content)
        return converted_content
    except FileNotFoundError:
        return None

def get_entry_markdown(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        content = f.read().decode("utf-8")
        return content
    except FileNotFoundError:
        return None


def get_filename(title):
    """
    Gets entry's filename from path. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        with open(f"entries/{title}.md") as f:
            entry_title = f.readline()
            entry_title = entry_title.replace("# ", "")
        return entry_title
    except FileNotFoundError:
        return None