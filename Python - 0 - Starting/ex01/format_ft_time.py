import time

seconds_since_epoch = time.time()

print(f"Seconds since January 1, 1970: {seconds_since_epoch:,.4f} \
or {seconds_since_epoch:.2e} in scientific notation")

print(time.strftime("%b %d %Y", time.localtime(seconds_since_epoch)))
