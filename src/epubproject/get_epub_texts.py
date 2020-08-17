import jinja2
import markdown
import uuid

from pathlib import Path
from ebooklib.epub import EpubHtml
from lxml.html import fromstring

# from .configuration import Text

def sequence():
    x = 0
    while True:
        x += 1
        yield x

def get_epub_texts(directory, templates):

    templateLoader = jinja2.FileSystemLoader(searchpath=templates)
    templateEnv = jinja2.Environment(loader=templateLoader)

    md = markdown.Markdown(extensions=[
        'tables',
        'full_yaml_metadata',
        'attr_list'])

    text_sequence = sequence()

    for filename in Path(directory).glob('**/*.md'):
        with open(filename, encoding='utf-8') as f:
            txt = f.read()
            html = md.convert(txt)
            meta = getattr(md, "Meta")
            md.reset()
        if meta.get('ready', False):
            tpl = templateEnv.get_template(
                '{template}.html'.format(template = meta.get('template', 'default')))
            lang = meta.get('lang', 'en')
            html = tpl.render(contents = html, meta = meta)

            doc = fromstring(html)

            fn = 'text-{:0>4}.xhtml'.format(next(text_sequence))
            uid = uuid.uuid5(uuid.NAMESPACE_DNS, fn).hex
            text = EpubHtml(
                uid = uid,
                file_name = fn,
                title = doc.find(".//h1").text,
                lang = lang)
            text.content = html

            style = meta.get('style')
            if style:
                text.add_link(href='style/{style}.css'.format(style=style), rel='stylesheet', type='text/css')

            yield text