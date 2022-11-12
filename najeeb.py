W = '\033[97;1m'

R = '\033[91;1m'

G = '\033[92;1m'

Y = '\033[93;1m'

B = '\033[94;1m'

P = '\033[95;1m'

C = '\033[96;1m'

N = '\x1b[0m'

import os

try:

	import requestsexcept ImportError:

	os.system("pip install requests")

 

try:

	import concurrent.futures

except ImportError:

	os.system("pip install futures")

 

import os

import sys

import time

import requests

import random

import platform

import base64

import subprocess

from concurrent.futures import ThreadPoolExecutor

import requests,bs4,uuid,json,os,sys,random,datetime,time,re,subprocess

try:

	import rich

except ImportError:

	os.system('pip install rich')

	time.sleep(1)

	try:

		import rich

	except ImportError:

		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')

from rich.table import Table as me

from rich.console import Console as sol

from bs4 import BeautifulSoup as sop

from concurrent.futures import ThreadPoolExecutor as tred

from rich.console import Group as gp

from rich.panel import Panel as nel

import base64

from rich import print as cetak

from rich.markdown import Markdown as mark

from rich.columns import Columns as col

from urllib.parse import quote

# UA LIST

#ugen2=open('frec.txt','r').read().splitlines()

#ugen=open('m.txt','r').read().splitlines()

ugen2=['Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser','Mozilla/5.0 (Android 2.2; id-id; HTC Desire)/GoBrowser']

ugen=['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-P610) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.0 Chrome/83.
