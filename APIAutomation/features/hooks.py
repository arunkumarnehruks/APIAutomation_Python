from behave import *
import json
import requests
import configparser
from utilities.config import *
from utilities.logger import *


def before_feature(context, scenario):
    print('From environment file : before_feature')


def after_feature(context, scenario):
    print('From environment file : after_feature')
