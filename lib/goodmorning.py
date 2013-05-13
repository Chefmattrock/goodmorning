#!/usr/bin/env python

"""Good morning Mr Stein. You asked me to wake you up today at 8:00.  It's currently a lovely day, """

import pyttsx, datetime, time

def run():
    now = getTime()
    greeting = properGreeting(now)
    print greeting
    engine = pyttsx.init()
    engine.setProperty('rate', 160)
    engine.say("Good")
    engine.say(greeting)
    engine.say("mister stein")
    engine.runAndWait()

    
def properGreeting(time):
    if int(time[0:2]) < 12:
	greeting = 'morning'
    elif int(time[0:2]) < 17:
	greeting = 'afternoon'
    else:
	greeting = 'evening'
    return greeting

def getTime():
   now = datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M')
   return now

if __name__ == '__main__':
    run()
