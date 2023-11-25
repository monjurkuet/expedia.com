import undetected_chromedriver as uc
import pandas as pd

df_ip=pd.read_csv('input.csv').stories.to_list()
out_json=[]
driver = uc.Chrome()

for url in df_ip:
    driver.get(url)
    author=driver.find_element('xpath','//div[@class="ag-intro"]/span').text
    title=driver.find_element('xpath','//div[@class="ag-intro"]/h1').text
    content=driver.find_element('xpath','//div[@class="ag-post-container"]').text
    content_html=driver.find_element('xpath','//div[@class="ag-post-container"]').get_attribute('innerHTML')
    data={'author':author,'title':title,'content':content,'content_html':content_html,'url':url}
    out_json.append(data)

df_out=pd.DataFrame(out_json)

df_out.to_excel('output.xlsx')