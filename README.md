This repo documents efforts to reverse engineer the P11 Smartwatch.

[AliExpress link](https://vi.aliexpress.com/i/4001115214370.html?gatewayAdapt=glo2vnm)

# Specs
The watch has the following sensors:

 - Accelerometer (step counting)
 - PPG (heart rate, blood pressure?
 - EKG (electrodes)

It has a colour TFT display


# Mobile Apps

The official app is HealthWare ([google play](https://play.google.com/store/apps/details?id=com.yucheng.HealthWear), [manufacturer link](https://staticpage.ycaviation.com/app/smart/app_download.html?apkname=HealthWear), [mirror](https://cdn.tahnok.ca/u/HealthWear.apk))

There is also another app I found mentioned called MeCare. Unclear what it's relationship is.

# Bluetooth Protocol

GATT services:

 - `be940000-7333-be46-b7ae-689e71722bd5`: this is the primary I think
 - `0x1801`
 - `0x180D`: Heart Rate from bluetooth spec
 - `0x180F`: Battery
 - `0x180A`: (device info?)
 - `6e400001-b5a3-f393-e0a9-e50e24dcca9e`: Nordic UART Service (NUS)
 - `0xFE59`: Unknown
 - `0xFEE7`: Unknown
