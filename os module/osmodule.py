import os

if not os.path.exists("man"):
    os.mkdir("man")   # Create 'data' directory if it doesn't exist

for y in range(0, 100):
    os.mkdir(f"man/Day{y+1}")  # Create a directory named 'Day2' to 'Day100' inside 'data'
#     os.rmdir(f"man/Day{y+1}")  # Remove the directory immediately after creation
#     os.rename(f"man/Day{y+1}", f"man/Tutorial{y+1}")  # Attempt to rename the directory (not executed properly in the original script)
#
# # debug
