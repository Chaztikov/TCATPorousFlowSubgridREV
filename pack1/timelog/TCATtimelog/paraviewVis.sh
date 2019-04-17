#!/bin/bash -f

VARA=$(( 1000-$1 ))

VARB=$(( VARA+$1 ))

echo "{
  \"file-series-version\" : \"1.0\",
  \"files\" : ["

for i in $(seq -f "%03g" $1 $1 $VARA)
do
  echo " { \"name\" : \"./vis"$i"/summary.silo\", \"time\" : " $i " },"
done

if (( $2 < 1000 )); then
   echo ""
elif (( $2 >= 1000 )); then
   for i in $(seq -f "%04g" $VARB $1 $2)
   do
     echo " { \"name\" : \"./vis"$i"/summary.silo\", \"time\" : " $i " },"
   done
fi 


echo "   ]
}"
