import math #line:1
import numpy as np #line:2
import time #line:3
import time #line:4
import os .path #line:5
import getpass #line:6
from IPython .display import Markdown ,display #line:7
def pj (OOO0OO00O0OO000O0 ,OO00O000OO0O00OO0 ):#line:11
        print ("\nPasswords may not be changed using this notebook at present.")#line:15
ps =[]#line:19
wd =''#line:20
rid =0 #line:21
encoff1 =34 #line:22
encoff2 =567 #line:23
def a1 ():#line:41
    global ps #line:43
    OO000OO0O0000O00O =".a1_counter.npy"#line:46
    OO000OOOO0O0OOO0O =np .zeros (1 ,dtype ='int8,bool')#line:47
    OOO00OOO0OO0000O0 =0 #line:49
    OO000OO0OO00O0000 =ps [0 ]#line:50
    OOOOO0OOO0O00O000 =ps [1 ]#line:51
    if (waiter ()):#line:53
        while True :#line:54
            try :#line:55
                printmd ('**CA** (2%)')#line:56
                print (OO000OO0OO00O0000 ,"+",OOOOO0OOO0O00O000 )#line:57
                print ('tester')#line:58
                O00OOOOOO0OOOO000 =float (input ("Please enter your answer here: "))#line:59
                O00O0OO0O000O0O00 =OO000OO0OO00O0000 +OOOOO0OOO0O00O000 #line:60
                O00OO000O00OOO000 =np .isclose (O00OOOOOO0OOOO000 ,O00O0OO0O000O0O00 ,OOO00OOO0OO0000O0 )#line:61
                if O00OO000O00OOO000 :#line:62
                    print ("Well done, right answer is ",O00O0OO0O000O0O00 )#line:63
                else :#line:64
                    print ("Not right yet. Take another look then run this cell again.")#line:65
                OO000OOOO0O0OOO0O =trycount (OO000OO0O0000O00O ,O00OO000O00OOO000 )#line:67
                O0000O0OOOOOO000O =100 -(OO000OOOO0O0OOO0O [0 ]-1 )*10 #line:68
                if OO000OOOO0O0OOO0O [1 ]:#line:69
                    print ("First success after ",OO000OOOO0O0OOO0O [0 ]," tries, you have ",O0000O0OOOOOO000O ,"% on this exercise.")#line:70
                    print ("Enter this code into Brightspace:\n\n",genenc (1 +encoff1 ,O0000O0OOOOOO000O +encoff2 ),'\n')#line:71
                else :#line:72
                    print ("You have had ",OO000OOOO0O0OOO0O [0 ]," tries.")#line:73
                    print ("If next try is accepted you will achieve ",O0000O0OOOOOO000O -10 ,"% on this exercise.")#line:74
                break #line:76
            except ValueError :#line:78
                print ("I didn't understand that.")#line:79
                continue #line:80
        return #line:82
def a2 (OO0O0OOOO000000OO ):#line:91
    global ps #line:93
    OOOOOOOOO0O00OOOO =".a2_counter.npy"#line:96
    O0OO0OOO0OO0O0O00 =np .zeros (1 ,dtype ='int8,bool')#line:97
    OOO0O0O0O00OO00OO =6 #line:100
    O0O0OOO0000OOOO0O =7 #line:101
    OOOO0OO00O0O0O000 =0 #line:103
    O00OOO00O0OO00O00 =(ps [OOO0O0O0O00OO00OO ])%6 +1 #line:105
    O0OOO0O000O000O0O =(ps [O0O0OOO0000OOOO0O ])%6 +1 #line:106
    while O00OOO00O0OO00O00 +O0OOO0O000O000O0O ==7 or O00OOO00O0OO00O00 ==O0OOO0O000O000O0O :#line:107
        O0OOO0O000O000O0O +=1 #line:108
        O0OOO0O000O000O0O =O0OOO0O000O000O0O %6 +1 #line:109
    if (OO0O0OOOO000000OO ):#line:111
        printmd ('**CA** (2%)')#line:112
        print ("Run your program (when you are happy it is working correctly) for a=",O00OOO00O0OO00O00 ," and b=",O0OOO0O000O000O0O )#line:113
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:114
        return #line:115
    if (waiter ()):#line:117
        while True :#line:118
            try :#line:119
                print ("Enter your program's result for a=",O00OOO00O0OO00O00 ," and b=",O0OOO0O000O000O0O )#line:120
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:121
                OO0O00O00O00OOO0O =float (input ("Please enter your answer here: "))#line:122
                O000OO00O00O00O0O =(3 *(O00OOO00O0OO00O00 **3 *O0OOO0O000O000O0O -O00OOO00O0OO00O00 *O0OOO0O000O000O0O **3 ))%7 #line:123
                OOO0OO0OOO0O0OOOO =np .isclose (OO0O00O00O00OOO0O ,O000OO00O00O00O0O ,OOOO0OO00O0O0O000 )#line:124
                if OOO0OO0OOO0O0OOOO :#line:125
                    print ("Well done, right answer is ",O000OO00O00O00O0O )#line:126
                else :#line:127
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:128
                O0OO0OOO0OO0O0O00 =trycount (OOOOOOOOO0O00OOOO ,OOO0OO0OOO0O0OOOO )#line:130
                O0OOOOOO0OOO00000 =100 -(O0OO0OOO0OO0O0O00 [0 ]-1 )*10 #line:131
                if O0OO0OOO0OO0O0O00 [1 ]:#line:132
                    print ("First success after ",O0OO0OOO0OO0O0O00 [0 ]," tries, you have ",O0OOOOOO0OOO00000 ,"% on this exercise.")#line:133
                    print ("Enter this code into Brightspace:\n\n",genenc (2 +encoff1 ,O0OOOOOO0OOO00000 +encoff2 ),'\n')#line:134
                else :#line:135
                    print ("You have had ",O0OO0OOO0OO0O0O00 [0 ]," tries.")#line:136
                    print ("If next try is accepted you will achieve ",O0OOOOOO0OOO00000 -10 ,"% on this exercise.")#line:137
                break #line:139
            except ValueError :#line:141
                print ("I didn't understand that.")#line:142
                continue #line:143
        return #line:145
def a3 (OOOOO0O0O0OOOO0OO ):#line:154
    global ps #line:156
    O0O0000OO000OOOOO =".a3_counter.npy"#line:159
    OOOOO0OO0O0O0OO0O =np .zeros (1 ,dtype ='int8,bool')#line:160
    O000O0OOO0O00OOOO =23 #line:163
    O00O0O00O000O0O0O =24 #line:164
    OO0O0O0O0O00OO0O0 =(ps [O000O0OOO0O00OOOO ])%6 +1 #line:165
    O00O0000000OO0O0O =(ps [O00O0O00O000O0O0O ])%6 +1 #line:166
    O0OOOOO0OO0OOOOO0 =0 #line:168
    OO0O0O0O0O00OO0O0 =10 *OO0O0O0O0O00OO0O0 +O00O0000000OO0O0O ;#line:170
    if (OOOOO0O0O0OOOO0OO ):#line:172
        printmd ('**CA** (6%)')#line:173
        print ("Run your program for ",OO0O0O0O0O00OO0O0 ,"people")#line:174
        print ('Once you have the result output by your program, run the next cell below and enter your answer in the dialogue box.')#line:175
        return #line:176
    if (waiter ()):#line:178
        while True :#line:179
            try :#line:180
                print ("Enter your program's result for",OO0O0O0O0O00OO0O0 ,"people")#line:181
                print ('(If you are not ready to enter an answer stop the kernel and go back to your program.)')#line:182
                OOOO00O0O00O00OOO =float (input ("Please enter your answer here: "))#line:183
                OOOOOO0OO000O0O00 =OO0O0O0O0O00OO0O0 +2 *OO0O0O0O0O00OO0O0 +2 *OO0O0O0O0O00OO0O0 +10 *OO0O0O0O0O00OO0O0 #line:184
                OOOO00O0O00O0OOOO =np .isclose (OOOO00O0O00O00OOO ,OOOOOO0OO000O0O00 ,O0OOOOO0OO0OOOOO0 )#line:185
                if OOOO00O0O00O0OOOO :#line:186
                    print ("Well done, right answer is ",OOOOOO0OO000O0O00 )#line:187
                else :#line:188
                    print ("Not right yet. Take another look then run this cell again. (Make sure you are working with integers!)")#line:189
                OOOOO0OO0O0O0OO0O =trycount (O0O0000OO000OOOOO ,OOOO00O0O00O0OOOO )#line:191
                O000O00000000O0OO =100 -(OOOOO0OO0O0O0OO0O [0 ]-1 )*10 #line:192
                if OOOOO0OO0O0O0OO0O [1 ]:#line:193
                    print ("First success after ",OOOOO0OO0O0O0OO0O [0 ]," tries, you have ",O000O00000000O0OO ,"% on this exercise.")#line:194
                    print ("Enter this code into Brightspace:\n\n",genenc (3 +encoff1 ,O000O00000000O0OO +encoff2 ),'\n')#line:195
                else :#line:196
                    print ("You have had ",OOOOO0OO0O0O0OO0O [0 ]," tries.")#line:197
                    print ("If next try is accepted you will achieve ",O000O00000000O0OO -10 ,"% on this exercise.")#line:198
                break #line:200
            except ValueError :#line:202
                print ("I didn't understand that.")#line:203
                continue #line:204
        return #line:206
