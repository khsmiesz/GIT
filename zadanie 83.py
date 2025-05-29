import pandas as pd
writer = pd.ExcelWriter('TaskFile.xlsx', engine='xlsxwriter')
url="https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551/"
data = pd.read_html(url, header=0)
df=data[0]
df.to_excel(writer, sheet_name="Task83")
writer.close()