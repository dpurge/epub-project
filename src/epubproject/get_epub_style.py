import uuid
from ebooklib.epub import EpubItem
from pathlib import Path

def get_epub_style(filename):
    p = Path(filename)

    if not p.is_file():
        raise Exception('Stylesheet file does not exist: {filename}'.format(filename = filename))

    fn = 'style/{filename}'.format(filename = p.name)
    uid = uuid.uuid5(uuid.NAMESPACE_DNS, fn).hex

    with open(p, mode='rb') as f:
        style = EpubItem(
            uid = uid,
            file_name = fn,
            media_type = 'text/css',
            content = f.read())

    return style