# Lambda Zip and Deploy

This will package your code into a zip and upload it to AWS 

### Create
```
./helper/lambda_helper.sh create GetWebResult

```

### Update
```
./helper/lambda_helper.sh update GetWebResult
```

# Run the application from the command line

First, select a target AWS environment with aws-saml-cli

Use the virtualenv python3 interpreter

```
[projectname]/bin/python3 [filename].py
```

# References

### Prerequisite python libraries
```
> python --version
Python 2.7.15
> pip --version
pip 10.0.1 from /usr/local/lib/python2.7/site-packages/pip (python 2.7)
> pip install virtualenv
> virtualenv --version
16.0.0
```

### Development Environment: Setting up Python virtualenv

go to the root of the directory 

create virtualenv... (note this is installing python3) 
```
$ virtualenv -p /usr/local/bin/python3.5 [name of virtual env]
```
Use the virtual environment, it needs to be activated:
```
$ source [root directory]/bin/activate
e.g.
$ source ami_auto_tagging/bin/activate
```

The name of the current virtual environment will now appear on the left of the prompt. From now on, any package that you install using pip will be placed in the my_project folder, isolated from the global Python installation.

Install packages as usual, for example:

```
> pip install -r requirements.txt
```

When finished with virtualenv, end the sessions with:
```
$ deactivate
```
This puts you back to the system’s default Python interpreter with all its installed libraries.

When setting up a local debugger, refer to the /volume_cleanup/bin/python3 as your python interpreter

### Python virtualenvs

http://docs.python-guide.org/en/latest/dev/virtualenvs/

### Python package virtualenvs for Lambda

https://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
