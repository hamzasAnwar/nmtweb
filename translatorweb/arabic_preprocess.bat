
python -V
python translatorweb/arabic_normalizer.py -corpus translatorweb/output/test.ara -output translatorweb/output/test.norm1.ara 

perl translatorweb/tokenizer/replace-unicode-punctuation.perl < translatorweb/output/test.norm1.ara > translatorweb/output/test.norm2.ara
perl translatorweb/tokenizer/normalize-punctuation.perl < translatorweb/output/test.norm2.ara > translatorweb/output/test.norm3.ara

perl translatorweb/tokenizer/remove-non-printing-char.perl < translatorweb/output/test.norm3.ara > translatorweb/output/test.norm4.ara

perl translatorweb/tokenizer/tokenizer.perl -l en -no-escape -threads 4 < translatorweb/output/test.norm4.ara > translatorweb/output/test.tok.ara

python translatorweb/transliterate.py -scheme hsb -input translatorweb/output/test.tok.ara > translatorweb/output/test.tok.rom.ara