def a4 (OOOO0OOOO0O0OOO0O ):#line:217
        import random #line:219
        import requests #line:220
        global ps #line:222
        global wd #line:223
        OO00O0OO0O00OO0OO =".a4_counter.npy"#line:226
        OO0OOOO00OO0OO0O0 =np .zeros (1 ,dtype ='int8,bool')#line:227
        OOOOO0000O0OO0O0O =60 #line:230
        OOO0O00OO0OOOOO0O =61 #line:231
        O00OOO000O0OO0O0O =62 #line:232
        O0OOO0000O00O000O =63 #line:233
        OO00OOOOOO00OO0O0 =64 #line:234
        OO00O00O0O00OO0O0 =0 #line:237
        if (OOOO0OOOO0O0OOO0O ):#line:239
                O000OO0OO00OOO000 ="https://users.cs.duke.edu/~ola/ap/linuxwords"#line:241
                requests .packages .urllib3 .disable_warnings ()#line:244
                O0OOOO0O00OO0OOO0 =requests .get (O000OO0OO00OOO000 ,verify =False )#line:245
                OO00OO0O0O000O0OO =O0OOOO0O00OO0OOO0 .content .splitlines ()#line:247
                random .seed (10 *ps [62 ]+ps [63 ])#line:248
                O00000O0OO0OOOO0O =4 +(10 *ps [64 ]+ps [65 ])%4 #line:249
                O00O0OO0OOO000OOO =True #line:250
                while O00O0OO0OOO000OOO :#line:251
                        OOOO0OO00OOO0O00O =OO00OO0O0O000O0OO [random .randint (0 ,len (OO00OO0O0O000O0OO )-1 )].decode ("utf-8")#line:252
                        if len (OOOO0OO00OOO0O00O )>7 and len (OOOO0OO00OOO0O00O )<14 and OOOO0OO00OOO0O00O [0 ].islower ():#line:254
                                O00O0OO0OOO000OOO =False #line:255
                                for OO00O0O00OO0O00OO in OOOO0OO00OOO0O00O :#line:256
                                        if chr (ord (OO00O0O00OO0O00OO )+O00000O0OO0OOOO0O )>'z':#line:257
                                                O00O0OO0OOO000OOO =True #line:258
                OOOO00OO0O0000OO0 =len (OOOO0OO00OOO0O00O )#line:260
                OO0O0OO0O00OO0O00 =''#line:261
                for OOO0000000OO0O0OO in range (0 ,OOOO00OO0O0000OO0 ):#line:262
                        OO0O0OO0O00OO0O00 +=chr (ord (OOOO0OO00OOO0O00O [OOO0000000OO0O0OO ])+O00000O0OO0OOOO0O )#line:264
                print ('Your encoded word is',OO0O0OO0O00OO0O00 )#line:266
                print ('Write your program in the cell below this one.\n')#line:267
                print ('When you have decoded the word (it should be a real word if you are correct),\n','run the CA cell underneath and enter the word into the dialogue box.')#line:269
                wd =OOOO0OO00OOO0O00O #line:270
                return #line:271
        if (waiter ()):#line:273
                while True :#line:274
                        try :#line:275
                                printmd ('**CA** (6%)')#line:276
                                OO000OOOO00OOOO00 =str (input ("Enter your DECODED word here: "))#line:277
                                OOO000OOO0O0OOOOO =wd #line:278
                                OO0OOOOOOO0OO0OOO =OO000OOOO00OOOO00 ==OOO000OOO0O0OOOOO #line:279
                                if OO0OOOOOOO0OO0OOO :#line:280
                                        print ("Well done, right answer is ",OOO000OOO0O0OOOOO )#line:281
                                else :#line:282
                                        print ("Not right yet. Take another look then run this cell again.")#line:283
                                OO0OOOO00OO0OO0O0 =trycount (OO00O0OO0O00OO0OO ,OO0OOOOOOO0OO0OOO )#line:285
                                O0O0O0O00O00OOO00 =100 -(OO0OOOO00OO0OO0O0 [0 ]-1 )*10 #line:286
                                if OO0OOOO00OO0OO0O0 [1 ]:#line:287
                                        print ("First success after ",OO0OOOO00OO0OO0O0 [0 ]," tries, you have ",O0O0O0O00O00OOO00 ,"% on this exercise.")#line:288
                                        print ("Enter this code into Brightspace:\n\n",genenc (4 +encoff1 ,O0O0O0O00O00OOO00 +encoff2 ),'\n')#line:289
                                else :#line:290
                                        print ("You have had ",OO0OOOO00OO0OO0O0 [0 ]," tries.")#line:291
                                        print ("If next try is accepted you will achieve ",O0O0O0O00O00OOO00 -10 ,"% on this exercise.")#line:292
                                break #line:293
                        except ValueError :#line:295
                                print ("I didn't understand that.")#line:296
                                continue #line:297
                return #line:299
