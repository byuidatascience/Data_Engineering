Automate More
-------------

#### By the end of this assignment you should have:

- Used Vagrant to launch an EC2 instance
- Used Airflow to schedule hourly emails
- Spammed your professor with hourly reports

***N.B.*** As usual, this lab will be done in pairs. _However_, all students expected to complete this lab. I want to be receiving hourly emails from all of you.

----

In this assignment we will be improving on the automation we started in the last lab.

Recall: in yesterday's lab you created a `bootstrap.sh` script to install the necessary libraries to run your Python scripts. You also configured `cron` to execute your emailer script at regular intervals.

Today you will direct Vagrant to use your `bootstrap.sh` script to set up your EC2 instance the way you want it.

Optional: Use [Apache Airflow](https://airflow.incubator.apache.org/) instead of `cron` to schedule your jobs. At this point, the advantages of using Airflow in place of `cron` will not be all that great. The main advantage for now is that you can configure it using your bootstrap script (though you will still need to setup `mailutils` by hand). Later on, however, the ability to set up a chain of tasks with dependencies (in a directed acyclic graph, or DAG) will become useful.

Step 1: Use Vagrant to manage your EC2 instance
-------

Follow the instructions for [Vagrant AWS Provider](https://github.com/mitchellh/vagrant-aws) to use Vagrant to manage your EC2 instance. You may want to change the `ami` to what you used in yesterday's lab. You will probably want to set `aws.instance_type = 't2.micro'`. And you definitely do not want to include your key and secret in your Vagrantfile since that will be part of your homework submission. If your AWS key and secret are already set as environment variables, you can follow [Oliver Veits' method](https://oliverveits.wordpress.com/2016/04/01/aws-automation-using-vagrant-a-hello-world-example/) and set `aws.access_key_id = ENV['AWS_KEY']` and `aws.secret_access_key = ENV['AWS_SECRET']`. If you haven't set that up and don't want to, you could also locate your key and secret in a YAML file like we did with our Twitter credentials and reference them using Ruby's YAML library as per [Scott Lowe's method](http://blog.scottlowe.org/2016/01/14/improved-way-yaml-vagrant/). Either way, make sure that do not end up putting your AWS key and secret on Github!

Step 2: Provision!
-------

Look at [Provisioning](https://www.vagrantup.com/docs/getting-started/provisioning.html) and see how to add your `bootstrap.sh` script to your Vagrantfile. (It just requires one line.) Now all those tedious `apt` and `pip` installs will be done automatically when you run `vagrant up`.

#### _N.B._
- Don't forget to include the `-y` option in your `apt` install to get it to assume "yes" for your installs (_i.e._ `apt -y install python3-pip`)
- Do **not** try to install `mailutils` this way. That installation requires user interaction (remember: to configure your node as an "Internet Site") so you will have to do this manually afterwards. But you can use this to install Pandas and everything else.

[OPTIONAL] Step 3: Schedule Workflows
-------

Begin by installing following the [Quick Start](https://pythonhosted.org/airflow/start.html) guide to Airflow with these two modifications:

1. `export AIRFLOW_HOME=/vagrant/airflow` not `~/airflow` (this will help later when you want to set up Airflow using Vagrant). You will probably
2. In order to avoid potential ambiguity between Python 2 and Python 3 packages, I recommend you use `python3 -m pip install airflow` (and not just `pip install airflow`) to install Airflow

[OPTIONAL] Step 4: Configure Airflow to execute your mail script
-------

You should now be able to compose a DAG for Airflow that will execute your mail script `@hourly`

[REQUIRED] Step 5: Share your results
-------

Now that everything's working, reconfigure your Airflow job to email your report to [alessandro+homework@galvanize.com](mailto:alessandro+homework@galvanize.com) hourly.

----

#### On completing this assignment, you should have submitted:

Old Files (these may or may not be changed from the previous assignment):

- A bootstrap file (`.sh`) that installs the necessary software on Linux
- A utility module (`.py`) that generates the HTML for your report
- A mailer app (`.py`) that emails your report

New Files (human generated):

- A `Vagrantfile` including `provision` and `provider` configured (with `bootstrap.sh` and `aws` respectively)
- Optional: A DAG file (`.py` under `airflow/dags`) that executes your mailer app hourly

In addition, I should be receiving an email from each of you every hour due to your cron job.
