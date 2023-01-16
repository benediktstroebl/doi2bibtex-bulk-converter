from distutils.file_util import write_file
import requests
import pandas as pd
import time

headers = {
    'authority': 'www.doi2bib.org',
    'referer': 'https://www.doi2bib.org/bib/',
}

dois = [
'10.1257/jep.31.2.211',
'10.1073/pnas.1517441113',
'10.1126/science.aau2706'
]


output = []
output = pd.DataFrame (output, columns=['doi','bibtex_str'])

# Test whether output at the end of the script works
output.to_excel("export_py.xlsx")
output = []

i = 1
for id in dois:
    response = requests.get('https://www.doi2bib.org/8350e5a3e24c153df2275c9f80692773/doi2bib?id=' + id, headers=headers)
    bibtex_item = response._content.decode("utf-8")

    item = [id, bibtex_item]
    output.append(item)
    print(bibtex_item)
    i += 1

    if i in range(50,601,25):
        print("Waiting for 10 minutes....")
        time.sleep(600)

    time.sleep(5)

print(output)


output = pd.DataFrame (output, columns=['doi','bibtex_str'])


output.to_excel("export_py.xlsx")