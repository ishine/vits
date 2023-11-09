import re
import cn2an
import opencc



# List of (Latin alphabet, ipa) pairs:
_latin_to_ipa = [(re.compile('%s' % x[0]), x[1]) for x in [
    ('A', 'ei˥'),
    ('B', 'biː˥'),
    ('C', 'siː˥'),
    ('D', 'tiː˥'),
    ('E', 'iː˥'),
    ('F', 'e˥fuː˨˩'),
    ('G', 'tsiː˥'),
    ('H', 'ɪk̚˥tsʰyː˨˩'),
    ('I', 'ɐi˥'),
    ('J', 'tsei˥'),
    ('K', 'kʰei˥'),
    ('L', 'e˥llou˨˩'),
    ('M', 'ɛːm˥'),
    ('N', 'ɛːn˥'),
    ('O', 'ou˥'),
    ('P', 'pʰiː˥'),
    ('Q', 'kʰiːu˥'),
    ('R', 'aː˥lou˨˩'),
    ('S', 'ɛː˥siː˨˩'),
    ('T', 'tʰiː˥'),
    ('U', 'juː˥'),
    ('V', 'wiː˥'),
    ('W', 'tʊk̚˥piː˥juː˥'),
    ('X', 'ɪk̚˥siː˨˩'),
    ('Y', 'waːi˥'),
    ('Z', 'iː˨sɛːt̚˥')
]]


def number_to_cantonese(text):
    return re.sub(r'\d+(?:\.?\d+)?', lambda x: cn2an.an2cn(x.group()), text)


def latin_to_ipa(text):
    for regex, replacement in _latin_to_ipa:
        text = re.sub(regex, replacement, text)
    return text

converter = None
def init_converter():
    global converter
    from pathlib import Path
    if Path('./jyutjyu.json').is_file():
        converter = opencc.OpenCC('./jyutjyu.json')
    else:
        converter = opencc.OpenCC('jyutjyu')

def cantonese_to_ipa(text):
    if converter is None:
        init_converter()
    text = number_to_cantonese(text.upper())
    text = converter.convert(text).replace('-','').replace('$',' ')
    text = re.sub(r'[A-Z]', lambda x: latin_to_ipa(x.group())+' ', text)
    text = re.sub(r'[、；：]', '，', text)
    text = re.sub(r'\s*，\s*', ', ', text)
    text = re.sub(r'\s*。\s*', '. ', text)
    text = re.sub(r'\s*？\s*', '? ', text)
    text = re.sub(r'\s*！\s*', '! ', text)
    text = re.sub(r'\s*$', '', text)
    return text
