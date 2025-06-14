import pandas as pd
import os

data = { 'Name': ['Muskan', 'Yogesh', 'Manish'],
        'Age': ['19', '17', '23'],
        'City': ['Prayagraj', 'Narnaul', 'Bokaro']
}
df= pd.DataFrame(data)

new_row_loc = {'Name': 'Paramvir', 'Age': '47', 'City': 'Hajipur'}
df.loc[len(df.index)]= new_row_loc

data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)
#file path
file_path = os.path.join(data_dir,'Sample_data.csv')
# dataframe to csv file
df.to_csv(
    file_path,index = False
)
print(f" csv file saved to {file_path}")