from onvif import ONVIFCamera
mycam = ONVIFCamera('192.168.1.102', 6688, 'admin', '87651234')#, '/etc/onvif/wsdl/')
#media_service = mycam.create_media_service()
#print(media_service)

# Get Hostname
resp = mycam.devicemgmt.GetHostname()
print('My camera`s hostname: ' + str(resp.Name))

# Get system date and time
dt = mycam.devicemgmt.GetSystemDateAndTime()
tz = dt.TimeZone
year = dt.UTCDateTime.Date.Year
hour = dt.UTCDateTime.Time.Hour

#http://192.168.1.101:6688/onvif/device_service
#640x360: rtsp://admin:87651234@192.168.1.101:8554/profile1
#2304x1296: rtsp://admin:87651234@192.168.1.101:8554/profile0
