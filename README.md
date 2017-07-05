# Kaiju_to_kraken
Project to convert a kaiju report file into a kraken report file.

## Requirements:
- Python version 2.7
- Awk 
- Kaiju version 1.5.0

## Convert your file:
First, you need to download the following scripts/file (available at https://github.com/JeremieMG/Kaiju_to_kraken):
- kraken_maker.py
- taxa_parser.awk
- id_nodes

Then, to make this scripts executables, you have to run the hereafter command:
```
chmod 755 [script]
```

Finally, run this command to convert your kaiju.out file into a kraken report file:
```
./kraken_maker.py -i kaiju.out -t nodes.dmp -n names.dmp -f id_nodes > [output]
```

or

```
./kraken_maker.py -h
```
### Important note: Be sure that the both scripts are in the same folder.

## Update id_nodes
If you are updating your nodes.dmp file, please update the id_nodes file by running this command:
```
awk 'BEGIN{FS="\t"} {print $1 "\t" $3 "\t" $5}' nodes.dmp > id_nodes
```
