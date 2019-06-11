

def speed_of_time(acceleration, run_speed, time_sec=1):
    while (acceleration + run_speed) < 340:
        result = 1
        for sec in range(340 // (acceleration + run_speed)):
            result = result * acceleration
            time_sec += 1
        return time_sec



print(speed_of_time(2, 4))