def a5 (OO00000O00O00O00O ):#line:309
        import random #line:311
        import requests #line:312
        global ps #line:314
        global P0 #line:315
        OO00O0OO00O000000 =".a5_counter.npy"#line:319
        OOO0000O00O00000O =np .zeros (1 ,dtype ='int8,bool')#line:320
        OOO0OO00OOOO0OO0O =70 #line:323
        OO0000O0O0OO0O0OO =71 #line:324
        O0OO00OOOOOO0000O =72 #line:325
        OO0OO00000OOO000O =73 #line:326
        OO0000O0O00O0OOOO =74 #line:327
        O00OOO00OO00OOOO0 =0 #line:330
        if (OO00000O00O00O00O ):#line:332
                P0 =[]#line:333
                OO0OOOO00O00OOO0O =7 +(10 *ps [OOO0OO00OOOO0OO0O ]+ps [OO0000O0O0OO0O0OO ])%4 #line:334
                for O00O000O00O0O0O0O in range (OO0OOOO00O00OOO0O ):#line:335
                        P0 .append (max (0 ,ps [O0OO00OOOOOO0000O +O00O000O00O0O0O0O ]-1 ))#line:336
                print ('Run your program for the list below:\n',P0 )#line:337
                print ('Run the next cell and copy and paste your result, as a list of the same length, into the dialogue box.')#line:339
        elif (waiter ()):#line:341
                while True :#line:342
                        try :#line:343
                                printmd ('**CA** (6%)')#line:346
                                O0O0O00O0OOOO0OOO =eval (input ("Enter your list here: "))#line:347
                                O0OOO000O00O00OOO =3 #line:352
                                OOOOO000OO0OOOOO0 =P0 .copy ()#line:353
                                OOOOO000OO0OOOOO0 .append (0 )#line:354
                                print (OOOOO000OO0OOOOO0 )#line:355
                                OO0OOOO00O00OOO0O =len (P0 )#line:356
                                for O0O0OO0OO0O00OOO0 in range (O0OOO000O00O00OOO ):#line:357
                                        for O00O000O00O0O0O0O in range (OO0OOOO00O00OOO0O ):#line:358
                                                OOOOO000OO0OOOOO0 [O00O000O00O0O0O0O ]=OOOOO000OO0OOOOO0 [O00O000O00O0O0O0O +1 ]*(O00O000O00O0O0O0O +1 )#line:360
                                OOOOO000OO0OOOOO0 .pop ()#line:361
                                OO0OOOO0OOOO0OO00 =OOOOO000OO0OOOOO0 #line:364
                                if not type (O0O0O00O0OOOO0OOO )==type (OO0OOOO0OOOO0OO00 ):#line:366
                                        print ('You need to enter answer as a list (not counted as an attempt).')#line:367
                                elif not len (O0O0O00O0OOOO0OOO )==len (OO0OOOO0OOOO0OO00 ):#line:368
                                        print ('You need to enter answer as list of same length (not counted as an attempt).')#line:369
                                else :#line:370
                                        O00O0OOO0OO00000O =O0O0O00O0OOOO0OOO ==OO0OOOO0OOOO0OO00 #line:371
                                        if O00O0OOO0OO00000O :#line:372
                                                print ("Well done, right answer is ",OO0OOOO0OOOO0OO00 )#line:373
                                        else :#line:374
                                                print ("Not right yet. Take another look then run this cell again.")#line:375
                                        OOO0000O00O00000O =trycount (OO00O0OO00O000000 ,O00O0OOO0OO00000O )#line:377
                                        O0O00O00OOO000000 =100 -(OOO0000O00O00000O [0 ]-1 )*10 #line:378
                                        if OOO0000O00O00000O [1 ]:#line:379
                                                print ("First success after ",OOO0000O00O00000O [0 ]," tries, you have ",O0O00O00OOO000000 ,"% on this exercise.")#line:380
                                                print ("Enter this code into Brightspace:\n\n",genenc (5 +encoff1 ,O0O00O00OOO000000 +encoff2 ),'\n')#line:381
                                        else :#line:382
                                                print ("You have had ",OOO0000O00O00000O [0 ]," tries.")#line:383
                                                print ("If next try is accepted you will achieve ",O0O00O00OOO000000 -10 ,"% on this exercise.")#line:384
                                        break #line:385
                                OOOOO000OO0OOOOO0 =None #line:388
                                OO0OOOO0OOOO0OO00 =None #line:389
                        except ValueError :#line:390
                                print ("I didn't understand that.")#line:391
                                continue #line:392
        return #line:394
def a6 (OO0OOOO00O0OOOO00 ):#line:403
        import random #line:405
        import requests #line:406
        global ps #line:408
        global P0 #line:409
        O0OO0O000OO0OO00O =".a6_counter.npy"#line:413
        O0OO0OO00O0O000OO =np .zeros (1 ,dtype ='int8,bool')#line:414
        O0OOO00O0O0O000O0 =11 #line:417
        OO0000O0O0O00OOO0 =16 #line:418
        OO0OO00O00O0O00OO =7 #line:419
        OO00000OO0OO000O0 =33 #line:420
        OO000OO00O00OO000 =21 #line:421
        O0OO00OOOOO0OO00O =0 #line:424
        if (OO0OOOO00O0OOOO00 ):#line:426
                O0000OOOOO0OO0000 =ps [O0OOO00O0O0O000O0 ]+ps [OO0000O0O0O00OOO0 ]+ps [OO0OO00O00O0O00OO ]+ps [OO00000OO0OO000O0 ]+ps [OO000OO00O00OO000 ]#line:427
                random .seed (O0000OOOOO0OO0000 )#line:428
                P0 =random .randint (1000 ,2000 )#line:429
                print ('Run your program to obtain the stopping time for the value:\n',P0 )#line:430
                print ('Run the next cell and enter the stopping time into the dialogue box.')#line:432
        elif (waiter ()):#line:434
                while True :#line:435
                        try :#line:436
                                printmd ('**CA** (6%)')#line:439
                                OOO00O00OOO0OOO00 =eval (input ("Enter your stopping number here: "))#line:440
                                OOO0OO0O00OO00000 =P0 #line:444
                                O0OOOOO0OO0O0OOOO =[OOO0OO0O00OO00000 ]#line:445
                                while not OOO0OO0O00OO00000 ==1 :#line:446
                                        if OOO0OO0O00OO00000 %2 :#line:447
                                                OOO0OO0O00OO00000 =3 *OOO0OO0O00OO00000 +1 #line:448
                                        else :#line:449
                                                OOO0OO0O00OO00000 =OOO0OO0O00OO00000 //2 #line:450
                                        O0OOOOO0OO0O0OOOO .append (OOO0OO0O00OO00000 )#line:451
                                O000000O0OOOOOO00 =len (O0OOOOO0OO0O0OOOO )#line:452
                                O0O00OOOOOO0OO000 =O000000O0OOOOOO00 #line:456
                                if not type (OOO00O00OOO0OOO00 )==type (O0O00OOOOOO0OO000 ):#line:458
                                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:459
                                else :#line:462
                                        OOOOO00O0000O00OO =OOO00O00OOO0OOO00 ==O0O00OOOOOO0OO000 #line:463
                                        if OOOOO00O0000O00OO :#line:464
                                                print ("Well done, right answer is ",O0O00OOOOOO0OO000 )#line:465
                                        else :#line:466
                                                print ("Not right yet. Take another look then run this cell again.")#line:467
                                        O0OO0OO00O0O000OO =trycount (O0OO0O000OO0OO00O ,OOOOO00O0000O00OO )#line:469
                                        OO0O0OO00OO0O0OO0 =100 -(O0OO0OO00O0O000OO [0 ]-1 )*10 #line:470
                                        if O0OO0OO00O0O000OO [1 ]:#line:471
                                                print ("First success after ",O0OO0OO00O0O000OO [0 ]," tries, you have ",OO0O0OO00OO0O0OO0 ,"% on this exercise.")#line:472
                                                print ("Enter this code into Brightspace:\n\n",genenc (6 +encoff1 ,OO0O0OO00OO0O0OO0 +encoff2 ),'\n')#line:473
                                        else :#line:474
                                                print ("You have had ",O0OO0OO00O0O000OO [0 ]," tries.")#line:475
                                                print ("If next try is accepted you will achieve ",OO0O0OO00OO0O0OO0 -10 ,"% on this exercise.")#line:476
                                        break #line:477
                                O000000O0OOOOOO00 =None #line:480
                                O0O00OOOOOO0OO000 =None #line:481
                        except ValueError :#line:482
                                print ("I didn't understand that.")#line:483
                                continue #line:484
        return #line:486
