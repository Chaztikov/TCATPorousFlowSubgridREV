#!/bin/bash

echo "RUNNING CLEAR SCRIPT AND UPDATING EXAMPLE FILES"

cd /Users/cpf/Repos/adaptive/LBM/example/Sph1896
rm -rf *

cd /Users/cpf/Repos/master_LBM/build_LBM/example/Sph1896
rm -rf *
cd /Users/cpf/Repos/master_LBM/LBM/example/Sph1896
rm -rf *

cd /Users/cpf/Repos/legacy_LBM/build_LBM/example/Sph1896
rm -rf *
cd /Users/cpf/Repos/legacy_LBM/LBM/example/Sph1896
rm -rf *

cd /Users/cpf/Repos/master_LBM/build_LBM/example/REV/
rm -rf *
cd /Users/cpf/Repos/master_LBM/LBM/example/REV/
rm -rf *

echo "COPYING INPUT FILES FROM /Users/cpf/Repos/adaptive/build/example/Sph1896/ TO OTHER BRANCHES"
cd /Users/cpf/Repos/adaptive/build/example/Sph1896/

rm Restart.*
rm LBM.visit
rm timelog.*
rm ID.*
rm SignDist.*
rm Phase.*
rm components.*
rm -r vis*

cp /Users/cpf/Repos/adaptive/build/example/Sph1896/*  /Users/cpf/Repos/adaptive/LBM/example/Sph1896/

cp /Users/cpf/Repos/adaptive/build/example/Sph1896/*  /Users/cpf/Repos/master_LBM/build_LBM/example/Sph1896/
cp /Users/cpf/Repos/adaptive/build/example/Sph1896/*  /Users/cpf/Repos/master_LBM/LBM/example/Sph1896/

cp /Users/cpf/Repos/adaptive/build/example/Sph1896/*  /Users/cpf/Repos/master_LBM/build_LBM/example/REV
cp /Users/cpf/Repos/adaptive/build/example/Sph1896/*  /Users/cpf/Repos/master_LBM/LBM/example/REV

cp /Users/cpf/Repos/adaptive/build/example/Sph1896/*  /Users/cpf/Repos/legacy_LBM/build_LBM/example/Sph1896/
cp /Users/cpf/Repos/adaptive/build/example/Sph1896/*  /Users/cpf/Repos/legacy_LBM/LBM/example/Sph1896/
