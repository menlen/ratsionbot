import telebot
bot = telebot.TeleBot("1130068960:AAEbi4iFgSCRTrL2LEWciSbWFP--Ueu90wM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Creator is Uralov O")

@bot.message_handler(commands=['settings'])
def send_welcome(message):
	bot.reply_to(message, "beda 0-99\naralash ot 100-199\nbaxorgi bugdoy paxoli 200-299\nsilos 300-399\nsenaj 400-499\nmakkajoxori 500-599\nsoya 600-699\nbugdoy kepak 700-799\nshunaqa karochi")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.text == "1":
        bot.reply_to(message, "1.0 kg Bedadagi  Oziqa birligi 0.44 \n Alm energiya qoramolda (mj) 6.72 \n Quruq modda(gr) 830.0 \n Tozalanmagan protein(gr) 144.0 \n Hazmlanuvchi protein(gr) 101.0 \n Tozalanmagan yog(gr) 22.0\nTozalanmagan klechatka(gr) 253.0\nQand(gr) 20.0\nKraxmal(gr) 9.0\nLizin(gr) 7.3\nMeton-sistin(gr) 5.5\nKalsiy(gr) 17.0\nFosfor(gr) 2.2\nMagniy(gr) 3.0\nKaliy(gr) 15.6\nNatriy(gr) 1.5\nOltingugurt(gr) 1.8\nTemir(mg) 168.0\nMis(mg) 8.2\nRux(mg) 19.1\nMarganets(mg) 26.4\nKobalt(mg) 0.2\nYod(mg) 0.3\nKarotin(mg) 49.0\nVitamin D 360.0\nVitamin E 1")
	elif message.text == "2":
        bot.reply_to(message, "2.0 kg Bedadagi \n Oziqa birligi 0.88\nAlm energiya qoramolda (mj) 13.44\nQuruq modda(gr) 1660.0\nTozalanmagan protein(gr) 288.0\nHazmlanuvchi protein(gr) 202.0\nTozalanmagan yog(gr) 44.0\nTozalanmagan klechatka(gr) 506.0\nQand(gr) 40.0\nKraxmal(gr) 18.0\nLizin(gr) 14.6\nMeton-sistin(gr) 11.0\nKalsiy(gr) 34.0\nFosfor(gr) 4.4\nMagniy(gr) 6.0\nKaliy(gr) 31.2\nNatriy(gr) 3.0\nOltingugurt(gr) 3.6\nTemir(mg) 336.0\nMis(mg) 16.4\nRux(mg) 38.2\nMarganets(mg) 52.8\nKobalt(mg) 0.4\nYod(mg) 0.6\nKarotin(mg) 98.0\nVitamin D 720.0\nVitamin E 2.68")
	elif message.text == "3":
        bot.reply_to(message, "3.0 kg Bedadagi  Oziqa birligi 1.32 \nAlm energiya qoramolda (mj) 20.16 \nQuruq modda(gr) 2490.0 \nTozalanmagan protein(gr) 432.0 \nHazmlanuvchi protein(gr) 303.0 \nTozalanmagan yog(gr) 66.0 \nTozalanmagan klechatka(gr) 759.0 \nQand(gr) 60.0 \nKraxmal(gr) 27.0 \nLizin(gr) 21.9 \nMeton-sistin(gr) 16.5 \nKalsiy(gr) 51.0 \nFosfor(gr) 6.6000000000000005 \nMagniy(gr) 9.0 \nKaliy(gr) 46.8 \nNatriy(gr) 4.5 \nOltingugurt(gr) 5.4 \nTemir(mg) 504.0 \nMis(mg) 24.599999999999998 \nRux(mg) 57.300000000000004 \nMarganets(mg) 79.19999999999999 \nKobalt(mg) 0.6000000000000001 \nYod(mg) 0.8999999999999999 \nKarotin(mg) 147.0 \nVitamin D 1080.0 \nVitamin E 4.0200000000000005")
	elif message.text == "4":
        bot.reply_to(message, "4.0 kg Bedadagi  Oziqa birligi 1.76 \nAlm energiya qoramolda (mj) 26.88 \nQuruq modda(gr) 3320.0 \nTozalanmagan protein(gr) 576.0 \nHazmlanuvchi protein(gr) 404.0 \nTozalanmagan yog(gr) 88.0 \nTozalanmagan klechatka(gr) 1012.0 \nQand(gr) 80.0 \nKraxmal(gr) 36.0 \nLizin(gr) 29.2 \nMeton-sistin(gr) 22.0 \nKalsiy(gr) 68.0 \nFosfor(gr) 8.8 \nMagniy(gr) 12.0 \nKaliy(gr) 62.4 \nNatriy(gr) 6.0 \nOltingugurt(gr) 7.2 \nTemir(mg) 672.0 \nMis(mg) 32.8 \nRux(mg) 76.4 \nMarganets(mg) 105.6 \nKobalt(mg) 0.8 \nYod(mg) 1.2 \nKarotin(mg) 196.0 \nVitamin D 1440.0 \nVitamin E 5.36")
	elif message.text == "5":
        bot.reply_to(message, "5.0 kg Bedadagi  Oziqa birligi 2.2 \nAlm energiya qoramolda (mj) 33.6 \nQuruq modda(gr) 4150.0 \nTozalanmagan protein(gr) 720.0 \nHazmlanuvchi protein(gr) 505.0 \nTozalanmagan yog(gr) 110.0 \nTozalanmagan klechatka(gr) 1265.0 \nQand(gr) 100.0 \nKraxmal(gr) 45.0 \nLizin(gr) 36.5 \nMeton-sistin(gr) 27.5 \nKalsiy(gr) 85.0 \nFosfor(gr) 11.0 \nMagniy(gr) 15.0 \nKaliy(gr) 78.0 \nNatriy(gr) 7.5 \nOltingugurt(gr) 9.0 \nTemir(mg) 840.0 \nMis(mg) 41.0 \nRux(mg) 95.5 \nMarganets(mg) 132.0 \nKobalt(mg) 1.0 \nYod(mg) 1.5 \nKarotin(mg) 245.0 \nVitamin D 1800.0 \nVitamin E 6.7")
	elif message.text == "6":
        bot.reply_to(message, "6.0 kg Bedadagi  Oziqa birligi 2.64 \nAlm energiya qoramolda (mj) 40.32 \nQuruq modda(gr) 4980.0 \nTozalanmagan protein(gr) 864.0 \nHazmlanuvchi protein(gr) 606.0 \nTozalanmagan yog(gr) 132.0 \nTozalanmagan klechatka(gr) 1518.0 \nQand(gr) 120.0 \nKraxmal(gr) 54.0 \nLizin(gr) 43.8 \nMeton-sistin(gr) 33.0 \nKalsiy(gr) 102.0 \nFosfor(gr) 13.200000000000001 \nMagniy(gr) 18.0 \nKaliy(gr) 93.6 \nNatriy(gr) 9.0 \nOltingugurt(gr) 10.8 \nTemir(mg) 1008.0 \nMis(mg) 49.199999999999996 \nRux(mg) 114.60000000000001 \nMarganets(mg) 158.39999999999998 \nKobalt(mg) 1.2000000000000002 \nYod(mg) 1.7999999999999998 \nKarotin(mg) 294.0 \nVitamin D 2160.0 \nVitamin E 8.040000000000001")
	elif message.text == "7":
        bot.reply_to(message, "7.0 kg Bedadagi  Oziqa birligi 3.08 \nAlm energiya qoramolda (mj) 47.04 \nQuruq modda(gr) 5810.0 \nTozalanmagan protein(gr) 1008.0 \nHazmlanuvchi protein(gr) 707.0 \nTozalanmagan yog(gr) 154.0 \nTozalanmagan klechatka(gr) 1771.0 \nQand(gr) 140.0 \nKraxmal(gr) 63.0 \nLizin(gr) 51.1 \nMeton-sistin(gr) 38.5 \nKalsiy(gr) 119.0 \nFosfor(gr) 15.400000000000002 \nMagniy(gr) 21.0 \nKaliy(gr) 109.2 \nNatriy(gr) 10.5 \nOltingugurt(gr) 12.6 \nTemir(mg) 1176.0 \nMis(mg) 57.39999999999999 \nRux(mg) 133.70000000000002 \nMarganets(mg) 184.79999999999998 \nKobalt(mg) 1.4000000000000001 \nYod(mg) 2.1 \nKarotin(mg) 343.0 \nVitamin D 2520.0 \nVitamin E 9.38")
	elif message.text == "8":
        bot.reply_to(message, "8.0 kg Bedadagi  Oziqa birligi 3.52 \nAlm energiya qoramolda (mj) 53.76 \nQuruq modda(gr) 6640.0 \nTozalanmagan protein(gr) 1152.0 \nHazmlanuvchi protein(gr) 808.0 \nTozalanmagan yog(gr) 176.0 \nTozalanmagan klechatka(gr) 2024.0 \nQand(gr) 160.0 \nKraxmal(gr) 72.0 \nLizin(gr) 58.4 \nMeton-sistin(gr) 44.0 \nKalsiy(gr) 136.0 \nFosfor(gr) 17.6 \nMagniy(gr) 24.0 \nKaliy(gr) 124.8 \nNatriy(gr) 12.0 \nOltingugurt(gr) 14.4 \nTemir(mg) 1344.0 \nMis(mg) 65.6 \nRux(mg) 152.8 \nMarganets(mg) 211.2 \nKobalt(mg) 1.6 \nYod(mg) 2.4 \nKarotin(mg) 392.0 \nVitamin D 2880.0 \nVitamin E 10.72")
	elif message.text == "9":
        bot.reply_to(message, "9.0 kg Bedadagi  Oziqa birligi 3.96 \nAlm energiya qoramolda (mj) 60.48 \nQuruq modda(gr) 7470.0 \nTozalanmagan protein(gr) 1296.0 \nHazmlanuvchi protein(gr) 909.0 \nTozalanmagan yog(gr) 198.0 \nTozalanmagan klechatka(gr) 2277.0 \nQand(gr) 180.0 \nKraxmal(gr) 81.0 \nLizin(gr) 65.7 \nMeton-sistin(gr) 49.5 \nKalsiy(gr) 153.0 \nFosfor(gr) 19.8 \nMagniy(gr) 27.0 \nKaliy(gr) 140.4 \nNatriy(gr) 13.5 \nOltingugurt(gr) 16.2 \nTemir(mg) 1512.0 \nMis(mg) 73.8 \nRux(mg) 171.9 \nMarganets(mg) 237.6 \nKobalt(mg) 1.8 \nYod(mg) 2.6999999999999997 \nKarotin(mg) 441.0 \nVitamin D 3240.0 \nVitamin E 12.06")
	elif message.text == "10":
        bot.reply_to(message, "10.0 kg Bedadagi  Oziqa birligi 4.4 \nAlm energiya qoramolda (mj) 67.2 \nQuruq modda(gr) 8300.0 \nTozalanmagan protein(gr) 1440.0 \nHazmlanuvchi protein(gr) 1010.0 \nTozalanmagan yog(gr) 220.0 \nTozalanmagan klechatka(gr) 2530.0 \nQand(gr) 200.0 \nKraxmal(gr) 90.0 \nLizin(gr) 73.0 \nMeton-sistin(gr) 55.0 \nKalsiy(gr) 170.0 \nFosfor(gr) 22.0 \nMagniy(gr) 30.0 \nKaliy(gr) 156.0 \nNatriy(gr) 15.0 \nOltingugurt(gr) 18.0 \nTemir(mg) 1680.0 \nMis(mg) 82.0 \nRux(mg) 191.0 \nMarganets(mg) 264.0 \nKobalt(mg) 2.0 \nYod(mg) 3.0 \nKarotin(mg) 490.0 \nVitamin D 3600.0 \nVitamin E 1")
	elif message.text == "11":
        bot.reply_to(message, "11.0 kg Bedadagi  Oziqa birligi 4.84 \nAlm energiya qoramolda (mj) 73.92 \nQuruq modda(gr) 9130.0 \nTozalanmagan protein(gr) 1584.0 \nHazmlanuvchi protein(gr) 1111.0 \nTozalanmagan yog(gr) 242.0 \nTozalanmagan klechatka(gr) 2783.0 \nQand(gr) 220.0 \nKraxmal(gr) 99.0 \nLizin(gr) 80.3 \nMeton-sistin(gr) 60.5 \nKalsiy(gr) 187.0 \nFosfor(gr) 24.200000000000003 \nMagniy(gr) 33.0 \nKaliy(gr) 171.6 \nNatriy(gr) 16.5 \nOltingugurt(gr) 19.8 \nTemir(mg) 1848.0 \nMis(mg) 90.19999999999999 \nRux(mg) 210.10000000000002 \nMarganets(mg) 290.4 \nKobalt(mg) 2.2 \nYod(mg) 3.3 \nKarotin(mg) 539.0 \nVitamin D 3960.0 \nVitamin E 14.74")
	elif message.text == "12":
        bot.reply_to(message, "12.0 kg Bedadagi  Oziqa birligi 5.28 \nAlm energiya qoramolda (mj) 80.64 \nQuruq modda(gr) 9960.0 \nTozalanmagan protein(gr) 1728.0 \nHazmlanuvchi protein(gr) 1212.0 \nTozalanmagan yog(gr) 264.0 \nTozalanmagan klechatka(gr) 3036.0 \nQand(gr) 240.0 \nKraxmal(gr) 108.0 \nLizin(gr) 87.6 \nMeton-sistin(gr) 66.0 \nKalsiy(gr) 204.0 \nFosfor(gr) 26.400000000000002 \nMagniy(gr) 36.0 \nKaliy(gr) 187.2 \nNatriy(gr) 18.0 \nOltingugurt(gr) 21.6 \nTemir(mg) 2016.0 \nMis(mg) 98.39999999999999 \nRux(mg) 229.20000000000002 \nMarganets(mg) 316.79999999999995 \nKobalt(mg) 2.4000000000000004 \nYod(mg) 3.5999999999999996 \nKarotin(mg) 588.0 \nVitamin D 4320.0 \nVitamin E 16.080000000000002")
	elif message.text == "13":
        bot.reply_to(message, "13.0 kg Bedadagi  Oziqa birligi 5.72 \nAlm energiya qoramolda (mj) 87.36 \nQuruq modda(gr) 10790.0 \nTozalanmagan protein(gr) 1872.0 \nHazmlanuvchi protein(gr) 1313.0 \nTozalanmagan yog(gr) 286.0 \nTozalanmagan klechatka(gr) 3289.0 \nQand(gr) 260.0 \nKraxmal(gr) 117.0 \nLizin(gr) 94.89999999999999 \nMeton-sistin(gr) 71.5 \nKalsiy(gr) 221.0 \nFosfor(gr) 28.6 \nMagniy(gr) 39.0 \nKaliy(gr) 202.79999999999998 \nNatriy(gr) 19.5 \nOltingugurt(gr) 23.400000000000002 \nTemir(mg) 2184.0 \nMis(mg) 106.6 \nRux(mg) 248.3 \nMarganets(mg) 343.2 \nKobalt(mg) 2.6 \nYod(mg) 3.9 \nKarotin(mg) 637.0 \nVitamin D 4680.0 \nVitamin E 17.42")
	elif message.text == "14":
        bot.reply_to(message, "14.0 kg Bedadagi  Oziqa birligi 6.16 \nAlm energiya qoramolda (mj) 94.08 \nQuruq modda(gr) 11620.0 \nTozalanmagan protein(gr) 2016.0 \nHazmlanuvchi protein(gr) 1414.0 \nTozalanmagan yog(gr) 308.0 \nTozalanmagan klechatka(gr) 3542.0 \nQand(gr) 280.0 \nKraxmal(gr) 126.0 \nLizin(gr) 102.2 \nMeton-sistin(gr) 77.0 \nKalsiy(gr) 238.0 \nFosfor(gr) 30.800000000000004 \nMagniy(gr) 42.0 \nKaliy(gr) 218.4 \nNatriy(gr) 21.0 \nOltingugurt(gr) 25.2 \nTemir(mg) 2352.0 \nMis(mg) 114.79999999999998 \nRux(mg) 267.40000000000003 \nMarganets(mg) 369.59999999999997 \nKobalt(mg) 2.8000000000000003 \nYod(mg) 4.2 \nKarotin(mg) 686.0 \nVitamin D 5040.0 \nVitamin E 18.76")
	elif message.text == "15":
        bot.reply_to(message, "15.0 kg Bedadagi  Oziqa birligi 6.6 \nAlm energiya qoramolda (mj) 100.8 \nQuruq modda(gr) 12450.0 \nTozalanmagan protein(gr) 2160.0 \nHazmlanuvchi protein(gr) 1515.0 \nTozalanmagan yog(gr) 330.0 \nTozalanmagan klechatka(gr) 3795.0 \nQand(gr) 300.0 \nKraxmal(gr) 135.0 \nLizin(gr) 109.5 \nMeton-sistin(gr) 82.5 \nKalsiy(gr) 255.0 \nFosfor(gr) 33.0 \nMagniy(gr) 45.0 \nKaliy(gr) 234.0 \nNatriy(gr) 22.5 \nOltingugurt(gr) 27.0 \nTemir(mg) 2520.0 \nMis(mg) 122.99999999999999 \nRux(mg) 286.5 \nMarganets(mg) 396.0 \nKobalt(mg) 3.0 \nYod(mg) 4.5 \nKarotin(mg) 735.0 \nVitamin D 5400.0 \nVitamin E 20.1")
	elif message.text == "16":
        bot.reply_to(message, "16.0 kg Bedadagi  Oziqa birligi 7.04 \nAlm energiya qoramolda (mj) 107.52 \nQuruq modda(gr) 13280.0 \nTozalanmagan protein(gr) 2304.0 \nHazmlanuvchi protein(gr) 1616.0 \nTozalanmagan yog(gr) 352.0 \nTozalanmagan klechatka(gr) 4048.0 \nQand(gr) 320.0 \nKraxmal(gr) 144.0 \nLizin(gr) 116.8 \nMeton-sistin(gr) 88.0 \nKalsiy(gr) 272.0 \nFosfor(gr) 35.2 \nMagniy(gr) 48.0 \nKaliy(gr) 249.6 \nNatriy(gr) 24.0 \nOltingugurt(gr) 28.8 \nTemir(mg) 2688.0 \nMis(mg) 131.2 \nRux(mg) 305.6 \nMarganets(mg) 422.4 \nKobalt(mg) 3.2 \nYod(mg) 4.8 \nKarotin(mg) 784.0 \nVitamin D 5760.0 \nVitamin E 21.44")
	elif message.text == "17":
        bot.reply_to(message, "17.0 kg Bedadagi  Oziqa birligi 7.48 \nAlm energiya qoramolda (mj) 114.24 \nQuruq modda(gr) 14110.0 \nTozalanmagan protein(gr) 2448.0 \nHazmlanuvchi protein(gr) 1717.0 \nTozalanmagan yog(gr) 374.0 \nTozalanmagan klechatka(gr) 4301.0 \nQand(gr) 340.0 \nKraxmal(gr) 153.0 \nLizin(gr) 124.1 \nMeton-sistin(gr) 93.5 \nKalsiy(gr) 289.0 \nFosfor(gr) 37.400000000000006 \nMagniy(gr) 51.0 \nKaliy(gr) 265.2 \nNatriy(gr) 25.5 \nOltingugurt(gr) 30.6 \nTemir(mg) 2856.0 \nMis(mg) 139.39999999999998 \nRux(mg) 324.70000000000005 \nMarganets(mg) 448.79999999999995 \nKobalt(mg) 3.4000000000000004 \nYod(mg) 5.1 \nKarotin(mg) 833.0 \nVitamin D 6120.0 \nVitamin E 22.78")
	elif message.text == "18":
        bot.reply_to(message, "18.0 kg Bedadagi  Oziqa birligi 7.92 \nAlm energiya qoramolda (mj) 120.96 \nQuruq modda(gr) 14940.0 \nTozalanmagan protein(gr) 2592.0 \nHazmlanuvchi protein(gr) 1818.0 \nTozalanmagan yog(gr) 396.0 \nTozalanmagan klechatka(gr) 4554.0 \nQand(gr) 360.0 \nKraxmal(gr) 162.0 \nLizin(gr) 131.4 \nMeton-sistin(gr) 99.0 \nKalsiy(gr) 306.0 \nFosfor(gr) 39.6 \nMagniy(gr) 54.0 \nKaliy(gr) 280.8 \nNatriy(gr) 27.0 \nOltingugurt(gr) 32.4 \nTemir(mg) 3024.0 \nMis(mg) 147.6 \nRux(mg) 343.8 \nMarganets(mg) 475.2 \nKobalt(mg) 3.6 \nYod(mg) 5.3999999999999995 \nKarotin(mg) 882.0 \nVitamin D 6480.0 \nVitamin E 24.12")
	elif message.text == "19":
        bot.reply_to(message, "19.0 kg Bedadagi  Oziqa birligi 8.36 \nAlm energiya qoramolda (mj) 127.67999999999999 \nQuruq modda(gr) 15770.0 \nTozalanmagan protein(gr) 2736.0 \nHazmlanuvchi protein(gr) 1919.0 \nTozalanmagan yog(gr) 418.0 \nTozalanmagan klechatka(gr) 4807.0 \nQand(gr) 380.0 \nKraxmal(gr) 171.0 \nLizin(gr) 138.7 \nMeton-sistin(gr) 104.5 \nKalsiy(gr) 323.0 \nFosfor(gr) 41.800000000000004 \nMagniy(gr) 57.0 \nKaliy(gr) 296.4 \nNatriy(gr) 28.5 \nOltingugurt(gr) 34.2 \nTemir(mg) 3192.0 \nMis(mg) 155.79999999999998 \nRux(mg) 362.90000000000003 \nMarganets(mg) 501.59999999999997 \nKobalt(mg) 3.8000000000000003 \nYod(mg) 5.7 \nKarotin(mg) 931.0 \nVitamin D 6840.0 \nVitamin E 25.46")
	elif message.text == "20":
        bot.reply_to(message, "20.0 kg Bedadagi  Oziqa birligi 8.8 \nAlm energiya qoramolda (mj) 134.4 \nQuruq modda(gr) 16600.0 \nTozalanmagan protein(gr) 2880.0 \nHazmlanuvchi protein(gr) 2020.0 \nTozalanmagan yog(gr) 440.0 \nTozalanmagan klechatka(gr) 5060.0 \nQand(gr) 400.0 \nKraxmal(gr) 180.0 \nLizin(gr) 146.0 \nMeton-sistin(gr) 110.0 \nKalsiy(gr) 340.0 \nFosfor(gr) 44.0 \nMagniy(gr) 60.0 \nKaliy(gr) 312.0 \nNatriy(gr) 30.0 \nOltingugurt(gr) 36.0 \nTemir(mg) 3360.0 \nMis(mg) 164.0 \nRux(mg) 382.0 \nMarganets(mg) 528.0 \nKobalt(mg) 4.0 \nYod(mg) 6.0 \nKarotin(mg) 980.0 \nVitamin D 7200.0 \nVitamin E 26.8")
	elif message.text == "21":
        bot.reply_to(message, "21.0 kg Bedadagi  Oziqa birligi 9.24 \nAlm energiya qoramolda (mj) 141.12 \nQuruq modda(gr) 17430.0 \nTozalanmagan protein(gr) 3024.0 \nHazmlanuvchi protein(gr) 2121.0 \nTozalanmagan yog(gr) 462.0 \nTozalanmagan klechatka(gr) 5313.0 \nQand(gr) 420.0 \nKraxmal(gr) 189.0 \nLizin(gr) 153.29999999999998 \nMeton-sistin(gr) 115.5 \nKalsiy(gr) 357.0 \nFosfor(gr) 46.2 \nMagniy(gr) 63.0 \nKaliy(gr) 327.59999999999997 \nNatriy(gr) 31.5 \nOltingugurt(gr) 37.800000000000004 \nTemir(mg) 3528.0 \nMis(mg) 172.2 \nRux(mg) 401.1 \nMarganets(mg) 554.4 \nKobalt(mg) 4.2 \nYod(mg) 6.3 \nKarotin(mg) 1029.0 \nVitamin D 7560.0 \nVitamin E 28.14")
	elif message.text == "22":
        bot.reply_to(message, "22.0 kg Bedadagi  Oziqa birligi 9.68 \nAlm energiya qoramolda (mj) 147.84 \nQuruq modda(gr) 18260.0 \nTozalanmagan protein(gr) 3168.0 \nHazmlanuvchi protein(gr) 2222.0 \nTozalanmagan yog(gr) 484.0 \nTozalanmagan klechatka(gr) 5566.0 \nQand(gr) 440.0 \nKraxmal(gr) 198.0 \nLizin(gr) 160.6 \nMeton-sistin(gr) 121.0 \nKalsiy(gr) 374.0 \nFosfor(gr) 48.400000000000006 \nMagniy(gr) 66.0 \nKaliy(gr) 343.2 \nNatriy(gr) 33.0 \nOltingugurt(gr) 39.6 \nTemir(mg) 3696.0 \nMis(mg) 180.39999999999998 \nRux(mg) 420.20000000000005 \nMarganets(mg) 580.8 \nKobalt(mg) 4.4 \nYod(mg) 6.6 \nKarotin(mg) 1078.0 \nVitamin D 7920.0 \nVitamin E 29.48")
	elif message.text == "23":
        bot.reply_to(message, "23.0 kg Bedadagi  Oziqa birligi 10.12 \nAlm energiya qoramolda (mj) 154.56 \nQuruq modda(gr) 19090.0 \nTozalanmagan protein(gr) 3312.0 \nHazmlanuvchi protein(gr) 2323.0 \nTozalanmagan yog(gr) 506.0 \nTozalanmagan klechatka(gr) 5819.0 \nQand(gr) 460.0 \nKraxmal(gr) 207.0 \nLizin(gr) 167.9 \nMeton-sistin(gr) 126.5 \nKalsiy(gr) 391.0 \nFosfor(gr) 50.6 \nMagniy(gr) 69.0 \nKaliy(gr) 358.8 \nNatriy(gr) 34.5 \nOltingugurt(gr) 41.4 \nTemir(mg) 3864.0 \nMis(mg) 188.6 \nRux(mg) 439.3 \nMarganets(mg) 607.1999999999999 \nKobalt(mg) 4.6000000000000005 \nYod(mg) 6.8999999999999995 \nKarotin(mg) 1127.0 \nVitamin D 8280.0 \nVitamin E 30.82")
	elif message.text == "101":
        bot.reply_to(message, "1.0 kg Aralsh o't pichanidagi  Oziqa birligi 0.44 \nAlm energiya qoramolda (mj) 6.45 \nQuruq modda(gr) 850.0 \nTozalanmagan protein(gr) 95.0 \nHazmlanuvchi protein(gr) 56.0 \nTozalanmagan yog(gr) 24.0 \nTozalanmagan klechatka(gr) 257.0 \nQand(gr) 10.0 \nKraxmal(gr) 0.0 \nLizin(gr) 3.8 \nMeton-sistin(gr) 3.0 \nKalsiy(gr) 8.3 \nFosfor(gr) 1.1 \nMagniy(gr) 2.3 \nKaliy(gr) 11.3 \nNatriy(gr) 3.0 \nOltingugurt(gr) 1.2 \nTemir(mg) 450.0 \nMis(mg) 4.0 \nRux(mg) 15.0 \nMarganets(mg) 50.0 \nKobalt(mg) 0.45 \nYod(mg) 0.04 \nKarotin(mg) 15.0 \nVitamin D 160.0 \nVitamin E 50.0")
	elif message.text == "102":
        bot.reply_to(message, "2.0 kg Aralsh o't pichanidagi  Oziqa birligi 0.88 \nAlm energiya qoramolda (mj) 12.9 \nQuruq modda(gr) 1700.0 \nTozalanmagan protein(gr) 190.0 \nHazmlanuvchi protein(gr) 112.0 \nTozalanmagan yog(gr) 48.0 \nTozalanmagan klechatka(gr) 514.0 \nQand(gr) 20.0 \nKraxmal(gr) 0.0 \nLizin(gr) 7.6 \nMeton-sistin(gr) 6.0 \nKalsiy(gr) 16.6 \nFosfor(gr) 2.2 \nMagniy(gr) 4.6 \nKaliy(gr) 22.6 \nNatriy(gr) 6.0 \nOltingugurt(gr) 2.4 \nTemir(mg) 900.0 \nMis(mg) 8.0 \nRux(mg) 30.0 \nMarganets(mg) 100.0 \nKobalt(mg) 0.9 \nYod(mg) 0.08 \nKarotin(mg) 30.0 \nVitamin D 320.0 \nVitamin E 100.0")
	elif message.text == "103":
        bot.reply_to(message, "3.0 kg Aralsh o't pichanidagi  Oziqa birligi 1.32 \nAlm energiya qoramolda (mj) 19.35 \nQuruq modda(gr) 2550.0 \nTozalanmagan protein(gr) 285.0 \nHazmlanuvchi protein(gr) 168.0 \nTozalanmagan yog(gr) 72.0 \nTozalanmagan klechatka(gr) 771.0 \nQand(gr) 30.0 \nKraxmal(gr) 0.0 \nLizin(gr) 11.399999999999999 \nMeton-sistin(gr) 9.0 \nKalsiy(gr) 24.900000000000002 \nFosfor(gr) 3.3000000000000003 \nMagniy(gr) 6.8999999999999995 \nKaliy(gr) 33.900000000000006 \nNatriy(gr) 9.0 \nOltingugurt(gr) 3.5999999999999996 \nTemir(mg) 1350.0 \nMis(mg) 12.0 \nRux(mg) 45.0 \nMarganets(mg) 150.0 \nKobalt(mg) 1.35 \nYod(mg) 0.12 \nKarotin(mg) 45.0 \nVitamin D 480.0 \nVitamin E 150.0")
	elif message.text == "104":
        bot.reply_to(message, "4.0 kg Aralsh o't pichanidagi  Oziqa birligi 1.76 \nAlm energiya qoramolda (mj) 25.8 \nQuruq modda(gr) 3400.0 \nTozalanmagan protein(gr) 380.0 \nHazmlanuvchi protein(gr) 224.0 \nTozalanmagan yog(gr) 96.0 \nTozalanmagan klechatka(gr) 1028.0 \nQand(gr) 40.0 \nKraxmal(gr) 0.0 \nLizin(gr) 15.2 \nMeton-sistin(gr) 12.0 \nKalsiy(gr) 33.2 \nFosfor(gr) 4.4 \nMagniy(gr) 9.2 \nKaliy(gr) 45.2 \nNatriy(gr) 12.0 \nOltingugurt(gr) 4.8 \nTemir(mg) 1800.0 \nMis(mg) 16.0 \nRux(mg) 60.0 \nMarganets(mg) 200.0 \nKobalt(mg) 1.8 \nYod(mg) 0.16 \nKarotin(mg) 60.0 \nVitamin D 640.0 \nVitamin E 200.0")
	elif message.text == "105":
        bot.reply_to(message, "5.0 kg Aralsh o't pichanidagi  Oziqa birligi 2.2 \nAlm energiya qoramolda (mj) 32.25 \nQuruq modda(gr) 4250.0 \nTozalanmagan protein(gr) 475.0 \nHazmlanuvchi protein(gr) 280.0 \nTozalanmagan yog(gr) 120.0 \nTozalanmagan klechatka(gr) 1285.0 \nQand(gr) 50.0 \nKraxmal(gr) 0.0 \nLizin(gr) 19.0 \nMeton-sistin(gr) 15.0 \nKalsiy(gr) 41.5 \nFosfor(gr) 5.5 \nMagniy(gr) 11.5 \nKaliy(gr) 56.5 \nNatriy(gr) 15.0 \nOltingugurt(gr) 6.0 \nTemir(mg) 2250.0 \nMis(mg) 20.0 \nRux(mg) 75.0 \nMarganets(mg) 250.0 \nKobalt(mg) 2.25 \nYod(mg) 0.2 \nKarotin(mg) 75.0 \nVitamin D 800.0 \nVitamin E 250.0")
	elif message.text == "106":
        bot.reply_to(message, "6.0 kg Aralsh o't pichanidagi  Oziqa birligi 2.64 \nAlm energiya qoramolda (mj) 38.7 \nQuruq modda(gr) 5100.0 \nTozalanmagan protein(gr) 570.0 \nHazmlanuvchi protein(gr) 336.0 \nTozalanmagan yog(gr) 144.0 \nTozalanmagan klechatka(gr) 1542.0 \nQand(gr) 60.0 \nKraxmal(gr) 0.0 \nLizin(gr) 22.799999999999997 \nMeton-sistin(gr) 18.0 \nKalsiy(gr) 49.800000000000004 \nFosfor(gr) 6.6000000000000005 \nMagniy(gr) 13.799999999999999 \nKaliy(gr) 67.80000000000001 \nNatriy(gr) 18.0 \nOltingugurt(gr) 7.199999999999999 \nTemir(mg) 2700.0 \nMis(mg) 24.0 \nRux(mg) 90.0 \nMarganets(mg) 300.0 \nKobalt(mg) 2.7 \nYod(mg) 0.24 \nKarotin(mg) 90.0 \nVitamin D 960.0 \nVitamin E 300.0")
	elif message.text == "107":
        bot.reply_to(message, "7.0 kg Aralsh o't pichanidagi  Oziqa birligi 3.08 \nAlm energiya qoramolda (mj) 45.15 \nQuruq modda(gr) 5950.0 \nTozalanmagan protein(gr) 665.0 \nHazmlanuvchi protein(gr) 392.0 \nTozalanmagan yog(gr) 168.0 \nTozalanmagan klechatka(gr) 1799.0 \nQand(gr) 70.0 \nKraxmal(gr) 0.0 \nLizin(gr) 26.599999999999998 \nMeton-sistin(gr) 21.0 \nKalsiy(gr) 58.10000000000001 \nFosfor(gr) 7.700000000000001 \nMagniy(gr) 16.099999999999998 \nKaliy(gr) 79.10000000000001 \nNatriy(gr) 21.0 \nOltingugurt(gr) 8.4 \nTemir(mg) 3150.0 \nMis(mg) 28.0 \nRux(mg) 105.0 \nMarganets(mg) 350.0 \nKobalt(mg) 3.15 \nYod(mg) 0.28 \nKarotin(mg) 105.0 \nVitamin D 1120.0 \nVitamin E 350.0")
	elif message.text == "108":
        bot.reply_to(message, "8.0 kg Aralsh o't pichanidagi  Oziqa birligi 3.52 \nAlm energiya qoramolda (mj) 51.6 \nQuruq modda(gr) 6800.0 \nTozalanmagan protein(gr) 760.0 \nHazmlanuvchi protein(gr) 448.0 \nTozalanmagan yog(gr) 192.0 \nTozalanmagan klechatka(gr) 2056.0 \nQand(gr) 80.0 \nKraxmal(gr) 0.0 \nLizin(gr) 30.4 \nMeton-sistin(gr) 24.0 \nKalsiy(gr) 66.4 \nFosfor(gr) 8.8 \nMagniy(gr) 18.4 \nKaliy(gr) 90.4 \nNatriy(gr) 24.0 \nOltingugurt(gr) 9.6 \nTemir(mg) 3600.0 \nMis(mg) 32.0 \nRux(mg) 120.0 \nMarganets(mg) 400.0 \nKobalt(mg) 3.6 \nYod(mg) 0.32 \nKarotin(mg) 120.0 \nVitamin D 1280.0 \nVitamin E 400.0")
	elif message.text == "109":
        bot.reply_to(message, "9.0 kg Aralsh o't pichanidagi  Oziqa birligi 3.96 \nAlm energiya qoramolda (mj) 58.050000000000004 \nQuruq modda(gr) 7650.0 \nTozalanmagan protein(gr) 855.0 \nHazmlanuvchi protein(gr) 504.0 \nTozalanmagan yog(gr) 216.0 \nTozalanmagan klechatka(gr) 2313.0 \nQand(gr) 90.0 \nKraxmal(gr) 0.0 \nLizin(gr) 34.199999999999996 \nMeton-sistin(gr) 27.0 \nKalsiy(gr) 74.7 \nFosfor(gr) 9.9 \nMagniy(gr) 20.7 \nKaliy(gr) 101.7 \nNatriy(gr) 27.0 \nOltingugurt(gr) 10.799999999999999 \nTemir(mg) 4050.0 \nMis(mg) 36.0 \nRux(mg) 135.0 \nMarganets(mg) 450.0 \nKobalt(mg) 4.05 \nYod(mg) 0.36 \nKarotin(mg) 135.0 \nVitamin D 1440.0 \nVitamin E 450.0")
	elif message.text == "110":
        bot.reply_to(message, "9.0 kg Aralsh o't pichanidagi  Oziqa birligi 3.96 \nAlm energiya qoramolda (mj) 58.050000000000004 \nQuruq modda(gr) 7650.0 \nTozalanmagan protein(gr) 855.0 \nHazmlanuvchi protein(gr) 504.0 \nTozalanmagan yog(gr) 216.0 \nTozalanmagan klechatka(gr) 2313.0 \nQand(gr) 90.0 \nKraxmal(gr) 0.0 \nLizin(gr) 34.199999999999996 \nMeton-sistin(gr) 27.0 \nKalsiy(gr) 74.7 \nFosfor(gr) 9.9 \nMagniy(gr) 20.7 \nKaliy(gr) 101.7 \nNatriy(gr) 27.0 \nOltingugurt(gr) 10.799999999999999 \nTemir(mg) 4050.0 \nMis(mg) 36.0 \nRux(mg) 135.0 \nMarganets(mg) 450.0 \nKobalt(mg) 4.05 \nYod(mg) 0.36 \nKarotin(mg) 135.0 \nVitamin D 1440.0 \nVitamin E 450.0")
	elif message.text == "111":
        bot.reply_to(message, "11.0 kg Aralsh o't pichanidagi  Oziqa birligi 4.84 \nAlm energiya qoramolda (mj) 70.95 \nQuruq modda(gr) 9350.0 \nTozalanmagan protein(gr) 1045.0 \nHazmlanuvchi protein(gr) 616.0 \nTozalanmagan yog(gr) 264.0 \nTozalanmagan klechatka(gr) 2827.0 \nQand(gr) 110.0 \nKraxmal(gr) 0.0 \nLizin(gr) 41.8 \nMeton-sistin(gr) 33.0 \nKalsiy(gr) 91.30000000000001 \nFosfor(gr) 12.100000000000001 \nMagniy(gr) 25.299999999999997 \nKaliy(gr) 124.30000000000001 \nNatriy(gr) 33.0 \nOltingugurt(gr) 13.2 \nTemir(mg) 4950.0 \nMis(mg) 44.0 \nRux(mg) 165.0 \nMarganets(mg) 550.0 \nKobalt(mg) 4.95 \nYod(mg) 0.44 \nKarotin(mg) 165.0 \nVitamin D 1760.0 \nVitamin E 550.0")
	elif message.text == "112":
        bot.reply_to(message, "12.0 kg Aralsh o't pichanidagi  Oziqa birligi 5.28 \nAlm energiya qoramolda (mj) 77.4 \nQuruq modda(gr) 10200.0 \nTozalanmagan protein(gr) 1140.0 \nHazmlanuvchi protein(gr) 672.0 \nTozalanmagan yog(gr) 288.0 \nTozalanmagan klechatka(gr) 3084.0 \nQand(gr) 120.0 \nKraxmal(gr) 0.0 \nLizin(gr) 45.599999999999994 \nMeton-sistin(gr) 36.0 \nKalsiy(gr) 99.60000000000001 \nFosfor(gr) 13.200000000000001 \nMagniy(gr) 27.599999999999998 \nKaliy(gr) 135.60000000000002 \nNatriy(gr) 36.0 \nOltingugurt(gr) 14.399999999999999 \nTemir(mg) 5400.0 \nMis(mg) 48.0 \nRux(mg) 180.0 \nMarganets(mg) 600.0 \nKobalt(mg) 5.4 \nYod(mg) 0.48 \nKarotin(mg) 180.0 \nVitamin D 1920.0 \nVitamin E 600.0")
	elif message.text == "113":
        bot.reply_to(message, "13.0 kg Aralsh o't pichanidagi  Oziqa birligi 5.72 \nAlm energiya qoramolda (mj) 83.85000000000001 \nQuruq modda(gr) 11050.0 \nTozalanmagan protein(gr) 1235.0 \nHazmlanuvchi protein(gr) 728.0 \nTozalanmagan yog(gr) 312.0 \nTozalanmagan klechatka(gr) 3341.0 \nQand(gr) 130.0 \nKraxmal(gr) 0.0 \nLizin(gr) 49.4 \nMeton-sistin(gr) 39.0 \nKalsiy(gr) 107.9 \nFosfor(gr) 14.3 \nMagniy(gr) 29.9 \nKaliy(gr) 146.9 \nNatriy(gr) 39.0 \nOltingugurt(gr) 15.6 \nTemir(mg) 5850.0 \nMis(mg) 52.0 \nRux(mg) 195.0 \nMarganets(mg) 650.0 \nKobalt(mg) 5.8500000000000005 \nYod(mg) 0.52 \nKarotin(mg) 195.0 \nVitamin D 2080.0 \nVitamin E 650.0")
	elif message.text == "114":
        bot.reply_to(message, "14.0 kg Aralsh o't pichanidagi  Oziqa birligi 6.16 \nAlm energiya qoramolda (mj) 90.3 \nQuruq modda(gr) 11900.0 \nTozalanmagan protein(gr) 1330.0 \nHazmlanuvchi protein(gr) 784.0 \nTozalanmagan yog(gr) 336.0 \nTozalanmagan klechatka(gr) 3598.0 \nQand(gr) 140.0 \nKraxmal(gr) 0.0 \nLizin(gr) 53.199999999999996 \nMeton-sistin(gr) 42.0 \nKalsiy(gr) 116.20000000000002 \nFosfor(gr) 15.400000000000002 \nMagniy(gr) 32.199999999999996 \nKaliy(gr) 158.20000000000002 \nNatriy(gr) 42.0 \nOltingugurt(gr) 16.8 \nTemir(mg) 6300.0 \nMis(mg) 56.0 \nRux(mg) 210.0 \nMarganets(mg) 700.0 \nKobalt(mg) 6.3 \nYod(mg) 0.56 \nKarotin(mg) 210.0 \nVitamin D 2240.0 \nVitamin E 700.0")
	elif message.text == "115":
        bot.reply_to(message, "15.0 kg Aralsh o't pichanidagi  Oziqa birligi 6.6 \nAlm energiya qoramolda (mj) 96.75 \nQuruq modda(gr) 12750.0 \nTozalanmagan protein(gr) 1425.0 \nHazmlanuvchi protein(gr) 840.0 \nTozalanmagan yog(gr) 360.0 \nTozalanmagan klechatka(gr) 3855.0 \nQand(gr) 150.0 \nKraxmal(gr) 0.0 \nLizin(gr) 57.0 \nMeton-sistin(gr) 45.0 \nKalsiy(gr) 124.50000000000001 \nFosfor(gr) 16.5 \nMagniy(gr) 34.5 \nKaliy(gr) 169.5 \nNatriy(gr) 45.0 \nOltingugurt(gr) 18.0 \nTemir(mg) 6750.0 \nMis(mg) 60.0 \nRux(mg) 225.0 \nMarganets(mg) 750.0 \nKobalt(mg) 6.75 \nYod(mg) 0.6 \nKarotin(mg) 225.0 \nVitamin D 2400.0 \nVitamin E 750.0")
	elif message.text == "116":
        bot.reply_to(message, "16.0 kg Aralsh o't pichanidagi  Oziqa birligi 7.04 \nAlm energiya qoramolda (mj) 103.2 \nQuruq modda(gr) 13600.0 \nTozalanmagan protein(gr) 1520.0 \nHazmlanuvchi protein(gr) 896.0 \nTozalanmagan yog(gr) 384.0 \nTozalanmagan klechatka(gr) 4112.0 \nQand(gr) 160.0 \nKraxmal(gr) 0.0 \nLizin(gr) 60.8 \nMeton-sistin(gr) 48.0 \nKalsiy(gr) 132.8 \nFosfor(gr) 17.6 \nMagniy(gr) 36.8 \nKaliy(gr) 180.8 \nNatriy(gr) 48.0 \nOltingugurt(gr) 19.2 \nTemir(mg) 7200.0 \nMis(mg) 64.0 \nRux(mg) 240.0 \nMarganets(mg) 800.0 \nKobalt(mg) 7.2 \nYod(mg) 0.64 \nKarotin(mg) 240.0 \nVitamin D 2560.0 \nVitamin E 800.0")
	elif message.text == "117":
        bot.reply_to(message, "17.0 kg Aralsh o't pichanidagi  Oziqa birligi 7.48 \nAlm energiya qoramolda (mj) 109.65 \nQuruq modda(gr) 14450.0 \nTozalanmagan protein(gr) 1615.0 \nHazmlanuvchi protein(gr) 952.0 \nTozalanmagan yog(gr) 408.0 \nTozalanmagan klechatka(gr) 4369.0 \nQand(gr) 170.0 \nKraxmal(gr) 0.0 \nLizin(gr) 64.6 \nMeton-sistin(gr) 51.0 \nKalsiy(gr) 141.10000000000002 \nFosfor(gr) 18.700000000000003 \nMagniy(gr) 39.099999999999994 \nKaliy(gr) 192.10000000000002 \nNatriy(gr) 51.0 \nOltingugurt(gr) 20.4 \nTemir(mg) 7650.0 \nMis(mg) 68.0 \nRux(mg) 255.0 \nMarganets(mg) 850.0 \nKobalt(mg) 7.65 \nYod(mg) 0.68 \nKarotin(mg) 255.0 \nVitamin D 2720.0 \nVitamin E 850.0")
	elif message.text == "118":
        bot.reply_to(message, "18.0 kg Aralsh o't pichanidagi  Oziqa birligi 7.92 \nAlm energiya qoramolda (mj) 116.10000000000001 \nQuruq modda(gr) 15300.0 \nTozalanmagan protein(gr) 1710.0 \nHazmlanuvchi protein(gr) 1008.0 \nTozalanmagan yog(gr) 432.0 \nTozalanmagan klechatka(gr) 4626.0 \nQand(gr) 180.0 \nKraxmal(gr) 0.0 \nLizin(gr) 68.39999999999999 \nMeton-sistin(gr) 54.0 \nKalsiy(gr) 149.4 \nFosfor(gr) 19.8 \nMagniy(gr) 41.4 \nKaliy(gr) 203.4 \nNatriy(gr) 54.0 \nOltingugurt(gr) 21.599999999999998 \nTemir(mg) 8100.0 \nMis(mg) 72.0 \nRux(mg) 270.0 \nMarganets(mg) 900.0 \nKobalt(mg) 8.1 \nYod(mg) 0.72 \nKarotin(mg) 270.0 \nVitamin D 2880.0 \nVitamin E 900.0")
	elif message.text == "119":
        bot.reply_to(message, "19.0 kg Aralsh o't pichanidagi  Oziqa birligi 8.36 \nAlm energiya qoramolda (mj) 122.55 \nQuruq modda(gr) 16150.0 \nTozalanmagan protein(gr) 1805.0 \nHazmlanuvchi protein(gr) 1064.0 \nTozalanmagan yog(gr) 456.0 \nTozalanmagan klechatka(gr) 4883.0 \nQand(gr) 190.0 \nKraxmal(gr) 0.0 \nLizin(gr) 72.2 \nMeton-sistin(gr) 57.0 \nKalsiy(gr) 157.70000000000002 \nFosfor(gr) 20.900000000000002 \nMagniy(gr) 43.699999999999996 \nKaliy(gr) 214.70000000000002 \nNatriy(gr) 57.0 \nOltingugurt(gr) 22.8 \nTemir(mg) 8550.0 \nMis(mg) 76.0 \nRux(mg) 285.0 \nMarganets(mg) 950.0 \nKobalt(mg) 8.55 \nYod(mg) 0.76 \nKarotin(mg) 285.0 \nVitamin D 3040.0 \nVitamin E 950.0")
	elif message.text == "120":
        bot.reply_to(message, "20.0 kg Aralsh o't pichanidagi  Oziqa birligi 8.8 \nAlm energiya qoramolda (mj) 129.0 \nQuruq modda(gr) 17000.0 \nTozalanmagan protein(gr) 1900.0 \nHazmlanuvchi protein(gr) 1120.0 \nTozalanmagan yog(gr) 480.0 \nTozalanmagan klechatka(gr) 5140.0 \nQand(gr) 200.0 \nKraxmal(gr) 0.0 \nLizin(gr) 76.0 \nMeton-sistin(gr) 60.0 \nKalsiy(gr) 166.0 \nFosfor(gr) 22.0 \nMagniy(gr) 46.0 \nKaliy(gr) 226.0 \nNatriy(gr) 60.0 \nOltingugurt(gr) 24.0 \nTemir(mg) 9000.0 \nMis(mg) 80.0 \nRux(mg) 300.0 \nMarganets(mg) 1000.0 \nKobalt(mg) 9.0 \nYod(mg) 0.8 \nKarotin(mg) 300.0 \nVitamin D 3200.0 \nVitamin E 1000.0")
	elif message.text == "201":
	    bot.reply_to(message, "1.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 0.22 \nAlm energiya qoramolda (mj) 4.91 \nQuruq modda(gr) 849.0 \nTozalanmagan protein(gr) 46.0 \nHazmlanuvchi protein(gr) 9.0 \nTozalanmagan yog(gr) 15.0 \nTozalanmagan klechatka(gr) 351.0 \nQand(gr) 3.0 \nKraxmal(gr) 0.0 \nLizin(gr) 1.3 \nMeton-sistin(gr) 1.3 \nKalsiy(gr) 3.3 \nFosfor(gr) 0.9 \nMagniy(gr) 1.4 \nKaliy(gr) 8.0 \nNatriy(gr) 0.6 \nOltingugurt(gr) 1.0 \nTemir(mg) 409.0 \nMis(mg) 1.1 \nRux(mg) 35.0 \nMarganets(mg) 53.0 \nKobalt(mg) 0.5 \nYod(mg) 0.45 \nKarotin(mg) 5.0 \nVitamin D 40.0 \nVitamin E 0.0")
	elif message.text == "202":
	    bot.reply_to(message, "2.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 0.44 \nAlm energiya qoramolda (mj) 9.82 \nQuruq modda(gr) 1698.0 \nTozalanmagan protein(gr) 92.0 \nHazmlanuvchi protein(gr) 18.0 \nTozalanmagan yog(gr) 30.0 \nTozalanmagan klechatka(gr) 702.0 \nQand(gr) 6.0 \nKraxmal(gr) 0.0 \nLizin(gr) 2.6 \nMeton-sistin(gr) 2.6 \nKalsiy(gr) 6.6 \nFosfor(gr) 1.8 \nMagniy(gr) 2.8 \nKaliy(gr) 16.0 \nNatriy(gr) 1.2 \nOltingugurt(gr) 2.0 \nTemir(mg) 818.0 \nMis(mg) 2.2 \nRux(mg) 70.0 \nMarganets(mg) 106.0 \nKobalt(mg) 1.0 \nYod(mg) 0.9 \nKarotin(mg) 10.0 \nVitamin D 80.0 \nVitamin E 0.0")
	elif message.text == "203":
	    bot.reply_to(message, "3.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 0.66 \nAlm energiya qoramolda (mj) 14.73 \nQuruq modda(gr) 2547.0 \nTozalanmagan protein(gr) 138.0 \nHazmlanuvchi protein(gr) 27.0 \nTozalanmagan yog(gr) 45.0 \nTozalanmagan klechatka(gr) 1053.0 \nQand(gr) 9.0 \nKraxmal(gr) 0.0 \nLizin(gr) 3.9000000000000004 \nMeton-sistin(gr) 3.9000000000000004 \nKalsiy(gr) 9.899999999999999 \nFosfor(gr) 2.7 \nMagniy(gr) 4.199999999999999 \nKaliy(gr) 24.0 \nNatriy(gr) 1.7999999999999998 \nOltingugurt(gr) 3.0 \nTemir(mg) 1227.0 \nMis(mg) 3.3000000000000003 \nRux(mg) 105.0 \nMarganets(mg) 159.0 \nKobalt(mg) 1.5 \nYod(mg) 1.35 \nKarotin(mg) 15.0 \nVitamin D 120.0 \nVitamin E 0.0")
	elif message.text == "204":
	    bot.reply_to(message, "4.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 0.88 \nAlm energiya qoramolda (mj) 19.64 \nQuruq modda(gr) 3396.0 \nTozalanmagan protein(gr) 184.0 \nHazmlanuvchi protein(gr) 36.0 \nTozalanmagan yog(gr) 60.0 \nTozalanmagan klechatka(gr) 1404.0 \nQand(gr) 12.0 \nKraxmal(gr) 0.0 \nLizin(gr) 5.2 \nMeton-sistin(gr) 5.2 \nKalsiy(gr) 13.2 \nFosfor(gr) 3.6 \nMagniy(gr) 5.6 \nKaliy(gr) 32.0 \nNatriy(gr) 2.4 \nOltingugurt(gr) 4.0 \nTemir(mg) 1636.0 \nMis(mg) 4.4 \nRux(mg) 140.0 \nMarganets(mg) 212.0 \nKobalt(mg) 2.0 \nYod(mg) 1.8 \nKarotin(mg) 20.0 \nVitamin D 160.0 \nVitamin E 0.0")
	elif message.text == "205":
	    bot.reply_to(message, "5.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 1.1 \nAlm energiya qoramolda (mj) 24.55 \nQuruq modda(gr) 4245.0 \nTozalanmagan protein(gr) 230.0 \nHazmlanuvchi protein(gr) 45.0 \nTozalanmagan yog(gr) 75.0 \nTozalanmagan klechatka(gr) 1755.0 \nQand(gr) 15.0 \nKraxmal(gr) 0.0 \nLizin(gr) 6.5 \nMeton-sistin(gr) 6.5 \nKalsiy(gr) 16.5 \nFosfor(gr) 4.5 \nMagniy(gr) 7.0 \nKaliy(gr) 40.0 \nNatriy(gr) 3.0 \nOltingugurt(gr) 5.0 \nTemir(mg) 2045.0 \nMis(mg) 5.5 \nRux(mg) 175.0 \nMarganets(mg) 265.0 \nKobalt(mg) 2.5 \nYod(mg) 2.25 \nKarotin(mg) 25.0 \nVitamin D 200.0 \nVitamin E 0.0")
	elif message.text == "206":
	    bot.reply_to(message, "6.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 1.32 \nAlm energiya qoramolda (mj) 29.46 \nQuruq modda(gr) 5094.0 \nTozalanmagan protein(gr) 276.0 \nHazmlanuvchi protein(gr) 54.0 \nTozalanmagan yog(gr) 90.0 \nTozalanmagan klechatka(gr) 2106.0 \nQand(gr) 18.0 \nKraxmal(gr) 0.0 \nLizin(gr) 7.800000000000001 \nMeton-sistin(gr) 7.800000000000001 \nKalsiy(gr) 19.799999999999997 \nFosfor(gr) 5.4 \nMagniy(gr) 8.399999999999999 \nKaliy(gr) 48.0 \nNatriy(gr) 3.5999999999999996 \nOltingugurt(gr) 6.0 \nTemir(mg) 2454.0 \nMis(mg) 6.6000000000000005 \nRux(mg) 210.0 \nMarganets(mg) 318.0 \nKobalt(mg) 3.0 \nYod(mg) 2.7 \nKarotin(mg) 30.0 \nVitamin D 240.0 \nVitamin E 0.0")
	elif message.text == "207":
	    bot.reply_to(message, "7.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 1.54 \nAlm energiya qoramolda (mj) 34.370000000000005 \nQuruq modda(gr) 5943.0 \nTozalanmagan protein(gr) 322.0 \nHazmlanuvchi protein(gr) 63.0 \nTozalanmagan yog(gr) 105.0 \nTozalanmagan klechatka(gr) 2457.0 \nQand(gr) 21.0 \nKraxmal(gr) 0.0 \nLizin(gr) 9.1 \nMeton-sistin(gr) 9.1 \nKalsiy(gr) 23.099999999999998 \nFosfor(gr) 6.3 \nMagniy(gr) 9.799999999999999 \nKaliy(gr) 56.0 \nNatriy(gr) 4.2 \nOltingugurt(gr) 7.0 \nTemir(mg) 2863.0 \nMis(mg) 7.700000000000001 \nRux(mg) 245.0 \nMarganets(mg) 371.0 \nKobalt(mg) 3.5 \nYod(mg) 3.15 \nKarotin(mg) 35.0 \nVitamin D 280.0 \nVitamin E 0.0")
	elif message.text == "208":
	    bot.reply_to(message, "8.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 1.76 \nAlm energiya qoramolda (mj) 39.28 \nQuruq modda(gr) 6792.0 \nTozalanmagan protein(gr) 368.0 \nHazmlanuvchi protein(gr) 72.0 \nTozalanmagan yog(gr) 120.0 \nTozalanmagan klechatka(gr) 2808.0 \nQand(gr) 24.0 \nKraxmal(gr) 0.0 \nLizin(gr) 10.4 \nMeton-sistin(gr) 10.4 \nKalsiy(gr) 26.4 \nFosfor(gr) 7.2 \nMagniy(gr) 11.2 \nKaliy(gr) 64.0 \nNatriy(gr) 4.8 \nOltingugurt(gr) 8.0 \nTemir(mg) 3272.0 \nMis(mg) 8.8 \nRux(mg) 280.0 \nMarganets(mg) 424.0 \nKobalt(mg) 4.0 \nYod(mg) 3.6 \nKarotin(mg) 40.0 \nVitamin D 320.0 \nVitamin E 0.0")
	elif message.text == "209":
	    bot.reply_to(message, "9.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 1.98 \nAlm energiya qoramolda (mj) 44.19 \nQuruq modda(gr) 7641.0 \nTozalanmagan protein(gr) 414.0 \nHazmlanuvchi protein(gr) 81.0 \nTozalanmagan yog(gr) 135.0 \nTozalanmagan klechatka(gr) 3159.0 \nQand(gr) 27.0 \nKraxmal(gr) 0.0 \nLizin(gr) 11.700000000000001 \nMeton-sistin(gr) 11.700000000000001 \nKalsiy(gr) 29.7 \nFosfor(gr) 8.1 \nMagniy(gr) 12.6 \nKaliy(gr) 72.0 \nNatriy(gr) 5.3999999999999995 \nOltingugurt(gr) 9.0 \nTemir(mg) 3681.0 \nMis(mg) 9.9 \nRux(mg) 315.0 \nMarganets(mg) 477.0 \nKobalt(mg) 4.5 \nYod(mg) 4.05 \nKarotin(mg) 45.0 \nVitamin D 360.0 \nVitamin E 0.0")
	elif message.text == "210":
	    bot.reply_to(message, "")
	elif message.text == "211":
	    bot.reply_to(message, "")
	elif message.text == "212":
	    bot.reply_to(message, "")
	elif message.text == "213":
	    bot.reply_to(message, "")
	elif message.text == "214":
	    bot.reply_to(message, "")
	elif message.text == "215":
	    bot.reply_to(message, "")
	elif message.text == "216":
		bot.reply_to(message, "")
	elif message.text == "217":
	    bot.reply_to(message, "17.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 3.74 \nAlm energiya qoramolda (mj) 83.47 \nQuruq modda(gr) 14433.0 \nTozalanmagan protein(gr) 782.0 \nHazmlanuvchi protein(gr) 153.0 \nTozalanmagan yog(gr) 255.0 \nTozalanmagan klechatka(gr) 5967.0 \nQand(gr) 51.0 \nKraxmal(gr) 0.0 \nLizin(gr) 22.1 \nMeton-sistin(gr) 22.1 \nKalsiy(gr) 56.099999999999994 \nFosfor(gr) 15.3 \nMagniy(gr) 23.799999999999997 \nKaliy(gr) 136.0 \nNatriy(gr) 10.2 \nOltingugurt(gr) 17.0 \nTemir(mg) 6953.0 \nMis(mg) 18.700000000000003 \nRux(mg) 595.0 \nMarganets(mg) 901.0 \nKobalt(mg) 8.5 \nYod(mg) 7.65 \nKarotin(mg) 85.0 \nVitamin D 680.0 \nVitamin E 0.0")
	elif message.text == "218":
	    bot.reply_to(message, "18.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 3.96 \nAlm energiya qoramolda (mj) 88.38 \nQuruq modda(gr) 15282.0 \nTozalanmagan protein(gr) 828.0 \nHazmlanuvchi protein(gr) 162.0 \nTozalanmagan yog(gr) 270.0 \nTozalanmagan klechatka(gr) 6318.0 \nQand(gr) 54.0 \nKraxmal(gr) 0.0 \nLizin(gr) 23.400000000000002 \nMeton-sistin(gr) 23.400000000000002 \nKalsiy(gr) 59.4 \nFosfor(gr) 16.2 \nMagniy(gr) 25.2 \nKaliy(gr) 144.0 \nNatriy(gr) 10.799999999999999 \nOltingugurt(gr) 18.0 \nTemir(mg) 7362.0 \nMis(mg) 19.8 \nRux(mg) 630.0 \nMarganets(mg) 954.0 \nKobalt(mg) 9.0 \nYod(mg) 8.1 \nKarotin(mg) 90.0 \nVitamin D 720.0 \nVitamin E 0.0")
	elif message.text == "219":
	    bot.reply_to(message, "19.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 4.18 \nAlm energiya qoramolda (mj) 93.29 \nQuruq modda(gr) 16131.0 \nTozalanmagan protein(gr) 874.0 \nHazmlanuvchi protein(gr) 171.0 \nTozalanmagan yog(gr) 285.0 \nTozalanmagan klechatka(gr) 6669.0 \nQand(gr) 57.0 \nKraxmal(gr) 0.0 \nLizin(gr) 24.7 \nMeton-sistin(gr) 24.7 \nKalsiy(gr) 62.699999999999996 \nFosfor(gr) 17.1 \nMagniy(gr) 26.599999999999998 \nKaliy(gr) 152.0 \nNatriy(gr) 11.4 \nOltingugurt(gr) 19.0 \nTemir(mg) 7771.0 \nMis(mg) 20.900000000000002 \nRux(mg) 665.0 \nMarganets(mg) 1007.0 \nKobalt(mg) 9.5 \nYod(mg) 8.55 \nKarotin(mg) 95.0 \nVitamin D 760.0 \nVitamin E 0.0")
	elif message.text == "220":
	    bot.reply_to(message, "19.0 kg Baxorgi bug'doy paxolidagi  Oziqa birligi 4.18 \nAlm energiya qoramolda (mj) 93.29 \nQuruq modda(gr) 16131.0 \nTozalanmagan protein(gr) 874.0 \nHazmlanuvchi protein(gr) 171.0 \nTozalanmagan yog(gr) 285.0 \nTozalanmagan klechatka(gr) 6669.0 \nQand(gr) 57.0 \nKraxmal(gr) 0.0 \nLizin(gr) 24.7 \nMeton-sistin(gr) 24.7 \nKalsiy(gr) 62.699999999999996 \nFosfor(gr) 17.1 \nMagniy(gr) 26.599999999999998 \nKaliy(gr) 152.0 \nNatriy(gr) 11.4 \nOltingugurt(gr) 19.0 \nTemir(mg) 7771.0 \nMis(mg) 20.900000000000002 \nRux(mg) 665.0 \nMarganets(mg) 1007.0 \nKobalt(mg) 9.5 \nYod(mg) 8.55 \nKarotin(mg) 95.0 \nVitamin D 760.0 \nVitamin E 0.0")
	elif message.text == "301":
	    bot.reply_to(message, "")
	elif message.text == "302":
	    bot.reply_to(message, "")
	elif message.text == "303":
	    bot.reply_to(message, "")
	elif message.text == "304":
	    bot.reply_to(message, "")
	elif message.text == "305":
	    bot.reply_to(message, "")
	elif message.text == "306":
	    bot.reply_to(message, "")
	elif message.text == "307":
	    bot.reply_to(message, "")
	elif message.text == "308":
	    bot.reply_to(message, "")
	elif message.text == "309":
	    bot.reply_to(message, "")
	elif message.text == "310":
	    bot.reply_to(message, "")
	elif message.text == "311":
	    bot.reply_to(message, "")
	elif message.text == "312":
	    bot.reply_to(message, "")
	elif message.text == "313":
	    bot.reply_to(message, "")
	elif message.text == "314":
	    bot.reply_to(message, "")
	elif message.text == "315":
	    bot.reply_to(message, "")
	elif message.text == "316":
	    bot.reply_to(message, "")
	elif message.text == "317":
	    bot.reply_to(message, "")
	elif message.text == "318":
	    bot.reply_to(message, "")
	elif message.text == "319":
	    bot.reply_to(message, "")
	elif message.text == "320":
	    bot.reply_to(message, "")
	elif message.text == "401":
	    bot.reply_to(message, "")
	elif message.text == "402":
	    bot.reply_to(message, "")
	elif message.text == "403":
	    bot.reply_to(message, "")
	elif message.text == "404":
	    bot.reply_to(message, "")
	elif message.text == "405":
	    bot.reply_to(message, "")
	elif message.text == "406":
	    bot.reply_to(message, "")
	elif message.text == "407":
	    bot.reply_to(message, "")
	elif message.text == "408":
	    bot.reply_to(message, "")
	elif message.text == "409":
	    bot.reply_to(message, "")
	elif message.text == "410":
	    bot.reply_to(message, "")
	elif message.text == "411":
	    bot.reply_to(message, "")
	elif message.text == "412":
	    bot.reply_to(message, "")
	elif message.text == "413":
	    bot.reply_to(message, "")
	elif message.text == "414":
	    bot.reply_to(message, "")
	elif message.text == "415":
	    bot.reply_to(message, "")
	elif message.text == "416":
	    bot.reply_to(message, "")
	elif message.text == "417":
	    bot.reply_to(message, "")
	elif message.text == "418":
	    bot.reply_to(message, "")
	elif message.text == "419":
	    bot.reply_to(message, "")
	elif message.text == "420":
	    bot.reply_to(message, "")
	elif message.text == "501":
	    bot.reply_to(message, "")
	elif message.text == "502":
	    bot.reply_to(message, "")
	elif message.text == "503":
	    bot.reply_to(message, "")
	elif message.text == "504":
	    bot.reply_to(message, "")
	elif message.text == "505":
	    bot.reply_to(message, "")
	elif message.text == "506":
	    bot.reply_to(message, "")
	elif message.text == "507":
	    bot.reply_to(message, "")
	elif message.text == "508":
	    bot.reply_to(message, "")
	elif message.text == "509":
	    bot.reply_to(message, "")
	elif message.text == "510":
	    bot.reply_to(message, "")
	elif message.text == "601":
	    bot.reply_to(message, "")
	elif message.text == "602":
	    bot.reply_to(message, "")
	elif message.text == "603":
	    bot.reply_to(message, "")
	elif message.text == "604":
	    bot.reply_to(message, "")
	elif message.text == "605":
	    bot.reply_to(message, "")
	elif message.text == "606":
	    bot.reply_to(message, "")
	elif message.text == "607":
	    bot.reply_to(message, "")
	elif message.text == "608":
	    bot.reply_to(message, "")
	elif message.text == "609":
	    bot.reply_to(message, "")
	elif message.text == "610":
	    bot.reply_to(message, "")
	elif message.text == "701":
	    bot.reply_to(message, "")
	elif message.text == "702":
	    bot.reply_to(message, "")
	elif message.text == "703":
	    bot.reply_to(message, "")
	elif message.text == "704":
	    bot.reply_to(message, "")
	elif message.text == "705":
	    bot.reply_to(message, "")
	elif message.text == "706":
	    bot.reply_to(message, "")
	elif message.text == "707":
	    bot.reply_to(message, "")
	elif message.text == "708":
	    bot.reply_to(message, "")
	elif message.text == "709":
	    bot.reply_to(message, "")
	elif message.text == "710":
	    bot.reply_to(message, "")
	else:
        bot.reply_to(message, "Moling bokib qoldi")
bot.polling()
