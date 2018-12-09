#!/usr/bin/env python

import os
import random
import string
import sys
import time
from fpdf import FPDF

if sys.version_info[0] != 3:
    print("This script requires Python version 3.x")
    sys.exit(1)

# when run with 'test' argument, this is the default output file
TEST_PDF = 'example.pdf'

# BabelStonePigpen from http://www.babelstone.co.uk/Fonts/Pigpen.html
PIGPEN_FONT_FILE = 'BabelStonePigpen.ttf'
PIGPEN_FONT = 'BabelStonePigpen'

# braille from https://www.dafont.com/braille.font
BRAILLE_FONT_FILE = 'BRAILLE1.ttf'
BRAILLE_FONT = 'BRAILLE1'

SUPPORTED_TYPES = ['decimal', 'binary', 'morse', 'hex']

BRAILLE_SUPPORTED = False
if os.path.exists(BRAILLE_FONT_FILE):
    SUPPORTED_TYPES.append('braille')
    BRAILLE_SUPPORTED = True

PIGPEN_SUPPORTED = False
if os.path.exists(PIGPEN_FONT_FILE):
    SUPPORTED_TYPES.append('pigpen')
    PIGPEN_SUPPORTED = True

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'}
    # '1': '.----',
    # '2': '..---',
    # '3': '...--',
    # '4': '....-',
    # '5': '.....',
    # '6': '-....',
    # '7': '--...',
    # '8': '---..',
    # '9': '----.',
    # '0': '-----',
    # ',': '--..--',
    # '.': '.-.-.-',
    # '?': '..--..',
    # '/': '-..-.',
    # '-': '-....-',
    # '(': '-.--.',
    # ')': '-.--.-'}

PHONETIC = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie',
    'D': 'Delta',
    'E': 'Echo',
    'F': 'Foxtrot',
    'G': 'Golf',
    "H": "Hotel",
    'I': 'India',
    'J': 'Juliet',
    'K': 'Kilo',
    'L': 'Lima',
    'M': 'Mike',
    'N': 'November',
    'O': 'Oscar',
    'P': 'Papa',
    'Q': 'Quebec',
    'R': 'Romeo',
    'S': 'Sierra',
    'T': 'Tango',
    'U': 'Uniform',
    'V': 'Victor',
    'W': 'Whiskey',
    'X': 'Xray',
    'Y': 'Yankee',
    'Z': 'Zulu'}

BRAILLE = {
    'A': chr(10241),
    'B': chr(10243),
    'C': chr(10249),
    'D': chr(10265),
    'E': chr(10257),
    'F': chr(10251),
    'G': chr(10267),
    "H": chr(10259),
    'I': chr(10250),
    'J': chr(10266),
    'K': chr(10245),
    'L': chr(10247),
    'M': chr(10253),
    'N': chr(10269),
    'O': chr(10261),
    'P': chr(10255),
    'Q': chr(10271),
    'R': chr(10263),
    'S': chr(10254),
    'T': chr(10270),
    'U': chr(10277),
    'V': chr(10279),
    'W': chr(10298),
    'X': chr(10285),
    'Y': chr(10301),
    'Z': chr(10293)}

UPPER_ALPHA = string.ascii_uppercase

ALPHA_TO_NUM = {}
for i, x in enumerate(UPPER_ALPHA, 1):
    ALPHA_TO_NUM[x] = i

