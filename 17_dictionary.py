monthConversions = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "July":"July",
}

print(monthConversions["Apr"])

print(monthConversions.get("Jun"))

print(monthConversions.get("grt","Not a validkey"))

print(monthConversions.get("Jan","Not a validkey"))

