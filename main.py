from core.notifiers import ConsoleNotifier, TelegramNotifier
from core.protocols import Notifier
from core.processor import PaymentProcessor
from core.registry import buat_metode, daftar_plugin
from core.utils import rupiah
import plugins.transfer_bank
import plugins.ewallet
import plugins.qris


def main():

    print("Plugin terdaftar:", daftar_plugin())
    print("-" * 60)

    pemroses = PaymentProcessor(ConsoleNotifier())

    skenario = [
        ("transfer", {"saldo": 1_000_000, "bank": "BCA"}, 250_000),
        ("ewallet", {"saldo": 100_000}, 150_000),
        ("ewallet", {"saldo": 5_000_000}, 2_500_000),
        ("qris", {}, 50_000),
    ]

    for kode, parameter, jumlah in skenario:

        try:
            metode = buat_metode(kode, **parameter)

        except KeyError as err:
            print("[PERINGATAN]", err)
            continue

        pemroses.checkout(
            metode,
            jumlah,
            "mahasiswa@utr.ac.id"
        )

    print("-" * 60)
    print("Riwayat transaksi berhasil:")

    for trx_id, nama, jumlah in pemroses.riwayat:
        print(
            f"{trx_id} | {nama} | {rupiah(jumlah)}"
        )

    print("-" * 60)
    print("Pengujian TelegramNotifier:")

    telegram = TelegramNotifier()

    print(
        "Memenuhi Notifier?",
        isinstance(telegram, Notifier)
    )

    pemroses_telegram = PaymentProcessor(telegram)

    pemroses_telegram.checkout(
        buat_metode("qris"),
        100_000,
        "081234567890"
    )


if __name__ == "__main__":
    main()