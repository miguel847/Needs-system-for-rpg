import sys
import time
import pyperclip

def lines():
      print("------------------------------------------------------")



# Ask what is the consumption per hour
lines()
needs = float(input("Whats is the consumption, per hour"))
lines()

# Ask how many minutes have passed?
minuts = int(input("how many minutes have passed?"))
lines()

# Ask what is the actual need
actual_needs = float(input("whats is the actual need"))
lines()

# Divide the consumption per hour by 60
needs_per_minute = needs/60

#Use the needs per minute value to discover how much will be consumed in that time
consumption = needs_per_minute*minuts

#Take the current need and subtract consumption to get the final value
end_valor = actual_needs - consumption

print("the final need is {:.1f}".format(end_valor))
lines()
pyperclip.copy(end_valor)

e = input("want to exit??? [Y,N]")
if e == "S":
      sys.exit()
elif e == "N":
      time.sleep(10)


