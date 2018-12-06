# -*- coding: utf-8 -*-
# @Author: Boya Chiou
# @Date:   2018-03-22 17:16:22
# @Last Modified by:   boyac
# @Last Modified time: 2018-05-09 23:01:24


class ScoreTrade(object):
	"""docstring for ClassName"""
	def __init__(self, ticker):
		self.ticker = ticker

	def entry_score(self, high=0, low=0, bought=0):
		"""進場分數(控制在50以下) 1 - High-Buy/(High-Low) * 100"""
		self.bought = bought
		entrys = (1-(high-self.bought)/(high-low))*100
		if entrys < 50:
			print "Entry score = {} / Below 50, Good Job".format(entrys)
		else:
			print "Entry score = {} / Keep it below 50".format(entrys)

	def exit_score(self, high=0, low=0, sold=0):
		"""出場分數(控制在50以上) 1 - High-Sell/(High-Low) * 100"""
		self.sold = sold
		exits = (1 - (high-self.sold)/(high-low))*100
		if exits > 50:
			print "Exit score = {} / Above 50, Good Job".format(exits)
		else:
			print "Exit score = {} / Keep it above 50".format(exits)

	def channel_score(self, channel_h=0, channel_l=0):
		#self.bought = bought
		#self.sold = sold
		self.channel_h = channel_h
		self.channel_l = channel_l
		self.channel_width = round((self.channel_h-self.channel_l),1)
		self.pctg = round((self.sold-self.bought)/self.channel_width,1)

		if self.pctg >= 0.3:
			print "Channel Score: A"
		elif 0.3 > self.pctg >= 0.2:
			print "Channel Score: B"
		elif 0.2 > self.pctg >= 0.1:
			print "Channel Score: C"
		elif self.pctg < 0.1:
			print "Channel Score: D" 

		print self.pctg

	def target_price(self, fee=0, quantity=0):
		self.target = 0.3*self.channel_width+self.bought+fee/quantity
		print "{} / Target Price: {}".format(self.ticker, self.target)

	def equity_curve(self):
		""""""
		pass

	def twopct_money(self, ticker=None, total=0, buy=0):
		"""Date, account equity, 2%, 6%"""
		self.ticker = ticker
		self.total = total
		self.buy = buy 
		#self.stoploss = stoploss
		self.stoploss = self.buy*0.9 #-10%
		#self.position = (self.total*0.02)/(self.buy-self.stoploss)
		self.position = (self.total*0.02)/(0.1*self.buy) # self.buy - 0.9*self.buy
		print "{} / Allowed Position: {}".format(self.ticker, round(self.position))

	def sixpct_money(self, ticker=None, total=0, buy=0, stock_num=0):
		"""Date, account equity, 2%, 6%"""
		self.ticker = ticker
		self.total = total
		self.buy = buy
		self.stock_num = stock_num 
		#self.stoploss = stoploss
		self.stoploss = self.buy*0.9 #-10%
		#self.position = (self.total*0.02)/(self.buy-self.stoploss)
		self.position = (self.total*0.06/self.stock_num)/(0.1*self.buy) # self.buy - 0.9*self.buy
		print "{} / Allowed Position: {}".format(self.ticker, round(self.position))



if __name__ == "__main__":
	S = ScoreTrade('THD')

	#How do I know the high and low of the day before I make a buy decision?
	S.entry_score(high=104, low=95, bought=95)
	#How do I know the high and low of the day before I make a sell decision?
	S.exit_score(high=101, low=98, sold=100)

	S.channel_score(channel_h=100, channel_l=82)
	S.target_price(fee=2.95, quantity=10)
	
	#S.twopct_money(total=3000, buy=246)
	#S.twopct_money(total=3000, buy=84)


	"""
	Note: THD exit @ 101.022
	*0.94 of upper edge of the channel
	"""

	print "-------------------BREAK-------------------"
