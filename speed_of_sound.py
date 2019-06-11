

def speed_of_time(acceleration, run_speed):
    while (acceleration + run_speed) < 340:
       for sec in range(340 // (acceleration + run_speed)):
            acceleration = acceleration * 2
    else:
        return print(sec)

print(speed_of_time(2, 4))