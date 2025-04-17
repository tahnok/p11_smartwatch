from dataclasses import dataclass


def parse_features(bArr: bytearray):
    # Initialize an empty dictionary to store the values
    features = {}

    # Process the first byte (bArr[0])
    features["HAS_STEPCOUNT"] = (bArr[0] >> 7) & 1
    features["HAS_SLEEP"] = (bArr[0] >> 6) & 1
    features["HAS_REALDATA"] = (bArr[0] >> 5) & 1
    features["HAS_FIRMWAREUPDATE"] = (bArr[0] >> 4) & 1
    features["HAS_HEARTRATE"] = (bArr[0] >> 3) & 1
    features["HAS_INFORMATION"] = (bArr[0] >> 2) & 1
    features["HAS_MANYLANGUAGE"] = (bArr[0] >> 1) & 1
    features["HAS_BLOOD"] = bArr[0] & 1

    # Process the second byte (bArr[1])
    features["HAS_HEARTALARM"] = (bArr[1] >> 7) & 1
    features["HAS_BLOODALARM"] = (bArr[1] >> 6) & 1
    features["HAS_ECGREALUPLOAD"] = (bArr[1] >> 5) & 1
    features["HAS_ECGHISTORYUPLOAD"] = (bArr[1] >> 4) & 1
    features["HAS_BLOODOXYGEN"] = (bArr[1] >> 3) & 1
    features["HAS_RESPIRATORYRATE"] = (bArr[1] >> 2) & 1
    features["HAS_HRV"] = (bArr[1] >> 1) & 1
    features["HAS_MORESPORT"] = bArr[1] & 1

    # Process the third byte (bArr[2])
    features["ALARMCOUNT"] = bArr[2] & 255

    # Process the fourth byte (bArr[3])
    features["HAS_CUSTOM"] = (bArr[3] >> 7) & 1
    features["HAS_MEETING"] = (bArr[3] >> 6) & 1
    features["HAS_PARTY"] = (bArr[3] >> 5) & 1
    features["HAS_APPOINT"] = (bArr[3] >> 4) & 1
    features["HAS_TAKEPILLS"] = (bArr[3] >> 3) & 1
    features["HAS_TAKEEXERCISE"] = (bArr[3] >> 2) & 1
    features["HAS_TAKESLEEP"] = (bArr[3] >> 1) & 1
    features["HAS_GETUP"] = bArr[3] & 1

    # Process the fifth byte (bArr[4])
    features["HAS_CALLPHONE"] = (bArr[4] >> 7) & 1
    features["HAS_MESSAGE"] = (bArr[4] >> 6) & 1
    features["HAS_EMAIL"] = (bArr[4] >> 5) & 1
    features["HAS_QQ"] = (bArr[4] >> 4) & 1
    features["HAS_WECHAT"] = (bArr[4] >> 3) & 1
    features["HAS_SINA"] = (bArr[4] >> 2) & 1
    features["HAS_FACEBOOK"] = (bArr[4] >> 1) & 1
    features["HAS_TWITTER"] = bArr[4] & 1

    # Process the sixth byte (bArr[5])
    features["HAS_WHATSAPP"] = (bArr[5] >> 7) & 1
    features["HAS_MESSENGER"] = (bArr[5] >> 6) & 1
    features["HAS_INSTAGRAM"] = (bArr[5] >> 5) & 1
    features["HAS_LINKEDIN"] = (bArr[5] >> 4) & 1
    features["HAS_LINE"] = (bArr[5] >> 3) & 1
    features["HAS_SNAPCHAT"] = (bArr[5] >> 2) & 1
    features["HAS_SKYPE"] = (bArr[5] >> 1) & 1
    features["HAS_OTHERMESSENGER"] = bArr[5] & 1

    # Process the seventh byte (bArr[6])
    features["HAS_LONGSITTING"] = (bArr[6] >> 7) & 1
    features["HAS_ANTILOST"] = (bArr[6] >> 6) & 1
    features["HAS_FINDPHONE"] = (bArr[6] >> 5) & 1
    features["HAS_FINDDEVICE"] = (bArr[6] >> 4) & 1
    features["HAS_FACTORYSETTING"] = (bArr[6] >> 3) & 1
    features["HAS_BLOODLEVEL"] = (bArr[6] >> 2) & 1
    features["HAS_NOTITOGGLE"] = (bArr[6] >> 1) & 1
    features["HAS_LIFTBRIGHT"] = bArr[6] & 1

    # Process the eighth byte (bArr[7])
    features["HAS_SKINCOLOR"] = (bArr[7] >> 7) & 1
    features["HAS_WECHATSPORT"] = (bArr[7] >> 6) & 1
    features["HAS_SEARCHAROUND"] = (bArr[7] >> 5) & 1
    features["HAS_TODAYWEATHER"] = (bArr[7] >> 4) & 1
    features["HAS_TOMORROWWEATHER"] = (bArr[7] >> 3) & 1
    features["HAS_ECGDIAGNOSIS"] = (bArr[7] >> 2) & 1
    features["HAS_PHONESUPPORT"] = (bArr[7] >> 1) & 1
    features["HAS_ENCRYPTION"] = bArr[7] & 1

    # Process the ninth byte (bArr[8])
    features["HAS_TEMPALARM"] = (bArr[8] >> 7) & 1
    features["HAS_TEMPAXILLARYTEST"] = (bArr[8] >> 6) & 1
    features["HAS_CVRR"] = (bArr[8] >> 5) & 1
    features["HAS_BLOODPRESSURECALIBRATION"] = (bArr[8] >> 4) & 1
    features["HAS_ECGRIGHTELECTRODE"] = (bArr[8] >> 3) & 1
    features["HAS_THEME"] = (bArr[8] >> 2) & 1
    features["HAS_MUSIC"] = (bArr[8] >> 1) & 1
    features["HAS_TEMP"] = bArr[8] & 1

    # Process the tenth byte (bArr[9])
    features["HAS_INACCURATEECG"] = (bArr[9] >> 7) & 1
    features["HAS_CONTACTS"] = (bArr[9] >> 6) & 1
    features["HAS_DIAL"] = (bArr[9] >> 5) & 1
    features["HAS_FEMALEPHYSIOLOGICALCYCLE"] = (bArr[9] >> 4) & 1
    features["HAS_SHAKETAKEPHOTO"] = (bArr[9] >> 3) & 1
    features["HAS_MANUALTAKEPHOTO"] = (bArr[9] >> 2) & 1
    features["HAS_SETINFO"] = (bArr[9] >> 1) & 1
    features["HAS_TEMPCALIBRATION"] = bArr[9] & 1

    # Process the eleventh byte (bArr[10])
    features["HAS_REALTIMEMONITORINGMODE"] = (bArr[10] >> 7) & 1
    features["HAS_INDOORWALKING"] = (bArr[10] >> 6) & 1
    features["HAS_OUTDOORWALKING"] = (bArr[10] >> 5) & 1
    features["HAS_INDOORRUNING"] = (bArr[10] >> 4) & 1
    features["HAS_OUTDOORRUNING"] = (bArr[10] >> 3) & 1
    features["HAS_PINGPONG"] = (bArr[10] >> 2) & 1
    features["HAS_FOOTBALL"] = (bArr[10] >> 1) & 1
    features["HAS_MOUNTAINCLIMBING"] = bArr[10] & 1

    # Process the twelfth byte (bArr[11])
    features["HAS_RUNNING"] = (bArr[11] >> 7) & 1
    features["HAS_FITNESS"] = (bArr[11] >> 6) & 1
    features["HAS_RIDING"] = (bArr[11] >> 5) & 1
    features["HAS_ROPESKIPPING"] = (bArr[11] >> 4) & 1
    features["HAS_BASKETBALL"] = (bArr[11] >> 3) & 1
    features["HAS_SWIMMING"] = (bArr[11] >> 2) & 1
    features["HAS_WALKING"] = (bArr[11] >> 1) & 1
    features["HAS_BADMINTON"] = bArr[11] & 1

    if len(bArr) >= 18:
        if len(bArr) >= 20:
            features["HAS_ONFOOT"] = (bArr[14] >> 7) & 1

        features["HAS_YOGA"] = (bArr[14] >> 6) & 1
        features["HAS_WEIGHTTRAINING"] = (bArr[14] >> 5) & 1
        features["HAS_JUMPING"] = (bArr[14] >> 4) & 1
        features["HAS_SITUPS"] = (bArr[14] >> 3) & 1
        features["HAS_ROWINGMACHINE"] = (bArr[14] >> 2) & 1
        features["HAS_STEPPER"] = (bArr[14] >> 1) & 1
        features["HAS_INDOORRIDING"] = bArr[14] & 1

        features["HAS_REALEXERCISEDATA"] = bArr[15] & 1
        features["ISHATESTHEART"] = (bArr[15] >> 1) & 1
        features["HAS_TESTBLOOD"] = (bArr[15] >> 2) & 1
        features["HAS_TESTSPO2"] = (bArr[15] >> 3) & 1
        features["HAS_TESTTEMP"] = (bArr[15] >> 4) & 1
        features["HAS_TESTRESPIRATIONRATE"] = (bArr[15] >> 5) & 1
        features["HAS_KINDSINFORMATIONPUSH"] = (bArr[15] >> 6) & 1
        features["HAS_CUSTOMDIAL"] = (bArr[15] >> 7) & 1

        features["HAS_INFLATED"] = bArr[16] & 1
        features["HAS_SOS"] = (bArr[16] >> 1) & 1
        features["HAS_BLOODOXYGENALARM"] = (bArr[16] >> 2) & 1
        features["HAS_UPLOADINFLATEBLOOD"] = (bArr[16] >> 3) & 1
        features["HAS_VIBERNOTIFY"] = (bArr[16] >> 4) & 1
        features["HAS_OTHRENOTIFY"] = (bArr[16] >> 5) & 1
        features["ISFLIPDIALIMAGE"] = (bArr[16] >> 6) & 1
        features["WATCHSCREENBRIGHTNESS"] = (bArr[16] >> 7) & 1

        features["HAS_VIBRATIONINTENSITY"] = bArr[17] & 1
        features["HAS_SETSCREENTIME"] = (bArr[17] >> 1) & 1
        features["HAS_WATCHSCREENBRIGHTNESS"] = (bArr[17] >> 2) & 1
        features["HAS_BLOODSUGAR"] = (bArr[17] >> 3) & 1
        features["HAS_PAUSEEXERCISE"] = (bArr[17] >> 4) & 1
        features["HAS_DRINKWATERREMINDER"] = (bArr[17] >> 5) & 1
        features["HAS_BUSINESSCARD"] = (bArr[17] >> 6) & 1
        features["HAS_URICACIDMEASUREMENT"] = (bArr[17] >> 7) & 1

    if len(bArr) >= 20:
        features["HAS_VOLLEYBALL"] = bArr[18] & 1
        features["HAS_KAYAK"] = (bArr[18] >> 1) & 1
        features["HAS_ROLLERSKATING"] = (bArr[18] >> 2) & 1
        features["HAS_TENNIS"] = (bArr[18] >> 3) & 1
        features["HAS_GOLF"] = (bArr[18] >> 4) & 1
        features["HAS_ELLIPTICALMACHINE"] = (bArr[18] >> 5) & 1
        features["HAS_DANCE"] = (bArr[18] >> 6) & 1
        features["HAS_ROCKCLIMBING"] = (bArr[18] >> 7) & 1

        features["HAS_AEROBICS"] = bArr[19] & 1
        features["HAS_OTHERSPORTS"] = (bArr[19] >> 1) & 1

    if len(bArr) >= 21:
        features["HAS_BLOODKETONEMEASUREMENT"] = bArr[20] & 1
        features["HAS_ALIIOT"] = (bArr[20] >> 1) & 1
        features["HAS_CREATEBOND"] = (bArr[20] >> 2) & 1
        features["HAS_RESPIRATORYRATEALARM"] = (bArr[20] >> 3) & 1
        features["HAS_IMPRECISEBLOODFAT"] = (bArr[20] >> 4) & 1
        features["HAS_INDEPENDENT_AUTOMATIC_TIME_MEASUREMENT"] = (bArr[20] >> 5) & 1
        features["HAS_RECORDING_FILE"] = (bArr[20] >> 6) & 1
        features["HAS_PHYSIOTHERAPY"] = (bArr[20] >> 7) & 1

    if len(bArr) >= 22:
        features["HAS_ZOOMNOTIFY"] = bArr[21] & 1
        features["HAS_TIKTOKNOTIFY"] = (bArr[21] >> 1) & 1
        features["HAS_KAKAOTALKNOTIFY"] = (bArr[21] >> 2) & 1

    if len(bArr) >= 23:
        features["HAS_SLEEP_REMIND"] = bArr[22] & 1
        features["HAS_DEVICE_SPEC"] = (bArr[22] >> 1) & 1
        features["HAS_LOCAL_SPORT_DATA"] = (bArr[22] >> 2) & 1
        features["HAS_LOGO"] = (bArr[22] >> 3) & 1

    return features


