from ste.tools import *
from ste.settings import *  # file with settings


class STE:
    """Spend Time Exception (STE)"""

    @staticmethod
    def test(list_exc: list = "", manual_raise: bool = False, count: int = 1, output: str = "list"):
        """
        :param list_exc: List with Exception
        :param manual_raise: bool True use raise, False make error in function
        :param count: int  The number of cycles
        :param output: Only list (xml, json in next edition).
        :raise TypeError
        :return: list with test  time (ns) the cycle was running
        """
        if not isinstance(manual_raise, bool):
            raise TypeError("Manual_raise only bool")
        if manual_raise is False and not all(item in VALID_EXCEPTION for item in list_exc):
            raise TypeError(f"Output only {VALID_EXCEPTION}")
        if manual_raise is True and not all(issubclass(item, Exception) for item in list_exc):
            raise TypeError("Output only class Exception")
        if output not in VALID_OUTPUT:
            raise TypeError(f"Output only {VALID_OUTPUT}")
        if not isinstance(count, int) or count > MAX_COUNT or count < MIN_COUNT:
            raise TypeError(f"Count must int and in range ({MIN_COUNT}-{MAX_COUNT})")

        return [make_count(count, exc, manual_raise) for exc in list_exc]