def a7 (OO00O00O0OOOO000O ):#line:496
        O0O0OOO0OOO0OO000 =".a7_counter.npy"#line:500
        OOO0OOO0000OO00O0 =np .zeros (1 ,dtype ='int8,bool')#line:501
        def O00OOOO000OOO0OO0 ():#line:503
                pass #line:504
        O0OO0OO000O0OOOO0 =[(30 ,10 )]#line:507
        O0000O0O0OO00OO0O =1.0e-4 #line:510
        if (waiter ()):#line:513
                printmd ('**CA** (6%)')#line:515
                if not type (OO00O00O0OOOO000O )==type (O00OOOO000OOO0OO0 ):#line:517
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:518
                else :#line:521
                        def O0O0O00OOOOO0O00O (OO00OOO0OO0OOOOO0 ,OOOOO000O000O0000 ):#line:524
                                import math #line:525
                                O00O0O0O0OOO0000O =9.81 #line:526
                                O00OOOO00OOO0OO0O =math .pi *OOOOO000O000O0000 /180. #line:527
                                O0000O0O0OOOO00OO =OO00OOO0OO0OOOOO0 **2 *math .sin (2 *O00OOOO00OOO0OO0O )/O00O0O0O0OOO0000O #line:528
                                OO0O0O0OO0O000OO0 =OO00OOO0OO0OOOOO0 **2 *(math .sin (O00OOOO00OOO0OO0O ))**2 /(2. *O00O0O0O0OOO0000O )#line:529
                                return O0000O0O0OOOO00OO ,OO0O0O0OO0O000OO0 #line:530
                        import random as r #line:533
                        O0OO0OO000O0OOOO0 =[]#line:534
                        O0O0O00000OOOOOO0 =False #line:535
                        O0O00OOO0000000O0 =[]#line:536
                        OOO0OOO0OOOOOOO0O =10 #line:537
                        OOO000OO00OOO0O00 =100 #line:538
                        O0OOOOOOOOO0OO000 =5 #line:539
                        OOO00O000O0000O0O =85 #line:540
                        for O000O00O0O0OOOOO0 in range (5 ):#line:541
                                O0OO0OO000O0OOOO0 .append ((r .uniform (OOO0OOO0OOOOOOO0O ,OOO000OO00OOO0O00 ),r .uniform (O0OOOOOOOOO0OO000 ,OOO00O000O0000O0O )))#line:542
                        for (O00OOO000OO0O0OO0 ,OOOOOOO00O0O00O00 )in O0OO0OO000O0OOOO0 :#line:543
                                print ('Testing:',O00OOO000OO0O0OO0 ,OOOOOOO00O0O00O00 )#line:544
                                OOO000OO0000000OO =OO00O00O0OOOO000O (O00OOO000OO0O0OO0 ,OOOOOOO00O0O00O00 )#line:545
                                print ('Output:',*OOO000OO0000000OO )#line:546
                                O0OO0OOO0OOOO0O0O =O0O0O00OOOOO0O00O (O00OOO000OO0O0OO0 ,OOOOOOO00O0O00O00 )#line:547
                                print ('Actual:',*O0OO0OOO0OOOO0O0O )#line:548
                                print ()#line:549
                                if (not type (OOO000OO0000000OO )==type (O0OO0OOO0OOOO0O0O ))or (not len (OOO000OO0000000OO )==len (O0OO0OOO0OOOO0O0O )):#line:550
                                        if O0O0O00000OOOOOO0 ==False :#line:551
                                           O0O0O00000OOOOOO0 =True #line:552
                                else :#line:553
                                        O0O00OOO0000000O0 .append (all (np .isclose (OOO000OO0000000OO ,O0OO0OOO0OOOO0O0O ,O0000O0O0OO00OO0O )))#line:554
                        if O0O0O00000OOOOOO0 :#line:556
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:557
                        else :#line:559
                                O00OOO00000O00OO0 =all (O0O00OOO0000000O0 )#line:560
                                if O00OOO00000O00OO0 :#line:561
                                        print ("Well done, all correct.")#line:562
                                else :#line:563
                                        print ("Not right yet. Take another look then run this cell again.")#line:564
                                OOO0OOO0000OO00O0 =trycount (O0O0OOO0OOO0OO000 ,O00OOO00000O00OO0 )#line:566
                                OOOO0O000OO0O00O0 =100 -(OOO0OOO0000OO00O0 [0 ]-1 )*10 #line:567
                                if OOO0OOO0000OO00O0 [1 ]:#line:568
                                        print ("First success after ",OOO0OOO0000OO00O0 [0 ]," tries, you have ",OOOO0O000OO0O00O0 ,"% on this exercise.")#line:569
                                        print ("Enter this code into Brightspace:\n\n",genenc (7 +encoff1 ,OOOO0O000OO0O00O0 +encoff2 ),'\n')#line:570
                                else :#line:571
                                        print ("You have had ",OOO0OOO0000OO00O0 [0 ]," tries.")#line:572
                                        print ("If next try is accepted you will achieve ",OOOO0O000OO0O00O0 -10 ,"% on this exercise.")#line:573
                        O0OO0OOO0OOOO0O0O =None #line:576
                        O0O0O00OOOOO0O00O =None #line:577
        return #line:579
def a8 (O0OOOO0000OO000OO ):#line:589
        OOO00OO00O00OO000 =".a8_counter.npy"#line:593
        O00O00OOO0O000000 =np .zeros (1 ,dtype ='int8,bool')#line:594
        def OOO0O000O0O00O0OO ():#line:596
                pass #line:597
        OOO00O0O00000O0O0 =1.0e-4 #line:601
        if (waiter ()):#line:604
                printmd ('**CA** (6%)')#line:606
                if not type (O0OOOO0000OO000OO )==type (OOO0O000O0O00O0OO ):#line:610
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:611
                else :#line:615
                        import inspect #line:618
                        OO00OO0O0OOO00OO0 =inspect .getsourcelines (O0OOOO0000OO000OO )#line:619
                        OOOOO0O00O0000OOO =True #line:620
                        OOOOO0000O0OOO00O =[]#line:621
                        for O0000OOO0OOOO00O0 ,O00O0OOO0O0O0OO0O in enumerate (OO00OO0O0OOO00OO0 [0 ]):#line:622
                                if 'for'in O00O0OOO0O0O0OO0O or 'while'in O00O0OOO0O0O0OO0O :#line:623
                                        OOOOO0O00O0000OOO =False #line:625
                                        OOOOO0000O0OOO00O .append (O0000OOO0OOOO00O0 )#line:626
                        if not OOOOO0O00O0000OOO :#line:627
                                print ('Function needs to be written without loops (using NumPy), check lines',*OOOOO0000O0OOO00O )#line:628
                                print ('No marks lost for this attempt.')#line:629
                                return #line:630
                        def O000O00000O00OOO0 (O0O0000000000O000 ):#line:633
                                OO00O0OOO00OOOO00 =np .vstack ((O0O0000000000O000 ,O0O0000000000O000 [0 ]))#line:634
                                O0O00OO0OO00O00OO =sum (OO00O0OOO00OOOO00 [:-1 ,0 ]*OO00O0OOO00OOOO00 [1 :,1 ])#line:635
                                OOOO0O00OO00O000O =sum (OO00O0OOO00OOOO00 [:-1 ,1 ]*OO00O0OOO00OOOO00 [1 :,0 ])#line:636
                                return abs (O0O00OO0OO00O00OO -OOOO0O00OO00O000O )/2 #line:637
                        import random as r #line:640
                        O0O0O000OO0OO000O =r .randint (6 ,11 )#line:641
                        O000O00000OOOO000 =np .ones ((O0O0O000OO0OO000O ,2 ))#line:642
                        OO0OOO0OO0OOOO0O0 =False #line:643
                        O000OO0O0OOO0OO0O =[]#line:644
                        O000O00OO0O0O000O =1. #line:645
                        OO0O0OO00O0000O0O =20. #line:646
                        OO00OOO0OO0OOO0O0 =O000O00OO0O0O000O #line:647
                        O0000O0OOOOO00OO0 =OO0O0OO00O0000O0O #line:648
                        for O00O0OOO0O0000000 in range (O0O0O000OO0OO000O ):#line:649
                                O000O00000OOOO000 [O00O0OOO0O0000000 ]=[r .uniform (O000O00OO0O0O000O ,OO0O0OO00O0000O0O ),r .uniform (OO00OOO0OO0OOO0O0 ,O0000O0OOOOO00OO0 )]#line:650
                        print ('Testing:',O000O00000OOOO000 )#line:651
                        O000OOOOO0O0OO000 =O0OOOO0000OO000OO (O000O00000OOOO000 )#line:652
                        print ('Output:',O000OOOOO0O0OO000 )#line:653
                        OOO0O0OOO0O0OOOOO =O000O00000O00OOO0 (O000O00000OOOO000 )#line:654
                        print ('Actual:',OOO0O0OOO0O0OOOOO )#line:655
                        print ()#line:656
                        if not type (O000OOOOO0O0OO000 )==type (OOO0O0OOO0O0OOOOO ):#line:657
                                if OO0OOO0OO0OOOO0O0 ==False :#line:658
                                        OO0OOO0OO0OOOO0O0 =True #line:659
                        else :#line:660
                                O000OO0O0OOO0OO0O .append (np .isclose (O000OOOOO0O0OO000 ,OOO0O0OOO0O0OOOOO ,OOO00O0O00000O0O0 ))#line:661
                        if OO0OOO0OO0OOOO0O0 :#line:663
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:664
                        else :#line:666
                                OOOO000O0O0000OOO =all (O000OO0O0OOO0OO0O )#line:667
                                if OOOO000O0O0000OOO :#line:668
                                        print ("Well done, all correct.")#line:669
                                else :#line:670
                                        print ("Not right yet. Take another look then run this cell again.")#line:671
                                O00O00OOO0O000000 =trycount (OOO00OO00O00OO000 ,OOOO000O0O0000OOO )#line:673
                                OO0O0000000000OO0 =100 -(O00O00OOO0O000000 [0 ]-1 )*10 #line:674
                                if O00O00OOO0O000000 [1 ]:#line:675
                                        print ("First success after ",O00O00OOO0O000000 [0 ]," tries, you have ",OO0O0000000000OO0 ,"% on this exercise.")#line:676
                                        print ("Enter this code into Brightspace:\n\n",genenc (8 +encoff1 ,OO0O0000000000OO0 +encoff2 ),'\n')#line:677
                                else :#line:678
                                        print ("You have had ",O00O00OOO0O000000 [0 ]," tries.")#line:679
                                        print ("If next try is accepted you will achieve ",OO0O0000000000OO0 -10 ,"% on this exercise.")#line:680
                        OOO0O0OOO0O0OOOOO =None #line:683
                        O000O00000O00OOO0 =None #line:684
        return #line:686
