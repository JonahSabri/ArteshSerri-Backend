from kavenegar import KavenegarAPI

KAVENEGAR_TOKEN = "314D4974324B7679685A4F6B306865346F656F584F474D32576D62702B6732636C4850465957437853416F3D"


def send_welcome_sms(phone, user_fullname):
    api = KavenegarAPI(KAVENEGAR_TOKEN)
    params = {
        'receptor': phone,
        'token': "ArteshSerriSms",
        'token20': user_fullname,
        'template': "signup",
    }
    response = api.verify_lookup(params)
    return response


def send_otp_code_sms(phone, code):
    api = KavenegarAPI(KAVENEGAR_TOKEN)
    params = {
        'receptor': phone,
        'token': code,
        'template': "arteshserri_otp",
    }
    response = api.verify_lookup(params)
    return response


