# Instagram Bot

This project is a Python-based Instagram automation tool. Currently, it automatically comments on photos based on a selected tag.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project uses Python 3 and Google Chrome. Required libraries will be listed below, I suggest using Anaconda to quickly get this project running.

```
Libraries needed:

paramiko
requests
selenium

Download chromedriver here: https://sites.google.com/a/chromium.org/chromedriver/downloads
Make note of where it's been downloaded! You'll need to know that directory soon.
```

### Installing

Once the above prerequisites have been installed, follow these steps to run the script on your system.

```
Replace the path from chromedriver on line 20 of the code to the directory on your system. By default, it's my file path, but it should give an example of what it looks like.
```

Next

```
Customize the comment.txt file with comments of your choice. Separate the comments by using one line for each comment. For example:

-----
Nice photo
Cool
Fun!
-----
```


## Running the bot

Steps to run the bot. Start by opening your command line (through Anaconda if you use it).

Change directories to the bot.py file location

```
cd C:\directory
```

Next run the script by entering:

```
python bot.py
```

It will now begin to request a series of information.

```
username: your Instagram username
password: your Instagram password (don't worry, no information is saved)

enter comment list file name (example.txt): the .txt file with your comments in them. By default, it's 'comment.txt'. Be sure to include the .txt at the end!

what tag should we search for: enter the Instagram tag you would like to use. For example: nature.
```
The bot will now open a chrome browser and begin commenting on photos. The delay between posts and total posts is pre-set, but can be customized.

## Contributing

Please read [CONTRIBUTING.md] for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Vezel** - *Initial work*
* **Francesco Aiello** * - *Project updating and improvements*

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License.

