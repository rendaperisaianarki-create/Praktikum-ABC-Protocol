from core.base import PaymentMethod, PembayaranGagal
from core.protocols import Notifier
from core.utils import rupiah


class PaymentProcessor:

    def __init__(self, notifier: Notifier):

        if not isinstance(notifier, Notifier):
            raise TypeError(
                "notifier harus memiliki method kirim(penerima, pesan)"
            )

        self.notifier = notifier
        self.riwayat = []

    def checkout(
        self,
        metode: PaymentMethod,
        jumlah: float,
        pelanggan: str
    ) -> bool:

        try:
            biaya = metode.biaya_admin(jumlah)
            trx_id = metode.proses(jumlah)

        except PembayaranGagal as err:
            self.notifier.kirim(
                pelanggan,
                f"Pembayaran gagal: {err}"
            )
            return False

        self.riwayat.append(
            (trx_id, metode.nama, jumlah)
        )

        total = jumlah + biaya

        self.notifier.kirim(
            pelanggan,
            f"Pembayaran {rupiah(jumlah)} via {metode.nama} berhasil. "
            f"Biaya admin: {rupiah(biaya)}. "
            f"Total: {rupiah(total)}. ID: {trx_id}"
        )

        return True