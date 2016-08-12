import time
from machine import Pin, PWM

defaultDuty = 300
rate = 2000

pwm = PWM(Pin(0), freq=0, duty=defaultDuty)

freq = {
    '.' : 0, '-' : 0,
    'c1': 32, 'c2': 55, 'c3': 130, 'c4': 261, 'c5': 523,
    '#c1': 34, '#c2': 69, '#c3': 138, '#c4': 277, '#c5': 554,
    'd1': 36, 'd2': 73, 'd3': 146, 'd4': 293, 'd5': 554,
    '#d1': 38, '#d2': 77, '#d3': 155, '#d4': 311, '#d5': 622,
    'e1': 41, 'e2': 82, 'e3': 164, 'e4': 329, 'e5': 659,
    'f1': 43, 'f2': 87, 'f3': 174, 'f4': 349, 'f5': 698,
    '#f1': 46, '#f2': 92, '#f3': 185, '#f4': 370, '#f5': 740,
    'g1': 49, 'g2': 98, 'g3': 196, 'g4': 392, 'g5': 784,
    '#g1': 51, '#g2': 103, '#g3': 207, '#g4': 415, '#g5': 830,
    'a1': 55, 'a2': 110, 'a3': 220, 'a4' : 440, 'a5': 880,
    '#a1': 58, '#a2': 116, '#a3': 233, '#a4' : 466, '#a5': 932,
    'b1': 61, 'b2': 123, 'b3': 246, 'b4' : 493, 'b5': 987
}

def setTempo(n):
    global rate
    rate = 24*n

def playOne(note, duration):
    if (note not in freq):
        return
    pwm.freq(freq[note])
    if freq[note] == 0:
        pwm.duty(0)
    else:
        pwm.duty(defaultDuty)
    time.sleep_ms(int(rate/duration))

# Play Nokia Melody http://nokia.nigelcoldwell.co.uk
def playNokia(s,octaveOffset = 1):
    for c in s.split(" "):
        if '0' <= c[1] <= '9':
            duration = int(c[0:2])
            note = c[2::]
        else:
            duration = int(c[0])
            note = c[1::]
        if note != '-':
            note = note[:-1] + str(int(note[-1]) + octaveOffset)
        playOne(note, duration)
    playOne(".", duration)

def stop():
    playOne('-', 1)

#Play Nokia Forever
def pnf(s,octaveOffset = 1, tempo=None):
    if tempo is not None:
        setTempo(tempo)
    while True:
        try:
            playNokia(s,octaveOffset)
        finally:
            stop()

def playStarWars():
    pnf("8#c1 8#c1 16#c1 2#f1 2#c2 8b1 16#a1 8#g1 2#f2 4#c2 8b1 16#a1 8#g1 2#f2 4#c2 8b1 16#a1 8b1 2#g1 8#c1 8#c1 16#c1 2#f1 2#c2 8b1 16#a1 8#g1 2#f2 4#c2 8b1 16#a1 8#g1 2#f2 4#c2 8b1 16#a1 8b1 2#g1 4#c1 16#c1 2#d1 8#c2 8b1 8#a1 8#g1 8#f1 16#f1 8#g1 16#a1 4#g1", tempo=100)("8#c1 8#c1 16#c1 2#f1 2#c2 8b1 16#a1 8#g1 2#f2 4#c2 8b1 16#a1 8#g1 2#f2 4#c2 8b1 16#a1 8b1 2#g1 8#c1 8#c1 16#c1 2#f1 2#c2 8b1 16#a1 8#g1 2#f2 4#c2 8b1 16#a1 8#g1 2#f2 4#c2 8b1 16#a1 8b1 2#g1 4#c1 16#c1 2#d1 8#c2 8b1 8#a1 8#g1 8#f1 16#f1 8#g1 16#a1 4#g1", tempo=100)
