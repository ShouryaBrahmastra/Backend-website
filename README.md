# Backend-website
This is a fully functional backend website with responsive web-pages &amp; contact form database using flask
## Remember not to give your personal detail anywhere in this project.
### This is for windows users how they can run on their device:-
Cut-Paste all the files from this repository into your desktop and give the file name "port".
#### In the search bar of your windows write powershell and open it now, copy-paste the below code:
###### set-ExecutionPolicy Unrestricted
##### (Some option are there) type capital Y
#### Now go into your directory where only the downloaded repository folder,i.e,port folder and open it.
#### Now close the powershell and open a new powershell, and now type:
###### cd .\Desktop\port\
###### python
If >> symbol is not shown download python and enable the environment option during installation; to exit from >> press Ctrl+Z and then press enter
#### Now type
###### python -m virtualenv venv
#### And then copy the below line:
###### .\venv\Scripts\activate.ps1
#### We are now into an virtual environment. Now type:
###### pip install flask
#### Once the installation is completed write:
###### pip install flask-sqlalchemy
#### Once the installation is completed write:
###### python 
#### when ">>" this symbol appears write
###### >>from app import db
###### >>db.create_all()
#### Now write: 
###### python .\app.py
#### The server starts running 
#### Copy the url port and boom backend full working website is active.(The port will be http://127.0.0.1:5000/ [copy this in your browser])
#### Once you close this powershell and want to run again just give the following code in the new powershell:
###### cd .\Desktop\port\
###### .\venv\Scripts\activate.ps1
###### python .\app.py
and the port will be active again.
##### To view the database entries visit https://inloop.github.io/sqlite-viewer/ , drag and drop "todo2" file and there you can view all the entries.

---

## Deployment
To view the deployment of my original portfolio website that is inspired from this basic structure [Click Here](https://shouryaportfolio.herokuapp.com/)
