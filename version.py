import sys

if not sys.version_info.major == 3 and sys.version_info.minor >= 5:
    print("Этот скрипт требует Python 3.5 или выше!")
    print("Вы используете Python {}.{}.".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)