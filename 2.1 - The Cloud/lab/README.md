Move your Linux machine to the Cloud
====

#### By the end of this assignment you should have:

- Launched a Linux server in the Cloud
- Created a publicly accessible web server
- Created a mail server
- Subscribed yourself to hourly HTML reports

Hosting a web server on your own laptop is well and good, but if you want anyone else to be able to access it, you'll need to put it on the Internet. The easiest way to do this is to use a so-called "Cloud" provider such as Amazon Web Services.

Part 0: Set up an EC2 key pair
----------------------

To connect to an Amazon EC2 instances, you need to create an **SSH key pair**.

- After setting up your account, go to the <https://console.aws.amazon.com/ec2>

- Choose **N.Virginia** as your region. Do not use a different region.
  *N. Virginia* is the default. Using a different region will require
  configuration to work correctly.

  ![image](https://s3-us-west-2.amazonaws.com/dsci/6007/assets/region.png)

- On the left click **Key Pair** and then **Create Key Pair**

  ![image](https://s3-us-west-2.amazonaws.com/dsci/6007/assets/keypair.png)

- Download and save the `.pem` private key file to a new folder `.ssh`
  in your home directory. Any folder that starts with a `.` will be
  hidden in the folder. In this case, you want to hide the sensitive
  information.

- This file contains the private key identifying your SSH client and so
  needs to be protected from snooping.

  Change the permissions of the file using this command:

  ```
  $ chmod 600 </path/to/saved/keypair/file.pem>
  ```

  These new permissions ensure that only the file's owner will be able to
  read or write the file.

Part 1: EC2 on AWS
------------------

EC2 is a remote virtual machine that runs programs much like your
local machine. Here you will learn how to run tasks on an EC2 machine.

- Launch an Ubuntu Server. Choose an instance that is free tier eligible (_i.e._ `t2.micro`). Remember to pick a keypair for which you have the `.pem` file.

- Log into the instance you have launched using `ssh`. The user name
  is `ubuntu`. Replace `KEY-PAIR` and `EC2-INSTANCE` with
  the appropriate values.  The latter is the instance's public DNS name.

        ssh -i ~/.ssh/KEY-PAIR.pem ubuntu@EC2-INSTANCE.amazonaws.com

- Remember to change the permissions on your `.pem` file if you have
  not already. `chmod 600 KEY-PAIR.pem`

- Create a file called `bootstrap.sh` containing the steps you took to set up your Ubuntu box in the [Virtualization lab](../../1.3%20-%20Virtualization/lab) (steps 6 through 8) to run on your EC2 instance:
	1. update apt-get
	2. install python packages using apt
	3. install and update python packages using pip

- Use `scp` to copy files (including your `bootstrap.sh` file) into your EC2 machine

- Run your webserver on port 80. There are two things you must keep in mind when it comes to accessing your webserver.
	- The URL or IP address - When you created a webserver in a VM, the VM lived at a locally accessible IP address: 22.22.22.22. (If you completed the optional step, this IP address would have been mapped to the URL mytestsite.com/.) The URL for your EC2 instance will be given after you launch it. It will look something like ec2-XXX-XXX-XXX-XXX.compute-1.amazonaws.com where XXX-XXX-XXX-XXX is the public IP address of the EC2 instance.
	- The port number - Every standard transfer protocol has a default port number associated with it. For HTTP, that default is 80. As we discussed in the [Virtualization lab](../../1.3 - Virtualization/lab), the default port used by Flask is 5000. This is to make sure it doesn't collide with an already running HTTP server. However, for our purposes, Flask will be our HTTP server so, we will want to tell Flask to run on port 80 (and not the default port 5000). This is easily done by specifying the port number in the `run` method of our app (_i.e._ `app.run("0.0.0.0", port=80)`). As before, you will want to run it with `nohup` and `&` to make sure it doesn't die when you exit.

- You'll notice that even though you have a web server running, you still cannot access it from your laptop. That is because AWS has helpfully blocked that port for you. In order to fix it, you must change the
  **Security Settings** to enable the inbound requests to be made.

- Click on the Security Group for your instance.

  ![Security Groups](https://s3-us-west-2.amazonaws.com/dsci/6007/assets/ec2-security-groups.png)


- In the Security Group, select **Inbound**, then **Edit**, and then
  **Add Rule**:
  	- Type: HTTP
  	- Protocol: TCP
  	- Port Range: 80 (the default for HTTP)
  	- Source: Anywhere (0.0.0.0/0)

- Save the rule.

Part 2: Use cron to email report
-----

Now you've got your web server, but it turns out your boss is very high maintenance and doesn't like having to go to a website to see your report. He wants it emailed to him every morning at 5 a.m. Since you don't want to wake up before 5 to email it to him yourself, you set up your server to do that for you.

1. Get started with `mailutils`:

    - `sudo apt install mailutils`
    	- When it asks, choose to configure as an "Internet Site". If you make a mistake here, you can go back and fix it with `sudo dpkg-reconfigure postfix`
    - Use Python's [smtplib](https://docs.python.org/3/library/email-examples.html) module to send your report to yourself from `student.[your last name]@galvanize.it` with the subject "Twitter Trends".
    - Gmail should recognize that your messages aren't actually coming from Galvanize, so it may send them to the spam folder. Keep this in mind when testing. (It may actually be working though you may not see the result if you don't look in Spam.)

2. Encapsulate your code:

    - Perhaps you now have a single script that does everything. Or maybe you have two scripts: one for running your web server and one for sending email. This is better, but if you've done this, you've probably [written everything twice](https://en.wikipedia.org/wiki/Don't_repeat_yourself#DRY_vs_WET_solutions). In order to make your code more modular, you should extract the code that is used to generate the report into a utility module which is called by both your web server and your emailer.

Stretch Goal: Deploy using Elastic Beanstalk
----

Flask's built in web server is not designed to handle a lot of traffic. While that will do for our purposes, you may want to look into a better solution. In the previous lab we discussed how to do this with [NGINX](http://flask.pocoo.org/docs/0.12/deploying/uwsgi/#configuring-nginx). However, now that you are using Amazon Web Services, you may find it easier to let [Elastic Beanstalk](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html) do the work for you. As stretch goal, use Elastic Beanstalk to deploy your server for you.

----

#### On completing this assignment, you should have submitted:

- A bootstrap file (`.sh`) that installs the necessary software on Linux
- A utility module (`.py`) that generates the HTML for your report
- A Flask app (`.py`) that runs your web server on port 80
- A mailer app (`.py`) that emails your report
- A crontab file (you may copy this from your Linux server using `crontab -l`)
