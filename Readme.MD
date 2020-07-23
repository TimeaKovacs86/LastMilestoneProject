# Last Milestone Project

## Build status

[![Build Status](https://travis-ci.com/TimeaKovacs86/LastMilestoneProject.svg?branch=master)](https://travis-ci.com/TimeaKovacs86/LastMilestoneProject)

## Index

- I. [UX](#ux)
- II. [Technologies_Used](#technologies_used)
- III. [Features](#features)
- IV. [Test](#test)
- VI [Deployment_and_version_control](#deployment_and_version_control)
- VI. [AWS](#aws)
- VII. [Media](#media)

## Description
[Up to top](#index)


## UX
[Up to top](#index)

## Technologies_Used
[Up to top](#index)

- [HTML5](https://www.w3.org/html/)
    - Hypertext Markup Language is the standard markup language for creating web pages and web applications.
- [CSS3](https://www.w3.org/Style/CSS/)
    - Cascading Style Sheets is a style sheet language used for describing the presentation of a document written in a 
    markup language like HTML.
- [Materialize](https://materializecss.com/about.html)
    - Materialize is a modern responsive CSS framework based on Material Design by Google.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - JavaScript is a lightweight interpreted or just-in-time compiled programming language with first-class functions. While it is most well-known as the scripting language for Web pages.
- [JQuery 3.2.1](https://jquery.com)
    - The project uses to simplify DOM manipulation.
- [Git](https://git-scm.com/)
    - Git is a distributed version-control system for tracking changes in source code during software development.
- [GitHub](https://github.com/)
    - GitHub Inc. is a web-based hosting service for version control using Git.
- [Django version=1.11.25](https://www.djangoproject.com/)
    -  Django is a Python-based free and open-source web framework, which follows the model-template-view architectural pattern. Django's primary goal is to ease the creation of complex, database-driven websites.
- [Python](https://www.python.org/)
    - Python is an interpreted, high-level, general-purpose programming language
- [Heroku](https://www.heroku.com/)
    - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud
- [PostgreSQL](https://www.postgresql.org/)
    - PostgreSQL, also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and technical standards compliance. It is designed to handle a range of workloads, from single machines to data warehouses or Web services with many concurrent users.
- [SQLite](https://www.sqlite.org/)
    - SQLite is a relational database management system    
- [Jinja2](https://palletsprojects.com/p/jinja/)
    - Jinja is a web template engine for the Python programming language. Jinja2 is a modern and designer-friendly templating language for Python, modelled after Django's templates.
- [Amazon Web Services (AWS)](https://aws.amazon.com/)
    - Amazon Web Services is a subsidiary of Amazon that provides on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.
- [Amazon S3](https://aws.amazon.com/s3/)
    - Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers of all sizes and industries can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics.
- [Amazon IAM (Identity and Access Management)](https://aws.amazon.com/iam/)
    - AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely. Using IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. IAM is a feature of your AWS account offered at no additional charge.

## Features
[Up to top](#index)

### Features left to implement

## Test
[Up to top](#index)

You can see the test description under this link [link]()

- Information about why I commit the .travis.yml file (Copied from the Travis official site):
    - "Note that for historical reasons .travis.yml needs to be present on all active branches of your project."

## Deployment_and_version_control:
[Up to top](#index)

I use git for version control

- Git commit after every given useful part of the project
- Git push into my github repository (Parallel runs the travis tests)
- Automatic deploy on Heroku to QA application when the running Travis test is passed
- Automatic deploy on Heroku to master branch
- Run the additional commands:
    - "migrate" command (When the database schema changed):
    ```bash
    python manage.py migrate
    ```
    - "makemigration" command (When the database schema changed):
    ```bash
    python manage.py makemigration
    ```
    - "colletcstatic" (If the static files change and need to upload into AWS bucket):
    ```bash
    python manage.py colletcstatic
    ```
  
- Before every deployment:
    - Upload database schema:
        - Change database url in env.py and type the following command to migrate changes:
        ````bash
        python manage.py migrate
       ````
        - After that I run te following command in order to update the database schema:
        ````bash
        python manage.py makemigration
       ````

#### Application hosts and databases

- For Architecture design I use MVT design pattern (Model-View-Template). Thanks for this I don't have to write raw sql queries.
- Application and Database
    - Heroku with PostgreSQL
    - Localhost with sqlite3 (Automated test with travis is running on sqlite3 as well.)
- **Database schema**:
    ![Log in page](project-description/database/database-schema.PNG)
    
#### Security

- Django authentication:
    - Django comes with a user authentication system. It handles user accounts, groups, permissions and cookie-based user sessions
- Secret keys and confidential data:
    - Locally:
        - Environmental variables contains
            - Environmental information
            - Secret keys
            - Database connection details
            - AWS authentication
            - Stripe paying information
    - Online:
        - Storing as environmental variables (Travis CI and Heroku)

## AWS
[Up to top](#index)
You can see the AWS Setup description under this [link]()

## Media
[Up to top](#index)

- Favicon picture:
    - Picture 1: [link]()
    
- Header and footer picture:
    - Picture 1: [link](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT8ho-QShrEcenwzO-XwYUbpUjsT3fKN7xxFw&usqp=CAU)

- Welcome page picture:
    - Picture 1: [link]()

- Feed page pictures:
    - Picture 1: [link](https://thumbs.dreamstime.com/b/horseradish-honey-166263672.jpg)
    - Picture 2: [link](https://foodal.com/wp-content/uploads/2017/06/Raw-Horseradish-Wrapped-in-Paper-and-Twine.jpg)
    - Picture 3: [link]()

- Products page pictures:
    - Picture 1: [link]()
    - Picture 2: [link](https://i.pinimg.com/236x/ca/87/78/ca8778a4e96433594a97618b1ab0b5d1.jpg)
    - Picture 3: [link](https://foodal.com/wp-content/uploads/2017/06/Raw-and-Grated-Horseradish.jpg)
    - Picture 4: [link](https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcTVSUlkw6Y2KTS-dM5b-SacIGUKJW_93GyNew&usqp=CAU)
    - Picture 5: [link](https://www.permaculturenews.org/wp-content/uploads/2018/10/Horseradish-Root.jpg)
    - Picture 6: [link](https://media.istockphoto.com/photos/green-peppers-horseradish-garlic-and-herbs-on-a-slate-cutting-board-picture-id1055873534?k=6&m=1055873534&s=612x612&w=0&h=7Ow2K18uFZJb8OYSYK6_WYZlx2PqX9NrapN5XtUkwNw=)