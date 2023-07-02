# Highlight for deMon2k

These files provide syntax highlighting for 
[deMon2k](http://www.demon-software.com/ "deMon2k Home Page") input files.

Keywords and options are defined in _./syntax/deMon.vim_. Every file which name
matches either _*.inp_ or _*.new_ will be highlighted according to the 
definitions in the syntax file. To choose which files to apply the highlight, 
edit the _./ftdetect/deMon.vim_ file.

## Installation

1. Create the following directory tree:
```
mkdir ~/.vim
mkdir ~/.vim/syntax
mkdir ~/.vim/ftdetect
```
2. Copy the _./syntax/deMon.vim_ into your local _syntax_ directory.
3. Copy the _./ftdetect/deMon.vim_ into your local _ftdetect_ directory.

## TODO 

- Add missing keywords and options.
- Fix highlight for words that are both keyword and option.
- Highlight keywords body options.
- Update deMon-strict file.
