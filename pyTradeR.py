# -*- coding: utf-8 -*-
# @Author: Boya Chiou
# @Date: 2018-03-22 17:16:22
# @Last Modified by: boyac
# @Last Modified time: 2019-12-23 09:06:48

import ffn

class ScoreTrade(object):
	"""docstring for ClassName"""
	def __init__(self, ticker, principal):
		self.ticker = ticker
		self.principal = principal


	def entry_score(self, high=0, low=0, bought=0):
		"""進場分數(控制在50以下) 1 - (High - Buy)/(High - Low) * 100"""
		self.bought = bought
		entrys = (1 - (high - self.bought) / (high - low)) * 100
		if entrys < 50:
			print "Entry score = {} / Below 50, Good Job".format(round(entrys, 2))
		else:
			print "Entry score = {} / Keep it below 50".format(round(entrys, 2))


	def exit_score(self, high=0, low=0, sold=0):
		"""出場分數(控制在50以上) 1 - High-Sell/(High-Low) * 100"""
		self.sold = sold
		exits = (1 - (high - self.sold) / (high - low)) * 100
		if exits > 50:
			print "Exit score = {} / Above 50, Good Job".format(round(exits, 2))
		else:
			print "Exit score = {} / Keep it above 50".format(round(exits, 2))


	def channel_score(self, channel_h=0, channel_l=0):
		#self.bought = bought
		#self.sold = sold
		self.channel_h = channel_h
		self.channel_l = channel_l
		self.channel_width = round((self.channel_h - self.channel_l), 1)
		self.pctg = round((self.sold - self.bought) / self.channel_width, 1)

		if self.pctg >= 0.3:
			print "Channel Score: A"
		elif 0.3 > self.pctg >= 0.2:
			print "Channel Score: B"
		elif 0.2 > self.pctg >= 0.1:
			print "Channel Score: C"
		elif self.pctg < 0.1:
			print "Channel Score: D" 
		# print self.pctg # to confirm what the pctg means here 


	def target_price(self, fee=0, quantity=0):
		self.tp = 0.3 * self.channel_width + self.bought + (fee / quantity)
		print "{} / Target Price: {}".format(self.ticker, self.tp)


	def equity_curve(self):
		""""""
		pass


	def mm(self, price=0, exposure=0.3, stoploss=0.4):
		"""Money management, keep principal exposure to a single stock: 2%, 6%"""

		threshold = exposure * stoploss
		self.pos = (self.principal * exposure) / (price)
		if threshold <= 0.06:
			print "{0}, threshold:{1}, allowed position: {2}".format(self.ticker, threshold, round(self.pos))
		else:
			print "Exposure over Threshold!"


	

if __name__ == "__main__":
	S = ScoreTrade('THD', 1000)

	"""
	Note: THD exit @ 101.022
	*0.94 of upper edge of the channel
	"""

	print "-------------------BREAK-------------------"

	dta = ffn.get('thd:Open, thd:High, thd:Low, thd:Close', start='2019-01-01')

	highlow = dta.iloc[:,1:3]
	print highlow
	# for index, row in highlow.iterrows():
	# 	print row, S.entry_score(row['pcghigh'], row['pcglow'], 3.8)

	print S.mm(price=90, exposure=0.2, stoploss=0.2)

	# test sublime git, global variable