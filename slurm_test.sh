#! /bin/bash

#Batch Job Paremeters
#SBATCH --nodes=1
#SBATCH --gpus-per-node=1
#SBATCH --ntasks-per-node=1
#SBATCH --account=MST112230

SAMPLE_RATES=(8000 12000 16000 24000)

# Loop over sample rates and run the Python script
for SR in "${SAMPLE_RATES[@]}"
do
    echo "Running AudioSR for sample rate: ${SR}"
    audiosr -il batch_${SR}.lst -s test_samples/${SR} --model_name speech --suffix _up
done