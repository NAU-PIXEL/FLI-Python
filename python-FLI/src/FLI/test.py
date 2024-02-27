import ctypes
import lib
import camera

dll = lib.FLILibrary.getDll(debug=True)

dom = lib.flidomain_t(lib.FLIDOMAIN_USB | lib.FLIDEVICE_CAMERA)
ls = ctypes.POINTER(ctypes.c_char_p)()
dll.FLIList(dom,ls)

cams = camera.USBCamera.find_devices()
cam0 = cams[0]
print("info:", cam0.get_info())
print("image size:", cam0.get_image_size())
print("temperature:", cam0.get_temperature())
print("mode:", cam0.get_camera_mode_string())
cam0.set_image_binning(2,2)
# cam0.set_bitdepth("16bit") #this should generate a warning for any USB camera in libfli-1.104
cam0.set_exposure(5)
cam0._libfli.FLIControlShutter(cam0._dev, lib.FLI_SHUTTER_OPEN)
img = cam0.take_photo()
cam0._libfli.FLIControlShutter(cam0._dev, lib.FLI_SHUTTER_CLOSE)

print(img)