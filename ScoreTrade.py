# -*- coding: utf-8 -*-
# @Author: Boya Chiou
# @Date:   2018-03-22 17:16:22
# @Last Modified by:   Boya Chiou
# @Last Modified time: 2018-03-26 11:21:24


class ScoreTrade(object):
	"""docstring for ClassName"""
	def __init__(self, ticker):
		self.ticker = ticker

	def entry_score(self, high=0, low=0, bought=0):
		"""進場分數(控制在50以下) 1 - High-Buy/(High-Low) * 100"""
		self.bought = bought
		entrys = (1-(high-self.bought)/(high-low))*100
		if entrys < 50:
			print "entry score = {} / Below 50, Good Job".format(entrys)
		else:
			print "entry score = {} / Keep it below 50".format(entrys)

	def exit_score(self, high=0, low=0, sold=0):
		"""出場分數(控制在50以上) 1 - High-Sell/(High-Low) * 100"""
		self.sold = sold
		exits = (1 - (high-self.sold)/(high-low))*100
		if exits > 50:
			print "exit score = {} / Above 50, Good Job".format(exits)
		else:
			print "exit score = {} / Keep it above 50".format(exits)

	def channel_score(self, channel_h=0, channel_l=0):
		#self.bought = bought
		#self.sold = sold
		self.channel_h = channel_h
		self.channel_l = channel_l
		self.channel_width = self.channel_h-self.channel_l
		self.pctg = (self.sold-self.bought)/self.channel_width

		if self.pctg >= 0.3:
			print "Channel Score: A"
		elif 0.3 > self.pctg >= 0.2:
			print "Channel Score: B"
		elif 0.2 > self.pctg >= 0.1:
			print "Channel Score: C"
		else:
			print "Channel Score: D" 

	def target_price(self, fee=0, quantity=0):
		self.target = 0.3*self.channel_width+self.bought+fee/quantity
		print "{} / Target Price: {}".format(self.ticker, self.target)

	def equity_curve(self):
		""""""
		pass

	def twopct_money(self, total=0, buy=0):
		"""Date, account equity, 2%, 6%"""
		self.total = total
		self.buy = buy 
		#self.stoploss = stoploss
		self.stoploss = self.buy*0.9 #-10%
		#self.position = (self.total*0.02)/(self.buy-self.stoploss)
		self.position = (self.total*0.02)/(0.1*self.buy) # self.buy - 0.9*self.buy
		print "Allowed Position: {}".format(round(self.position))



if __name__ == "__main__":
	S = ScoreTrade('THD')

	#How do I know the high and low of the day before I make a buy decision?
	S.entry_score(high=104, low=95, bought=95)
	#How do I know the high and low of the day before I make a sell decision?
	S.exit_score(high=104, low=95, sold=103)

	S.channel_score(channel_h=104.97, channel_l=85.88)
	S.target_price(fee=2.95, quantity=10)

	S.twopct_money(total=3000, buy=246)
	S.twopct_money(total=3000, buy=84)


	"""
	Note: THD exit @ 101.022
	"""
