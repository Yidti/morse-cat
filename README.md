# Morse Cat
Morse Cat is a Python script which translate between [Morse code](http://en.wikipedia.org/wiki/Morse_code)
and basic Latin letters(A through Z) and Arabic numbers.

## Run the script
```sh
git clone https://github.com/Yidti/morse-cat.git
cd morse-cat
python3.10 main.py
```

## Examples for encoding
```console
-------------- Start --------------
Type encode(0) or decode(1) for Morse code? blank to quit. (0/1): 0
-------------- Encode --------------
Please enter any words for encoding to Morse code: sos
Content of original message: ['SOS']
Content of word_1: ['S', 'O', 'S']
Convert to Morse Code: ['...', '---', '...']
Encode string for Morse code: ... --- ...
Enter blank to try again... 
```

## Examples for decoding
```console
-------------- Start --------------
Type encode(0) or decode(1) for Morse code? blank to quit. (0/1): 1
-------------- Decode --------------
Please enter any Morse Code for decoding: ... --- ...
Content of original message: ['... --- ...']
Content of word_1: ['...', '---', '...']
Convert to Text: ['S', 'O', 'S']
Decode string for Morse code: SOS
Enter blank to try again... 
```


## Introduction - [Morse code](http://en.wikipedia.org/wiki/Morse_code) 
1. 摩斯密碼是電信通話使用的一種方法，將文本字符編碼成兩種不同信號長度的標準化序列，信號稱為點號與破折號 (dots and dashes or dits and dahs)。
2. 國際摩斯密碼對26個基本拉丁字母(a through z)、一個重音拉丁字母(é)、阿拉伯數字與一小組標點符號與程序符號(prosigns)進行編碼，沒有大小寫字母的區別。
3. 每個摩斯密碼都由一連串dits與dahs所組成，以時間量測，dit持續長度是基本單位，dah的持續時間是dit的三倍。每個編碼字元內的dit or dah都會伴隨著一段訊號空白(時間等於bit長度)，字元間是由時間長度為3個bit空白來區隔，單詞間是由時間長度為7個bit空白來區隔。


## Version History
### V.1.0 - 2022.06.01
  1. encoding and decoding for Morse Code with multiple words.
  2. only support basic-latin letters and arabic_numbers.
  3. allow to change symbol of dit and dah and space.
