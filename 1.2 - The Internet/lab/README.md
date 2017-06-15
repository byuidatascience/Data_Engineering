Generating Reports
====

#### By the end of this assignment you should have:

- Used OAuth to connect to a RESTful API
- Developed a script that automatically queries this API and generates a static web page containing the results

----

Our first report will be a simple one: what are the top 10 trending topics on Twitter today or T6.

**Don't forget:**

	$ source activate dsci6007

Part 1: Of Consumer Keys and Access Tokens
----

Before you begin, you will need your consumer key, consumer secret, access token, and access token secret. This was generated when you created your Twitter "app" at [apps.twitter.com](https://apps.twitter.com/). You will not want to store this in your code directly, as that is a security risk. Instead, put it in a YAML file outside of your git repo (replacing the strings as appropriate):

```yaml
twitter:
    consumer_key: MY_CONSUMER_KEY
    consumer_secret: MY_CONSUMER_SCRET
    token: MY_ACCESS_TOKEN
    token_secret: MY_ACCESS_TOKEN_SECRET
```

You can then load your credentials into a Python dictionary thus:

```python
import os
import yaml
credentials = yaml.load(open(os.path.expanduser('~/api_cred.yml')))
```

Your Twitter credentials would then be nested under `'twitter'` so, for example, you could get your `consumer_key` with `credentials['twitter'].get('consumer_key')`

Part 2: Accessing the Twitter API in Python
------

There are about [a dozen Python libraries](https://dev.twitter.com/resources/twitter-libraries) for accessing the Twitter API. I like [Python Twitter Tools](https://github.com/sixohsix/twitter) which can easily be installed with `pip install twitter`. Which ever one you use, you will need to then use your credentials to authenticate with the Twitter API and then you are off to the races.

Consult the [Twitter Developer Documentation](https://dev.twitter.com/rest/public) to find out how to get the top 10 trending topics for a specific place. (You may need to search a little.) Depending on the Python library you use, this feature may be built in as a specific method in an object you instantiate, or you may simply specify the endpoint and provide the parameters. Either way, you will be using Twitter's REST API (more or less directly) so it will behoove you to know how the REST API works.

Part 3: Generating the Report
------

You are limited only by your creativity in how you want to generate this report in the form of a HTML page named `top10.html`. The only constraint is that it be in the form of a static web page and that it include a timestamp footer showing when the report was generated. The simplest thing would probably be to load the data into a pandas DataFrame and call the `.to_html()` method. This main downside to this is that it makes your script dependent upon pandas. When we deploy your script to EC2, this will slow you down as pandas has a lot of dependencies.

On the other hand, if you want to be more fancy (and don't mind a lot of dependencies) you might try generating a bar plot or some other visualization (a word cloud, perhaps?). You could either output this to SVG and embed it in your HTML or you could output it as an image file and reference it using the HTML `IMG` tag.

Part 4: Publishing the Report
------

Use boto or boto3 to publish your HTML to the website bucket you created yesterday. Mitch Garnaat's [s3_website.py](https://gist.github.com/garnaat/833135) gist may provide a helpful template of how to do this.

If you include an image (_i.e._ a plot), don't forget to put the image asset on S3 along with the HTML!

Part 5: Bundling it up into a script
------

If you are like me, perhaps you have been working entirely in Jupyter up to this point. If so, that's okay, but now you need to move your code into an executable Python script. An easy way to get this process started is go to File > Download as > Python (.py). This will produce a Python script that may be executable off the bat.

Clean this script up to make it PEP 8 compliant and put `#!/usr/bin/env python` at the top so the shell knows how to execute it. (See Wikipedia's article on [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) for details on how that works.) `chmod` the file to make it executable from the command line (_i.e._ `+x`).

#### On completing this assignment, you should have submitted:

- An executable Python script (`.py`)
- The URL of the report (include this as a comment at the head of your Python script)
