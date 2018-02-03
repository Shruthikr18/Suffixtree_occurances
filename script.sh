#!bin/sh
interval=20
for((i=1;i<51;i++))
do
  python3 suffixtree1.py $i.txt
done
