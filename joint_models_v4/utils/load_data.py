import numpy as np
import pandas as pd
import glob
import sqlite3


def load_clean_dbs(path_to_summary, path_to_lf, filter_varied=True):
    # Load cleaned dbs
    df_summary = pd.read_csv(path_to_summary)
    df_longform = pd.read_csv(path_to_lf)

    filtered_df_summary = pd.DataFrame()
    filtered_df_longform = pd.DataFrame()

        # Rename columns
    filtered_df_summary.rename(
        columns={
            "pid": "PID",
            "timestamp": "Timestamp",
            "other_key": "Other Key",
            "block_order": "Block Order",
            "reversal_timings": "Reversal Timings",
            "base_craving": "Base Craving",
            "base_mood": "Base Mood",
            "money_acc": "Money Accuracy",
            "other_acc": "Other Accuracy",
            # "block_three_acc": "Block Three Accuracy",
        },
        inplace=True,
    )

    filtered_df_longform.rename(
        columns={
            "pid": "PID",
            "block": "Block",
            "block_type": "Type",
            "trial_num": "Trial",
            "cue_time": "Cue Time",
            "action": "Action",
            "action_time": "Action Time",
            "reward": "Reward",
            "reward_time": "Reward Time",
            "rt": "RT",
            "spinspeed": "Spin Speed",
            "craving_rating": "Craving Rating",
            "mood_rating": "Mood Rating",
        },
        inplace=True,
    )

    for id_db in df_summary["id"].unique():

        ## Calculate accuracies for money and other blocks
        sub_summary = df_summary[df_summary["id"] == id_db].copy()
        print("sub_summary:", sub_summary) #debugging
        sub_longform = df_longform[df_longform["pid_db"] == id_db].copy()
        print("sub_longform:", sub_longform)

        # fmt: off
        #print("rev timings vals:", sub_summary["Reversal Timings"].values[0]) #debugging
        timing_code = sub_summary["reversal_timings"].values[0]
        #print("timing code:", timing_code) #debugging
        money_actions = sub_longform[(sub_longform["block_type"] == "money")]["action"].values
        #print("money_actions:", money_actions)
        other_actions = sub_longform[(sub_longform["block_type"] == "other")]["action"].values
        # blockthree_actions = sub_longform[(sub_longform["block"] == "block_three")]["action"].values

        if timing_code == "C" or timing_code == "D":
            money_actions = 1 - money_actions
            other_actions = 1 - other_actions
            # blockthree_actions = 1 - blockthree_actions
        sub_longform.loc[sub_longform["block_type"] == "money", "action"] = money_actions
        sub_longform.loc[sub_longform["block_type"] == "other", "action"] = other_actions
        # sub_longform.loc[sub_longform["block"] == "block_three", 'action'] = blockthree_actions
        # fmt: on

        ## Define the optimal choices and reward structure
        if timing_code == "A" or timing_code == "C":
            timings = np.array([12, 11, 12, 14, 11])
        elif timing_code == "B" or timing_code == "D":
            timings = np.array([14, 11, 11, 12, 12])
        reward_structure = np.array(
            [
                np.array(
                    [0.8] * timings[0]
                    + [0.2] * timings[1]
                    + [0.8] * timings[2]
                    + [0.2] * timings[3]
                    + [0.8] * timings[4]
                ),
                np.array(
                    [0.2] * timings[0]
                    + [0.8] * timings[1]
                    + [0.2] * timings[2]
                    + [0.8] * timings[3]
                    + [0.2] * timings[4]
                ),
            ]
        )
        money_optimal_choices = np.array(
            reward_structure[0, :] < reward_structure[1, :]
        ).astype(int)

        #print("MY PRINT STATEMENTS:") # for debbugging
        #print("money_optimal_choices =", money_optimal_choices)
        other_optimal_choices = 1 - money_optimal_choices
        # blockthree_optimal_choices = blockone_optimal_choices

        #print("np.sum(money_actions == money_optimal_choices) =", np.sum(money_actions == money_optimal_choices))
        #print("len(money_actions) =", len(money_actions))


        sub_summary["money_acc"] = np.sum(money_actions == money_optimal_choices) / len(
            money_actions
        )


        sub_summary["other_acc"] = np.sum(other_actions == other_optimal_choices) / len(
            other_actions
        )
        # sub_summary["block_three_acc"] = np.sum(
        #     blockthree_actions == blockthree_optimal_choices
        # ) / len(blockthree_actions)

        filtered_df_summary = pd.concat([filtered_df_summary, sub_summary])
        filtered_df_longform = pd.concat([filtered_df_longform, sub_longform])

    #Rename columns 
    filtered_df_summary.rename(
        columns={
            "pid": "PID",
            "timestamp": "Timestamp",
            "other_key": "Other Key",
            "block_order": "Block Order",
            "reversal_timings": "Reversal Timings",
            "base_craving": "Base Craving",
            "base_mood": "Base Mood",
            "money_acc": "Money Accuracy",
            "other_acc": "Other Accuracy",
            # "block_three_acc": "Block Three Accuracy",
        },
        inplace=True,
    )
    filtered_df_longform.rename(
        columns={
            "pid": "PID",
            "block": "Block",
            "block_type": "Type",
            "trial_num": "Trial",
            "cue_time": "Cue Time",
            "action": "Action",
            "action_time": "Action Time",
            "reward": "Reward",
            "reward_time": "Reward Time",
            "rt": "RT",
            "spinspeed": "Spin Speed",
            "craving_rating": "Craving Rating",
            "mood_rating": "Mood Rating",
        },
        inplace=True,
    )

    if filter_varied:
        var_pids = []

        for pid in filtered_df_longform['PID'].unique():
            varied = True
            for block in ['money', 'other']:
                sub_df = filtered_df_longform[filtered_df_longform['PID']==pid]
                cr = sub_df[(sub_df['Type']==block) & (sub_df['Craving Rating']>-1)]['Craving Rating'].values
                cr[12] = -1
                cr = cr[cr>-1]
                if cr.std() == 0:
                    varied = False
            if varied:
                var_pids.append(pid)

        filtered_df_longform = filtered_df_longform[filtered_df_longform['PID'].isin(var_pids)]
        filtered_df_summary = filtered_df_summary[filtered_df_summary['PID'].isin(var_pids)]
        
    return filtered_df_summary, filtered_df_longform
