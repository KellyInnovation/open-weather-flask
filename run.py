import sys
import os

from app import app
try: 
	import settings
except ImportError:
	print("Please copy settings-dist.py to settings.py and update your API key")
	sys.exit()

app.config.from_object(settings)
app.run(debug=True)