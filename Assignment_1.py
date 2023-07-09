#!/usr/bin/env python
# coding: utf-8

# # Assignment-1

# In[28]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
Soup = BeautifulSoup(page.content)
#title = Soup.find('span',class_="mw-headline")
#title.text

title = []

for i in Soup.find_all('span',class_="mw-headline"):
    title.append(i.text)
     
    
df = pd.DataFrame({'Title':title}) 

df


# In[58]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
Soup = BeautifulSoup(page.content)
#title = Soup.find('div',class_="presidentListing")
#title.text.split('(')[0]

 #first_Name.split('\n')
Name = []

for i in Soup.find_all('div',class_="presidentListing"):
    Name.append((i.text.split('(')[0]).split('\n')[1])
    
Name
    


# In[69]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
Soup = BeautifulSoup(page.content)
#title = Soup.find('div',class_="presidentListing")
#(title.text.split(':')[1]).split('\n')[0]


Term = []

for j in Soup.find_all('div',class_="presidentListing"):
    Term.append((j.text.split(':')[1]).split('\n')[0])
    
    
    
df = pd.DataFrame({'Name':Name,'Terms':Term})

df

    


# In[163]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')

Soup = BeautifulSoup(page.content)
#player = Soup.find('span',class_="u-hide-phablet")
#player.text
team = []
for i in Soup.find_all('span',class_="u-hide-phablet"):
    team.append(i.text)
    
df = pd.DataFrame({'Match':team})
df.head(10)


# In[ ]:





# In[175]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')

soup = BeautifulSoup(page.content)

match = soup.find('td',class_="rankings-block__banner--matches")

matche = []
matche.append(match.text)
#normal = soup.find('td',class_="table-body__cell u-center-text")

Allmatch = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    Allmatch.append(i.text)
for i in range(0,len(Allmatch),2):
        matche.append(Allmatch[i])
     
   # Allmatch.append(i.text)

df = pd.DataFrame({'Matches':matche})   
df


# In[176]:


from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')

soup = BeautifulSoup(page.content)

matchspoint = soup.find('td',class_="rankings-block__banner--points")
points = []

points.append(matchspoint.text)
#normal = soup.find('td',class_="table-body__cell u-center-text")

All = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    All.append(i.text)
for i in range(1,len(All),2):
        points.append(All[i])
     
   # Allmatch.append(i.text)
points


# In[183]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/odi')

soup = BeautifulSoup(page.content)
value = soup.find('td',class_="rankings-block__banner--rating u-text-right")
rating = []
rating.append(value.text.split('\n')[1])

for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
    
df = pd.DataFrame({'Match':matche, 'Points':points, 'Rating':rating})
df.head(10)


# In[88]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')

soup = BeautifulSoup(page.content)
player = soup.find('div',class_="rankings-block__banner--name-large")


top10 = []

top10.append(player.text)

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    top10.append(i.text.split('\n')[1])
    
top10


# In[98]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')

soup = BeautifulSoup(page.content)
player = soup.find('div',class_="rankings-block__banner--nationality")

Country = []

Country.append(player.text.split('\n')[2])

for i in soup.find_all('span',class_="table-body__logo-text"):
    Country.append(i.text)
    
Country


# In[161]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

pages = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')

soup = BeautifulSoup(pages.content)

rank = soup.find('div',class_="rankings-block__banner--rating")
Ranking = []

Ranking.append(rank.text)

for i in soup.find_all('td',class_="table-body__cell rating"):
    Ranking.append(i.text)
    
df = pd.DataFrame({'Batsman':top10, 'Team':Country,'Rating':Ranking})

df.head(10)


# In[144]:


from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')
soup = BeautifulSoup(page.content)

bowlers = soup.find('div',class_="rankings-block__banner--name-large")

teamPlayer = []
teamPlayer.append(bowlers.text)

for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    teamPlayer.append(i.text.split('\n')[1])
    
teamPlayer


# In[132]:


from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')

soup = BeautifulSoup(page.content)
#for team player name
team = soup.find('div',class_="rankings-block__banner--nationality")
Team = []

Team.append(team.text.split('\n')[2])

for i in soup.find_all('span',class_="table-body__logo-text"):
    Team.append(i.text)
    
Team


# In[160]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')

soup = BeautifulSoup(page.content)

rating = soup.find('div',class_="rankings-block__banner--rating")

rating_final = []

rating_final.append(rating.text)

for i in soup.find_all('td',class_="table-body__cell rating"):
    rating_final.append(i.text)
    
#rating_final
    
df = pd.DataFrame({'Bowlers':teamPlayer, 'Team':Team, 'Rating':rating_final})

df.head(10)


# In[164]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')

soup = BeautifulSoup(page.content)

country = soup.find('span',class_="u-hide-phablet")

Allcountry = []

Allcountry.append(country.text)


for i in soup.find_all('span',class_="u-hide-phablet"):
    Allcountry.append(i.text)
    
 
df = pd.DataFrame({'Match':Allcountry})
df.head(10)


# In[ ]:





# In[85]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')

soup = BeautifulSoup(page.content)

match = soup.find('td',class_="rankings-block__banner--matches")

matche = []
matche.append(match.text)
#normal = soup.find('td',class_="table-body__cell u-center-text")

Allmatch = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    Allmatch.append(i.text)
for i in range(0,len(Allmatch),2):
        matche.append(Allmatch[i])
     
   # Allmatch.append(i.text)

df = pd.DataFrame({'Match':matche})   
df

    


# In[ ]:





# In[107]:


from bs4 import BeautifulSoup
import requests

page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')

soup = BeautifulSoup(page.content)

matchspoint = soup.find('td',class_="rankings-block__banner--points")
points = []

