import uuid
from ebooklib.epub import EpubItem
from pathlib import Path

def get_epub_font(filename):
    p = Path(filename)

    if not p.is_file():
        raise 'Font file does not exist: {filename}'.format(filename = filename)

    fn = 'fonts/{filename}'.format(filename = p.name)
    uid = uuid.uuid5(uuid.NAMESPACE_DNS, fn).hex

    with open(p, mode='rb') as f:
        font = EpubItem(
            uid = uid,
            file_name = fn,
            media_type = 'application/vnd.ms-opentype',
            content = f.read())

    return font
