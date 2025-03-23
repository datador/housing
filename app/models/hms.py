from typing import Optional
from decimal import Decimal
from sqlalchemy import String, Integer, Numeric, DateTime, UniqueConstraint, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Model


class HMS(Model):
    __tablename__ = 'hms'

    faerslunumer: Mapped[str] = mapped_column(String(6), index=True, nullable=False, primary_key=True)
    emnr: Mapped[str] = mapped_column(String(3), nullable=False)
    skjalanumer: Mapped[str] = mapped_column(String(13), index=True, nullable=False)
    fastnum: Mapped[str] = mapped_column(String(7), nullable=False, primary_key=True)
    heimilisfang: Mapped[Optional[str]] = mapped_column(String(255))
    postnr: Mapped[Optional[str]] = mapped_column(String(3))
    heinum: Mapped[Optional[str]] = mapped_column(String(7))
    svfn: Mapped[str] = mapped_column(String(4), nullable=False)
    sveitarfelag: Mapped[str] = mapped_column(String(255), nullable=False)
    utgdag: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    thinglystdags: Mapped[DateTime] = mapped_column(DateTime, nullable=False)
    kaupverd: Mapped[int] = mapped_column(Integer, nullable=False)
    fasteignamat: Mapped[int] = mapped_column(Integer, nullable=False)
    fasteignamat_gildandi: Mapped[Optional[int]] = mapped_column(Integer)
    fyrirhugad_fasteignamat: Mapped[Optional[int]] = mapped_column(Integer)
    brunabotamat_gildandi: Mapped[Optional[int]] = mapped_column(Integer)
    byggar: Mapped[int] = mapped_column(String, nullable=False)
    fepilog: Mapped[str] = mapped_column(String(6), nullable=False)
    einflm: Mapped[Decimal] = mapped_column(Numeric, nullable=False)
    lod_flm: Mapped[Optional[str]] = mapped_column(String)
    lod_flmein: Mapped[Optional[str]] = mapped_column(String(2))
    fjherb: Mapped[Optional[int]] = mapped_column(Integer)
    tegund: Mapped[str] = mapped_column(String(255), nullable=False)
    fullbuid: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    onothaefur_samningur: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint("faerslunumer", "fastnum"),
        UniqueConstraint("faerslunumer", "fastnum", name="uq_faerslunumer_fastnum"),
    )
    def __repr__(self):
        return f'HMSBase({self.id}, "{self.faerslunumer}")'
