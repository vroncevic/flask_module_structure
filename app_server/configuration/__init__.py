# encoding: utf-8
__author__ = "Vladimir Roncevic"
__copyright__ = "Copyright 2017, Free software to use and distributed it."
__credits__ = ["Vladimir Roncevic"]
__license__ = "GNU General Public License (GPL)"
__version__ = "1.0.0"
__maintainer__ = "Vladimir Roncevic"
__email__ = "elektron.ronca@gmail.com"
__status__ = "Updated"

class BaseConfig(object):
	"""
	Define class BaseConfig with attribute(s) and method(s).
	Base initial configuration.
	It defines:
		attribute:
			SECRET_KEY - Development key for session accessing
		method:
			None
	"""

	SECRET_KEY = "my_precious"
