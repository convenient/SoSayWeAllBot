# Installation

```
mysql < database-generation.sql
sudo apt-get install python-pip
sudo pip install praw
sudo apt-get install python-dev libmysqlclient-dev
sudo pip install MySQL-python
sudo pip install requests==2.5.3
```

Then pop this in your crontab

```
* * * * * python SoSayWeAllBot
```