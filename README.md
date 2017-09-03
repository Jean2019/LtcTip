# LiteTipper

A simple tip bot for litecoin on Reddit

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Python 2.7+

MySQL 5.6+



Lastest version of praw, pymysql, pyyaml

```
pip install praw
pip install pymysql
pip install pyyaml

```

or 

```
pip install praw --upgrade
pip install pymysql --upgrade
pip install pyyaml --upgrade
```

### Configuration


Open `config/config.yml` and fill the Reddit and MySQL sections.

You can get Reddit credentials on https://ssl.reddit.com/prefs/apps

#### Create MySQL tables
```
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE Answered (
  id int(11) NOT NULL,
  post_id varchar(11) COLLATE utf8mb4_bin NOT NULL,
  `date` datetime DEFAULT '0000-00-00 00:00:00'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;


ALTER TABLE Answered
  ADD PRIMARY KEY (id);


ALTER TABLE Answered
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;
```


