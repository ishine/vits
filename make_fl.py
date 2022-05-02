import random

# this will prepare the file lists for LJSpeech
with open("LJSpeech-1.1/metadata.csv") as file:

    lines = file.readlines()
    random.shuffle(lines)

    train = open("filelists/ljs_audio_text_train_filelist.txt", 'w')
    val = open("filelists/ljs_audio_text_val_filelist.txt", 'w')
    test = open("filelists/ljs_audio_text_test_filelist.txt", 'w')

    jdx = 0

    for i in range(100):
        splits = lines[jdx].split("|")
        val.write("LJSpeech-1.1/wavs/" + splits[0] + ".wav" + "|" + splits[1])
        jdx += 1

    for i in range(500):
        splits = lines[jdx].split("|")
        jdx += 1
        test.write("LJSpeech-1.1/wavs/" + splits[0] + ".wav" + "|" + splits[1])

    while jdx < len(lines):
        splits = lines[jdx].split("|")
        jdx += 1
        train.write("LJSpeech-1.1/wavs/" + splits[0] + ".wav" + "|" + splits[1])

    train.close()
    val.close()
    test.close()
