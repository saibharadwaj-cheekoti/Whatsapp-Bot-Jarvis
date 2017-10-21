#!/usr/local/bin/python
# coding: latin-1
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
import random

class BasicViews():
    def __init__(self, interface_layer):
        self.interface_layer = interface_layer
        #self.url_print_sender = UrlPrintSender(self.interface_layer)
        self.routes = [("(?P<hiOrHello>hi|hello|hey|hay|Hi|Hello)", self.hi),
              ("^ping$", self.ping),
              ("^btc0$", self.btc0),
              ("^btc1$", self.btc1),
              ("^btc2$", self.btc2),
              ("^btc3$", self.btc3),
              ("^btc4$", self.btc4),
              ("^btc5$", self.btc5),
              ("^faq$", self.faq),
              ("^bhb_clg$", self.bhb_clg),
              #platforms
              ("^WIN1$", self.WIN1),
              ("^MAC$", self.WIN1),
              ("^ANDY$", self.ANDY),
              ("^IOS$", self.IOS),
              ("^WIN2$", self.WIN2),
              ("^BBRY$", self.BBRY),
              ("^WEB$", self.WEB),
              ("^HD$", self.HD),
              #Platforms End

              ("^HD$", self.HD),
              ("^e(cho)?\s(?P<echo_message>[^$]+)$", self.echo)]
       
    def echo(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("%s" % match.group("echo_message"), to=message.getFrom())

    def ping(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity("Pong!", to=message.getFrom())

    def faq(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(faq, to=message.getFrom())
    
    def btc0(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BTC0, to=message.getFrom())
    
    def btc1(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BTC1, to=message.getFrom())

    def btc2(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BTC2, to=message.getFrom())

    def btc3(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BTC3, to=message.getFrom())

    def btc4(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BTC4, to=message.getFrom())

    def btc5(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BTC5, to=message.getFrom())

    def bhb_clg(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BHB, to=message.getFrom())

    ######################Platforms###############################

    def WIN1(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(WIN1, to=message.getFrom())

    def ANDY(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(ANDY, to=message.getFrom())

    def IOS(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(IOS, to=message.getFrom())

    def WIN2(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(WIN2, to=message.getFrom())

    def BBRY(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(BBRY, to=message.getFrom())

    def WEB(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(WEB, to=message.getFrom())

    def HD(self, message=None, match=None, to=None):
        return TextMessageProtocolEntity(HD, to=message.getFrom())
    
    #########################ENd Of Platforms######################
    def hi(self, message=None, match=None, to=None):
        #first,second = "",""
        #user = message.getFrom(False)
        #check = list(user)
        #if "@" in check:
        #    first,last = user.split("@")
        #    second = list(first)
        #if "-" in second:
        #    first,last = first.split("-")
        return TextMessageProtocolEntity("Hello" , to=message.getFrom())



faq = """
*Bitcointalk Signature-Ad Campaigns
https://bitcointalk.org/index.php?topic=615953

*[EDU] Faucet risks
https://bitcointalk.org/index.php?topic=1044399

*Are faucets a waste of time? (Answer: yes)
https://bitcointalk.org/index.php?topic=825370.msg9220285#msg9220285

*The Bitcoins Earning Guide for poor countries
https://bitcointalk.org/index.php?topic=1263461.0

*List of sites / services for earning btc
https://bitcointalk.org/index.php?topic=985550

*[TUTORIAL] Earn Bitcoins Here!
https://bitcointalk.org/index.php?topic=1244332
PDF =https://sabercathost.com/Ugh/Bitcoin_Earning_Tutorial.pdf

*Scam Site List
https://bitcointalk.org/index.php?topic=1339672

*How to (seriously) earn Bitcoins for "dummies"
https://bitcointalk.org/index.php?topic=1414824.msg14335511#msg14335511

*The Complete Guide To Earning Free Bitcoin
https://thebitcoinstrip.com/free-bitcoins/"""

BTC0 = """*Advantages of Bitcoin?* ?

*Milletrt Grade Secuity* - HAckers 24x7 Protection

*World Wide Payment* - Transact anywhere in the world

*Minimum or zero Fees* - fees lower than banks

*Instant Transactions anywhere* - Over the globe

*Free Network* - Nobody(Govt or Bank) has control over this system

*Transparent Network* - Can view anyones transaction
History and their balance

*Anonymous Network - Does'nt requires any of your
personal Information Not even your name.
"""
BTC1 = """*Dis-Advantages of Bitcoin?* ?

*Bitcoin price is volatile* - The price of a bitcoin
can unpredictably increase or decrease over a short
period of time due to its young economy

*Bitcoin payments are irreversible* - Any transaction issued
with Bitcoin cannot be reversed, they can only be refunded
by the person receiving the funds

*Unconfirmed transactions aren't secure* -  Each confirmation
takes between a few seconds and 90 minutes, with 10 minutes
being the average. If the transaction pays too low a fee or
is otherwise atypical, getting the first confirmation can
take much longer

*Bitcoin is still experimental* - Bitcoin is an experimental
new currency that is in active development. Each improvement
makes Bitcoin more appealing but also reveals new challenges
as Bitcoin adoption grows. During these growing pains you
might encounter increased fees, slower confirmations, or
even more severe issues. Be prepared for problems and consult
a technical expert before making any major investments, but
keep in mind that nobody can predict Bitcoin's future.
"""
BTC2 = """*Choose Your Platform*

*Desktop*

*Windows* - WIN1
*Mac* - MAC
*Linux* - LNX

*Mobile*

*Android* - ANDY
*iOS* - IOS
*Windows* - WIN2
*BlackBerry* - BBRY

*Online Wallets* - WEB 

*Hardware Wallets* - HD"""
BTC3 = """*How to Earn it?*

http://bitcointalk.org
http://freebitco.in/?r=1990
"""




BTC4 = """[Exchange List]

*International*

Bitsquare
Bitstamp
Bitwage
Coinbase
Kraken
Local Bitcoins
Xapo 

*India*

BTCXIndia
Coinsecure
Unocoin
Zebpay

*Australia*

Bitcoin Australia
CoinJar
CoinLoft
CoinTree 


*Japan*

bitFlyer
BtcBox
Coincheck 

*South Africa*

iceCUBED
Luno 

*United Kingdom*

Bittylicious
CoinCorner
Coinfloor 

*United States*

Coinbase
Gemini 

And So on"""







BTC5 = """*How to spend it?*

Bank Transfer
Paypal,Paytm
�Money Gram
Gold
�Money Exchange to international Countries
Shopping
etc

Find merchants = http://usebitcoins.info
"""

BHB = """*Berhampore Collage*

This is a Collage
"""













##########Platforms#################

WIN1 = """[Avalible Wallets For Your Platform]

*Bitcoin-core*
*Bitcoin-Knots*
*Electrum*
*mSIGNA*
*Bither*
*MultiBit HD*
*Armory*
*Green Address*
*ArcBit*
*Copay*
*BitGo*"""

ANDY = """[Wallets For Android]

*GreenBits*
*Simple Bitcoin Wallet*
*Electrum*
*Bitcoin Wallet*
*breadwallet*
*Bither*
*ArcBit*
*BTC.com*
*Copay*
*Airbitz*
*Mycelium*
*Green Address*
*Coinomi*
*Coin.Space*"""

IOS = """[Wallets For iOS]

*breadwallet*
*Bither*
*ArcBit*
*BTC.com*
*Copay*
*Airbitz*
*Mycelium*
*Green Address*
*Coin.Space*"""

WIN2 = """[Wallets For Windows Phone]

*Copay*
*Coin.Space*"""

BBRY = """[Wallets For BlackBerry]

*Bitcoin Wallet*"""

WEB = """[Online Wallets]

*Coin.Space*
*Xapo*
*Coinapult*
*Coinbase*
*BTC.com*
*BitGo*
*Green Address*"""

HD = """[Hardware Wallets]

*Ledger Nano S* - https://www.ledgerwallet.com
*Digital Bitbox* - https://digitalbitbox.com
*KeepKey* - https://www.keepkey.com
*Trezor* - https://trezor.io
*Ledger Nano* - https://www.ledgerwallet.com"""
