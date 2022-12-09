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
        if Total_Runners == 0:
            print("No data found.")
        elif Total_Runners > 0:
            try:
                Average_Time = Average_Time / Total_Runners
                print()
                print("Total Runners:", Total_Runners)
                print("Average Time:", convert(Average_Time))
                print("Fastest Time:", convert(Fastest_Time))
                print("Slowest Time:", convert(Slowest_Time))
                print()
                print("Best Time Here: Runner", Winner)
            except ZeroDivisionError or ValueError or IndexError or TypeError:
                print("Error, No data to analyse")
                continue
        break
    elif user_input.isalpha() is True:
        print("Error")
    else:
        try:
            runners_no_check = []
            runners_no_check.extend(user_input.split("::"))
            if runners_no_check[0] not in runners_no:
                runners_no.extend(user_input.split("::"))
                Time.extend(user_input.split("::"))
                try:
                    Time_Val = Time[1]
                except:
                    print("Error")
                    continue
                Time_Val = int(Time_Val)
                Total_Runners += 1
                Average_Time = Average_Time + Time_Val
                Slowest_Time = int(Slowest_Time)
                try:
                    if Time_Val < Fastest_Time or Fastest_Time == 0:
                        Fastest_Time = Time[1]
                        Winner = Time[0]
                        Fastest_Time = int(Fastest_Time)
                    else:
                        pass
                    if Time_Val > Slowest_Time or Slowest_Time == 0:
                        Slowest_Time = Time[1]
                        Slowest_Time = int(Slowest_Time)
                    else:
                        continue
                except ValueError or IndexError or TypeError:
                    print("Error")
                    continue
            else:
                print("Error, duplicate runner Number")
                continue
        except ValueError or IndexError or TypeError:
            print("Error")
            continue
