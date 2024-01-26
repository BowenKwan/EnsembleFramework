#Setting up local environment for FINN
echo "Setting up Vitis"
source /home/ocousin/tools/Xilinx/Vitis/2022.2/settings64.sh
echo "Vitis config done!"
echo "Setting up XRT"
source /opt/xilinx/xrt/setup.sh
echo "setup done!"
echo "Setting PLATFORM_REPO_PATHS"
export FINN_XILINX_PATH=/home/ocousin/tools/Xilinx
export FINN_XILINX_VERSION=2022.2
#points to the Vitis platform files (DSA).
export PLATFORM_REPO_PATHS=/opt/xilinx/platforms
#specifies the .deb to be installed for XRT inside the container (see default value in run-docker.sh).
export XRT_DEB_VERSION=xrt_202220.2.14.354_20.04-amd64-xrt
#(default 4) specifies the degree of parallelization for the transformations that can be run in parallel, potentially reducing build time
export NUM_DEFAULT_WORKERS
echo "setup done!"
echo "setup FINN_HOST_BUILD_DIR to /home/ocousin/work/FINN/build"
#specifies which directory on the host will be used as the build directory. Defaults to /tmp/finn_dev_<username>        
export FINN_HOST_BUILD_DIR=/home/ocousin/work/FINN/build
echo "setup done!"
#(default 8888) changes the port for Jupyter inside Docker          
export JUPYTER_PORT      
#(default “”) Set the Jupyter notebook password hash. If set to empty string, token authentication will be used (token printed in terminal on launch).
export JUPYTER_PASSWD_HASH
#(default localhost) sets the base URL for accessing e.g. Netron from inside the container. Useful when running FINN remotely.          
export LOCALHOST_URL 
#(default 8081) changes the port for Netron inside Docker
export NETRON_PORT
#specifies the type of PYNQ/Alveo board used (see “supported hardware” below) for the test suite                    
export ALVEO_BOARD    
#specify ip address and port number to access the PYNQ board / Alveo target                
export ALVEO_IP 
export ALVEO_PORT       
#specify the PYNQ board / Alveo host access credentials for the test suite. For PYNQ, password is always needed to run as sudo. For Alveo, you can leave the password empty and place your ssh private key in the finn/ssh_keys folder to use keypair authentication.              
export ALVEO_USERNAME
export ALVEO_PASSWORD  
#specifies the target dir on the PYNQ board / Alveo host for the test suite               
export ALVEO_TARGET_DIR    
#specifies the path to the ImageNet validation directory for tests.           
export IMAGENET_VAL_PATH
#(default 0) if set to 1 then skip Docker image building and use the image tagged with FINN_DOCKER_TAG.               
export FINN_DOCKER_PREBUILT=1 #ocrc setup for dev branch
#(autogenerated) specifies the Docker image tag to use.         
export FINN_DOCKER_TAG=maltanar/finn:dev_latest  #this is the dev branch
#export FINN_DOCKER_TAG=maltanar/finn:main_latest
#(default 0) if set to 1 then run Docker container as root, default is the current user.          
export FINN_DOCKER_RUN_AS_ROOT  
#(autodetected) if not 0 then expose all Nvidia GPUs or those selected by NVIDIA_VISIBLE_DEVICES to Docker container for accelerated DNN training. Requires Nvidia Container Toolkit               
export FINN_DOCKER_GPU      
#(default “”) pass extra arguments to the docker run command when executing ./run-docker.sh   
export FINN_DOCKER_EXTRA
#(default “0”) skips the download of FINN dependency repos (uses the ones already downloaded under deps/.          
export FINN_SKIP_DEP_REPOS            
#(default “”) specifies specific Nvidia GPUs to use in Docker container. Possible values are a comma-separated list of GPU UUID(s) or index(es) e.g. 0,1,2, all, none, or void/empty/unset.
export DOCKER_BUILDKIT    
export NVIDIA_VISIBLE_DEVICES        
#(default “1”) enables Docker BuildKit for faster Docker image rebuilding (recommended).
