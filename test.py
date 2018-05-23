#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import re
regexp = re.compile(r':\b', re.UNICODE)
statia='''Алсынбаев, ???????Н. З. Й2йге селл2: повестар / Н. Алсынбаев. - )ф0: Китап, 2014. – 160 бит. 
Нияз Алсынбаевты8 «Й2йге селл2» повесында 316 арабы66а й0р01се замандаштарыбы6, улар6ы8 уй-фекер62ре, эш-42м2лд2ре, й24ни бе66е8 32р беребе6 тура3ында бара. Йыйынты77а инг2н баш7а 2с2р62р62 л2 32р кем 16ен таныр.
'''

statia = re.sub(r'1', 'ү',statia)	
statia = re.sub(r'!', 'Ү',statia)	
statia = re.sub(r'2', 'ә',statia)	
statia = re.sub(r'"', 'Ә',statia)	
statia = re.sub(r'3', 'һ',statia)	
statia = re.sub(r'№', 'Һ',statia)	
statia = re.sub(r'4', 'ғ',statia)	
statia = re.sub(r';', 'Ғ',statia)	
statia = re.sub(r'5', 'ҫ',statia)	
statia = re.sub(r'%', 'Ҫ',statia)	
statia = re.sub(r'6', 'ҙ',statia)	
statia = regexp.sub('Ҙ',statia) 	
statia = re.sub(r'7', 'ҡ',statia)	
statia = re.sub(r"\?", 'Ҡ',statia)	
statia = re.sub(r'8', 'ң',statia)	
statia = re.sub(r'\*', 'Ң',statia)	
statia = re.sub(r'9', 'ҫ',statia)	
statia = re.sub(r"\(", 'Ҫ',statia)	
statia = re.sub(r'0', 'ө',statia)	
statia = re.sub(r'\)', 'Ө',statia)	


print statia


#result = re.sub(r':\b', 'BASHSTR',A)