points.append(matchspoint.text)
#normal = soup.find('td',class_="table-body__cell u-center-text")

All = []

for i in soup.find_all('td',class_="table-body__cell u-center-text"):
    All.append(i.text)
for i in range(1,len(All),2):
        points.append(All[i])
     
   # Allmatch.append(i.text)
points


# In[108]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.icc-cricket.com/rankings/womens/team-rankings/odi')

soup = BeautifulSoup(page.content)

value = soup.find('td',class_="rankings-block__banner--rating u-text-right")


rating = []
rating.append(value.text.split('\n')[1])
for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    rating.append(i.text)
    
df = pd.DataFrame({'Matches':matche,'Points':points, 'Rating':rating})

df.head(10)


# In[ ]:





# In[70]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import islice

page =  requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')
soup = BeautifulSoup(page.content)

Batsman = soup.find('div',class_="rankings-block__banner--name")

Allbatsman = []

Allbatsman.append(Batsman.text)

for i in soup.find_all('td',class_="table-body__cell name"):
    Allbatsman.append(i.text.split('\n')[1])
    

Allbatsman = list(islice(Allbatsman, len(Allbatsman)-1))
df = pd.DataFrame({'Batsman':Allbatsman})

df


# In[69]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import islice

page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')

soup = BeautifulSoup(page.content)

ladies = soup.find('div',class_="rankings-block__banner--nationality")

ladiesteam = []

ladiesteam.append(ladies.text.split('\n')[2])


for i in soup.find_all('span',class_="table-body__logo-text"):
    ladiesteam.append(i.text)

    
ladiesteam = list(islice(ladiesteam, len(ladiesteam)-1))
    
df = pd.DataFrame({'Team':ladiesteam})

df



# In[76]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import islice



page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi')

soup = BeautifulSoup(page.content)

value = soup.find('div',class_="rankings-block__banner--rating")

totalrating = []

totalrating.append(value.text)


for i in soup.find_all('td',class_="table-body__cell u-text-right rating"):
    totalrating.append(i.text)
    
    
totalrating = list(islice(totalrating, len(totalrating)-1))



#li = list(islice(li, len(li)-1))
    
#df = pd.DataFrame({'Rating':totalrating})
    
df = pd.DataFrame({'Batsman':Allbatsman, 'Ladies_Team':ladiesteam, 'Rating':totalrating})

df.head(10)


# In[169]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import islice



page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')

soup = BeautifulSoup(page.content)

value = soup.find('div',class_="rankings-block__banner--nationality")

team = []

team.append(value.text.split('\n')[2])
for i in soup.find_all('span',class_="table-body__logo-text"):
    team.append(i.text)
    
    
df = pd.DataFrame({'Team':team})

df.head(10)


# In[173]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')

soup = BeautifulSoup(page.content)

value = soup.find('div',class_="rankings-block__banner--rating")

rating = []

rating.append(value.text)

for i in soup.find_all('td',class_="table-body__cell rating"):
    rating.append(i.text)

    
df = pd.DataFrame({'Rating':rating})
df.head(10)


# In[174]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import islice



page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')

soup = BeautifulSoup(page.content)

value = soup.find('div',class_="rankings-block__banner--name-large")
bowlers = []

bowlers.append(value.text)
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    bowlers.append(i.text.split('\n')[1])
        
df = pd.DataFrame({'All_Rounder':bowlers, 'Team':team, 'Rating':rating})

df.head(10)


# In[ ]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
from itertools import islice



page = requests.get('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')

soup = BeautifulSoup(page.content)


# In[14]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')

soup = BeautifulSoup(page.content)

paper_title = []

for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    paper_title.append(i.text)
    
df = pd.DataFrame({'Paer_Title':paper_title})

df


# In[16]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')

soup = BeautifulSoup(page.content)

Authors = []

for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    Authors.append(i.text)
    
df = pd.DataFrame({'Authors':Authors})

df


# In[19]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')

soup = BeautifulSoup(page.content)

published_date = []
for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    published_date.append(i.text)
    
df = pd.DataFrame({'Date':published_date})

df


# In[37]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
soup = BeautifulSoup(page.content)

paper_url = []
for i in soup.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    paper_url.append(i.get('href'))
    
df = pd.DataFrame({'Paper_Title':paper_title,'Authors':Authors,'Published_Date':published_date,'Paper_Url':paper_url})

df
    
   
    


# In[ ]:





# In[59]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

soup = BeautifulSoup(page.content)

restaurant_name = []

for i in soup.find_all('div',class_="restnt-info cursor"):
    restaurant_name.append(i.text)
    
df = pd.DataFrame({'Restaurants':restaurant_name})

df


# In[ ]:





# In[60]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

cuisine = []

for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])
    
    
df = pd.DataFrame({'Cuisine':cuisine})

df
    


# In[62]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

soup = BeautifulSoup(page.content)

location = []

for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
    
df = pd.DataFrame({'Location':location})

df


# In[65]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

soup = BeautifulSoup(page.content)

rating = []

for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)

df = pd.DataFrame({'Rating':rating})
df  
    


# In[67]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

soup = BeautifulSoup(page.content)

image = []

for i in soup.find_all('img',class_="no-img"):
    image.append(i.get('data-src'))
    
df = pd.DataFrame({'Restaurant_Name':restaurant_name, 'Cuisine':cuisine, 'Location':location, 'Rating':rating, 'Image_URL':image})

df
    
    


# In[197]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get('https://www.cnbc.com/search/?query=headlines&qsearchterm=headlines')

soup = BeautifulSoup(page.content)

head = soup.find('span',class_="SearchResult-publishedDate")
head



# In[ ]:




