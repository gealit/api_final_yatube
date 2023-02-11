# YaTube

###### Description:
Sample project, like blog, with your posts and preferences between the authors.
But it's an API version. Authentication performed by simpleJWT.

### Как запустить проект:

Clone the repo:

```
git clone <url_to_the_project> <where_you_wanna_clone>
```

```
cd kittygram
```

Create and activate your virtual environment:

```
python3 -m venv env
source env/bin/activate
```

In case of using windows machine:

```
python -m venv env
env/Scripts/activate
```

Install all required dependencies from the file requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

You have to execute existing migrations:

```
python3 manage.py migrate
```

And run the project!

```
python3 manage.py runserver
```
the command will run the project on http://127.0.0.1:8000/

### Examples:

All the data you will see in [JSON](https://www.json.org/) format.

All addition information to build a frontend client you can see on:
http://<your_domain.com>/redoc/

In case you run this project locally:
http://127.0.0.1:8000/redoc/
