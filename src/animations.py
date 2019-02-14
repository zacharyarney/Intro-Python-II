import time
from functions import clear

splash = [
'''         
        ''',
'''         
        ''',
'''         
        ''',
'''         
        ''',
'''         
        ''',
'''         
A        ''',
'''         
AD       ''',
'''         
ADV      ''',
'''         
ADVE     ''',
'''         
ADVEN    ''',
'''     C   
ADVENT   ''',
'''     CA  
ADVENTU  ''',
'''     CAV 
ADVENTUR ''',
'''     CAVE
ADVENTURE''',
'''     CAVE
 DVENTURE''',
'''     CAVE
A VENTURE''',
'''     CAVE
AD ENTURE''',
'''     CAVE
ADV NTURE''',
'''     CAVE
ADVE TURE''',
'''      AVE
ADVEN URE''',
'''     C VE
ADVENT RE''',
'''     CA E
ADVENTU E''',
'''     CAV 
ADVENTUR ''',
'''     CAVE
ADVENTURE''',
'''     
         ''',
'''     CAVE
ADVENTURE''',
'''     
         ''',
'''     CAVE
ADVENTURE''',
'''     
         ''',
'''     CAVE
ADVENTURE''',
]

walk = [
'''
''',
'''o<>
''',
'''o<>
   o<>''',
'''      o<>
   o<>''',
'''      o<>
         o<>''',
'''
''',
'''o<>
         ''',
'''o<>
   o<>''',
'''      o<>
   o<>''',
'''      o<>
         o<>''',
'''
'''
]

def fast_animation(animation):
    clear()
    for i in range(len(animation)):
        print(animation[i])
        time.sleep(0.2)
        if i == len(animation) - 1:
            time.sleep(1.5)
            clear()
        else:
            clear()

def slow_animation(animation):
    clear()
    for i in range(len(animation)):
        print(animation[i])
        time.sleep(0.4)
        clear()