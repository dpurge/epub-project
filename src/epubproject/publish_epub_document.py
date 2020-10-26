import subprocess

from pathlib import Path, PurePath

def publish_epub_document(doc):
	ebook_convert = "D:\\pgm\\Calibre\\Calibre\\ebook-convert.exe"
	input_file = PurePath(doc.filename)

	output_azw3 = input_file.with_suffix('.azw3')
	result = subprocess.run([ebook_convert, str(input_file), str(output_azw3)])
	yield output_azw3

	# output_pdf = input_file.with_suffix('.pdf')
	# result = subprocess.run([ebook_convert, str(input_file), str(output_pdf),
	# 	"--paper-size", "a5",
	# 	"--pdf-page-margin-bottom", "36",
	# 	"--pdf-page-margin-left", "24",
	# 	"--pdf-page-margin-right", "24",
	# 	"--pdf-page-margin-top", "24",
	# 	"--pdf-page-numbers"])
	# yield output_pdf

	# output_pdf_b6 = input_file.with_suffix('.b6.pdf')
	# result = subprocess.run([ebook_convert, str(input_file), str(output_pdf_b6),
	# 	"--paper-size", "b6",
	# 	"--pdf-page-margin-bottom", "36",
	# 	"--pdf-page-margin-left", "24",
	# 	"--pdf-page-margin-right", "24",
	# 	"--pdf-page-margin-top", "24",
	# 	"--pdf-page-numbers"])
	# yield output_pdf_b6
