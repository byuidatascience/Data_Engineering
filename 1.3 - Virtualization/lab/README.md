Your Very Own Web Server
====

#### By the end of this assignment you should have:

- Initialized a virtual machine using Vagrant
- Created web server using Flask

----

This lab is adapted from [Getting Started with Vagrant, SSH & Linux Server](https://gist.github.com/learncodeacademy/5f84705f2229f14d758d) only instead of [Precise Pangolin](http://releases.ubuntu.com/12.04/), we'll be using [Xenial Xerus](http://releases.ubuntu.com/16.04/) and instead of [NGINX](https://www.nginx.com/resources/wiki/) we'll be using [Flask](http://flask.pocoo.org/).

By now you should have installed [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and [Vagrant](https://www.vagrantup.com/downloads.html). (If you haven't, do so now!)

1. Follow the instructions for building [a minimal Flask application](http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application) and test it.

2. Once it's working, run:

		vagrant init ubuntu/xenial64

	to generate a Vagrantfile.

3. start and ssh into your new machine to make sure it works

		vagrant up
		vagrant ssh

	- `exit` to disconnect

4. Open the Vagrantfile and uncomment the private_network line & change to your desired IP:

    	config.vm.network "private_network", ip: "22.22.22.22"

	- Optional: make a fake domain for that ip
   		- run `sudo open /etc/hosts -a atom` to open your /etc/hosts file in Atom
    	- add this line to the end of the file and save `22.22.22.22 mytestsite.com`

5. reload and ssh into your new machine

		vagrant reload
		vagrant ssh

	One of the neat things about Vagrant is that it automatically maps the directory on the host machine where the Vagrantfile is located to the `/vagrant/` directory on the VM. So any files that are in the same directory as your Vagrantfile (including the Vagrantfile itself) should be visible if you navigate to `/vagrant/`. You should see the `hello.py` file you generated in step 1.

	This will make it easy to move files in and out of your VM.

6. 	update apt-get

		sudo apt-get update

7. 	Install python packages using apt:

		sudo apt install python3-pip

8. 	Install and update python packages using pip (notice that in our Ubuntu box we will be using `python3` and not `python` to run Python 3.5 applications)

		python3 -m pip install pip pandas twitter Flask -U

9. Make your web server externally accessible by adding `--host=0.0.0.0` to the command line:

		flask run --host=0.0.0.0

	Now, if you navigate to `22.22.22.22:5000` you should see your 'Hello, World!' web page.

10. Port your code from last week's lab to generate an HTML file that will be served by SimpleHTTPServer.

	- _N.B._ You will need to copy your `api_cred.yml` file into your VM. You may use the `/vagrant/` folder to do this but it is not recommended you leave it there. In other words you should do something like this (starting in the host machine; `exit` if you are still in the VM.)
		1. `cp ~/api_cred.yml ./`  # copy credentials file to Vagrant folder
		2. `vagrant ssh`  # ssh into VM
		3. `mv /vagrant/api_cred.yml ~/`  # move credentials file to home directory

		If you then exit the VM your credentials file should no longer be in that directory (and therefore no longer in your repo).

At the end, if you navigate to `22.22.22.22:5000` you should see a report of the top 10 trending topics on Twitter.

11. Run your webserver

	1. If you want to run Flask in the background so you can do other things, append `&` to the end:

			flask run --host=0.0.0.0 &

	2. This will leave Flask running in the background until you exit, at which point it will quit. In order to keep SimpleHTTPServer even after you exit (or "hangup", recalling ancient dialup TTY systems), prepend your command with `nohup`:

			nohup flask run --host=0.0.0.0 &

		Note: this technique of running a command with [`nohup [COMMAND] &`](https://en.wikipedia.org/wiki/Nohup) is useful any time you want to keep a continuously running script going on a remote server. There are more advanced ways to do this, such as with [supervisord](http://supervisord.org/) but this will work in a pinch.

Stretch Goal: Configure NGINX
------------

Flask's built in web server is not designed to handle a lot of traffic. While that will do for our purposes, you may want to look into a better solution. In the video you watched, you saw [how to configure NGINX on your virtual machine](https://gist.github.com/learncodeacademy/5f84705f2229f14d758d). As a stretch goal, complete that exercise and then [configure it to work with your Flask app](http://flask.pocoo.org/docs/0.12/deploying/uwsgi/#configuring-nginx).

----

#### On completing this assignment, you should have submitted:

- A Flask app (`.py`) that pulls data from Twitter and presents it in HTML
- A Vagrantfile with the `private_network` configured
