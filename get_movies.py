import requests
from bs4 import BeautifulSoup
import subprocess
import json
import ast


url = 'https://mubi.com/en/no/collections/new-on-mubi'
response = requests.get(url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')
script_tag = soup.find('script', type='application/json')
json_text = script_tag.string  # or script_tag.contents[0] if .string doesn't work
r = json.loads(json_text)

# print(r);

m = r['props']['initialProps']['pageProps']['collection']['films']

movies = []
movie_list = {}

for movie in range(0, len(m)):
    movies.append(m[movie])


for movie in range(0,len(movies)):
    movie_list[movie] = {}
    movie_list[movie]['title'] = movies[movie]['original_title']
    movie_list[movie]['directors'] = movies[movie]['directors']
    movie_list[movie]['short_synopsis'] = movies[movie]['short_synopsis']
    movie_list[movie]['year'] = str(movies[movie]['year'])
    movie_list[movie]['country'] = movies[movie]['title_locale']

    print('################### MOVIE META ######################')
    print(' ')
    print('title: ' + movie_list[movie]['title'])
    print('short_synopsis: ' + movie_list[movie]['short_synopsis'])
    print('year: ' + movie_list[movie]['year'])
    print('country: ' + movie_list[movie]['country'])
    print('------------------ MAGNET META ---------------------')

    try:
        title = movie_list[movie]['title']
        year = movie_list[movie]['year']

        print(title)
        print(year)
        title = title.replace("'", "")

        torrent = subprocess.check_output(['python', 'torrent-hound.py','-q', title + ' ' + year]).decode()
        torrent = ast.literal_eval(torrent)

        movie_list[movie]['magnetlink'] = torrent['1337x']['results']['0']['magnet']
        movie_list[movie]['magnetlinktitle'] = str(torrent['1337x']['results']['0']['name']) + ' ratio: ' + str(torrent['1337x']['results']['0']['ratio']) + ' seeders: '+ str(torrent['1337x']['results']['0']['seeders'])

        print('magnetlinktitle: '+ movie_list[movie]['magnetlinktitle'])
        print('magnetlink: \n'+ movie_list[movie]['magnetlink'])
    except Exception as e:
        print(e)
        movie_list[movie]['magnetlink'] = 'Nothing found '
        movie_list[movie]['magnetlinktitle'] = '¯\_(ツ)_/¯'
        print('magnetlinktitle: '+ movie_list[movie]['magnetlinktitle'])
        print('magnetlink: '+ movie_list[movie]['magnetlink'])
        print('####################################################')

with open('movie_list.json','w') as f:
    json.dump(movie_list, f, indent=4, sort_keys=False)
