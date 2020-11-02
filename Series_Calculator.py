print("=" * 15, "Series_Calculator", "=" * 15)

episodes = input("How many episodes each season have:")

try:
    ep = int(episodes)
except:
    while True:
        try:
            print("Invlid Input")
            episodes = input("How many episodes each season have:")
            ep = int(episodes)
            if type(ep) is int:
                break
        except:
            pass


seasons = input("How many season the serie have:")

try:
    s = int(seasons)
except:
    while True:
        try:
            print("Invlid Input")
            seasons = input("How many season the serie have:")
            s = int(seasons)
            if type(s) is int:
                break
        except:
            pass

        
hours_pday = input("How many hours per day do you will watch:")

try:
    h = int(hours_pday)
except:
    while True:
        try:
            print("Invlid Input")
            hours_pday = input("How many hours per day do you will watch:")
            h = int(hours_pday)
            if type(h) is int:
                break
        except:
            pass

print("=" * 49)

hours = (ep * s) / h
days = hours / 24

print("It will take you:", hours, "hours")
print("It will take you:", str(days)[:3], "days")