import subprocess

from pathlib import Path, PurePath
from .external_tool import calibre_ebook_convert

def publish_azw3_document(doc):
	input_file = PurePath(doc.filename)

	output_file = input_file.with_suffix('.azw3')
	result = subprocess.run([calibre_ebook_convert, str(input_file), str(output_file)])
	return output_file