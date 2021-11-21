#!/usr/bin/env python
# coding: utf-8

# In[164]:


file = 'give bson file path'


# In[165]:


import pandas as pd
import json
import csv


# In[166]:


file_list=[file,file3,file4,file5,file6,file7,file8,file9]
for file in file_list:
 file_output_name=file.split('.')
 raw_data = pd.read_json(file,
                        lines=True,
                        orient='columns')
 raw_data.to_excel(f"{file_output_name[0]}.xlsx")
 

