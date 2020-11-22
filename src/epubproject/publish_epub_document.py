from pathlib import Path

from .publish import publish_azw3_document, publish_pdf_document, publish_vocabulary_document

def publish_epub_document(doc):
	input_file = Path(doc.filename)

	if input_file.exists():
		yield publish_vocabulary_document(doc)
		# yield publish_azw3_document(doc)
		# yield publish_pdf_document(doc, 'a5')
		# yield publish_pdf_document(doc, 'b6')
	else:
		print('ePub file does not exist: {filename}'.format(filename = doc.filename))
