from ebooklib import epub, ITEM_DOCUMENT
from pathlib import Path, PurePath
from .vocabulary_parser import VocabularyParser

def publish_vocabulary_document(doc):
    input_file = PurePath(doc.filename)
    output_file = input_file.with_suffix('.vocabulary.csv')

    parser = VocabularyParser()
    book = epub.read_epub(doc.filename) 

    for item in book.get_items_of_type(ITEM_DOCUMENT):
        content = item.get_content()
        parser.feed(content.decode("utf-8"))
    parser.close()

    vocabulary = parser.get_vocabulary()
    with open(output_file, "w", encoding='utf8') as f:
        f.write("Phrase\tGrammar\tTranscription\tTranslation\tNotes\n")
        for i in vocabulary:
            f.write("{phrase}\t{grammar}\t{transcription}\t{translation}\t{notes}\n".format(
                phrase = i.phrase,
                grammar = i.grammar,
                transcription = i.transcription,
                translation = i.translation,
                notes = i.notes))

    return output_file