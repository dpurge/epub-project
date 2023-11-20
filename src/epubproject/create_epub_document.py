# import os
import uuid

from pathlib import Path, PurePath

from ebooklib import epub
# from ebooklib import ITEM_FONT

from .get_epub_font import get_epub_font
from .get_epub_style import get_epub_style
from .get_epub_section import get_epub_section
from .get_epub_texts import get_epub_texts
from .task_tools import sequence, uid_for_path

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
    section_sequence = sequence()
    text_sequence = sequence()
    for s in doc.texts:

        section, text = get_epub_section(section=s, templates=doc.templates, sequence = section_sequence)
        if section and text:
            book.add_item(text)
            book.spine.append(text)

            section_texts = []
            for text in get_epub_texts(directory=s.directory, templates=doc.templates, sequence = text_sequence):
                book.add_item(text)
                book.spine.append(text)
                section_texts.append(text)

            book.toc.append((section, section_texts))

    
    
    ncx = epub.EpubNcx()
    nav = epub.EpubNav()
    style_nav = book.get_item_with_id(uid_for_path('style/nav.css'))
    if style_nav:
        ncx.add_item(style_nav)
        nav.add_item(style_nav)
    book.add_item(ncx)
    book.add_item(nav)

    epub.write_epub(doc.filename, book, {})
    return doc.filename