def parse_device_info(b_arr: bytearray) -> dict:
    device_id = (b_arr[0] & 0xFF) + ((b_arr[1] & 0xFF) << 8)
    sub_version = b_arr[2] & 0xFF
    main_version = b_arr[3] & 0xFF
    battery_state = b_arr[4] & 0xFF
    battery_value = b_arr[5] & 0xFF
    bind_state = b_arr[6] & 0xFF
    sync_state = b_arr[7] & 0xFF

    version_str = f"{main_version}.{sub_version}"

    # Create data dictionary
    data = {
        "deviceId": device_id,
        "deviceVersion": version_str,
        "deviceBatteryState": battery_state,
        "deviceBatteryValue": battery_value,
        "deviceMainVersion": main_version,
        "deviceSubVersion": sub_version,
        "devicetBindState": bind_state,
        "devicetSyncState": sync_state,
    }

    hardware_type = 0

    # Process additional data if available
    if len(b_arr) >= 24:
        ble_agreement_sub_version = b_arr[8] & 0xFF
        ble_agreement_main_version = b_arr[9] & 0xFF
        blood_algo_sub_version = b_arr[10] & 0xFF
        blood_algo_main_version = b_arr[11] & 0xFF
        tp_sub_version = b_arr[12] & 0xFF
        tp_main_version = b_arr[13] & 0xFF
        blood_sugar_sub_version = b_arr[14] & 0xFF
        blood_sugar_main_version = b_arr[15] & 0xFF
        ui_sub_version = b_arr[16] & 0xFF
        ui_main_version = b_arr[17] & 0xFF
        hardware_type = b_arr[18] & 0xFF

        # Add additional data to dictionary
        data.update(
            {
                "bleAgreementSubVersion": ble_agreement_sub_version,
                "bleAgreementMainVersion": ble_agreement_main_version,
                "bloodAlgoSubVersion": blood_algo_sub_version,
                "bloodAlgoMainVersion": blood_algo_main_version,
                "tpSubVersion": tp_sub_version,
                "tpMainVersion": tp_main_version,
                "bloodSugarSubVersion": blood_sugar_sub_version,
                "bloodSugarMainVersion": blood_sugar_main_version,
                "uiSubVersion": ui_sub_version,
                "uiMainVersion": ui_main_version,
                "hardwareType": hardware_type,
            }
        )

    data["hardwareType"] = hardware_type

    return data


