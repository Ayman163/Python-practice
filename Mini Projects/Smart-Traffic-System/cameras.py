import json 
import sqlite3

class TrafficCamera:
    def __init__(self, resolution, fps):
        self.resolution = resolution
        self.fps = fps
        self._is_active = True

    def capture_video(self):
        if self._is_active:
            print(f"The camera now captures video at {self.resolution} resolution and {self.fps} frame/second speed.")
        else:
            print("The camera is currently not working.")

    def deactivate(self):
        self._is_active = False
        print("The camera was safely disabled via the central system.")

class SpeedCamera(TrafficCamera):
    def __init__(self, resolution, fps, speed_limit):
        super().__init__(resolution, fps)
        self.speed_limit = speed_limit

    def check_speed(self, vehicle_speed, **details):

        

        try:
            if not self._is_active:
                print("The radar is currently out of service.")
                return

            if vehicle_speed > self.speed_limit:
                print(f"Violation detected! Vehicle traveling at {vehicle_speed} km/h!")
                
                violation_entry = {
                    "speed_detected": vehicle_speed,
                    "road_limit": self.speed_limit
                }

                violation_entry.update(details)

                conn = sqlite3.connect("traffic_system.db")
                cursor = conn.cursor()
                
                cursor.execute("INSERT INTO violations (speed, speed_limit) VALUES (?, ?)", (vehicle_speed, self.speed_limit))
                conn.commit()
                conn.close()
                print("Violation recorded successfully in SQL Database!")
                    
            else:
                print(f"A car passing at a safe speed: {vehicle_speed} km/h.")

        except TypeError:
            print("Error: Invalid speed data received. Speed must be a number!")

    def check_multiple_speeds(self, *speeds):

        print(f"--- Processing a batch of {len(speeds)} vehicles---")

        for speed in speeds:
            self.check_speed(speed)
