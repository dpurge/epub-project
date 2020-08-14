# import os
from pathlib import Path, PurePath

from ebooklib import epub
from ebooklib import ITEM_FONT

from .get_file_uid import get_file_uid
from .get_texts import get_texts

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
        with open(font_file, mode='rb') as f:
            font_uid = get_file_uid(filename=font_file, prefix='font')
            font = epub.EpubItem(
                uid = font_uid,
                file_name = 'fonts/{filename}'.format(filename = font_basename),
                media_type = 'application/vnd.ms-opentype',
                content = f.read())
            book.add_item(font)

    for font_stylesheet in doc.fontstyles:
        uid_font_style = get_file_uid(filename=font_stylesheet, prefix='style_fonts')
        style = get_epub_style(uid_font_style, font_stylesheet)
        book.add_item(style)

    book.spine = ['nav']

    book.toc = []
    for textdir in doc.texts:
        for text in get_texts(directory=textdir, templates=doc.templates):
            item = epub.EpubHtml(
                title = text.title,
                file_name = text.filename,
                lang = text.lang)
            item.content = text.html
            book.add_item(item)
            book.spine.append(item)
            print(text.filename)

    book.add_item(epub.EpubNcx())
    
    nav = epub.EpubNav()

    book.add_item(nav)

    epub.write_epub(doc.filename, book, {})
    return doc.filename