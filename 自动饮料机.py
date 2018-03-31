#!/bin/python
#coding = utf-8
money = 0 #投币
coins = [5,10,20] #面额
print('请投币，退出请输入q,系统只能识别5,10,20面额。')
loop = True
      #投币环节
while loop:
      coin = input('请投币,q退出:')
      if coin == 'q':
          print('投币结束，您本次投了%d元' %money)
          #loop = False
          break
      else:
          if coin.isdigit() == False:
              print('plz try agian!')
              continue
          coin = int(coin)
          if coin not in coins:
              print('we only accept 5,10,20')
              continue
          money += coin
          print('this time %d yuan , total %d yuan' %(coin,money))
#饮料界面
drinklist = {
    'jdb':4,
    'kele':3,
    'xuebi':2
    } #饮料列表

drinkNum = 0
for key,value in drinklist.items():
      drinkNum += 1
      #print(k,v)
      print('饮料编号： %d , 饮料名称： %s  , 价格：%s' %(drinkNum,key,value))
      
#顾客购买饮料
bucket = []
total = money
while True:
    if money == 0:
        print('not enough moneny')
        break
    drink = input('chiose your drink,q for quit:')
    if drink == 'q':
        print('购买结束，您还剩%d元。' %money)
        break
    elif drink.isdigit()==False:
        print('try again')
        continue
    else:
        drink = int(drink)
        if drink >= 0 and drink <= len(drinklist):
            x = 0
            for k,v in drinklist.items():
                x += 1
                if x == drink:
                    if money >= v:
                        money -= v
                        bucket.append(k)
                        print('your buyed %s yuan, %d leaved.' %(v,money))
                        break
                    else:
                        print('余额不足')
                        break
        else:
            print('not exist, try again.')
            continue            
#找零
if money >= 0:
    print('you buyed %d drinks,include %s ,cost %d yuan, give %d yuan you back , tks.' %(len(bucket),bucket,(total-money),money))
else:
    print('余额用完，再见')



import wx

app = wx.App()
win = wx.Frame(None, title='Simple Editor', size=(410, 335))
bkg = wx.Panel(win)

loadButton = wx.Button(bkg, label='open')
saveButton = wx.Button(bkg, label='save')
filename = wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=50, flag=wx.EXPAND)
hbox.Add(loadButton, proportion=1, flag=wx.LEFT, border=5)
hbox.Add(saveButton, proportion=1, flag=wx.LEFT, border=5)

vbox = wx.BoxSizer()
vbox.Add(hbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)
vbox.Add(contents, proportion=1, flag=wx.EXPAND | wx.ALL, border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
