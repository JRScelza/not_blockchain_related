from tabulate import tabulate
import pandas as pd

file_name = './final_table.csv'

df_unformatted_load = pd.read_csv(file_name)

# converting simple csv txt inot formatted markdown
# each function represents the complete set inside table pipes

def logo_md(im_source, site_link):
    im_md = '[<img src="' + im_source + '" width="50">]' 
    site_md = '(' + site_link + ')'
    return(im_md+site_md)

def name_md(name):
    name_front = '[' + name + ']'
    section = '(#' + name + ')'
    return(name_front + section)

def git_md(git_url):
    git_icon = '[<img src="https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png" width="40">]'
    git_link = '(' + git_url + ')'
    return(git_icon + git_link)

def demo_md(demo_url):
    phone_emoji = ':iphone:'
    demo_link = '(' + demo_url + ')'
    return(phone_emoji + demo_link)

def tech_spec_md(spec_url):
    paper_emoji = ':page_facing_up:'
    spec_link = '(' + spec_url + ')'
    return(paper_emoji + spec_link)


#compiling the new df, listxlist

name_stack = []
git_stack = []
site_stack = []
demo_stack = []
tech_stack = []

for i in range(len(df_unformatted_load)):
    im_source, site_link = df_unformatted_load['logo_source'][i] , df_unformatted_load['Site'][i]
    name = df_unformatted_load['Name'][i]
    git_url = df_unformatted_load['Code'][i]
    demo_url = df_unformatted_load['Demo'][i]
    spec_url = df_unformatted_load['spec_url'][i]



    site_stack.append(logo_md(im_source, site_link))
    name_stack.append(name_md(name))
    git_stack.append(git_md(git_url))
    demo_stack.append(demo_md(demo_url))
    tech_stack.append(tech_spec_md(spec_url))


df_md = pd.DataFrame(columns = ['Site' , 'Name', 'Category' , 'Location' , 'Code', 'Demo', 'TS' ])
df_md['Site'] = site_stack
df_md['Name'] = name_stack
df_md['Category'] = list(df_unformatted_load['Category'])
df_md['Location'] = list(df_unformatted_load['Location'])
df_md['Code'] = git_stack
df_md['Demo'] = demo_stack
df_md['TS'] = tech_stack


headers = list(df_md.columns)

f = open('./markdown.txt', 'w')
f.write(tabulate(df_md,headers, tablefmt="pipe"))
f.close()

# # df = df_unformatted_load[df_unformatted_load.columns[0:11]]

# blockchain_dict = df.to_dict('index')

# blockchain_companies = list(df.index)
# blockchain_keys = list(df.columns)



# #Markdown Params.
# git_logo_source = "https://assets-cdn.github.com/images/modules/logos_page/GitHub-Mark.png"

# def section_name(name):
#     s = name.lower()
#     section_header = '(#' + s + ')'
#     return(section_header)

# # white_paper_emoji = 
# # computer_emoji =
# # smartphone_emoji = 

# # logo_hyperlink = [<img src="http://www.google.com.au/images/nav_logo7.png">](http://google.com.au/)

# #There are github markdown emoji's take note https://gist.github.com/rxaviers/7360908

# #Making Markdown

# column_count = len(df.columns)
# bar_count = column_count + 1

# headerSeparator = '|:--' * column_count + '|'

# table = []
# for i in range(len(df)):
#     table.append(list(df.iloc[i]))

# headers = list(df.columns)

# # print(tabulate(table, headers, tablefmt="pipe"))


