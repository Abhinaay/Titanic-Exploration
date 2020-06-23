# Titanic-Exploration
A website that take us in the past where we can book tickets for our journey on the largest ship of that time i.e. RMS Titanic . It will tell you the the chances of your Survival, based on your credentials, in case of any accident.

## Live Link To Website:
#### [View](http://13.232.26.255:8888/)

## Colab Link:
#### [View in Colab](https://colab.research.google.com/drive/1na1ZtJ5TXJCn4vKht7RkAJw1l3u4LSym)

## Technologies Used:
* HTML5
* CSS3
* Bootstrap
* JavaScript
* Python
* Flask
* Nginx
* Gunicorn

## Python Libraries Used: 
* NumPy
* Pandas
* Scikit Learn
* Pickle

## Machine Learning Algorithms Used For Analysis:
* [Decision Tree Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html)
* [Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)
* [Linear Regression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)

## Deployment Procedure
We deployed the site on AWS EC2 Instance having Ubuntu as OS.
Following commands are used to setup the environment.
```
sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
pip3 install flask
pip3 install numpy
pip3 install pandas
pip3 install matplotlib
pip3 install sklearn
sudo apt-get install nginx
sudo apt-get install gunicorn3

```
Guinorn is a python web server gateway interface (wsgi).
Nginx cannot directly communicate or interact with flask application. So we are using gunicorn to run as an interface web server and flask application.

Now we will clone our git repository that contains the project.
```
git clone REPOSITORY_NAME
cd REPOSITORY_NAME
```
Create gunicorn as a service.
```
sudo vi /etc/systemd/system/gunicorn3.service
```
```
[Unit]
Description=Gunicorn service
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=YOUR_WORKING_DIRECTORY
ExecStart=/usr/bin/gunicorn3 --workers 3 --bind unix:Titanic-Exploration.sock -m 007 app:app
```
```
sudo systemctl daemon-reload
sudo service gunicorn start
```
Once this is done, we will move to the nginx configuration file.
```
cd /etc/nginx/sites-enabled
sudo vi flaskApp
```
Now, write the following configuration in the flaskApp file
```
server{
    listen 8888;
    server_name YOUR_PUBLIC_IP;

    location / {
        proxy_pass http://unix:PATH_OF_SOCKET_FILE; 
        
    }

}
```
In our case socket file is Titanic-Exploration.sock
Restart the nginx service and follow the steps mentioned below.
```
sudo service nginx restart
```

Finally, our flask app is deployed! :)