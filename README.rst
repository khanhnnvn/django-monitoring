Monitoring
==========

Monitoring is a Django 1.7 app which adds logging and a dashboard to a
Django project.

Features
--------

-  Log model which any application can use.
-  Dashboard view and page which shows version information and recent
   log entries.
-  check\_mysql\_structure command which compares model definitions to
   equivalent mysql tables and reports any discrepancies. Useful for
   checking that live database structures are correct.

Quick start
-----------

1. Add "monitoring" to your ``INSTALLED_APPS`` settings.

2. Include the monitoring URLconf in your project urls.py like this::

     url(r'^monitoring/', include('monitoring.urls', namespace='monitoring')),

3. Run ``python manage.py syncdb`` to create the monitoring models.

4. Run ``python manage.py collectstatic`` to copy static files to your
   project's static root.

5. Identfy Django project root directory path in settings like this::

     from os.path import abspath, dirname
     DJANGO_ROOT = dirname(dirname(abspath(__file__)))

6. Start the development server and visit
   `/monitoring/dashboard/ <http://127.0.0.1:8000/monitoring/dashboard/>`__
   to see summary information about the state of the project.

7. Add model-based logging for [appname] to settings.py with::

       LOGGING = {
           'version': 1,
           'disable_existing_loggers': False,
           'handlers': {
               'db_log': {
                   'level': 'INFO',
                  # Reference to handler in log.py below
                   'class': 'monitoring.log.DbLogHandler',
               }
           },
           'loggers': {
               '[appname]': {
                   'handlers': ['db_log', ],
                   'level': 'INFO',
                   'propagate': True,
               },
           }
       }

8. Use logging in [appname] like this::

       import logging
       logger = logging.getLogger('[appname]')
       . . .
       logger.info('informational message text')
       logger.warning('warning message text')
       logger.error('error message text')

Dependencies
------------

-  `Django 1.7 <https://pypi.python.org/pypi/Django/1.7>`__
-  `django-braces 1.4.0 <https://pypi.python.org/pypi/django-braces/1.4.0>`__
-  `factory_boy 2.3.1 <https://pypi.python.org/pypi/factory_boy/2.3.1>`__
