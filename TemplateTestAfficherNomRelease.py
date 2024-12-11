import requests
import datetime
from datetime import datetime
import time

release = getCurrentRelease()
releaseName = release.title
NomCompletDeRelease = "XL Release - "+ releaseName

print(NomCompletDeRelease)