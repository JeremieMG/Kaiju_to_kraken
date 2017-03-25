# Kaiju_to_kraken
Project to convert a kaiju report file into a kraken report file.

## Requirements:
- Python version 2.7
- Awk 

## Convert your file:
To convert kaiju file, first you need to download the following scripts (available at https://github.com/JeremieMG/Kaiju_to_kraken):
- kraken_maker.py
- taxa_parser.awk

Secondly, you have to run this command to make these script executable:
```
chmod 755 [script]
```

Finally, run this command to convert directly your kaiju report file into a kraken report file:
```
./kraken_maker.py [Kaiju_file] > [output]
```
### Note: Be sure the both scripts are in the same folder.
