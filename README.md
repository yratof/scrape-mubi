# mubi

Arr! This one scrapes movies from the mubi.com now showing page, then looks for magnet links for those and hopefully finds them :D

You'll need to have torrent-hound in your system in order to search for magnet links. 


```
git clone this-repo
cd this-repo

python -m pip install --user -r requirements_for_th.txt
python -m pip install --user -r requirements.txt

```
Run the command and to get the output 

```
python get_movies.py
```

It saves output as a json file too.

Example output looks like this.

<center>
<img src="https://raw.githubusercontent.com/ozkc/pirate-mubi/master/screenshot.png" width="700" />
</center>

