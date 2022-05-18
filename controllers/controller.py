import sys
sys.path.insert(0, "..")
from gesture_liblary.camera import Camera
from controllers.camera_controller import CameraController
import threading
class Controller():
    def __init__(self,function_getter,sys_controller,win):
        self.camera_controller = CameraController(win)
        self.system_controller= sys_controller
        self.camera = Camera(function_getter,sys_controller,self.camera_controller)
        self.started = False
    def start_gesture_recognition(self):
        if self.started is False:
            self.started = True
            self.t=threading.Thread(name='daemon',target=self.camera.start_windows_gesture_library)
            self.t.start()
            print("Handy started")

    def stop_gesture_recognition(self):
        if self.started is True:
            self.system_controller.stop_mouse()
            self.camera.stop_gesture_recognition()
            self.t.join()
            self.started=False
            print("Handy stopped")
    def get_camera_controller(self):
        return self.camera_controller