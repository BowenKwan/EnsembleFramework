# Ensemble Framework



## Data 
Market data need to be downloaded from the following link:
```bash
 https://lobsterdata.com/info/DataSamples.php
 ```
## Tools
To install the FINN environment follow these installation steps
https://finn.readthedocs.io/en/latest/getting_started.html


## Environment
To set the environment for the tools and the Docker files, modify the following script with your own environment variables
 ```bash
 source FINN_setup.sh
 ```
## Start the docker container 
 ```bash
 source run_docker.sh
 ```
## Configuration for the hardware generation 
Two files control the hardware generation step in FINN. The two files are located in the configuration directory called configuration_files
1. dataflow_build_config.json (where the hardware target platform or FPGA device can be configure)
2. folding_config.json (configuration file to set the PE and SMID values for each layer)

Note: Multiple dataflow_build_config are provided to show different possible configuration

## Run Training, compiler, and result analysis
To run the training, generate the model and analyse the report use the following scripts
 ```bash
 python run_batch.py
 ```
 results.csv file will be created and appended according to the suite test results.