def a1_notlive ():#line:702
        print ('This CA test is not currently live.')#line:703
        return #line:704
def a2_notlive (OO00OO00O000OOO0O ):#line:712
        print ('This CA test is not currently live.')#line:713
        return #line:714
def a3_notlive (O0OOOO000O0000O0O ):#line:722
        print ('This CA test is not currently live.')#line:723
        return #line:724
def a4_notlive (OOOOOO000000O00O0 ):#line:732
        print ('This CA test is not currently live.')#line:733
        return #line:734
def a5_notlive (O00OO0O0OO0O0OOO0 ):#line:742
        print ('This CA test is not currently live.')#line:743
        return #line:744
def a6_notlive (OOOO000O0O00O0000 ):#line:752
        print ('This CA test is not currently live.')#line:753
        return #line:754
def a7_notlive ():#line:762
        print ('This CA test is not currently live.')#line:763
        return #line:764
def a8_notlive (OO00O0OOO000000OO ):#line:772
        print ('This CA test is not currently live.')#line:773
        return #line:774
def b1 ():#line:792
    global ps #line:794
    O0O0OO00OO0OOO0OO =".b1_counter.npy"#line:797
    OO00O000OO0OOO000 =np .zeros (1 ,dtype ='int8,bool')#line:798
    OO0OOOOOOO0OO0OO0 =0.05 #line:800
    if (waiter ()):#line:802
        while True :#line:803
            try :#line:804
                printmd ('**CA**')#line:805
                OO0O00O0OOO0O0000 =eval (input ("Please enter your answer here in the format D,k: "))#line:806
                OOOO0OO0O000OOO00 =(0.025 ,2.0 )#line:807
                O0O0O0O0O00OO0O0O =all (np .isclose (OO0O00O0OOO0O0000 ,OOOO0OO0O000OOO00 ,rtol =OO0OOOOOOO0OO0OO0 ))#line:808
                if O0O0O0O0O00OO0O0O :#line:809
                    print ("Well done, reasonable estimate is ",OOOO0OO0O000OOO00 )#line:810
                else :#line:811
                    print ("Not right yet. Take another look then run this cell again.")#line:812
                OO00O000OO0OOO000 =trycount (O0O0OO00OO0OOO0OO ,O0O0O0O0O00OO0O0O )#line:814
                O0O0O0OOOO0000O0O =100 -(OO00O000OO0OOO000 [0 ]-1 )*10 #line:815
                if OO00O000OO0OOO000 [1 ]:#line:816
                    print ("First success after ",OO00O000OO0OOO000 [0 ]," tries, you have ",O0O0O0OOOO0000O0O ,"% on this exercise.")#line:817
                    print ("Enter this code into Brightspace:\n\n",genenc (1 +encoff1 ,O0O0O0OOOO0000O0O +encoff2 ),'\n')#line:818
                else :#line:819
                    print ("You have had ",OO00O000OO0OOO000 [0 ]," tries.")#line:820
                    print ("If next try is accepted you will achieve ",O0O0O0OOOO0000O0O -10 ,"% on this exercise.")#line:821
                break #line:823
            except ValueError :#line:825
                print ("I didn't understand that.")#line:826
                continue #line:827
        return #line:829
