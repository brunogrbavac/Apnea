import csv
import os                                                                                                             
import copy
import mne
import shutil
import papermill as pm
import pandas as pd
import pyarrow.feather as feather
import pyarrow as pa

def one_df_trta():           
    
    root_path="C:\\Users\\bruno\\Desktop\\Diplomski"
    
    subdirs = [f.path for f in os.scandir(root_path) if f.is_dir()]
    for index,subdir in enumerate(subdirs): 
        if(root_path!=subdir and subdir!=os.path.join(root_path,".ipynb_checkpoints") and subdir!=os.path.join(root_path,"__pycache__")):
            print(subdir)

            signal  = feather.read_feather(os.path.join(subdir,'edf_signals.feather'))
            signal['Patient'] = subdir

            if(index==0):
                signal.to_csv('D:\\octrta.csv', index=False)
            else:
                signal.to_csv('D:\\octrta.csv', mode='a', header=False, index=False)
