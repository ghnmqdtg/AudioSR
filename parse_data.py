# We parse ./data/$sample_rate/**/*.wav, the sample rate is 8000, 12000, 16000, 24000
# And save paths to batch_${sample_rate}.lst one by one

import os
import glob


def parse_data(data_dir, output_dir, sample_rate):
    # Get folder names in data_dir
    test_folder = sorted(glob.glob(os.path.join(data_dir, str(sample_rate), "*")))
    # Get last 8
    test_folder = test_folder[-8:]

    # Output path
    lst_file = os.path.join(output_dir, "batch_%d.lst" % sample_rate)
    # Remove lst_file if exists
    if os.path.exists(lst_file):
        os.remove(lst_file)
    # Save paths to lst_file
    with open(lst_file, "w") as f:
        for folder in test_folder:
            # Get all wav files in folder
            wav_files = sorted(glob.glob(os.path.join(folder, "*.wav")))
            for wav_file in wav_files:
                f.write(wav_file + "\n")
    print("Save paths to %s" % lst_file)


if __name__ == "__main__":
    sample_rate = [8000, 12000, 16000, 24000]
    for sr in sample_rate:
        parse_data("./data", "./", sr)
