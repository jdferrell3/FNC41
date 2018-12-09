# FNC41

## FNC41 encoder script

Encoder script inspired by [Field Notes Clandestine](https://fieldnotesbrand.com/products/clandestine) notebook.

The script uses the `pyfpdf` [library](https://github.com/reingart/pyfpdf) to create a PDF file with the encoded message.

When run with `test` argument to generate a PDF with all possible encodings. When run without an argument it prompts for an encoder type and message.

```
> python3 fnc41_encoder.py test

A  1   1        .-    Alpha     ⠁
B  2   10       -...  Bravo     ⠃
...

- writing decimal
- writing binary
- writing morse
- writing braille
- writing pigpen
message written to 'test.pdf'
```

## Fonts

The following fonts are used for braille and pigpen:
- https://www.dafont.com/braille.font
- http://www.babelstone.co.uk/Fonts/Pigpen.html BabelStonePigpen