from ste.tools import *
from ste.settings import *  # file with settings


class STE:

    @staticmethod
    def list(list_exc=[DEFAULT_NAME_EXCEPTION], output='list_'):
        if output not in VALID_OUTPUT:
            raise TypeError(f"Output only {VALID_OUTPUT}")
        if list_exc not in get_list(list_exc=[DEFAULT_NAME_EXCEPTION], output='list'):
            raise TypeError(f"Input valid exception!")
        return get_list(list_exc=[BaseException], output='json')

    @staticmethod
    def test(list_exc, count, output):
        if count

        return timer(str)()
