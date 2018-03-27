from tabulate import tabulate
import pandas as pd

file_name = './clean_table_final.csv'

df_unformatted_load = pd.read_csv(file_name, index_col=0)

start_keys = ['Twitter' , 'Relevant to DataCoin']
df = df_unformatted_load[start_keys]
df = df.fillna(value = '-')


# df = df_unformatted_load[df_unformatted_load.columns[0:11]]

blockchain_dict = df.to_dict('index')

blockchain_companies = list(df.index)
blockchain_keys = list(df.columns)



#Markdown Params.
git_logo_source = "https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png"

def section_name(name):
    s = name.lower()
    section_header = '(#' + s + ')'
    return(section_header)

# white_paper_emoji = 
# computer_emoji =
# smartphone_emoji = 

# logo_hyperlink = [<img src="http://www.google.com.au/images/nav_logo7.png">](http://google.com.au/)

#There are github markdown emoji's take note https://gist.github.com/rxaviers/7360908

#Making Markdown

column_count = len(df.columns)
bar_count = column_count + 1

headerSeparator = '|:--' * column_count + '|'

table = []
for i in range(len(df)):
    table.append(list(df.iloc[i]))

headers = list(df.columns)

# print(tabulate(table, headers, tablefmt="pipe"))


