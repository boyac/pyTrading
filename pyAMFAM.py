# -*- coding: utf-8 -*-
# @Author: boyac
# @Date: 2020-03-31 16:35:30
# @Last Modified by: boyac
# @Last Modified time: 2020-03-31 16:35:30


class AMFAM(object):
	"""
	By luck, almost immediately after we began the indicators project at the end of 1979, 
	one of our researchers stumbled on the germinal idea for statistical arbitrage – 
	a single indicator that ranked stocks from best to worst and offered a short-term forecast 
	of their performance compared to the others. The idea was to rank stocks by their percentage change in price, 
	corrected for splits and dividends, over a recent past period such as the last two weeks. 
	We found that the stocks that were most up tended to fall relative to the market 
	over the next few weeks and the stocks which were the most down tended to rise relative to the market. 
	Using this forecast our computer simulations showed approximately a 20 per cent annualized return from buying the
	“best” decile of stocks, and selling short the “worst” decile. We called the system MUD for the
	recommended portfolio of “most up, most down” stocks. As my friend U.C.I. mathematician William F. Donoghue 
	used to joke, little realizing how close he was to a deep truth, “Thorp, my advice is to buy low and sell high.” 
	(He had the habit of calling even close friends by their last name.) The diversified portfolios of long and
	short stocks had mostly offsetting market risks so we had what we liked - a market neutral portfolio. 
	But the total portfolio, even though it was approximately market neutral, suffered from moderately large random 
	fluctuations. Spoiled by the continuing low risk and high return performance of 
	Princeton-Newport Partners, we put statistical arbitrage aside for the time being.


	ref: 
		http://www.ntuzov.com/Nik_Site/Niks_files/Research/papers/stat_arb/Thorp_Part2.pdf

	"""
	def __init__(self, arg):
		super(AMAM, self).__init__()
		self.arg = arg



if __name__ == "__main__":
	pass
