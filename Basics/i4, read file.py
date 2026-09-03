#line 42, 68
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

    def check_speed(self, vehicle_speed):
        try:
            if not self._is_active:
                print("The radar is currently out of service.")
                return

            if vehicle_speed > self.speed_limit:
                print(f" Violation detected! Vehicle exceeding the speed limit and traveling at {vehicle_speed} km/h (Limit: {self.speed_limit} km/h)!")
                with open("violations.txt", "a") as file:
                    file.write(f"Violation: Vehicle speed was {vehicle_speed} km/h on speed limit {self.speed_limit} km/h\n")
            else:
                print(f" A car passing at a safe speed: {vehicle_speed} km/h.")

        except TypeError:
            print("Error: Invalid speed data received. Speed must be a number!")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def show_violations(self):
        try:
            print("--- Traffic Violations Report ---")
            with open("violations.txt", "r") as file:
                for line in file:
                    print(line.strip())

        except FileNotFoundError:
            print("No violations recorded yet in the database!")

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def capture_video(self):
        if self._is_active:
            print("Radar Captured a quick snapshot of the violating vehicle's license plate!")
        else:
            super().capture_video()

# cam_1 = TrafficCamera("1080", 30)
# cam_1.capture_video()
# cam_1.deactivate()
# cam_1.capture_video()
radar_1 = SpeedCamera("4K", 60, 120)
radar_1.check_speed(140)
radar_1.capture_video()

radar_1.show_violations()
