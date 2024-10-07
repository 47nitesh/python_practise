monthconversions={
    "Jan":"January",
    "Feb":"Februrary",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "oct":"October",
    "Nov":"November",
    "Dec":"December",
}
print(monthconversions.get("Jan"))
print(monthconversions.items())
monthconversions["Year"]=2024
print(monthconversions.items())
if "Jan" in monthconversions:
    print("yes","Jan exists")
else:
    print("Invalid key")
for  x in monthconversions.items() :
    print(x)
for x,y in monthconversions.items():
    print(x,y)