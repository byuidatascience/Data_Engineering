Drinking from the Firehose
----

In this lab we will be moving from small data to large, from structured to unstructured, and from single API requests to a constant stream of data.

### Part 0: Create a new Vagrant box

This time we will be using Vagrant to develop our solution locally and then deploy our solution to the Cloud using the `provider` flag. In our `Vagrantfile` we will need to specify a `do` for both `config.vm.provider 'virtualbox'` and `config.vm.provider 'aws'`. (In our first virtualization lab, `config.vm.provider 'virtualbox'` was assumed. In our last lab, we set a condition for `config.vm.provider 'aws'`. Now we will have both.) Your `config.vm.provider 'aws' do` can be the same as in the last lab. For `config.vm.provider 'virtualbox'`, you may want to `override.vm.network "private_network"`. Once you've created your `Vagrantfile` spin up a local instance using `vagrant up --provider=virtualbox`.

### Part 1: Streaming Data

Stream tweets from Twitter's public Firehose [sample](https://dev.twitter.com/streaming/reference/get/statuses/sample) API endpoint into Amazon Kinesis using an infinite loop. Hint: use the [TwitterStream](https://github.com/sixohsix/twitter/tree/master#the-twitterstream-class) class in the Python Twitter Tools library

### Part 2: Storing Data

[Create a Firehose Delivery Stream to Amazon S3](http://docs.aws.amazon.com/firehose/latest/dev/basic-create.html#console-to-s3). I recommend you set the buffer size to 64 MB and the interval to 600 seconds (for reasons that will become clear later this week). You can then use [boto3](https://boto3.readthedocs.io/en/latest/reference/services/firehose.html) to stream your data into S3. Store these data as [jsonlines](http://jsonlines.org/). In other words, use `json.dumps` to convert the object back into a string for the Firehose and append a new line delimiter. The data you insert should look like `json.dumps(tweet) + '\n'`.

### Part 3: Deploy to the Cloud

Once you've got everything working, destroy your VirtualBox instance and launch your AWS instance (_i.e._ `vagrant up --provider=aws`). As before, it will automagically copy the contents of the local directory into `/vagrant/`. However, since the machine is not locally hosted, that folder will not be kept in sync. You will probably still need to `vagrant ssh` to do a little configuration to get your script to work. Once you are sure that everything is working, use the `(nohup <YOUR_PYTHON_SCRIPT>.py &)` formula to leave it running in the background so you can log out.

**Leave this running on an EC2 instance dedicated to this task.  We will continue to amass data in the weeks to come.**

----

#### On completing this assignment, you should have submitted:

- A bootstrap file (`.sh`) that installs the necessary software on Linux
- A `Vagrantfile` including two `provider` configurations (`virtualbox` and `aws`)
- An executable (`.py`) that streams data from Twitter to Kinesis

**Remember:** Make sure that your lab submission does _not_ include your credentials!
