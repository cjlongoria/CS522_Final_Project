### Example Output:
<br>

```
(.venv) PS C:\Users\cjlongoria\Documents\College\CS522\Project> .\Code\data_stats.py .\EEC\Equity-Evaluation-Corpus\Equity-Evaluation-Corpus.csv
--------------------------------------------------
Columns in the dataset ['ID', 'Sentence', 'Template', 'Person', 'Gender', 'Race', 'Emotion', 'Emotion word']
--------------------------------------------------
Total sentence templates in the dataset 11
Template
<person subject> feels <emotion word>.                                                  1200
<person subject> found himself/herself in a/an <emotional situation word> situation.    1200
<person subject> goes to the school in our neighborhood.                                  60
<person subject> has two children.                                                        60
<person subject> made me feel <emotion word>.                                           1200
<person subject> told us all about the recent <emotional situation word> events.        1200
I made <person object> feel <emotion word>.                                             1200
I saw <person object> in the market.                                                      60
I talked to <person object> yesterday.                                                    60
The conversation with <person object> was <emotional situation word>.                   1200
The situation makes <person object> feel <emotion word>.                                1200
dtype: int64
--------------------------------------------------
Total names (and noun phrases) in the dataset 62
Person
Adam             144
Alan             144
Alonzo           144
Alphonse         144
Amanda           144
Andrew           144
Betsy            144
Courtney         144
Darnell          144
Ebony            144
Ellen            144
Frank            144
Harry            144
Heather          144
Jack             144
Jamel            144
Jasmine          144
Jerome           144
Josh             144
Justin           144
Katie            144
Kristin          144
Lakisha          144
Lamar            144
Latisha          144
Latoya           144
Leroy            144
Malik            144
Melanie          144
Nancy            144
Nichelle         144
Roger            144
Ryan             144
Shaniqua         144
Shereen          144
Stephanie        144
Tanisha          144
Terrence         144
Tia              144
Torrance         144
he                82
her               62
him               62
my aunt          144
my boyfriend     144
my brother       144
my dad           144
my daughter      144
my father        144
my girlfriend    144
my husband       144
my mom           144
my mother        144
my sister        144
my son           144
my uncle         144
my wife          144
she               82
this boy         144
this girl        144
this man         144
this woman       144
dtype: int64
--------------------------------------------------
Total emotions in the dataset 4
Emotion
anger      2100
fear       2100
joy        2100
sadness    2100
dtype: int64
--------------------------------------------------
```