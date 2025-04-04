from parser import parse_features, parse_device_info


def test_parse_features():
    expected = {
        "ALARMCOUNT": 10,
        "HAS_ANTILOST": 1,
        "HAS_APPOINT": 0,
        "HAS_BADMINTON": 0,
        "HAS_BASKETBALL": 0,
        "HAS_BLOOD": 1,
        "HAS_BLOODALARM": 0,
        "HAS_BLOODLEVEL": 1,
        "HAS_BLOODOXYGEN": 1,
        "HAS_BLOODOXYGENALARM": 0,
        "HAS_BLOODPRESSURECALIBRATION": 1,
        "HAS_BLOODSUGAR": 1,
        "HAS_BUSINESSCARD": 0,
        "HAS_CALLPHONE": 1,
        "HAS_CONTACTS": 0,
        "HAS_CUSTOM": 0,
        "HAS_CUSTOMDIAL": 0,
        "HAS_CVRR": 0,
        "HAS_DIAL": 0,
        "HAS_DRINKWATERREMINDER": 0,
        "HAS_ECGDIAGNOSIS": 1,
        "HAS_ECGHISTORYUPLOAD": 0,
        "HAS_ECGREALUPLOAD": 1,
        "HAS_ECGRIGHTELECTRODE": 1,
        "HAS_EMAIL": 1,
        "HAS_ENCRYPTION": 0,
        "HAS_FACEBOOK": 1,
        "HAS_FACTORYSETTING": 1,
        "HAS_FEMALEPHYSIOLOGICALCYCLE": 0,
        "HAS_FINDDEVICE": 1,
        "HAS_FINDPHONE": 0,
        "HAS_FIRMWAREUPDATE": 1,
        "HAS_FITNESS": 1,
        "HAS_FOOTBALL": 0,
        "HAS_GETUP": 0,
        "HAS_HEARTALARM": 1,
        "HAS_HEARTRATE": 1,
        "HAS_HRV": 0,
        "HAS_INACCURATEECG": 0,
        "HAS_INDOORRIDING": 0,
        "HAS_INDOORRUNING": 0,
        "HAS_INDOORWALKING": 0,
        "HAS_INFLATED": 0,
        "HAS_INFORMATION": 1,
        "HAS_INSTAGRAM": 1,
        "HAS_JUMPING": 0,
        "HAS_KINDSINFORMATIONPUSH": 0,
        "HAS_LIFTBRIGHT": 1,
        "HAS_LINE": 1,
        "HAS_LINKEDIN": 1,
        "HAS_LONGSITTING": 1,
        "HAS_MANUALTAKEPHOTO": 0,
        "HAS_MANYLANGUAGE": 1,
        "HAS_MEETING": 0,
        "HAS_MESSAGE": 1,
        "HAS_MESSENGER": 1,
        "HAS_MORESPORT": 1,
        "HAS_MOUNTAINCLIMBING": 0,
        "HAS_MUSIC": 0,
        "HAS_NOTITOGGLE": 1,
        "HAS_OTHERMESSENGER": 1,
        "HAS_OTHRENOTIFY": 0,
        "HAS_OUTDOORRUNING": 0,
        "HAS_OUTDOORWALKING": 0,
        "HAS_PARTY": 0,
        "HAS_PAUSEEXERCISE": 0,
        "HAS_PHONESUPPORT": 0,
        "HAS_PINGPONG": 0,
        "HAS_QQ": 1,
        "HAS_REALDATA": 1,
        "HAS_REALEXERCISEDATA": 0,
        "HAS_REALTIMEMONITORINGMODE": 0,
        "HAS_RESPIRATORYRATE": 1,
        "HAS_RIDING": 1,
        "HAS_ROPESKIPPING": 0,
        "HAS_ROWINGMACHINE": 0,
        "HAS_RUNNING": 1,
        "HAS_SEARCHAROUND": 0,
        "HAS_SETINFO": 0,
        "HAS_SETSCREENTIME": 0,
        "HAS_SHAKETAKEPHOTO": 0,
        "HAS_SINA": 1,
        "HAS_SITUPS": 0,
        "HAS_SKINCOLOR": 1,
        "HAS_SKYPE": 1,
        "HAS_SLEEP": 1,
        "HAS_SNAPCHAT": 1,
        "HAS_SOS": 0,
        "HAS_STEPCOUNT": 1,
        "HAS_STEPPER": 0,
        "HAS_SWIMMING": 0,
        "HAS_TAKEEXERCISE": 0,
        "HAS_TAKEPILLS": 0,
        "HAS_TAKESLEEP": 0,
        "HAS_TEMP": 1,
        "HAS_TEMPALARM": 1,
        "HAS_TEMPAXILLARYTEST": 1,
        "HAS_TEMPCALIBRATION": 1,
        "HAS_TESTBLOOD": 0,
        "HAS_TESTRESPIRATIONRATE": 0,
        "HAS_TESTSPO2": 0,
        "HAS_TESTTEMP": 0,
        "HAS_THEME": 1,
        "HAS_TODAYWEATHER": 1,
        "HAS_TOMORROWWEATHER": 0,
        "HAS_TWITTER": 1,
        "HAS_UPLOADINFLATEBLOOD": 0,
        "HAS_URICACIDMEASUREMENT": 0,
        "HAS_VIBERNOTIFY": 0,
        "HAS_VIBRATIONINTENSITY": 0,
        "HAS_WALKING": 0,
        "HAS_WATCHSCREENBRIGHTNESS": 0,
        "HAS_WECHAT": 1,
        "HAS_WECHATSPORT": 1,
        "HAS_WEIGHTTRAINING": 0,
        "HAS_WHATSAPP": 1,
        "HAS_YOGA": 0,
        "ISFLIPDIALIMAGE": 0,
        "ISHATESTHEART": 0,
        "WATCHSCREENBRIGHTNESS": 0,
    }
    assert (
        parse_features(
            bytearray(
                b"\xff\xad\n\x00\xff\xff\xdf\xd4\xdd\x01\x00\xe0\xb6\x00\x00\x00\x00\x08"
            )
        )
        == expected
    )


def test_parse_device_info():
    raw = bytearray.fromhex("75000601005b000100030000000001000000000008000000")

    expected = {
        "deviceId": 117,
        "deviceVersion": "1.6",
        "deviceBatteryState": 0,
        "deviceBatteryValue": 91,
        "deviceMainVersion": 1,
        "deviceSubVersion": 6,
        "devicetBindState": 0,
        "devicetSyncState": 1,
        "bleAgreementSubVersion": 0,
        "bleAgreementMainVersion": 3,
        "bloodAlgoSubVersion": 0,
        "bloodAlgoMainVersion": 0,
        "tpSubVersion": 0,
        "tpMainVersion": 0,
        "bloodSugarSubVersion": 1,
        "bloodSugarMainVersion": 0,
        "uiSubVersion": 0,
        "uiMainVersion": 0,
        "hardwareType": 0,
    }

    assert parse_device_info(raw) == expected
