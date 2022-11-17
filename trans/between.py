from time import sleep

import translators as ts
from googletrans import Translator
from listen import *
from speak import *

while True:
    en_speak('how are you?')
    bn_speak('আপনি কেমন আছেন')
    hi_speak('आप कैसे हैं')
    ar_speak('كيف حالك؟')
