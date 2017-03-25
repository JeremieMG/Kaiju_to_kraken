# Kaiju_to_kraken
Project to convert a kaiju report file into a kraken report file.

## Requirements:
- Python version 2.7
- Awk 

## Convert your file:
To convert kaiju file, first you need to download the following scripts (available at https://github.com/JeremieMG/Kaiju_to_kraken):
- kraken_maker.py
- taxa_parser.awk

Secondly, to make this scripts executables, you have to run the hereafter command:
```
chmod 755 [script]
```

Finally, run this command to convert your kaiju report file into a kraken report file:
```
./kraken_maker.py [Kaiju_file] > [output]
```
### Important note: Be sure that the both scripts are in the same folder.
