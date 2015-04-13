import pandas as pd
import glob

path = 'data_csv'

allFiles = glob.glob(path + '/*.csv')
df = pd.DataFrame()

for i, filename in enumerate(allFiles):

    df_file = pd.read_csv(filename, skiprows=0)
    df_file['filename'] = filename
    df_file['file_ID'] = i

    df = df.append(df_file)

df.to_csv('full_dataset.csv')