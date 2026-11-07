from abc import ABC, abstractmethod
from core.utils import rupiah


class PembayaranGagal(Exception):
    pass


class PaymentMethod(ABC):

    def __init__(self, nama: str):
        self.nama = nama

    @abstractmethod
    def validasi(self, jumlah: float) -> bool:
        pass

    @abstractmethod
    def bayar(self, jumlah: float) -> str:
        pass

    @abstractmethod
    def biaya_admin(self, jumlah: float) -> float:
        pass

    def proses(self, jumlah: float) -> str:
        if jumlah <= 0:
            raise PembayaranGagal(
                "Jumlah pembayaran harus lebih dari 0"
            )

        biaya = self.biaya_admin(jumlah)
        total = jumlah + biaya

        if not self.validasi(total):
            raise PembayaranGagal(
                f"{self.nama} menolak pembayaran {rupiah(total)}"
            )

        return self.bayar(total)