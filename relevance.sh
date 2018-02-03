#!bin/sh
interval=20
for((i=1;i<51;i++))
do
  python3 relevance.py $i.txt>>relevance1.txt
done
