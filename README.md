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

## To-Do

- Create the API to send and receive data in batches
- make a database schema ER diag
- Learn Basics of AWS, AWS EC2, AMI

## Questions

- Communication from analytics module? JSON data for features? 
- 

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