import pandas as pd
import sys


def load_data(filepath):
    pd.set_option('display.max_rows', None)
    return(pd.read_csv(filepath)) 

def print_analysis(df):
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


if __name__ == "__main__":
    args = sys.argv
    if not len(args) == 2:
        print("Incorrect number of arguments! Please provide only the filepath to the dataset.")
        print("Example: \t data_stats.py <filepath for EEC dataset>")
        sys.exit()
    
    
    filepath = args[1]
    df = load_data(filepath)
    print_analysis(df)
