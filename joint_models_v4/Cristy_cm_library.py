## Latest version of the models for the slotscraving task
## Author: Kaustubh Kulkarni
## Original Date: June 2022
## Last Modified: Feb 5, 2022

import IPython
from IPython.display import clear_output

from cm_models.factorial_models import NoBias_CEC, NoBias_EEC, NoBias_JEC
from cm_models.factorial_models import LRBias_CEC, LRBias_EEC, LRBias_JEC
from cm_models.factorial_models import TempBias_CEC, TempBias_EEC, TempBias_JEC
from cm_models.factorial_models import Heu_CEC
from utils import load_data

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
       
if __name__ == "__main__":


    # EMU Data
    #project_dir = '/Users/cristybanuelos/Documents/Craving/Model_Comparison'    
    #longform_path = f'{project_dir}/KK_clean_data/all_group_longform.csv'
    #df_summary_path = f'{project_dir}/KK_clean_data/all_group_df_summary.csv' 

    # Prolific Data - Binge
    project_dir = '/Users/cristybanuelos/Documents/Craving'    
    longform_path = f'{project_dir}/KK_Prolific_data/Binge/binge_clean_df_longform.csv'
    df_summary_path = f'{project_dir}/KK_Prolific_data/Binge/binge_clean_df_summary.csv' 

    save_path = '/Users/cristybanuelos/Documents/Craving/Model_Comparison/Prolific' 
    save_mood_path = '/Users/cristybanuelos/Documents/Craving/Model_Comparison/Prolific/Binge' 

    df_summary, longform = load_data.load_clean_dbs(df_summary_path, longform_path)


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

    for pid in range(len(longform["PID"].unique())):
        print("trying pid=", pid)
        batchfit.fit(pid, "money")
        batchfit.fit(pid, "other")
        batchfit.fit_mood(pid, "money")
        batchfit.fit_mood(pid, "other")

            #pid_index = self.pid_list.tolist().index(pid_num)
            #pid = self.pid_list[pid_index]
