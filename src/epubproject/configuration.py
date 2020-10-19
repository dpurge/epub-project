from typing import NamedTuple, Dict, List

class Document(NamedTuple):
    filename: str
    identifier: str
    language: str
    title: str
    templates: str
    authors: List = []
    fonts: List = []
    stylesheets: List = []
    texts: List = []

class Section(NamedTuple):
    text: str
    directory: str
