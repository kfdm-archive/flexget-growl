__version__ = 0.1

from flexget.plugin import *

try:
	from gntp_notifier import GrowlNotifier
except:
	from Growl import GrowlNotifier

class OutputGrowl:
	"""
	growl:
	  app: xxxxxxx
	  [event: event title]
	  [hostname: hostname]
	  [password: password]
	  [icon: icon]
	  [priority: -2 - 2 (2 = highest), default 0]
	"""
	
	def validator(self):
		from flexget import validator
		config = validator.factory('dict')
		config.accept('text', key='app', required=True)
		config.accept('text', key='event')
		config.accept('text', key='hostname')
		config.accept('text', key='password')
		config.accept('text', key='icon')
		config.accept('number', key='priority')
		return config
	
	def on_feed_output(self,feed):
		config = feed.config['growl']
		app = config.get('app', 'Flexget')
		notice = config.get('event', 'New release')
		host = config.get('hostname', None)
		passwd = config.get('password', None)
		icon = config.get('icon', None)
		
		growl = GrowlNotifier(
			applicationName = app,
			notifications = [notice],
			hostname = host,
			password = passwd,
			applicationIcon = icon,
		)
		growl.register()
		for entry in feed.accepted:
			growl.notify(
				noteType = notice,
				title = notice,
				description = entry['title'],
			)

register_plugin(OutputGrowl, 'growl')