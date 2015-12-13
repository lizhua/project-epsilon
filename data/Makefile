.PHONY: download_data validate_data download_filtered_data download_test_data
download_data:
	wget http://openfmri.s3.amazonaws.com/tarballs/ds005_raw.tgz
	tar -xvzf ds005_raw.tgz

download_filtered_data:
	variable=Stop python ../data/filtered_data_sh_script.py
	variable=Stop bash ../data/dwn_filtered_data_script.sh

validate_data:
	wget http://openfmri.s3.amazonaws.com/tarballs/ds005_raw_checksums.txt
	python get_ds005_hashes_from_txt.py
	python data.py
 	
download_test_data:
	wget -P ../data/ds114/sub009/BOLD/task002_run001/ http://www.jarrodmillman.com/rcsds/_downloads/ds114_sub009_t2r1.nii
	wget -P ../data/ds114/sub009/behav/task002_run001/ http://www.jarrodmillman.com/rcsds/_downloads/ds114_sub009_t2r1_cond.txt
	wget -P ../data/ds114/sub009/behav/task002_run001/ http://www.jarrodmillman.com/rcsds/_downloads/ds114_sub009_t2r1_conv.txt

test: 
	 nosetests tests 

coverage:
	 nosetests tests --with-coverage --cover-package=data_hashes.py 


