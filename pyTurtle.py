# -*- coding: utf-8 -*-
# @Author: Boya Chiou
# @Date:   2018-09-04 11:31:41
# @Last Modified by:   Boya Chiou
# @Last Modified time: 2018-09-10 17:34:51

# market: liquidity, trend
# position: capital management
# entry: entry price, entry condition
# stop loss: decided before entry
# stop gain: n/a
# strategy: create a system, instead of intuition


def PDN():
	pass 


def N(H,L,PDC):
	"""
	N:市場的潛在波動性/一個市場在一天内的平均波動幅度
	TR:當日的實際範圍 true range
	H:當日最高價
	L:當日最低價
	PDC:前個交易日的收盤價
	PDN:前個交易的N值
	"""

	TR = max(H-L,H-PDC,PDC-L)
	N = (19*PDN+TR)/20	
	print N


def position(balance):
	#頭寸規模單位=賬戶的1%/市場的絕對波動幅度
	pos = balance*0.01/N*USD
	return pos


def entry():
	#sys1: if p > 20day average
	#sys2: if p > 55day average
	pass 


def entry_increment():
	pass


def stoploss():
	if p == N*2:
		print "sell"
	pass


if __name__ == "__main__":
	#print N(100,95,94)

	print max(0.722-0.7124,0.722-0.7124,0.7124-0.7124)
	print (19*0.0134+0.0096)/20

	print (1000000*0.01)/(0.0141*42000)

	N(105,102,100)
	N(95,90,100)
	N(105,90,100)