class FNC41Encoder():
    def __init__(self):
        self.encoded_msg = None

        self.pdf = FPDF()
        self.pdf.add_page()

        if os.path.exists(PIGPEN_FONT_FILE):
            self.pdf.add_font(PIGPEN_FONT, '', PIGPEN_FONT_FILE, uni=True)
        else:
            print('[!] pigpen font not found, pigpen not supported')

        if os.path.exists(BRAILLE_FONT_FILE):
            self.pdf.add_font(BRAILLE_FONT, '', BRAILLE_FONT_FILE, uni=True)
        else:
            print('[!] braille font not found, braille not supported')

        self.pdf.set_font('Times', '', 16)

    def save(self, outfile):
        self.pdf.output(outfile, 'F')
        print("message written to '{}'".format(outfile))

    def write_msg(self, msg, encode_type='decimal', wrap=True):
        self.encode_type = encode_type

        msg = msg.upper()

        if encode_type == 'decimal':
            self._encode_decimal(msg)

        if encode_type == 'morse':
            self._encode_morse(msg)

        if encode_type == 'braille':
            self.encoded_msg = msg

        if encode_type == 'binary':
            self._encode_binary(msg)

        if encode_type == 'pigpen':
            self.encoded_msg = msg

        if encode_type == 'hex':
            self._encode_hex(msg)

        if self.encoded_msg:
            self.pdf.set_font('Times', '', 16)
            if self.encode_type == 'pigpen' and PIGPEN_SUPPORTED:
                self.pdf.set_font(PIGPEN_FONT, '', 16)
            if self.encode_type == 'braille' and BRAILLE_SUPPORTED:
                self.pdf.set_font(BRAILLE_FONT, '', 16)
            # fpdf.cell(w, h = 0, txt = '', border = 0, ln = 0, align = '', fill = False, link = '')
            len = self.pdf.get_string_width(self.encoded_msg) + 5
            if wrap:
                self.pdf.multi_cell(0, 10, self.encoded_msg)
            else:
                self.pdf.cell(len, 10, self.encoded_msg, 0)
        else:
            raise Exception("call the encode() method first")

    def write_msg_random(self, msg):
        counter = 0
        for s in msg.split(' '):
            t = random.choice(SUPPORTED_TYPES)
            self.write_msg(s, t, False)
            counter += 1
            if counter % 3 == 0:
                self.pdf.ln(10)

    def _encode_decimal(self, msg):
        l = []
        for c in msg:
            if c in ALPHA_TO_NUM.keys():
                l.append(str(ALPHA_TO_NUM[c]))
            else:
                l.append(c)
        self.encoded_msg = " ".join(l)

    def _encode_hex(self, msg):
        l = []
        for c in msg:
            if c in ALPHA_TO_NUM.keys():
                l.append(hex(ALPHA_TO_NUM[c]))
            else:
                l.append(c)
        self.encoded_msg = " ".join(l)

    def _encode_morse(self, msg):
        l = []
        for c in msg:
            if c in MORSE_CODE_DICT.keys():
                l.append(str(MORSE_CODE_DICT[c]))
            else:
                l.append(c)
        self.encoded_msg = " ".join(l)

    def _encode_braille(self, msg):
        l = ''
        for c in msg:
            if c in BRAILLE.keys():
                l += BRAILLE[c]
            else:
                l += c
        self.encoded_msg = l

    def _encode_binary(self, msg):
        l = []
        for c in msg:
            if c in ALPHA_TO_NUM.keys():
                l.append(str(bin(ALPHA_TO_NUM[c]).lstrip('0b')))
            else:
                l.append(c)
        self.encoded_msg = " ".join(l)

def example1(outfile):
    test_string = 'hello there, this is a test with a long string'

    encoder = FNC41Encoder()
    for t in SUPPORTED_TYPES:
        encoder.write_msg(test_string, t)
        print('- writing {}'.format(t))
    encoder.save(outfile)

def example2(outfile):
    test_string = 'hello there, this is a test with a long string'

    encoder = FNC41Encoder()
    encoder.write_msg_random(test_string)
    print('- writing {}'.format('random'))
    encoder.save(outfile)

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'example1':
        example1(TEST_PDF)
        sys.exit(0)

    if len(sys.argv) == 2 and sys.argv[1] == 'example2':
        example1(TEST_PDF)
        sys.exit(0)

    print("Please specify encode type: %r" % SUPPORTED_TYPES)
    encode_type = input('type: ')
    if encode_type not in SUPPORTED_TYPES:
        print("'{}' is not a supported type".format(encode_type))
        sys.exit(1)

    print("Please specify message to:")
    msg = input('message: ')

    if msg:
        encoder = FNC41Encoder()
        encoder.write_msg(msg, encode_type)
        encoder.save('temp.pdf')
