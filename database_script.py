"""

Steps to run this script:

1. Run command: python manage.py shell
2. Exectue script line by line

NOTE: DO NOT RUN FILE AS A WHOLE

"""

from main.models import AnnotationBox
import pandas as pd

sent_df = pd.read_csv('reuters_sample200.csv', index_col=0)

for i, row in sent_df.iterrows():
    a = AnnotationBox()
    a.id = i
    a.article_id = int(row['article_id'])
    a.sentence = str(row['sentences'])
    a.save()

quit()
