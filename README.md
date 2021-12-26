# HTTP Logging

This is a simple class that inherits from the logging.Handler class. 
It allows to send POST requests to a given URL (e.g., a webhook) using the logging package from the standard library.

It is very usefull for applications deployed in cloud, because it allows to employ external error handlers (like for example Google Cloud Functions). 
It can be also exploited to get notifications through third-party APIs (like Telegram Bots, or Gmail) in case of critical errors.

---
## Installation 

Being just one class it can be integrated in your own code without any problems. 
But if you want to include it in your application programmatically 
(as you may want to do when deploying a cloud-based application) it can be easily done by installing it from this repository:

#### Using pip

`pip install git+https://github.com/Biumsp/HTTP-logging.git@main#egg=httplogging`

#### Using the __requirements.txt__ file

In the __requirements.txt__ file add the line 

`git+https://github.com/Biumsp/HTTP-logging.git@main#egg=httplogging`

In both cases `@main` is set to specify the branch and `egg=httplogging` to explicitly name the package.

---
## Usage

First of all you need to import the class

`from httplogging import HttpHandler`

Then you need to:
- Create an instance of the class HttpHandler
- Set the handler level (using the logging library conventions and classes)
- Define a json format of the type logging.Formatter
- Set the formatter of the handler
- Add the handler to a logging.Logger instance
- Use the logger as usual

A usage example is given in the `tutorials/logging_tutorial.py` file
