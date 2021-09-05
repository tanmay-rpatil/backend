# Backend

## Database

- Postgresql version 13
- TimescaleDB version 2.3.0 

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