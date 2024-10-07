import os

for y in range(0, 100):
    os.rename(f"man/Day{y+1}", f"man/Tutorial{y+1}")

# debug
