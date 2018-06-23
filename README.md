# Github Users API

## Functionalities

 - Create User (`login` and `email` should be unique)
 - Update existing user
 - Similar request will also update existing user details (if `login` and `email` are same)
 - Destroy user record
 - Search users based on `login`, `name`, `email`, `location`, `company` in Admin section
 - Filter users based on same parameters in `Search` API call
 - View report summary in admin panel
 - User details can be viewed in well organised Admin panel, along with the thumbnail (if available)


## Setup


### MySQL configuration

 - Install MySQL
 ```
 sudo apt-get update
 ```
 ```
 sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
 ```
 ```
 sudo mysql_install_db
 ```
 ```
 sudo mysql_secure_installation
 ```
 ```
 mysql -u root -p
 ```

- Create a Database and Database User
```
CREATE DATABASE github_users;
```

```
CREATE USER gituserproject@localhost IDENTIFIED BY 'git@123';
```

```
GRANT ALL PRIVILEGES ON github_users.* TO gituserproject@localhost;
```

---

### Project setup

 - Clone this repository
 ```
 https://github.com/omkar-dsd/github-users.git
 ```

 - Change to project root directory
 ```
 cd github-users
 ```

 - Initialize `virtualenv` with python 3.6
 ```
 virtualenv -p python3.6 venv
 ```

 - Activate `virtualenv`
 ```
 source venv/bin/activate
 ```

 - Install Python package requirements
 ```
 pip install -r requirements.txt
 ```

- Initial Migrations
```
python manage.py makemigrations
```

- Apply migrations
```
python manage.py migrate
```

- Create superuser, to get access to **Admin panel**
```
python manage.py createsuperuser
```

Follow with the steps.

- Start the server
```
python manage.py runserver 0:8000
```
## API Calls

### On Browser

- All users' list
```
http://127.0.0.1:8000/users/
```

On scrolling down, there is HTML form, which is primarily used to **create** new user. `login` and `email` are mandatory fields, and hold unique values. The functionality of this form has been modified to meet the requirements, it updates the existing user's record if found same (if `login` and `email` are same). Click on **OPTION** on top right to get form field details.

- Get user by id
```
http://127.0.0.1:8000/users/1/
```
> Note: replace `1` by desired id

This section provides option to **Update** and **Delete** the specific user's record. Click **OPTION** to get form field details.


### POSTMAN

![DEMO](http://i68.tinypic.com/wvsu86.png)

Include more parameters similarly. To make a `curl` request, include each parameter in separate `-F` flag, as each parameter is a form field, and should be sent as form post request.

### Search / Filter API :construction:

```
http://127.0.0.1:8000/users/search/
```

This provides functionality to filter users based on following parameters:

`login`, `name`, `company`, `email`, `hireable`, `location`, `total_private_repos`, `owned_private_repos`, `public_repos`, `public_gists`, `followers`, `following`, `created_at`, `private_gists`, `disk_usage`, `collaborators`, `two_factor_authentication`, `site_admin`

> :warning: Note: boolean parameters are case sensitive (`True` || `False`)


## Admin Panel

```
http://127.0.0.1:8000/admin/
```

Go to the above url, login with the credentials created in `createsuperuser` step.

The admin panel provides two views:
1. User Details
2. Report Summary

- **User Details Section**

This section displays each users details along with the thumbnail (if available). Additional functionality has also been provided to **search** user based on `login`, `created_at`, `name`, `email`, `location`, `company`. Click on login of user, and get advanced options.

- **Report Summary** :construction:

This section provides count of users added **Today**, **Week** (Past 7 days + today), **Month** and similarly aggregated count of total requests made to **search** API.

























 
