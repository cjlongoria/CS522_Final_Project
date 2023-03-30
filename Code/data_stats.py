import pandas as pd

pd.set_option('display.max_rows', None)
df = pd.read_csv('EEC\Equity-Evaluation-Corpus\Equity-Evaluation-Corpus.csv')  

# Counts for each sentence template
grouped_template = df.groupby(['Template']).size()
# Counts of sentences for each name
grouped_person = df.groupby(['Person']).size()
# Counts of sentences for each emotion
grouped_emotion = df.groupby(['Emotion']).size()

print("-"*50)
print(f'Columns in the dataset {df.columns.to_list()}')
print("-"*50)
print(f'Total sentence templates in the dataset {len(grouped_template)}')
print(grouped_template)
print("-"*50)
print(f'Total names (and noun phrases) in the dataset {len(grouped_person)}')
print(grouped_person)
print("-"*50)
print(f'Total emotions in the dataset {len(grouped_emotion)}')
print(grouped_emotion)
print("-"*50)
