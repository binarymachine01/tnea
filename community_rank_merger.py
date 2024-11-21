import os
import pandas as pd

def list_files(folder_path):
    file_list = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


allotment_folder_path = os.path.join(os.getcwd(), 'merger_data', 'data')
community_folder_path = os.path.join(os.getcwd(), 'merger_data', 'community')

allotment_files = list_files(allotment_folder_path)
community_files = list_files(community_folder_path)

community_dfs = {}

for file in community_files:
    year = os.path.basename(file).split(".")[0].split("_")[0]
    community_dfs[year] = pd.read_excel(file)

for file in allotment_files:
    year = os.path.basename(file).split(".")[0].split("_")[0]
    rd = os.path.basename(file).split(".")[0].split("_")[1]

    community_file = os.path.join(community_folder_path, '{}_Community_Rank.xlsx'.format(year))
    round_file = file

    community_df = community_dfs[year]
    round_df = pd.read_excel(round_file)

    pd.merge(round_df, community_df, on='APPLICATIONNO', how='left').to_excel('{}_{}_Community.xlsx'.format(year, rd))
