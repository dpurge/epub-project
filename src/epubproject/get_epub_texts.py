import jinja2
import markdown

from pathlib import Path
from ebooklib.epub import EpubHtml
from lxml.html import fromstring

from .extensions import VocabularyListExtension
from .extensions import DialogListExtension
from .task_tools import uid_for_path

def get_epub_texts(directory, templates, sequence):

    templateLoader = jinja2.FileSystemLoader(searchpath=templates)
    templateEnv = jinja2.Environment(loader=templateLoader)

    md = markdown.Markdown(extensions=[
        'tables',
        'full_yaml_metadata',
        'attr_list',
        VocabularyListExtension(),
        DialogListExtension()])

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

            fn = 'text-{:0>4}.xhtml'.format(next(sequence))
            uid = uid_for_path(fn)
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
