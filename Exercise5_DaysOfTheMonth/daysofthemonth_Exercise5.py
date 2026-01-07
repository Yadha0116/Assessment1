Months ={
    1: "31",
    2: "28",
    3: "31",
    4: "30",
    5: "31",
    6: "30",
    7: "31",
    8: "31",
    9: "30",
    10: "31",
    11: "30",
    12: "31"
}

question = int(input("Month number:"))

if question <= 12 and question > 0:
    print(Months[question])
else:
    print("invalid")