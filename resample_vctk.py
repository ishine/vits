import os
from glob import glob

filelist = glob('filelists/vctk*')

# make sure the directory exists
if not os.path.exists("VCTK"):
    os.mkdir("VCTK")
if not os.path.exists("VCTK/wav"):
    os.mkdir("VCTK/wav")

for p in filelist:

    with open(p) as f:

        out_meta_p = "VCTK/" + str(p).split("/")[-1]
        out_meta = open(out_meta_p, "w", newline="\n")

        lines = f.readlines()
        for l in lines:

            wav_path, speaker, text = l.split("|")

            input_path = wav_path
            input_path = input_path.replace(
                "VCTK/wav", "VCTK-Corpus/wav48")

            # does not exist
            if not os.path.exists(input_path):
                print(input_path)
                continue

            print("Processing %s" % input_path)
            dir_path = wav_path.replace(wav_path.split('/')[-1], "")
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path, 0o777)

            out_meta.write(wav_path + "|" + speaker + "|" + text)
            if os.system("/usr/bin/sox -v 0.94 " + input_path + " " + wav_path + " rate -v 22050 silence 1 0.1 1% reverse silence 1 0.1 1% reverse silence 1 0.1 1%") != 0:
                print("Failed!")
                exit(-1)

        out_meta.close()
