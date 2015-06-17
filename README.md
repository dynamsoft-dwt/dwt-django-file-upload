# Uploading Files with Django
The samples demonstrate how to upload files with Django.

Basic Steps
-----------
1. Create a new Django project
   ```django-admin startproject project```.

2. Create an application
   ```python manage.py startapp application```.

3. Create a folder templates under project root. Declare the directory ```[os.path.join(BASE_DIR, 'templates')]``` in settings.py.

   ```
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   ```

4. Create a basic HTML page **index.htm** under **templates**.

5. If you have static resources, such as CSS files, JavaScript files, image files and so on, declare the static resources path in **settings.py**.

   ```
   STATICFILES_DIRS = (
       os.path.join(BASE_DIR, "Resources"),
   )
   ```

6. Map URLs in **urls.py**

   ```
   urlpatterns = [
       url(r'^$', views.home, name="home"),
       url(r'^upload/', views.upload, name="upload"),
   ]
   ```

   And then create corresponding functions in **views.py**

   ```
   def home(request):
       return render(request, 'index.htm', {'what':'DWT File Upload with Django'})

   def upload(request):
       if request.method == 'POST':
           handle_uploaded_file(request.FILES['RemoteFile'], str(request.FILES['RemoteFile']))
           return HttpResponse("Successful")

       return HttpResponse("Failed")

   def handle_uploaded_file(file, filename):
       if not os.path.exists('upload/'):
           os.mkdir('upload/')

       with open('upload/' + filename, 'wb+') as destination:
           for chunk in file.chunks():
               destination.write(chunk)
   ```

7. Add **csrf token** to Web client. For example:

   ```
   <form action="{{ request.build_absolute_uri }}upload/" method="POST" enctype="multipart/form-data">
          {% csrf_token %}
          <input type="file" name="file"/>
          <br />
          <input type="submit" value="Upload File" />
        </form>
   ```

   If you don't want to use **csrf token**, you just need to comment out ```'django.middleware.csrf.CsrfViewMiddleware'``` in **settings.py**.

Uploading Files with Form
-----------
form-upload

Uploading Image Files with Dynamic Web TWAIN
--------------------------------------------
dwt-upload

Blog
----
Coming soon...
