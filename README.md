# Kaiju_to_kraken
Project to convert a kaiju report file into a kraken report file.

## Requirements:
- Python version 2.7
- Awk 
- Kaiju

## Convert your file:
To convert kaiju file, first you need to convert Kaiju's output file into a summary report file for a given taxonomic rank (Using Kaiju's tool, kaijuReport):
```
kaijuReport -t nodes.dmp -n names.dmp -i kaiju.out -r species -l superkingdom,phylum,order,class,family,genus,species -o kaiju.out.summary
```

Secondly, you need to download the following scripts (available at https://github.com/JeremieMG/Kaiju_to_kraken):
- kraken_maker.py
- taxa_parser.awk

Then, to make this scripts executables, you have to run the hereafter command:
```
chmod 755 [script]
```

Finally, run this command to convert your kaiju report file into a kraken report file:
```
./kraken_maker.py Kaiju.out.summary > [output]
```
### Important note: Be sure that the both scripts are in the same folder.
