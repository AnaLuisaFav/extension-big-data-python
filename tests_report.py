import os
import pandas as pd
from pathlib import Path
import plotly.express as px

from dotenv import load_dotenv

load_dotenv(override=True)

csv_file = os.getenv("CSV_FILE_PATH")

csv_file = Path(__file__).parent / csv_file

df = pd.read_csv(csv_file)

df_filtered = df[df['status'].isin(['Passed', 'Failed', 'Blocked'])]

suite_stats = df_filtered.groupby('suite').agg(
    total_tests=('status', 'count'),
    passed_tests=('status', lambda x: (x == 'Passed').sum()),
    failed_tests=('status', lambda x: (x == 'Failed').sum()),
    blocked_tests=('status', lambda x: (x == 'Blocked').sum())
).reset_index()

suite_stats['pass_percentage'] = (suite_stats['passed_tests'] / suite_stats['total_tests']) * 100
suite_stats['fail_percentage'] = (suite_stats['failed_tests'] / suite_stats['total_tests']) * 100
suite_stats['blocked_percentage'] = (suite_stats['blocked_tests'] / suite_stats['total_tests']) * 100

for _, row in suite_stats.iterrows():
    values = []
    names = []
    hovertemplate = []
    
    if row['pass_percentage'] > 0:
        values.append(row['passed_tests'])
        names.append('Passed')
        hovertemplate.append(f"Passed Tests: {row['passed_tests']}<extra></extra>")
    if row['fail_percentage'] > 0:
        values.append(row['failed_tests'])
        names.append('Failed')
        hovertemplate.append(f"Failed Tests: {row['failed_tests']}<extra></extra>")
    if row['blocked_percentage'] > 0:
        values.append(row['blocked_tests'])
        names.append('Blocked')
        hovertemplate.append(f"Blocked Tests: {row['blocked_tests']}<extra></extra>")
    
    if values:
        fig = px.pie(
            names=names,
            values=values,
            title=f"Resultado dos Testes para a Suíte: {row['suite']}"
        )
        
        fig.update_traces(
            textinfo='percent+label',  
            hovertemplate='<b>%{label}</b><br>%{value} Teste(s)<extra></extra>', 
            marker=dict(colors=['green', 'red', '#FFBF00'])
        )
        
        fig.show()
