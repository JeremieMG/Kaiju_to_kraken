#!/usr/bin/awk -f

BEGIN {
  FS = ";"
}
#/^.[0-9]/
match($1,/unclassified$/) {
  split($1,a," ")
  print a[1]"\t"a[2]"\t"a[3]
  print "-"
}
match($1,/Viruses$/) {
  split($1,a," ")
  print a[1]"\t"a[2]"\t"a[3]
  print "-"
}

/;.$/ {
  split($1,a," ")
  match($1,/[[:alpha:]]+/)
  print a[1]"\t"a[2]"\t"substr($1,RSTART)

}

/;.$/ {
  start_line = 1
  end_line = (NF-1)
  while (start_line != end_line) {
    start_line += 1
    print a[1]"\t"a[2]"\t"substr($(start_line),2)
  }
  print "-"
}

END {
}
