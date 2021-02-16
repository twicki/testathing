git clone git@github.com:VulcanClimateModeling/daint_venv.git
cd daint_venv
./install.sh test_ve
source test_ve/bin/activate
export MODULEPATH=${MODULEPATH}:/project/s1053/install/modulefiles
module load ccache/4.2

create_ccache `pwd`/ccahe
source /scratch/snx3000/tobwi/sbox/simole/ccahe/bin/activate_ccache
export CCACHE_BASEDIR=`pwd`
time python file.py