from cont import AutoSellerControl
from info import *
from time import sleep


def connect_to_two():
    AutoSellerControl(email1, password1)
    sleep(2.0)
    AutoSellerControl(email2, password2)


while True:
    connect_to_two()
    sleep(87120.0)
    print('Запуск скрипта')