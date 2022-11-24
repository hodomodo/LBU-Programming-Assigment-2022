print("Park Run Timer")
print("~~~~~~~~~~~~~~")
print()
print("On your marks")
print("Get set")
print("Go!")

runners_no = []
Total_Runners = 0
Time_Val = 0
Average_Time = 0
Fastest_Time = 999999999999999
Slowest_Time = 0
Winner = 0


def convert(Seconds):
    Seconds = Seconds % (24 * 3600)
    Seconds %= 3600
    minutes = Seconds // 60
    Seconds %= 60

    return "%02d minutes, %02d seconds" % (minutes, Seconds)


while True:
    user_input = input(">")
    Time = []
    if user_input == "END":
        if not runners_no:
            print("No data found.")
        else:
            Average_Time = Average_Time / Total_Runners
            print()
            print("Total Runners:", Total_Runners)
            print("Average Time:", convert(Average_Time))
            print("Fastest Time:", convert(Fastest_Time))
            print("Slowest Time:", convert(Slowest_Time))
            print()
            print("Best Time Here: Runner", Winner)
        break
    elif user_input.isalpha() is True:
        print("Error")
    else:
        try:
            runners_no.extend(user_input.split("::"))
            Total_Runners += 1
            Time.extend(user_input.split("::"))
            Time_Val = Time[1]
            Time_Val = int(Time_Val)
            Average_Time = Average_Time + Time_Val
            Fastest_Time = int(Fastest_Time)
        except ValueError or IndexError:
            print("Error")
            try:
                if Time_Val < Fastest_Time:
                    Fastest_Time = Time[1]
                    Winner = Time[0]
                else:
                    Fastest_Time = Fastest_Time
            except ValueError or IndexError:
                print("Error")
            try:
                if Time_Val > Slowest_Time:
                    Slowest_Time = Time_Val
                else:
                    Slowest_Time = Slowest_Time
            except ValueError or IndexError:
                print("Error")
        except ValueError or IndexError:
            print("Error")
# Add validation checking it is in xx::xx format. Also ignore inputs other than end. Maybe change current else into elif and new else for any incorrect inputs.
