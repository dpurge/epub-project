import jinja2
import markdown

from pathlib import Path

from .configuration import Text

def get_texts(directory, templates):

    templateLoader = jinja2.FileSystemLoader(searchpath=templates)
    templateEnv = jinja2.Environment(loader=templateLoader)

    md = markdown.Markdown(extensions=[
        'tables',
        'full_yaml_metadata',
        'attr_list'])

    for filename in Path(directory).glob('**/*.md'):
        with open(filename, encoding='utf-8') as f:
            txt = f.read()
            html = md.convert(txt)
            meta = getattr(md, "Meta")
            md.reset()
        if meta.get('ready', False):
            tpl = templateEnv.get_template(meta.get('template', 'section.html'))
            html = tpl.render(contents = html, meta = meta)
            text = Text(
                filename=filename.as_posix(),
                title='Test title',
                html=html,
                markdown=txt,
                lang=meta.get('lang', 'en'))
            yield text