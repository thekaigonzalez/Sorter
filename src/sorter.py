import os
from pathlib import Path
import yaml
import argparse

parser = argparse.ArgumentParser(description="SORTER is an application that sorts your files into different directories"+
                                      ", the way it works is that it reads a sorter.yml file in the current directory,"+
                                      " and it tries to load the file configurations, then looks in the directory and"+
                                      " sorts the files, following the config rules.")

parser.add_argument("-d", default=".", help="The directory to parse (without /)")

args = parser.parse_args()

dirc = args.d

if dirc.endswith("/"):
  dirc = dirc[:len(dirc)-1]

sortercfg = dirc + "/sorter.yml"

cfg = yaml.safe_load(open(sortercfg, "r"))

binds = dict(cfg["files"])

for file in binds:
  for f in os.listdir(dirc):
    if (f.endswith(file)):
      save = binds[file]
      print(save)

      if Path(dirc + "/" + save).exists() == False:
        os.mkdir(dirc + "/" + save)
      
      os.rename(dirc + "/" + f, dirc + "/" + save + "/" + f)