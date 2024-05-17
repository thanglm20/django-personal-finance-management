


## Create pipenv (First time when creating project)
```
Install
$ pipenv install
$ pipenv install django
```
```
Start project
$ django-admin startproject finance_manager
```

```
Install PostgresSQL
Restart password
ALTER USER postgres WITH PASSWORD 'admin'
$ ALTER DATABASE personal_finance_management_db OWNER TO admin;
$ GRANT CONNECT ON DATABASE pfm_db  TO admin;
$  GRANT ALL PRIVILEGES ON TABLE side_adzone TO jerry;
$ pipenv install psycopg2
```


## Deployment 
```
Using heroku
```


## References

```
https://github.com/CryceTruly/trulyexpensesyoutube
Note:  # name in path url is to set for url in html and redirect_to
For PDF exporting on Windows: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#windows and export  GTK3 path env
```