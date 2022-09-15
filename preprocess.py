import argparse
import text
from utils import load_filepaths_and_text
import random

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("--text_index", default=1, type=int)
  parser.add_argument("--metadata", nargs="+", default="filelists/metadata.csv")
  # parser.add_argument("--metadata", nargs="+", default="filelists/metadata.csv")
  parser.add_argument("--text_cleaners", nargs="+", default=["english_cleaners"])

  args = parser.parse_args()

      
  filepaths_and_text = load_filepaths_and_text(args.metadata)
  for i in range(len(filepaths_and_text)):
    print(i, '/', len(filepaths_and_text))
    original_text = filepaths_and_text[i][args.text_index]
    cleaned_text = text._clean_text(original_text, args.text_cleaners)
    filepaths_and_text[i][args.text_index] = cleaned_text
    print(original_text,'\n', cleaned_text)

  random.shuffle(filepaths_and_text)
  num_train = int(len(filepaths_and_text)*0.95)
  train_set = filepaths_and_text[:num_train]
  val_set = filepaths_and_text[num_train:]
  
  with open('filelists/train.txt', 'w', encoding='utf-8') as f:
    f.writelines(["|".join(x) + "\n" for x in train_set])

  with open('filelists/val.txt', 'w', encoding='utf-8') as f:
    f.writelines(["|".join(x) + "\n" for x in val_set])
