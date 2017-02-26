# Collaborative List API    

## Install
`$ python3 setup.py install`

## Setup
1. Add environment variable to your system.

  `$ echo 'export FLASK_CONFIGURATION=[dev|deploy|prod]`

2. Edit the hosts file in order to test OAuth2 login on the local machine.

  `127.0.0.1 api.vfree.org localhost`
  
## Usage
Access from `https://api.vfree.org`

Documentation: [https://teamghostbuster.github.io/restful-api/](https://teamghostbuster.github.io/restful-api/)


## Tools
Build documentation with APIDOC

`$ make doc`

Format code with PEP8 standard

`$ make format`
