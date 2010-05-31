# See http://flexget.com/wiki/Developers/TDD

from tests import FlexGetBase,log
import sys

class TestGrowl(FlexGetBase):
	__yaml__ = """
feeds:
  test:
    mock:
      - {title: 'foobar'}
    accept_all: true
    growl:
      app: flexget
"""
	def test_feature(self):
		# run the feed
		self.execute_feed('test')
