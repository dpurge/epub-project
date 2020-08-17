# import os
import uuid

from pathlib import Path, PurePath

from ebooklib import epub
# from ebooklib import ITEM_FONT

from .get_epub_font import get_epub_font
from .get_epub_style import get_epub_style
from .get_epub_texts import get_epub_texts

def create_epub_document(doc):

    doc_dir = PurePath(doc.filename).parent
    Path(doc_dir).mkdir(parents=True, exist_ok=True)

    book = epub.EpubBook()

    book.set_identifier(doc.identifier)
    book.set_title(doc.title)
    book.set_language(doc.language)

    for author in doc.authors:
        book.add_author(author)

    for font_file in doc.fonts:
        book.add_item(get_epub_font(font_file))

    for stylesheet in doc.stylesheets:
        book.add_item(get_epub_style(stylesheet))

    book.spine = ['nav']

    book.toc = []
    for textdir in doc.texts:
        for text in get_epub_texts(directory=textdir, templates=doc.templates):
            book.add_item(text)
            book.spine.append(text)
            book.toc.append(text)

    book.add_item(epub.EpubNcx())
    
    nav = epub.EpubNav()
    style_nav = book.get_item_with_id(uuid.uuid5(uuid.NAMESPACE_DNS, 'style/nav.css').hex)
    if style_nav:
        nav.add_item(style_nav)
    book.add_item(nav)

    epub.write_epub(doc.filename, book, {})
    return doc.filename