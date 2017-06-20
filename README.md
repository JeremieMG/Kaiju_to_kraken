# Kaiju_to_kraken
Project to convert a kaiju report file into a kraken report file.

## Requirements:
- Python version 2.7
- Awk 
- Kaiju version 1.5.0

## Convert your file:
First, you need to download the following scripts (available at https://github.com/JeremieMG/Kaiju_to_kraken):
- kraken_maker.py
- taxa_parser.awk

Then, to make this scripts executables, you have to run the hereafter command:
```
chmod 755 [script]
```

Finally, run this command to convert your kaiju report file into a kraken report file:
```
./kraken_maker.py -i kaiju.out -t nodes.dmp -n names.dmp > [output]
```

or

```
./kraken_maker.py -h
```

### Important note: Be sure that the both scripts are in the same folder.
