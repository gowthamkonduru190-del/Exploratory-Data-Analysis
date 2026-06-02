import pandas as pd
from data_profiling import ProfileReport
df = pd.read_csv(r"D:\internship\titanic.csv")
df.head()  # preview first 5 rows
profile = ProfileReport(df, title="Titanic Data Profiling Report", explorative=True)
profile.to_file("titanic_report.html")
profile.to_notebook_iframe()