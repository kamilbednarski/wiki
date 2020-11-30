# Django

Django is a web framework written using [Python](/wiki/Python) that allows for the design of web applications that generate [HTML](/wiki/HTML) dynamically.

Django was created in the fall of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. Jacob Kaplan-Moss was hired early in Django's development shortly before Simon Willison's internship ended. It was released publicly under a BSD license in July 2005. The framework was named after guitarist Django Reinhardt.

In June 2008, it was announced that a newly formed Django Software Foundation (DSF) would maintain Django in the future.

### Features
#### Components
Despite having its own nomenclature, such as naming the callable objects generating the HTTP responses "views", the core Django framework can be seen as an MVC architecture. It consists of an object-relational mapper (ORM) that mediates between data models (defined as Python classes) and a relational database ("Model"), a system for processing HTTP requests with a web templating system ("View"), and a regular-expression-based URL dispatcher ("Controller").
Also included in the core framework are:

* a lightweight and standalone web server for development and testing
* a form serialization and validation system that can translate between HTML forms and values suitable for storage in the database
* a template system that utilizes the concept of inheritance borrowed from object-oriented programming
* a caching framework that can use any of several cache methods
* support for middleware classes that can intervene at various stages of request processing and carry out custom functions
* an internal dispatcher system that allows components of an application to communicate events to each other via pre-defined signals
* an internationalization system, including translations of Django's own components into a variety of languages
* a serialization system that can produce and read XML and/or JSON representations of Django model instances
* a system for extending the capabilities of the template engine
* an interface to Python's built-in unit test framework

#### Bundled applications
The main Django distribution also bundles a number of applications in its "contrib" package, including:

* an extensible authentication system
* the dynamic administrative interface
* tools for generating RSS and Atom syndication feeds
* a "Sites" framework that allows one Django installation to run multiple websites, each with their own content and applications
* tools for generating Google Sitemaps
* built-in mitigation for cross-site request forgery, cross-site scripting, SQL injection, password cracking and other typical web attacks, most of them turned on by default
* a framework for creating GIS applications

#### Extensibility
Django's configuration system allows third party code to be plugged into a regular project, provided that it follows the reusable app conventions. More than 2500 packages are available to extend the framework's original behavior, providing solutions to issues the original tool didn't tackle: registration, search, API provision and consumption, CMS, etc.

This extensibility is, however, mitigated by internal components' dependencies. While the Django philosophy implies loose coupling, the template filters and tags assume one engine implementation, and both the auth and admin bundled applications require the use of the internal ORM. None of these filters or bundled apps are mandatory to run a Django project, but reusable apps tend to depend on them, encouraging developers to keep using the official stack in order to benefit fully from the apps ecosystem.

#### Server arrangements
Django can be run in conjunction with Apache, Nginx using WSGI, Gunicorn, or Cherokee using flup (a Python module). Django also includes the ability to launch a FastCGI server, enabling use behind any web server which supports FastCGI, such as Lighttpd or Hiawatha. It is also possible to use other WSGI-compliant web servers. Django officially supports five database backends: PostgreSQL, MySQL, MariaDB, SQLite, and Oracle. Microsoft SQL Server can be used with django-mssql on Microsoft operating systems, while similarly external backends exist for IBM Db2, SQL Anywhere and Firebird. There is a fork named django-nonrel, which supports NoSQL databases, such as MongoDB and Google App Engine's Datastore.

Django may also be run in conjunction with Jython on any Java EE application server such as GlassFish or JBoss. In this case django-jython must be installed in order to provide JDBC drivers for database connectivity, which also can provide functionality to compile Django in to a .war suitable for deployment.

Google App Engine includes support for Django version 1.x.x as one of the bundled frameworks.