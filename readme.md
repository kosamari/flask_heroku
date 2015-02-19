##Heroku flask app test

* Create Procfile with `web: gunicorn -b 0.0.0.0:$PORT app:app`
0. `virtualenv venv`
0. `source venv/bin/activate`
0. `pip install -r requirements.txt --allow-all-external`
0. `heroku create`
0. `heroku config:set BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git`
0. `git push heroku master`


create heroku app  
set build pack to multi  
create postgres  
`heroku run python`  
then import your app file with db congig to run `db.create_all()`
