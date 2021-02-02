

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Build a dataframe with 4 connections
df = pd.read_csv("comment pairs.csv")   # comment pair
df2 = pd.read_csv("Immediate Comments.csv")    #Immediate comments

# Build your graph
G = nx.from_pandas_edgelist(df, source='parent_id', target='id')


df_out=pd.DataFrame([[1, 1]], columns=['parent_com','com']) #appending output

#iterating trhough each immediate comment
for index, row in df2.iterrows():
    print (row["id"])
    try: 
        res = nx.descendants(G, row["id"])
        for val in res:
            df3=pd.DataFrame([[row["id"], val]], columns=['parent_com','com'])
            df_out=df_out.append(df3,ignore_index=True)      
    except:
        continue
    
    
df_out.to_csv("output.csv") 




'''
# Plot it
nx.draw(G, with_labels=True)
plt.show()


res = nx.descendants(G, "evnhk9o")
print (res)
'''