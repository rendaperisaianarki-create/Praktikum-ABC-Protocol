from typing import Protocol, runtime_checkable


@runtime_checkable
class Notifier(Protocol):

    def kirim(self, penerima: str, pesan: str) -> None:
        ...