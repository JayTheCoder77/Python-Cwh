# alarm clock

import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"alarm set for {alarm_time}")
    sound_file = "alarm.mp3"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time == alarm_time:
            print("wake up")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(1)
            is_running = False

if __name__ == '__main__':
    alarm_time = input("enter alarm time hr min seconds")
    set_alarm(alarm_time)