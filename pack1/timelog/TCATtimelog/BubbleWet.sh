#!/bin/bash

LBPM_DIR=../../tests

rm components.*
rm Restart.*
rm LBM.visit
rm -r vis*
rm timelog.*

#python multiProcBubble.py
#mpirun -np 1 $LBPM_DIR/lbpm_serial_decomp input.db
mpirun --oversubscribe -np 8 $LBPM_DIR/GenerateSphereTest input.db
mpirun --oversubscribe -np 8 $LBPM_DIR/lbpm_color_simulator input.db

cat timelog.tcat | awk '{print $1,$3,$4,$9,$48}'
