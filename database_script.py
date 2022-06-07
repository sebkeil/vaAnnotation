"""

Steps to run this script:

1. Run command: python manage.py shell
2. Exectue script line by line

NOTE: DO NOT RUN FILE AS A WHOLE

"""

from main.models import AnnotationBox
import pandas as pd
import random

sent_df = pd.read_csv('reuters_sample800_r2.csv', index_col=0)

random_idxs = random.sample(range(1, len(sent_df)+1), len(sent_df))

j = 0
for i, row in sent_df.iterrows():
    a = AnnotationBox()
    a.id = i
    a.article_id = int(row['article_id'])
    a.sentence = str(row['sentences'])
    a.rank_idx = int(random_idxs[j])
    a.save()
    j += 1

quit()
