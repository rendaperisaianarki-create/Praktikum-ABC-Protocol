import uuid


def rupiah(nilai: float) -> str:
    return "Rp" + f"{nilai:,.0f}".replace(",", ".")


def buat_id(prefix: str) -> str:
    return f"{prefix}-{uuid.uuid4().hex[:8].upper()}"