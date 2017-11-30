#############
#! /bin/bash

# 0. Arabic text normalization 
python arabic_normalizer.py -corpus ../corporaX/extract/test/test.ara -output ../corporaX/tmp/test.norm1.ara 

# CLEANING
# 1. replace-unicode-punctuation 
tokenizer/replace-unicode-punctuation.perl < ../corporaX/tmp/test.norm1.ara > ../corporaX/tmp/test.norm2.ara
# 2. normalize-punctuation
tokenizer/normalize-punctuation.perl < ../corporaX/tmp/test.norm2.ara > ../corporaX/tmp/test.norm3.ara

# 3. remove non printing
tokenizer/remove-non-printing-char.perl < ../corporaX/tmp/test.norm3.ara > ../corporaX/tmp/test.norm4.ara

# 4. TOKENIZATION
tokenizer/tokenizer.perl -l en -no-escape -threads 4 < ../corporaX/tmp/test.norm4.ara > ../corporaX/tmp/test.tok.ara

# 5. transliteration
python transliterate.py -scheme hsb -input ../corporaX/tmp/test.tok.ara > ../corporaX/tmp/test.tok.rom.ara

