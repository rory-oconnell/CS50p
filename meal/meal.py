def main():
    temporal = input("What time is it? ")
    temporal = convert(temporal)
    if temporal >= 7 and temporal <= 8:
        print("breakfast time")
    elif temporal >= 12 and temporal <= 13:
        print("lunch time")
    elif temporal >= 18 and temporal <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    temporal = float(hours) + (float(minutes) / 60)
    return temporal

if __name__ == "__main__":
    main()

# breakfast between 7:00 and 8:00,
# lunch between 12:00 and 13:00,
# and dinner between 18:00 and 19:00.