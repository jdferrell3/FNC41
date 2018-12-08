# FNC41

## FNC41 encoder script

Encoder script inspired by [Field Notes Clandestine](https://fieldnotesbrand.com/products/clandestine) notebook.

The script uses Python's `turtle` [library](https://docs.python.org/3/library/turtle.html) to create PostScript files with the encoded message.

When run with `test` argument it displays the following. When run without an argument it prompts for an encoder type and message.

```
> python3 fnc41_encoder.py test

A  1   1        .-    Alpha     ⠁
B  2   10       -...  Bravo     ⠃
C  3   11       -.-.  Charlie   ⠉
D  4   100      -..   Delta     ⠙
E  5   101      .     Echo      ⠑
F  6   110      ..-.  Foxtrot   ⠋
G  7   111      --.   Golf      ⠛
H  8   1000     ....  Hotel     ⠓
I  9   1001     ..    India     ⠊
J  10  1010     .---  Juliet    ⠚
K  11  1011     -.-   Kilo      ⠅
L  12  1100     .-..  Lima      ⠇
M  13  1101     --    Mike      ⠍
N  14  1110     -.    November  ⠝
O  15  1111     ---   Oscar     ⠕
P  16  10000    .--.  Papa      ⠏
Q  17  10001    --.-  Quebec    ⠟
R  18  10010    .-.   Romeo     ⠗
S  19  10011    ...   Sierra    ⠎
T  20  10100    -     Tango     ⠞
U  21  10101    ..-   Uniform   ⠥
V  22  10110    ...-  Victor    ⠧
W  23  10111    .--   Whiskey   ⠺
X  24  11000    -..-  Xray      ⠭
Y  25  11001    -.--  Yankee    ⠽
Z  26  11010    --..  Zulu      ⠵


msg: hello there
decimal: 8 5 12 12 15   20 8 5 18 5
binary: 1000 101 1100 1100 1111   10100 1000 101 10010 101
morse: .... . .-.. .-.. ---   - .... . .-. .
braille: ⠓⠑⠇⠇⠕ ⠞⠓⠑⠗⠑
```