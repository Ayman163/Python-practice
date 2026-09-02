class TrafficCamera:
    def __init__(self, resolution, fps):
        self.resolution = resolution
        self.fps = fps
        self.is_active = True

    def capture_video(self):
        if self.is_active:
            print(f"The camera now captures video at {self.resolution} resolution and {self.fps} frame/second speed.")
        else:
            print("The camera is currently not working.")

cam_1 = TrafficCamera("1080", 30)

cam_1.capture_video()

cam_1.is_active = False

cam_1.capture_video()
