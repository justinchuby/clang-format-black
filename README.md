# clang-format-black
A clang-format config / generator that mimics Python’s [black](https://black.readthedocs.io/en/stable/the_black_code_style/current_style.html) formatter style.

## Usage

Just use the `.clang-format` file in your own project.

## Config generator

You can use

```sh
python clang_format_black.py > .clang-format
```

to generate a customized config. Available options:

```
$ python clang_format_black.py -h

usage: clang_format_black.py [-h] [--line-length LINE_LENGTH]
                             [--indent-width INDENT_WIDTH] [--align-array-of-structures]
                             [--access-modifier-offset ACCESS_MODIFIER_OFFSET]
                             [--align-trailing-comments] [--reflow-comments]
                             [--sort-includes]

Create clang-format config that mimics Python's black formatter style.

options:
  -h, --help            show this help message and exit
  --line-length LINE_LENGTH, --column-limit LINE_LENGTH
                        How many characters per line to allow. [default: 88]
  --indent-width INDENT_WIDTH
                        Indent width. [default: 4]
  --align-array-of-structures
                        Align array of structures.
  --access-modifier-offset ACCESS_MODIFIER_OFFSET
                        Indent width for access modifiers. [default: -2]
  --align-trailing-comments
                        Align trailing comments.
  --reflow-comments     Reflow comments.
  --sort-includes       Sort includes.
```
