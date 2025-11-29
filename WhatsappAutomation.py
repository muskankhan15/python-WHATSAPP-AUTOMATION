import pywhatkit

# Send instant message
pywhatkit.sendwhatmsg_instantly("+91XXXXXXXXXX", "hello")

# Send scheduled message at 15:32
pywhatkit.sendwhatmsg("+91XXXXXXXXXX", "hi im from vgu", 15, 32)
