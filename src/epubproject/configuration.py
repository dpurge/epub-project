from typing import NamedTuple, Dict, List

class Document(NamedTuple):
    filename: str
    identifier: str
    language: str
    title: str
    templates: str
    authors: List = []
    fonts: List = []
    fontstyles: List = []
    texts: List = []

class Text(NamedTuple):
    title: str
    filename: str
    markdown: str
    html: str
    lang: str
