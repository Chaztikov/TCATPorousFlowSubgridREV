#!/bin/bash

echo "MAKE SURE Domain.in MATCHES input.db"

rm -r vis*
rm LBM.visit
rm timelog.*

cp /Users/cpf/Repos/adaptive/build/example/Sph1896/* /Users/cpf/Repos/master_LBM/build_LBM/example/Sph1896/

cd /Users/cpf/Repos/master_LBM/build_LBM/example/Sph1896

rm ID.0*
rm SignDist.0*
rm Phase.0*

rm -r vis*
rm LBM.visit
rm timelog.*

echo "RUNNING GENERATE SPHERE TEST"

mpirun --oversubscribe -np 8 ../../tests/GenerateSphereTest input.db


echo "RUNNING SEGMENTED PRE-PROCESSOR"




mpirun --oversubscribe -np 8 ../../tests/lbpm_segmented_pp input.db

cp /Users/cpf/Repos/master_LBM/build_LBM/example/Sph1896/* /Users/cpf/Repos/legacy_LBM/build_LBM/example/Sph1896/

cd /Users/cpf/Repos/legacy_LBM/build_LBM/example/Sph1896/

rm -r vis*
rm LBM.visit
rm timelog.*

echo "RUNNING RANDOM PRE-PROCESSOR"

mpirun --oversubscribe -np 8 ../../tests/lbpm_random_pp 0.1 0

cp /Users/cpf/Repos/legacy_LBM/build_LBM/example/Sph1896/* /Users/cpf/Repos/master_LBM/build_LBM/example/REV/

cd /Users/cpf/Repos/master_LBM/build_LBM/example/REV/

rm -r vis*
rm LBM.visit
rm timelog.*

echo "RUNNING LBPM ADAPTIVE SIMULATOR"

mpirun --oversubscribe --np 8 ../../tests/lbpm_color_simulator input.db

cat timelog.tcat | awk '{print $1,$3,$4,$9,$48}'
