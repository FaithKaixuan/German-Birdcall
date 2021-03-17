import os, sys
import pandas as pd
train_csv = pd.DataFrame(columns = ["gen","sp","filename"])
path = "/mnt/GermanyBirdcall/Germany_Birdcall_resampled"
primary_labels = os.listdir( path )
i = 0
for gen in primary_labels:
    path_sub = path + "/" + gen
    secondary_labels = os.listdir(path_sub)
    for sp in secondary_labels:
      path_sub_sub = path_sub + "/" + sp
      filenames = os.listdir(path_sub_sub)
      for filename in filenames:
          train_csv.loc[i] = [gen, sp, filename]
          i = i + 1
train_csv.to_csv('Germany_Birdcall_resampled.csv', index=False)
