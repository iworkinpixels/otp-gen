#!/bin/bash
blocksize=5
blockrow=4
rowcount=10
pagecount=10
otpath='/ramdisk/otp.txt'
bookserial=`base64 /dev/random | tr -d '+/\r\n0-9a-z' | head -c 10`

mkfs -q /dev/ram1 1024
mkdir -p /ramdisk
mount /dev/ram1 /ramdisk

rm $otpath
for ((x=1; x<=$pagecount; x++))
do  
  echo -n $bookserial >> $otpath;
  printf '%22s' $x"/"$pagecount >> $otpath;
  echo "" >> $otpath;
  for ((i=1; i<=$rowcount; i++))
  do
    for ((j=1; j<=$blockrow; j++))
    do
        randnum=`base64 /dev/random | tr -d '+/\r\n0-9a-z' | head -c $blocksize`
        echo -n $randnum >> $otpath;
        echo -n "  " >> $otpath;
    done
      echo "" >> $otpath;
  done
  echo "--------------------------------" >> $otpath
done
