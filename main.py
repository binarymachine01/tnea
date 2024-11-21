import pandas as pd
import pydash

cutoff = pd.read_excel('cutoff.xlsx').to_dict(orient='records')
college = pd.read_excel('college.xlsx').to_dict(orient='records')
branch = pd.read_excel('branch.xlsx').to_dict(orient='records')

college_list = {}
branch_list = {}

for itr in college:
    if itr['TNEA\nCode No.'] not in college_list:
        college_list[itr['TNEA\nCode No.']] = itr['Name of the College']

for itr in branch:
    if itr['BRANCH\nCODE'] not in college_list:
        branch_list[itr['BRANCH\nCODE']] = itr['BRANCH NAME']

try:
    for itr in cutoff:
        if itr['COLLEGE\nCODE'] in college_list:
            itr['COLLEGE NAME'] = college_list[itr['COLLEGE\nCODE']]
        else:
            itr['COLLEGE NAME'] = itr['COLLEGE\nCODE']
        if itr['BRANCH\nCODE'] in branch_list:
            itr['BRANCH NAME'] = branch_list[itr['BRANCH\nCODE']]
        else:
            itr['BRANCH NAME'] = ''
except Exception as e:
    itr['BRANCH NAME'] = ''
print("")
