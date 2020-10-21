from picamera import PiCamera

class scancamera(object):
    """
    This class handle the picamera
    """
    camera = PiCamera()
    camera.resolution = (160,160)
    #print("creating object")

    def set_scan_pic(self):
        self.camera.vflip=True
        #self.camera.resolution = (640,480)
        self.camera.resolution = (160,160)
        #self.camera.resolution = (2592,1944)
        #self.camera.resolution = (3280,2464  )
    
    #def open():
    #    camera.start_preview()

    def hflip(self):
        self.camera.hflip=True

    def vflip(self, val=True):
        self.camera.vflip=val

    def capture_stream(self, stream, type='jpeg'):
        self.camera.capture(stream, format=type, use_video_port=True)

    def capture_file(self, file):
        self.camera.capture(file, use_video_port=True)

    def close(self):
        self.camera.close()

    def start_preview(self):
        self.camera.start_preview(fullscreen=False, window=(1100,10,800,400))

    def stop_preview(self):
        self.camera.stop_preview()

    def color_effects(self, tuple):
        self.camera.color_effects = tuple

    def resolution(self, tuple):
        self.camera.resolution = tuple

    def info(self):
        print(" -- exposure --")
        print("Gain (Analog,Digital): ", self.camera.analog_gain, self.camera.digital_gain, end=" ")
        print("Brightness: ", self.camera.brightness, end=" ")
        print("Contrast: ", self.camera.contrast)
        print("Shutter speed: ", self.camera.shutter_speed)
        print("Awb gain: ", self.camera.awb_gains)

    def settings(self):
        print("****** settings *******")
        print("Resolution: ", self.camera.resolution)
        print("Framerate (high,low): ", self.camera.framerate_range, end=" ")
        print("Framerate: ", self.camera.framerate)
        print("Awb mode: ", self.camera.awb_mode)
        print("Exposure mode: ", self.camera.exposure_mode)
        print("Exposure speed: ", self.camera.exposure_speed)
        print("ISO: ", self.camera.iso)
        print("Saturation: ", self.camera.saturation)
        print("Sensor Mode: ", self.camera.sensor_mode)
        print("Sharpness: ", self.camera.sharpness)
        print("Zoom: ", self.camera.zoom)
