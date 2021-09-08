"""Repeating a beat in a loop."""

__author__ = "730312274"


# Begin your solution here...
the_sick_beat: str = input("What beat do you want to repeat? ")
the_beat_repeat: int = int(input("How many times do you want to repeat it? "))
the_final_beat: str = the_sick_beat
n: int = 0

if the_beat_repeat > 0:
    while n < (the_beat_repeat - 1):
        n = n + 1
        the_final_beat = the_final_beat + " " + the_sick_beat
    print(the_final_beat)
else:
    print("No beat...")