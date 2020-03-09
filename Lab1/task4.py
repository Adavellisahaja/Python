#@title Task 4
import requests
from bs4 import BeautifulSoup


page = requests.get('https://catalog.umkc.edu/course-offerings/graduate/comp-sci/')
soup = BeautifulSoup(page.text, 'html.parser')

a = soup.find_all("span")
b = soup.find_all(attrs={'class':'courseblock'})
ans = {}
for i in b:
  title = i.find(attrs={'class':'title'}).text.strip('\n')
  desc = i.find(attrs={'class':'courseblockdesc'}).text.strip('\n')
  code = i.find(attrs={'class':'code'}).text.strip('\n')
  ans.update({code:[title,desc]})
  print(title)
  print(desc)
  print()
