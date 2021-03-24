
class UnexpectedEndOfFile(Exception):

    def __init__(self) -> None:
        raise self
        return None

    def __str__(self) -> str:
        return "The file seemed to end unexpectedly"
