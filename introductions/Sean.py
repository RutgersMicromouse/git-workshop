import time
import random

def introduce():
    print("Booting up Sean.exe ...")
    time.sleep(1)
    print("Loading personality modules...")
    time.sleep(0.5)
    bars = ["█", "██", "███", "████", "█████", "██████", "███████", "████████", "█████████", "██████████"]
    for i in range(1, 11):
        print(f"{bars[i-1]}\t{i*10}% complete...")
        time.sleep(0.25)
    print("System check: OK")
    time.sleep(0.5)
    print("Activating ... ")
    time.sleep(0.5)
    print("All systems operational!")
    time.sleep(0.5)
    print()
    
    print("Hey everyone! I'm Sean — a gamer, hiker, traveler.")
    time.sleep(0.5)
    print("If there’s good scenery or good food, I’m already halfway there")
    time.sleep(0.5)
    print("I love exploring new trails, cities, and occasionally… the fridge at 2AM ")
    time.sleep(0.5)
    print("When I’m not out and about, you’ll find me gaming — probably losing. ")
    time.sleep(0.5)
    print("I’m always down to try new stuff — places, games, or cuisines.")
    time.sleep(0.5)
if __name__ == "__main__":
    introduce()



