{\rtf1\ansi\ansicpg936\cocoartf2709
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import random\
\
answer = random.randint(1, 100)\
max_attempts = 7\
\
print("\uc0\u27426 \u36814 \u26469 \u21040 \u29468 \u25968 \u23383 \u28216 \u25103 \u65281 ")\
print("\uc0\u25105 \u24050 \u32463 \u29983 \u25104 \u20102 \u19968 \u20010  1 \u21040  100 \u20043 \u38388 \u30340 \u25968 \u23383 \u12290 ")\
print(f"\uc0\u20320 \u26377  \{max_attempts\} \u27425 \u26426 \u20250 \u29468 \u20013 \u23427 \u12290 ")\
\
for attempt in range(1, max_attempts + 1):\
    while True:\
        try:\
            guess = int(input(f"\\n\uc0\u31532  \{attempt\} \u27425 \u29468 \u27979 \u65292 \u35831 \u36755 \u20837 \u19968 \u20010 \u25968 \u23383 \u65306 "))\
\
            if 1 <= guess <= 100:\
                break\
\
            print("\uc0\u35831 \u36755 \u20837  1 \u21040  100 \u20043 \u38388 \u30340 \u25968 \u23383 \u12290 ")\
        except ValueError:\
            print("\uc0\u36755 \u20837 \u26080 \u25928 \u65292 \u35831 \u36755 \u20837 \u25972 \u25968 \u12290 ")\
\
    if guess == answer:\
        print(f"\uc0\u24685 \u21916 \u20320 \u65292 \u29468 \u23545 \u20102 \u65281 \u31572 \u26696 \u23601 \u26159  \{answer\}\u12290 ")\
        break\
    elif guess < answer:\
        print("\uc0\u29468 \u23567 \u20102 \u65281 ")\
    else:\
        print("\uc0\u29468 \u22823 \u20102 \u65281 ")\
else:\
    print(f"\\n\uc0\u24456 \u36951 \u25022 \u65292 7 \u27425 \u26426 \u20250 \u24050 \u29992 \u23436 \u12290 \u27491 \u30830 \u31572 \u26696 \u26159  \{answer\}\u12290 ")}