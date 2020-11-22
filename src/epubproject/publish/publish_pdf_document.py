import subprocess

from pathlib import Path, PurePath
from .external_tool import calibre_ebook_convert

def publish_pdf_document(doc, page_format = 'a5'):
	input_file = PurePath(doc.filename)
	output_file = input_file.with_suffix('.{page_format}.pdf'.format(page_format = page_format))

	if page_format == 'a5' or page_format == 'b6':
		parameters = [
			"--paper-size", page_format,
			"--pdf-page-margin-bottom", "36",
			"--pdf-page-margin-left", "24",
			"--pdf-page-margin-right", "24",
			"--pdf-page-margin-top", "24",
			"--pdf-page-numbers"]
	else:
		raise Exception('Unsupported page format: {page_format}'.format(page_format = page_format))


	result = subprocess.run([calibre_ebook_convert, str(input_file), str(output_file)] + parameters)

	return output_file