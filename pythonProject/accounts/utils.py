import random
import string


def invite_generator(chars=string.ascii_uppercase + string.digits):
    """ Рандомная генерация инвайт кода """

    return ''.join(random.choice(chars) for i in range(6))
