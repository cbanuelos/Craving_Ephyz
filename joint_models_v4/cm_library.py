## Latest version of the models for the slotscraving task
## Author: Kaustubh Kulkarni
## Original Date: June 2022
## Last Modified: Feb 5, 2022

import IPython
from IPython.display import clear_output

from .cm_models.factorial_models import NoBias_CEC, NoBias_EEC, NoBias_JEC
from .cm_models.factorial_models import LRBias_CEC, LRBias_EEC, LRBias_JEC
from .cm_models.factorial_models import TempBias_CEC, TempBias_EEC, TempBias_JEC
from .cm_models.factorial_models import Heu_CEC

## Batchfit class
class BatchFit(object):
    def __init__(self, model_list, longform, df_summary, project_dir, save_path, save_mood_path=None):
        self.models = {}
        for model_name in model_list:
            self.models[model_name] = eval(f'{model_name}(longform, df_summary, project_dir, save_path, save_mood_path)')
        self.longform = longform
        self.df_summary = df_summary
        self.project_dir = project_dir
    
    def fit(self, pid_num, block, jupyter=False):
        for model_name in self.models:
            if jupyter:
                clear_output(wait=True)
            print(f'Fitting {model_name}: PID - {pid_num}, Block - {block}')
            self.models[model_name].fit(pid_num, block)
    
    def fit_mood(self, pid_num, block, jupyter=False):
        for model_name in self.models:
            if jupyter:
                clear_output(wait=True)
            print(f'Fitting {model_name}: PID - {pid_num}, Block - {block}')
            self.models[model_name].fit_mood(pid_num, block)
    
    def join(self, batch):
        for model_name in batch.models:
            if model_name not in self.models:
                self.models[model_name] = batch.models[model_name]
            else:
                print(f'Model {model_name} already exists in this batch')

project_dir = '/Documents/Craving'    

longform_path = f'{project_dir}/KK_clean_data/clean_df_longform.csv' #KK sent me
df_summary_path = f'{project_dir}/KK_clean_data/clean_df_summary.csv' #KK sent me

save_path = project_dir #just a directory, not a path to a file
save_mood_path = project_dir #just a directory, not a path to a file

longform = load_data.load_clean_dbs(longform_dir)
df_summary = load_data.load_clean_dbs(summary_dir)


batchfit = BatchFit(
        [
            'NoBias_CEC', 'NoBias_EEC', 'NoBias_JEC',
            'LRBias_CEC', 'LRBias_EEC', 'LRBias_JEC',
            'TempBias_CEC', 'TempBias_EEC', 'TempBias_JEC',
            'Heu_CEC'
        ],
        longform,
        df_summary,
        project_dir,
        save_path,
        save_mood_path,
    )
