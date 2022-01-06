# Backend

## Database
 
- Postgresql version 13
- TimescaleDB version 2.4.0 

```sql
 -- SQL query to check the timescaledb version is - 
 SELECT extversion
 FROM pg_extension
 where extname = 'timescaledb';
```

## Directory Structure
- ``` accounts/ ``` : Django app defining custom user model
- ``` api/ ``` : Django app defining all models and providing the api interface
- ``` backend/ ``` : Django settings, conf directory
- ``` database_design/ ``` : Documentation for the database schema. 
- ``` testing/ ``` : Scripts to test the APIs
- ``` media/ ``` : Temperory - location to store media files 

# TODO
- **IMP -> HANDLE ERROR CONDITIONS** such as invalid serializers
- Improve Documentation
- Beutify script dump below

# Server Setup
	Instructions to setup a development server on Debain/Desbian based systems.
### Install Custom Python Version (Python 3.8.1)
```bash
$ export PYTHON_VERSION=3.8.1
$ export PYTHON_MAJOR=3
$ cd /opt
$ sudo wget https://www.python.org/ftp/python/3.8.10/Python-3.8.10.tar.xz
$ sudo tar -xvf ./Python-3.8.10.tar.xz

$ cd ./Python-3.8.10
$ ./configure 
$ make 
$ sudo make altinstall
```
### Postgreql install
```bash
$ sudo apt update
$ sudo apt -y install gnupg2
$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

$ echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" |sudo tee  /etc/apt/sources.list.d/pgdg.list
 
$ sudo apt update
$ sudo apt -y install postgresql-13 postgresql-client-13
$ sudo pg_ctlcluster 13 main status
```
### TimescaleDB setup
```bash
$ sudo apt install postgresql-common
$ sudo sh /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh

$ sudo sh -c "echo 'deb [signed-by=/usr/share/keyrings/timescale.keyring] https://packagecloud.io/timescale/timescaledb/debian/ $ (lsb_release -c -s) main' > /etc/apt/sources.list.d/timescaledb.list"
$ wget --quiet -O - https://packagecloud.io/timescale/timescaledb/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/timescale.keyring
$ sudo apt update
$ sudo apt install timescaledb-2-postgresql-13
 
$ sudo timescaledb-tune --quiet --yes
# Restart PostgreSQL instance
$ sudo service postgresql restart

```
### psql setup

    sudo su - postgres
    psql
        postgres=# ALTER USER postgres PASSWORD 'admin4Post';
        ALTER ROLE
        postgres=# \q
    sudo psql -U postgres -h localhost
        postgres=# CREATE database backend;
        postgres=# CREATE EXTENSION IF NOT EXISTS timescaledb;
        postgres=# \q

### setup django server

    git clone 
    cd ./backend
    python3.8 -m venv env
    source ./env/bin/activate
    pip install -r ./requirements.txt
    
    export SECRET_KEY=$(cat /dev/urandom | LC_ALL=C tr -dc '[:alpha:]'| fold -w 50 | head -n1)
    
### For development server, dsable apacge and use django server.

    sudo update-rc.d apache2 disable
    sudo /etc/init.d/apache2 stop
    sudo /home/f20190054/backend/env/bin/python /home/f20190054/backend/manage.py  runserver 0.0.0.0:80

### For setting up cronjob to start serer at reboot

    crontab -e
        #insert the following line 
        @reboot /home/f20190054/backend/env/bin/python /home/f20190054/backend/manage.py  runserver 0.0.0.0:80

### For truncating a table

    sudo psql -U postgres -h localhost
        postgres=# \c backend
        backend=# TRUNCATE api_sensor_reading;


## Data Req

1/10th in terms 

40 users - accel, gro, mag, gps, heart 

accel - 100hz - gro, mag, 
heart - 0.5Hz

4fps each 320x240px 

for an entire semester's 

16hrs day 

https://stackoverflow.com/questions/33636973/how-to-store-hdf5-hdf-store-in-a-django-model-field

[Writing custom model fields | Django documentation | Django](https://docs.djangoproject.com/en/3.2/howto/custom-model-fields/)