def b2 (OO0000OOO0O000O00 ):#line:839
        OOOOOO00O00O00O0O =".b2_counter.npy"#line:843
        OOO0O0OOO000OOO00 =np .zeros (1 ,dtype ='int8,bool')#line:844
        def O00OOO00000000O0O ():#line:846
                pass #line:847
        OOO0OO000OOO0O00O =1.0e-2 #line:850
        OO00OOOO0OOOO0OO0 =0.0 #line:851
        if (waiter ()):#line:853
                printmd ('**CA**')#line:855
                if not type (OO0000OOO0O000O00 )==type (O00OOO00000000O0O ):#line:857
                        print ('You need to enter answer as correct type (not counted as an attempt).')#line:858
                else :#line:861
                        def O000OO00000OO00O0 (O0000O00000O0000O ):#line:865
                                OO00000000OOO0O0O =[]#line:866
                                O0000OO0OO0OO000O =20.0 #line:867
                                OO0000OO0000O0O0O =58.1e-3 #line:868
                                O00000OO0OOO0OO00 =9.81 #line:869
                                O00O00OOOOOO0O000 =0.0 #line:870
                                OO0000OOOO0O0OOO0 =0.0 #line:871
                                O00O00OOO0O0OO000 =0.0 #line:872
                                OO000OOO00O0000O0 =10 #line:873
                                OOOO000000O0O0O0O =3.35e-2 #line:874
                                O0OO0OO00O000O0O0 =0.51 #line:875
                                OO0O000000O0000O0 =1.25 #line:876
                                O00OO0O0O0O000O00 =math .pi *OOOO000000O0O0O0O **2 #line:877
                                OOO0O0OO0O0O000O0 =0.5 *O0OO0OO00O000O0O0 *O00OO0O0O0O000O00 *OO0O000000O0000O0 #line:878
                                OOO00OOOOO0O0O0OO =100000 #line:880
                                OO000000OO0OOO00O =np .zeros (OOO00OOOOO0O0O0OO ,float )#line:881
                                OOO000O0O00OOOO00 =np .zeros (OOO00OOOOO0O0O0OO ,float )#line:882
                                O00OO00000O00000O =np .zeros (OOO00OOOOO0O0O0OO ,float )#line:883
                                O000OO00O0O0OO0OO =np .zeros (OOO00OOOOO0O0O0OO ,float )#line:884
                                O0OOO0000OO00OOOO =np .zeros (OOO00OOOOO0O0O0OO ,float )#line:885
                                OO0O0000OO0O0O0OO =np .zeros (OOO00OOOOO0O0O0OO ,float )#line:886
                                OOOO00O0OO0O00OOO =np .zeros (OOO00OOOOO0O0O0OO ,float )#line:887
                                OO000000OO0OOO00O ,O00000O000000O0O0 =np .linspace (O00O00OOO0O0OO000 ,OO000OOO00O0000O0 ,OOO00OOOOO0O0O0OO ,retstep =True )#line:888
                                for O0OO0O000OO00O00O in O0000O00000O0000O :#line:890
                                        OO0O0O0O0OOO0OOOO =O0000OO0OO0OO000O *math .cos (O0OO0O000OO00O00O )#line:891
                                        O0OO0OOO0O0O00OO0 =O0000OO0OO0OO000O *math .sin (O0OO0O000OO00O00O )#line:892
                                        OO0O0000OO0O0O0OO [0 ]=O00O00OOOOOO0O000 #line:894
                                        OOOO00O0OO0O00OOO [0 ]=OO0000OOOO0O0OOO0 #line:895
                                        O000OO00O0O0OO0OO [0 ]=OO0O0O0O0OOO0OOOO #line:896
                                        O0OOO0000OO00OOOO [0 ]=O0OO0OOO0O0O00OO0 #line:897
                                        for O0000O0OOOOO0OO00 in range (OOO00OOOOO0O0O0OO -1 ):#line:898
                                                O0O0O0O00OOOO00O0 =math .sqrt (O000OO00O0O0OO0OO [O0000O0OOOOO0OO00 ]**2 +O0OOO0000OO00OOOO [O0000O0OOOOO0OO00 ]**2 )#line:899
                                                O000O0OO00O000OOO =-OOO0O0OO0O0O000O0 *O0O0O0O00OOOO00O0 *O000OO00O0O0OO0OO [O0000O0OOOOO0OO00 ]#line:900
                                                OOO000O0O00OOOO00 [O0000O0OOOOO0OO00 ]=O000O0OO00O000OOO /OO0000OO0000O0O0O #line:901
                                                O000OO00O0O0OO0OO [O0000O0OOOOO0OO00 +1 ]=O000OO00O0O0OO0OO [O0000O0OOOOO0OO00 ]+OOO000O0O00OOOO00 [O0000O0OOOOO0OO00 ]*O00000O000000O0O0 #line:902
                                                OO0O0000OO0O0O0OO [O0000O0OOOOO0OO00 +1 ]=OO0O0000OO0O0O0OO [O0000O0OOOOO0OO00 ]+O000OO00O0O0OO0OO [O0000O0OOOOO0OO00 +1 ]*O00000O000000O0O0 #line:903
                                                OO000O00O00O00O00 =-OO0000OO0000O0O0O *O00000OO0OOO0OO00 -OOO0O0OO0O0O000O0 *O0O0O0O00OOOO00O0 *O0OOO0000OO00OOOO [O0000O0OOOOO0OO00 ]#line:904
                                                O00OO00000O00000O [O0000O0OOOOO0OO00 ]=OO000O00O00O00O00 /OO0000OO0000O0O0O #line:905
                                                O0OOO0000OO00OOOO [O0000O0OOOOO0OO00 +1 ]=O0OOO0000OO00OOOO [O0000O0OOOOO0OO00 ]+O00OO00000O00000O [O0000O0OOOOO0OO00 ]*O00000O000000O0O0 #line:906
                                                OOOO00O0OO0O00OOO [O0000O0OOOOO0OO00 +1 ]=OOOO00O0OO0O00OOO [O0000O0OOOOO0OO00 ]+O0OOO0000OO00OOOO [O0000O0OOOOO0OO00 +1 ]*O00000O000000O0O0 #line:907
                                                if (OOOO00O0OO0O00OOO [O0000O0OOOOO0OO00 +1 ]<0 ):#line:908
                                                        break #line:909
                                        OO0OO00OO00000OO0 =O0000O0OOOOO0OO00 #line:910
                                        OO00000000OOO0O0O .append (OO0O0000OO0O0O0OO [OO0OO00OO00000OO0 ])#line:911
                                return (OO00000000OOO0O0O );#line:913
                        import random as r #line:916
                        OOOOO00O0OO00O000 =[]#line:917
                        OOOOOOOOO0000OO00 =False #line:918
                        O0OO000O00O0OOOO0 =[]#line:919
                        OOO0OOOO0O0OOO0O0 =0.1 #line:920
                        OOO00OO00OOOOO00O =1.5 #line:921
                        for O000O00OOO0OOO0O0 in range (5 ):#line:922
                                OOOOO00O0OO00O000 .append (r .uniform (OOO0OOOO0O0OOO0O0 ,OOO00OO00OOOOO00O ))#line:923
                        OOOOO00O0OO00O000 .sort ()#line:924
                        print ('Testing thetas=',OOOOO00O0OO00O000 )#line:925
                        OOOO0O0000O0OOO0O =OO0000OOO0O000O00 (OOOOO00O0OO00O000 )#line:926
                        print ('Output ximpacts=',OOOO0O0000O0OOO0O )#line:927
                        OO0OOOOO000O00O0O =O000OO00000OO00O0 (OOOOO00O0OO00O000 )#line:928
                        print ('Actual ximpacts=',OO0OOOOO000O00O0O )#line:929
                        print ()#line:930
                        if (not type (OOOO0O0000O0OOO0O )==type (OO0OOOOO000O00O0O ))or (not len (OOOO0O0000O0OOO0O )==len (OO0OOOOO000O00O0O )):#line:931
                                if OOOOOOOOO0000OO00 ==False :#line:932
                                        OOOOOOOOO0000OO00 =True #line:933
                        else :#line:934
                                O0OO000O00O0OOOO0 .append (all (np .isclose (OOOO0O0000O0OOO0O ,OO0OOOOO000O00O0O ,rtol =OOO0OO000OOO0O00O ,atol =OO00OOOO0OOOO0OO0 )))#line:935
                        if OOOOOOOOO0000OO00 :#line:937
                                print ('Check the returned value format of your function (not counted as an attempt).')#line:938
                        else :#line:940
                                OO000OOOO0OOOO0O0 =all (O0OO000O00O0OOOO0 )#line:941
                                if OO000OOOO0OOOO0O0 :#line:942
                                        print ("Well done, all correct.")#line:943
                                else :#line:944
                                        print ("Not close enough. Take another look then run this cell again.")#line:945
                                OOO0O0OOO000OOO00 =trycount (OOOOOO00O00O00O0O ,OO000OOOO0OOOO0O0 )#line:947
                                O000OOO0000O0OO0O =100 -(OOO0O0OOO000OOO00 [0 ]-1 )*10 #line:948
                                if OOO0O0OOO000OOO00 [1 ]:#line:949
                                        print ("First success after ",OOO0O0OOO000OOO00 [0 ]," tries, you have ",O000OOO0000O0OO0O ,"% on this exercise.")#line:950
                                        print ("Enter this code into Brightspace:\n\n",genenc (2 +encoff1 ,O000OOO0000O0OO0O +encoff2 ),'\n')#line:951
                                else :#line:952
                                        print ("You have had ",OOO0O0OOO000OOO00 [0 ]," tries.")#line:953
                                        print ("If next try is accepted you will achieve ",O000OOO0000O0OO0O -10 ,"% on this exercise.")#line:954
                        OO0OOOOO000O00O0O =None #line:957
                        O000OO00000OO00O0 =None #line:958
        return #line:960
def b3 ():#line:970
    global ps #line:972
    O00OO0OO0O00OOOO0 =".b3_counter.npy"#line:975
    OO00O0O0O00OOO0O0 =np .zeros (1 ,dtype ='int8,bool')#line:976
    OO0OO0OOOOO0OO00O =0.01 #line:979
    if (waiter ()):#line:981
        while True :#line:982
            try :#line:983
                printmd ('**CA**')#line:984
                O0OO0OO0OO0OO0000 =float (input ("Enter a real number here: "))#line:985
                O0000OOO00O00O0O0 =0.5 #line:986
                O0OOOOOOOOOOO0O0O =np .isclose (O0OO0OO0OO0OO0000 ,O0000OOO00O00O0O0 ,atol =OO0OO0OOOOO0OO00O )#line:987
                if O0OOOOOOOOOOO0O0O :#line:988
                    print ("Well done. Actual value is ",O0000OOO00O00O0O0 )#line:989
                else :#line:990
                    print ("Not right yet. Take another look then run this cell again.")#line:991
                OO00O0O0O00OOO0O0 =trycount (O00OO0OO0O00OOOO0 ,O0OOOOOOOOOOO0O0O )#line:993
                OO0OOO000OOOO00O0 =100 -(OO00O0O0O00OOO0O0 [0 ]-1 )*10 #line:994
                if OO00O0O0O00OOO0O0 [1 ]:#line:995
                    print ("First success after ",OO00O0O0O00OOO0O0 [0 ]," tries, you have ",OO0OOO000OOOO00O0 ,"% on this exercise.")#line:996
                    print ("Enter this code into Brightspace:\n\n",genenc (3 +encoff1 ,OO0OOO000OOOO00O0 +encoff2 ),'\n')#line:997
                else :#line:998
                    print ("You have had ",OO00O0O0O00OOO0O0 [0 ]," tries.")#line:999
                    print ("If next try is accepted you will achieve ",OO0OOO000OOOO00O0 -10 ,"% on this exercise.")#line:1000
                break #line:1002
            except ValueError :#line:1004
                print ("I didn't understand that.")#line:1005
                continue #line:1006
        return #line:1008
def b1_notlive ():#line:1020
        print ('This CA test is not currently live.')#line:1021
        return #line:1022