def parse_name(bArr: bytes | bytearray) -> str:
    assert bArr[-1] == 0
    return bArr[:-1].decode("utf-8")


@dataclass
class RealBloodResponse:
    """
    Real time response from request for "blood"

    Is sent during the ECG upload, may be possible during other
    things too
    """

    dbp: int
    """
    diastolic blood pressure
    """

    sbp: int
    """
    systolic blood pressure
    """

    hr: int
    """
    heart rate
    """

    hrv: int | None = None
    """
    heart rate variability
    """

    spo2: int | None = None
    """
    blood oxygen
    """

    temp_i: int | None = None
    """
    temperature as int
    """

    temp_f: float | None = None
    """
    temperature as float
    """


def parse_real_blood(bArr: bytes | bytearray) -> RealBloodResponse:
    assert len(bArr) > 2, "real blood packet not long enough"

    resp = RealBloodResponse(sbp=bArr[0], dbp=bArr[1], hr=bArr[2])

    if len(bArr) > 3:
        resp.hrv = bArr[3]

    if len(bArr) > 4:
        resp.spo2 = bArr[4]

    if len(bArr) > 6:
        resp.temp_i = bArr[5]
        resp.temp_f = bArr[
            6
        ]  # idk wtf this is doing, there's no float parsing in the android app

    return resp
