# Developer Log

##### Project Spec Sheet

- [x] Start a new Django project called Blog.
- [x] Create an app called blogs in the project, with a model called BlogPost.
- [x] The model should have fields like title, text, and date_added.
- [] Create a superuser for the project, and use the admin site to make a couple of short posts.
- [] Make a home page that shows all posts in chronological order.
- [] Create a form for making new posts and another for editing existing posts.
- [] Fill in your forms to make sure they work .

# Developer Instructions

##### Create Project

1. Run virtual environment with `source 11_env/bin/activate`
2. Run terminal command `pip install Django` if Django is not installed.
3. Start project with `django-admin.py startproject Blog .` if project
has not been created yet. Make sure you don't forget the `.` at the end of terminal project creation command.
4. Create the database with `python manage.py migrate` terminal command
if migration has not been applied.
5. Terminal run server with `python manage.py runserver`

##### Create APP

1. Activate virtual environment with `source 11_env/bin/activate`
2. Run the terminal command `python manage.py startapp BlogPost` to
create a new project.
3. Add title, text, and date_added to models.py
4. Add the tuple in settings.py under `INSTALLED_APPS = [ ]` list
`'BlogPost',`
5. Make migrations with `python manage.py makemigrations BlogPost`
6. Run `python manage.py migrate`

##### Creating a Superuser

1. Run terminal command (with manage.py file as directory)
`python manage.py createsuperuser`
2. Create Username and Password.


##### Registering a Model With the Admin Site
1. Open admin.py file
2. Check github commit `Register a model with admin site` in my repo.

##### Adding Topics
1. Check github commit `Adding topics.` in my repo.
2. Run terminal command `python manage.py makemigrations BlogPost`
3. Run terminal command `python manage.py migrate`




END AT Building Additional Pages : Template Inheritance












