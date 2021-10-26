import random
from django.core.cache import cache

from .tasks import send_sms


def set_code_to_phone(phone, count):
    code = str(random.randint(1000, 9999))
    key = '{}_code'.format(phone)
    count += 1
    cache.set(key, {'code': code, 'count': count}, 5 * 60)
    return code


def send_sms_code(phone, text):
    key = '{}_code'.format(phone)
    old = cache.get(key)
    if old:
        cache.delete(key)
        count = old['count']
        if count > 5:
            return False
        else:
            code = set_code_to_phone(phone, count)
            message = f'{text} {code}'
            send_sms.delay(phone, message)
            return code
    else:
        code = set_code_to_phone(phone, 0)
        message = f'{text} {code}'
        send_sms.delay(phone, message)
        return code


def is_code_correct(phone, code):
    key = '{}_code'.format(phone)
    correct_code = cache.get(key)
    if correct_code:
        if correct_code['code'] == code:
            cache.delete(key)
            cache.set(key, {'code': correct_code['code'], 'count': correct_code['count'], 'check':True}, 5*60)
            return True
        return False
    else:
        return False
