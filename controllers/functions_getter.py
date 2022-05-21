import sys
sys.path.insert(0, "..")
import user_scripts
import time
class FunctionsGetter():

    def __init__(self, controller):
        self.time_before = time.time()
        self.u_scripts=user_scripts
        self.controller = controller
        self.controller.set_reference(self)
        self.u_dict = self.u_scripts.get_functions()
        self.dct={"minimize_window": self.controller.minimize_window ,
            "maximize_window": self.controller.maximize_window ,
            "close_window": self.controller.close_window ,
            "scroll_up": self.controller.scroll_up ,
            "scroll_down": self.controller.scroll_down ,
            "windows_volume_up": self.controller.windows_volume_up ,
            "windows_volume_down": self.controller.windows_volume_down ,
            "zoom_in": self.controller.zoom_in ,
            "zoom_out": self.controller.zoom_out ,
            "brightness_up": self.controller.brightness_up ,
            "brightness_down": self.controller.brightness_down ,
            "scroll_right": self.controller.scroll_right ,
            "scroll_left": self.controller.scroll_left ,
            "switch_window": self.controller.switch_window ,
            "mouse_start": self.controller.mouse_start
        }
        self.dct = {**self.dct, **self.u_dict}
    def set_time_before(self):
        self.time_before=time.time()

    def call_function(self,name):
        self.time_now = time.time()
        if self.time_now - self.time_before >1.90:
            self.time_before= self.time_now
            for key in self.dct.keys():
                if name==key:
                    func=self.dct.get(key)
                    try:
                     func()
                    except:
                        return False
                    return True
            return False
        else:
            return False
    def get_all_functions_names(self):
        return self.dct.keys()


