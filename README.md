Article App
====

1. Install package

        pip install djangorestframework



      REST_FRAMEWORK = {
          'DEFAULT_RENDERER_CLASSES': [
              'rest_framework.renderers.JSONRenderer',
                #  если удалить rest_framework.renderers.BrowsableAPIRendere исчезнет браузерная версия
              'rest_framework.renderers.BrowsableAPIRenderer',
      
          ]
      }

2. Install django-cors-headers. 
Add cors to settings apps installed and middleware then whitelist 

           pip install django-cors-headers

3. In my case:

         CORS_ALLOW_ALL_ORIGINS = True

screenshot swagger on heroku
====

Link [https://postdjangobackend.herokuapp.com/swagger/](https://postdjangobackend.herokuapp.com/swagger/)

1. img_1

   ![](../../Users/adjie/Desktop/home_page.jpg)
   
2. img_2

   ![](../../Users/adjie/Desktop/home_page_2.jpg)

screenshot django REST framework on heroku
====

Link [https://postdjangobackend.herokuapp.com/api/v1/post/](https://postdjangobackend.herokuapp.com/api/v1/post/)

1. drf_1

   ![](../../Users/adjie/Desktop/DRF_1.jpg)
   
2. drf_2

   ![](../../Users/adjie/Desktop/DRF_2.jpg)