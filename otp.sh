#!/bin/bash
blocksize=5
blockrow=4
rowcount=10
pagecount=10

bookserial=`base64 /dev/random | tr -d '+/\r\n0-9a-z' | head -c 10`

rm otp.txt
for ((x=1; x<=$pagecount; x++))
do  
  echo -n $bookserial >> otp.txt;
  printf '%22s' $x"/"$pagecount >> otp.txt;
  echo "" >> otp.txt;
  for ((i=1; i<=$rowcount; i++))
  do
    for ((j=1; j<=$blockrow; j++))
    do
        randnum=`base64 /dev/random | tr -d '+/\r\n0-9a-z' | head -c $blocksize`
        echo -n $randnum >> otp.txt;
        echo -n "  " >> otp.txt;
    done
      echo "" >> otp.txt;
  done
  echo "--------------------------------" >> otp.txt
done
