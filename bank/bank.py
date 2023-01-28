Greeting = input("Greeting: ").strip().lower()
if Greeting.startswith("h"):
    if Greeting.startswith("hello"):
        print("$0")
    else: print("$20")
else: 
    print("$100")