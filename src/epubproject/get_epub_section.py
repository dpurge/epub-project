import jinja2
import markdown

from pathlib import Path
from ebooklib import epub
from ebooklib.epub import EpubHtml
from lxml.html import fromstring

from .task_tools import uid_for_path

def get_epub_section(section, templates, sequence):

    templateLoader = jinja2.FileSystemLoader(searchpath=templates)
    templateEnv = jinja2.Environment(loader=templateLoader)

    md = markdown.Markdown(extensions=[
        'tables',
        'full_yaml_metadata',
        'attr_list'])

    epub_section = None
    text = None

    section_markdown = Path(section.text)
    if section_markdown.exists():
        with open(section_markdown, encoding='utf-8') as f:
            txt = f.read()
            html = md.convert(txt)
            meta = getattr(md, "Meta")
            md.reset()
        if meta.get('ready', False):
            tpl = templateEnv.get_template(
                '{template}.html'.format(template = meta.get('template', 'section')))
            lang = meta.get('lang', 'en')
            html = tpl.render(contents = html, meta = meta)

            doc = fromstring(html)

            fn = 'section-{:0>4}.xhtml'.format(next(sequence))
            uid = uid_for_path(fn)
            title = doc.find(".//h1").text
            text = EpubHtml(
                uid = uid,
                file_name = fn,
                title = title,
                lang = lang)
            text.content = title
            style = meta.get('style')
            if style:
                text.add_link(href='style/{style}.css'.format(style=style), rel='stylesheet', type='text/css')
            epub_section = epub.Section(title, fn)
    return epub_section, text