# nzbiketracker

Flask web server and a database to keep track of bikes roaming the city

# Quickstart

**Setup Virtualenv**

`python -m virtualenv nzbiketracker-env`


**Activate Virtualenv**

Inside nzbiketracker directory

`. ../nzbiketracker-env/bin/activate`


**Install Requirements**

`pip install -r requirements.txt`


**Make the Files Executable**

`chmod +x nzbiketracker.sh update.py`


**Start Update.py script**

This will create the bike database, loop every 60 seconds to pole the 3rd party api for new bike objects and insert the results into the database. *- temporary*

`while true; do ./update.py; sleep 60; done`


**Start Flask Web Server**

In a new terminal:

`./nzbiketracker.sh`

*Optional - enable flask debug mode (do not do this in prod):*

`FLASK_ENV=development ./nzbiketracker.sh`


**View Bikes**

Browse to flask web server, by default - http://127.0.0.1:5000/ 

![map view](https://github.com/dunderhay/nzbiketracker/blob/master/map-view.png)



# Overview

![overview image](https://github.com/dunderhay/nzbiketracker/blob/master/app-overview.png)
