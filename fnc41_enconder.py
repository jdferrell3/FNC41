#!/usr/bin/env python

import string
import sys
import time
import turtle

if sys.version_info[0] != 3:
    print("This script requires Python version 3.x")
    sys.exit(1)

SAVE_TEST_FILES = False

SUPPORTED_TYPES = ['decimal', 'binary', 'morse', 'braille']

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
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ',': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'}

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

    def initialize_turtle(self):
        self.turtle = turtle.Turtle()
        # turtle.screensize(canvwidth=None, canvheight=None)
        self.turtle.screen.screensize(400, 400)
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto((-300, 250))
        self.turtle.pendown()

    def save(self, outfile):
        ts = self.turtle.getscreen()
        cv = ts.getcanvas()

        # colormode  Use 'color' for color output, 'gray' for grayscale, or 'mono' for black and white.
        # file       If supplied, names a file where the PostScript will be written. If this option is not given, the PostScript is returned as a string.
        # height     How much of the Y size of the canvas to print. Default is the entire visible height of the canvas.
        # rotate     If false, the page will be rendered in portrait orientation; if true, in landscape.
        # x          Leftmost canvas coordinate of the area to print.
        # y          Topmost canvas coordinate of the area to print.
        # width      How much of the X size of the canvas to print. Default is the visible width of the canvas.
        cv.postscript(file=outfile) #, colormode='color')
        print("message written to '{}'".format(outfile))

    def encode(self, msg, encode_type='decimal'):
        msg = msg.upper()

        if encode_type == 'decimal':
            self._encode_decimal(msg)

        if encode_type == 'morse':
            self._encode_morse(msg)

        if encode_type == 'braille':
            self._encode_braille(msg)

        if encode_type == 'binary':
            self._encode_binary(msg)

    def _encode_decimal(self, msg):
        l = []
        for c in msg:
            if c in ALPHA_TO_NUM.keys():
                l.append(str(ALPHA_TO_NUM[c]))
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

    def write(self):
        if self.encoded_msg:
            self.initialize_turtle()
            self.turtle.write(self.encoded_msg, font=("Times", 20, "bold"))
        else:
            raise Exception("call the encode() method first")

    def clear(self):
        self.turtle.clear()

def test():
    for x in UPPER_ALPHA:
        print('{:<1}  {:<2}  {:<7}  {:<4}  {:<8}  {:<4}'.format(
            x, ALPHA_TO_NUM[x], bin(ALPHA_TO_NUM[x]).lstrip('0b'), MORSE_CODE_DICT[x], PHONETIC[x], BRAILLE[x]))
    print('\n')

    test_string = 'hello there'
    print(test_string)

    for t in SUPPORTED_TYPES:
        encoder = FNC41Encoder()
        encoder.encode(test_string, t)
        print(t, encoder.encoded_msg)
        encoder.write()
        if SAVE_TEST_FILES:
            encoder.save('{}.ps'.format(t))
        time.sleep(5)
        encoder.clear()

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test()
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
        encoder.encode(msg, encode_type)
        encoder.write()
        encoder.save('temp.ps')
        time.sleep(5)