def b2_notlive (O0OO00OO0OO000000 ):#line:1032
        print ('This CA test is not currently live.')#line:1033
        return #line:1034
def b3_notlive ():#line:1041
        print ('This CA test is not currently live.')#line:1042
        return #line:1043
def printmd (OOOO000O0OOO00OOO ):#line:1053
    display (Markdown (OOOO000O0OOO00OOO ))#line:1054
def repeat_to_length (O0OO00O0OO0OO000O ,OOOOOOOO0O00OO000 ):#line:1056
   return (O0OO00O0OO0OO000O *((OOOOOOOO0O00OO000 //len (O0OO00O0OO0OO000O ))+1 ))[:OOOOOOOO0O00OO000 ]#line:1057
def getco (O000O0000000OO0OO ):#line:1059
    global ps #line:1060
    global rid #line:1067
    OO00OOO000OOO00O0 =rid #line:1068
    OO000OOOOOO0O0OOO =str (OO00OOO000OOO00O0 )#line:1070
    OOOOOOOOO00000O00 =repeat_to_length (OO000OOOOOO0O0OOO ,O000O0000000OO0OO )#line:1071
    ps =[int (O0000O0OOO0OO00O0 )+1 for O0000O0OOO0OO00O0 in OOOOOOOOO00000O00 ]#line:1072
def waiter ():#line:1077
    OOOOO00O0O0O00OOO =20 #line:1080
    OOOO000O000000O0O =".ts1.txt"#line:1082
    if os .path .isfile (OOOO000O000000O0O ):#line:1083
        OO00000O00OOOOOOO =np .loadtxt (OOOO000O000000O0O )#line:1084
    else :#line:1086
        OO00000O00OOOOOOO =0.0 #line:1087
    O0OO00O0OOOO0O000 =time .time ()#line:1090
    O0O00O0OO0OOO00O0 =O0OO00O0OOOO0O000 -OO00000O00OOOOOOO #line:1091
    if (O0O00O0OO0OOO00O0 <OOOOO00O0O0O00OOO ):#line:1093
        print ("%.1f  seconds since your last exercise answer.\nYou need to work on your estimate for %.1f seconds before you can try again!"%(O0O00O0OO0OOO00O0 ,OOOOO00O0O0O00OOO ))#line:1094
        return False #line:1095
    else :#line:1096
        OOOOO0OO0O000000O =open (OOOO000O000000O0O ,'w')#line:1097
        OOOOO0OO0O000000O .write (str (O0OO00O0OOOO0O000 ))#line:1098
        OOOOO0OO0O000000O .close ()#line:1099
        return True #line:1100
def trycount (OO000O00O0OOO000O ,O0O00OO00OO000OOO ):#line:1102
    if os .path .isfile (OO000O00O0OOO000O ):#line:1104
        OOO00OO000000000O =np .load (OO000O00O0OOO000O )#line:1105
    else :#line:1107
        OOO00OO000000000O =np .zeros (1 ,dtype ='int8,bool')#line:1108
        OOO00OO000000000O =[0 ,False ]#line:1109
    if not OOO00OO000000000O [1 ]:#line:1112
        OOO00OO000000000O [0 ]+=1 #line:1113
        OOO00OO000000000O [1 ]=O0O00OO00OO000OOO #line:1114
        np .save (OO000O00O0OOO000O ,OOO00OO000000000O )#line:1116
    return OOO00OO000000000O #line:1118
def valdho (OO0OOOO0O000OO0O0 ,O0O0O0O00OOOOO00O ):#line:1126
    OO0000000OOOO0O0O =".dho_counter.npy"#line:1130
    OO0OO00OOOOO0OO0O =np .zeros (1 ,dtype ='int8,bool')#line:1132
    if (waiter ()):#line:1134
        while True :#line:1135
            try :#line:1136
                OOO0O0000OOO00O00 =float (input ("Please enter your estimate here: "))#line:1137
                O0OO0OO0O000O0O00 =2 *np .sqrt (OO0OOOO0O000OO0O0 *O0O0O0O00OOOOO00O )#line:1138
                O0OOOOO0O0O00OO00 =np .isclose (OOO0O0000OOO00O00 ,O0OO0OO0O000O0O00 ,0.2 )#line:1139
                if O0OOOOO0O0O00OO00 :#line:1140
                    print ("Well done, that is close to the critical damping value ",O0OO0OO0O000O0O00 )#line:1141
                else :#line:1142
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1143
                OO0OO00OOOOO0OO0O =trycount (OO0000000OOOO0O0O ,O0OOOOO0O0O00OO00 )#line:1145
                OO00OOO00OO000000 =100 -(OO0OO00OOOOO0OO0O [0 ]-1 )*10 #line:1146
                if OO0OO00OOOOO0OO0O [1 ]:#line:1147
                    print ("First success after ",OO0OO00OOOOO0OO0O [0 ]," tries, you have ",OO00OOO00OO000000 ,"% on this exercise.")#line:1148
                    print ("Enter this code into Brightspace:\n\n",genenc (4 +encoff1 ,OO00OOO00OO000000 +encoff2 ),'\n')#line:1149
                else :#line:1150
                    print ("You have had ",OO0OO00OOOOO0OO0O [0 ]," tries.")#line:1151
                    print ("If next try is accepted you will achieve ",OO00OOO00OO000000 -10 ,"% on this exercise.")#line:1152
                break #line:1154
            except ValueError :#line:1156
                print ("I didn't understand that.")#line:1157
                continue #line:1158
        return #line:1161
def valdrivendho (O0OO0O0O0OOO0OO0O ,O0OOO0O0OO000OO00 ):#line:1171
    OOOOOOO0O00OOO0O0 =".drivendho_counter.npy"#line:1175
    O00OO0O0O0OOO00O0 =np .zeros (1 ,dtype ='int8,bool')#line:1177
    if (waiter ()):#line:1179
        while True :#line:1180
            try :#line:1181
                OO00O0OOO0O00O000 =float (input ("Please enter your estimate here: "))#line:1182
                OO0O000O0OO000000 =np .sqrt (O0OO0O0O0OOO0OO0O **2 -2 *O0OOO0O0OO000OO00 **2 )#line:1183
                O0000OO00OO0OO00O =np .isclose (OO00O0OOO0O00O000 ,OO0O000O0OO000000 ,0.2 )#line:1184
                if O0000OO00OO0OO00O :#line:1185
                    print ("Well done, that is close to the resonance value ",OO0O000O0OO000000 )#line:1186
                else :#line:1187
                    print ("Sorry, not very close. Take another look then run this cell again.")#line:1188
                O00OO0O0O0OOO00O0 =trycount (OOOOOOO0O00OOO0O0 ,O0000OO00OO0OO00O )#line:1190
                OO0OO0OOO0O00O00O =100 -(O00OO0O0O0OOO00O0 [0 ]-1 )*10 #line:1191
                if O00OO0O0O0OOO00O0 [1 ]:#line:1192
                    print ("First success after ",O00OO0O0O0OOO00O0 [0 ]," tries, you have ",OO0OO0OOO0O00O00O ,"% on this exercise.")#line:1193
                    print ("Enter this code into Brightspace:\n\n",genenc (5 +encoff1 ,OO0OO0OOO0O00O00O +encoff2 ),'\n')#line:1194
                else :#line:1195
                    print ("You have had ",O00OO0O0O0OOO00O0 [0 ]," tries.")#line:1196
                    print ("If next try is accepted you will achieve ",OO0OO0OOO0O00O00O -10 ,"% on this exercise.")#line:1197
                break #line:1199
            except ValueError :#line:1201
                print ("I didn't understand that.")#line:1202
                continue #line:1203
        return #line:1206
import ipywidgets as widgets #line:1221
import sys #line:1222
from IPython .display import display #line:1223
from IPython .display import clear_output #line:1224
def create_multipleChoice_widget (OOO0O0OOOO0OOOOO0 ,O0OOO000OOOO0O000 ,O0000OO000OOO000O ,O00000O000OO00O0O ):#line:1226
    O0000OOOOOOOO0O0O ='.q{:d}_counter.npy'.format (OOO0O0OOOO0OOOOO0 )#line:1227
    OOOO000O0000OOOO0 =np .zeros (1 ,dtype ='int8,bool')#line:1228
    OOOO0O00O0OOOO0O0 =len (O0000OO000OOO000O )#line:1230
    if O00000O000OO00O0O not in O0000OO000OOO000O :#line:1231
        O0000OO000OOO000O .append (O00000O000OO00O0O )#line:1232
    O0O0O000000000000 =O0000OO000OOO000O .index (O00000O000OO00O0O )#line:1234
    O0O0OOO0O000O000O =[(O00O0O0OO0OO000O0 ,O000O0OOOOO0O00OO )for O000O0OOOOO0O00OO ,O00O0O0OO0OO000O0 in enumerate (O0000OO000OOO000O )]#line:1236
    OOOOOO0O0OOO000OO =widgets .RadioButtons (options =O0O0OOO0O000O000O ,description ='',disabled =False )#line:1241
    O0OO00O0O000O00O0 =widgets .Output ()#line:1243
    with O0OO00O0O000O00O0 :#line:1244
        print (O0OOO000OOOO0O000 )#line:1245
    OO00OOO00O0000000 =widgets .Output ()#line:1247
    def OOO0O00O00OO0OOO0 (O0O0000OO0OOO0O00 ):#line:1249
        O0OO0OO0000O0OOOO =int (OOOOOO0O0OOO000OO .value )#line:1251
        OOO00OOO0O0OO0OO0 =O0OO0OO0000O0OOOO ==O0O0O000000000000 #line:1253
        O0OOOOOO0O0OOO0OO =trycount (O0000OOOOOOOO0O0O ,OOO00OOO0O0OO0OO0 )#line:1254
        O00O00000O00OOO0O =max (0 ,100 -(O0OOOOOO0O0OOO0OO [0 ]-1 )*100 /OOOO0O00O0OOOO0O0 )#line:1255
        OOO0OOO0O0O000OOO =OOOOOO0O0OOO000OO .options [O0OO0OO0000O0OOOO ][0 ]#line:1256
        if OOO00OOO0O0OO0OO0 :#line:1257
            OOO0OOO0O0O000OOO +=' correct\n'#line:1258
        else :#line:1259
            OOO0OOO0O0O000OOO +=' incorrect\n'#line:1260
        if O0OOOOOO0O0OOO0OO [1 ]:#line:1261
            OOO0OOO0O0O000OOO +='{:.0f}% on try {:d}'.format (O00O00000O00OOO0O ,O0OOOOOO0O0OOO0OO [0 ])#line:1262
        else :#line:1263
            OOO0OOO0O0O000OOO +='{:.0f}% remaining'.format (max (0 ,O00O00000O00OOO0O -100 /OOOO0O00O0OOOO0O0 ))#line:1264
        with OO00OOO00O0000000 :#line:1266
            clear_output ()#line:1267
            print (OOO0OOO0O0O000OOO )#line:1268
        return #line:1269
    OO000OOOOOOOOOOO0 =widgets .Button (description ="submit")#line:1271
    OO000OOOOOOOOOOO0 .on_click (OOO0O00O00OO0OOO0 )#line:1272
    return widgets .VBox ([O0OO00O0O000O00O0 ,OOOOOO0O0OOO000OO ,OO000OOOOOOOOOOO0 ,OO00OOO00O0000000 ])#line:1273
def runq1 ():#line:1280
    OOO0OO0OO0OO00000 =1 #line:1281
    OO0O0OO000O00000O =create_multipleChoice_widget (OOO0OO0OO0OO00000 ,'Complete program:',['n*fac(n+1)','n*fac(n-1)','(n-1)*fac(n)'],'n*fac(n-1)')#line:1282
    display (OO0O0OO000O00000O )#line:1283
def runQ1 ():#line:1293
    O0OOOOOOO0OO00OO0 =1 #line:1294
    O00O0O0O0OOOOOOO0 =create_multipleChoice_widget (O0OOOOOOO0OO00OO0 ,'1N=',['m/s^2','kg/m/s^2','kg m/s^2'],'kg m/s^2')#line:1295
    display (O00O0O0O0OOOOOOO0 )#line:1296
def runQ2x ():#line:1305
    OOO000O0000OOO000 =2 #line:1306
    O0O00OOOO0OO0O000 =create_multipleChoice_widget (OOO000O0000OOO000 ,'',['centred','backwards','forwards'],'centred')#line:1307
    display (O0O00OOOO0OO0O000 )#line:1308
def runQ3x ():#line:1316
    OO0O0000O0000OO00 =3 #line:1317
    O00000OOO000OO00O =create_multipleChoice_widget (OO0O0000O0000OO00 ,'After the Earth\'s gravity, the main effect on a falling tennis ball is: ',['moon','quantum','drag'],'drag')#line:1318
    display (O00000OOO000OO00O )#line:1319
def runQ4x ():#line:1328
    O000OO0OOOO00OO0O =4 #line:1329
    OOO00OO00O00OOOO0 =create_multipleChoice_widget (O000OO0OOOO00OO0O ,'If position y is given by Asin(wt), then the velocity v is: ',['Acos(wt)','-Awsin(wt)','Awcos(wt)'],'Awcos(wt)')#line:1330
    display (OOO00OO00O00OOOO0 )#line:1331
def runQ5x ():#line:1341
    OOOO0OOO0O0OO00O0 =5 #line:1342
    O0OO0OO0OO00O0OO0 =create_multipleChoice_widget (OOOO0OOO0O0OO00O0 ,'Newton\'s second law states that force is proportional to ',['everything','position','acceleration'],'acceleration')#line:1343
    display (O0OO0OO0OO00O0OO0 )#line:1344
def runQ6x ():#line:1353
    OOO0O0O0OOO00OO0O =6 #line:1354
    O0000O00OOO0O00OO =create_multipleChoice_widget (OOO0O0O0OOO00OO0O ,'Drag force magnitude increases with ',['speed','height','gravity'],'speed')#line:1355
    display (O0000O00OOO0O00OO )#line:1356
def runQ7x ():#line:1365
    O0O0000000O000OO0 =7 #line:1366
    O00OO000O0000O0OO =create_multipleChoice_widget (O0O0000000O000OO0 ,'Work has units of ',['Pascals','Newtons','Joules'],'Joules')#line:1367
    display (O00OO000O0000O0OO )#line:1368
pk =(283355 ,839329 )#line:1388
def getrid ():#line:1391
    import random #line:1392
    global rid #line:1393
    rid =random .randint (100000 ,999999 )#line:1394
def encrypt (O00000000OO0OOO00 ):#line:1397
    OO0OO00O000000OOO ,OO0OO0000OOO0OOOO =pk #line:1398
    OOOO00OO000OOO000 =len (str (OO0OO0000OOO0OOOO ))#line:1399
    if OOOO00OO000OOO000 !=6 :#line:1400
        print ('Chunk length hardcoded in format conversion to 6 characters.\n May need to adjust here and in getrid range.\n Exiting.\n')#line:1401
    O00000OO00OO0O0OO =['{:06d}'.format ((int (O00O00O0OOO000O0O )**OO0OO00O000000OOO )%OO0OO0000OOO0OOOO )for O00O00O0OOO000O0O in str (O00000000OO0OOO00 )]#line:1404
    return ''.join (O00000OO00OO0O0OO )#line:1407
def genenc (OO00O0O000O000000 ,OO0OO0O0O0OO0000O ):#line:1410
    global rid #line:1411
    O0OO000O0O00O0000 ='{:06d}'.format (rid )#line:1412
    OOOOO0OO0OOO0OO00 ='{:02d}'.format (OO00O0O000O000000 )#line:1413
    O0OOO0O0000OOO00O ='{:03d}'.format (OO0OO0O0O0OO0000O )#line:1414
    O00O0O0OO000OO00O =O0OO000O0O00O0000 +OOOOO0OO0OOO0OO00 +O0OOO0O0000OOO00O #line:1416
    O000OOOOOOO000O00 ='#'+encrypt (O00O0O0OO000OO00O )+'#'#line:1418
    print ("Your encrypted message is: ",O000OOOOOOO000O00 )#line:1419
    return O000OOOOOOO000O00 #line:1420
