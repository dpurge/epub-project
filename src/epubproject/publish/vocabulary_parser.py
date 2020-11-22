from html.parser import HTMLParser
from collections import namedtuple

class VocabularyParser(HTMLParser):
    """
    """

    VocabularyRecord = namedtuple('VocabularyRecord',['phrase','grammar','transcription','translation','notes']) 

    def __init__(self):
        super().__init__()
        self._vocabulary = []
        self._state_name = []
        self._state_tag = []
        self._record = {
            'phrase': '',
            'grammar': '',
            'transcription': '',
            'translation': '',
            'notes': ''
        }

    def handle_starttag(self, tag, attrs):
        for name,value in attrs:
            if name == 'class' and value.startswith('vocabulary-'):
                self._state_name.append(value)
                self._state_tag.append(tag)

    def handle_endtag(self, tag):
        if tag == self.get_state_tag():
            state_name = self._state_name.pop(-1)
            state_tag = self._state_tag.pop(-1)
            if state_name == 'vocabulary-definition':
                self.add_vocabulary_record()

    def handle_data(self, data):
        #print("Encountered some data  :", data)
        state_name = self.get_state_name()
        if state_name == 'vocabulary-phrase':
            self._record['phrase'] = data
        if state_name == 'vocabulary-grammar':
            self._record['grammar'] = data
        elif state_name == 'vocabulary-transcription':
            self._record['transcription'] = data
        elif state_name == 'vocabulary-translation':
            self._record['translation'] = data
        elif state_name == 'vocabulary-notes':
            self._record['notes'] = data

    def add_vocabulary_record(self):
        self._vocabulary.append(self.VocabularyRecord(
            phrase = self._record['phrase'],
            grammar = self._record['grammar'],
            transcription = self._record['transcription'],
            translation = self._record['translation'],
            notes = self._record['notes']
        ))

        self._record['phrase'] = ''
        self._record['grammar'] = ''
        self._record['transcription'] = ''
        self._record['translation'] = ''
        self._record['notes'] = ''

    def get_vocabulary(self):
        return self._vocabulary

    def get_state_name(self):
        state_name = None
        if self._state_name:
            state_name = self._state_name[-1]
        return state_name

    def get_state_tag(self):
        state_tag = None
        if self._state_tag:
            state_tag = self._state_tag[-1]
        return state_tag