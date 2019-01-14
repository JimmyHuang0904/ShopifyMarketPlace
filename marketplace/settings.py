import os

class BaseConfig():
  pass


# We use LDAP authentication because account look up for login and processing
# is used more than creation (LDAP will be able to handle more reads than write operation)

# Configuration for Production
class ProdConfig(BaseConfig):
  ENV   = 'prod'

class DevConfig(BaseConfig):
  ENV   = 'dev'
  DEBUG = True
