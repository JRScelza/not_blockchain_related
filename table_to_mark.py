from tabulate import tabulate
import pandas as pd

file_name = './final_table.csv'

df_unformatted_load = pd.read_csv(file_name)

# converting simple csv txt inot formatted markdown
# each function represents the complete set inside table pipes

def logo_md(im_source, site_link):
    im_md = '[<img src="' + im_source + '" width="80">]' 
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
    phone_emoji = '[:iphone:]'
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


df_md = pd.DataFrame(columns = ['Name', 'Category' , 'Location' , 'Code', 'Demo', 'TS' ], index=site_stack)
df_md.index.name = 'Site'
df_md['Name'] = name_stack
df_md['Category'] = list(df_unformatted_load['Category'])
df_md['Location'] = list(df_unformatted_load['Location'])
df_md['Code'] = git_stack
df_md['Demo'] = demo_stack
df_md['TS'] = tech_stack


headers = ['Site']
headers.extend(list(df_md.columns))

# f = open('./README.md', 'w')
# f.write(tabulate(df_md,headers, tablefmt="pipe"))
# f.close()



