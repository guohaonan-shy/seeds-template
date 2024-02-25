def convertMonth(month: str):
    if month == "January":
        return "01"
    elif month == "February":
        return "02"
    elif month == "March":
        return "03"
    elif month == "April":
        return "04"
    elif month == "May":
        return "05"
    elif month == "June":
        return "06"
    elif month == "July":
        return "07"
    elif month == "August":
        return "08"
    elif month == "September":
        return "09"
    elif month == "October":
        return "10"
    elif month == "November":
        return "11"
    else:
        return "12"


def convertDay(day: str):
    value = 0
    for byte in day:
        if 0 <= ord(byte) - ord('0') <= 9:
            value = value * 10 + ord(byte)-ord('0')
    if value < 10:
        return "0"+str(value)
    return str(value)
