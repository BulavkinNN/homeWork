from ste.tools import *
from ste.settings import *  # file with settings


class STE:

    @staticmethod
    def list(list_exc=[DEFAULT_NAME_EXCEPTION], output='list_'):
        if output not in VALID_OUTPUT:
            raise TypeError(f"Output only {VALID_OUTPUT}")
        if list_exc not in get_list(list_exc=[DEFAULT_NAME_EXCEPTION], output='list'):
            raise TypeError("Input valid exception!")
        return get_list(list_exc=[Exception], output='json')

    @staticmethod
    def test(list_exc: list = "", manual_raise: bool = False, count: int = 1, output: str = "list_"):
        """
        :param list_exc: List with Exception
        :param manual_raise: bool True use raise, False make error in function
        :param count: int  The number of cycles
        :param output: Only list (xml, json in next edition).
        :return: list with test  time (ns) the cycle was running
        """
        if not isinstance(count, int) or count > MAX_COUNT or count < MIN_COUNT:
            raise TypeError(f"Count must int and in range ({MIN_COUNT}-{MAX_COUNT})")

        return [make_count(count, exc, manual_raise) for exc in list_exc ]
