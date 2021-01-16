from pathlib import Path

from .publish import publish_azw3_document, publish_pdf_document, publish_vocabulary_document

def publish_epub_document(doc, formats = ('pdf-a5')):
	input_file = Path(doc.filename)

	if input_file.exists():
		if 'vocabulary' in formats:
			yield publish_vocabulary_document(doc)
		if 'azw3' in formats:
			yield publish_azw3_document(doc)
		if 'pdf-a5' in formats:
			yield publish_pdf_document(doc, 'a5')
		if 'pdf-b6' in formats:
			yield publish_pdf_document(doc, 'b6')
	else:
		print('ePub file does not exist: {filename}'.format(filename = doc.filename))
