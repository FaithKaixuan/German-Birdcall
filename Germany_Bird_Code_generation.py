import os, sys
import pandas as pd
train_csv = pd.DataFrame(columns = ["gen","sp","filename"])
path = "/mnt/GermanyBirdcall/Germany_Birdcall_resampled"
primary_labels = os.listdir( path )
i = 0
BIRD_CODE = {}
for gen in primary_labels:
  BIRD_CODE.append({gen: i})
  i = i + 1
print(BIRD_CODE)
