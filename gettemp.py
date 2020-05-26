import os
import time
def gpu_temperature():
    return os.popen("vcgencmd measure_temp").readline()

def cpu_temperature():
    return os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()

def throttled():
    return os.popen("vcgencmd get_throttled").readline()

def cpu_speed_requested():
    return os.popen("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq").readline()

def cpu_speed_actual():
    return os.popen("vcgencmd measure_clock arm").readline()

while True:
    print('-------------------------')
    print('GPU temp: {}'.format(gpu_temperature()))
    print('CPU temp: {}'.format(cpu_temperature()))
    print(throttled())
    print('CPU speed requested by the kernel: {}'.format(cpu_speed_requested()))
    print('CPU speed actual: {}'.format(cpu_speed_actual()))
    time.sleep(1)
