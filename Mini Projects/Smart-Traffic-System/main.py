from cameras import SpeedCamera 

radar_1 = SpeedCamera("4K", 60, 120)

radar_1.check_speed(140)

radar_1.capture_video()

radar_1.check_multiple_speeds(110, 145, 95)
