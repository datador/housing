from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    DateTime,
    Integer,
    Numeric,
    PrimaryKeyConstraint,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db import Model


class HMSRaw(Model):
    __tablename__ = "hms_raw"
    __table_args__ = (
        PrimaryKeyConstraint("faerslunumer", "fastnum"),
        UniqueConstraint("faerslunumer", "fastnum", name="uq_raw_faerslunumer_fastnum"),
        {"schema": "raw"},
    )

    faerslunumer: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    emnr: Mapped[str] = mapped_column(String)
    skjalanumer: Mapped[str] = mapped_column(String)
    fastnum: Mapped[str] = mapped_column(String, primary_key=True)
    heimilisfang: Mapped[Optional[str]] = mapped_column(String)
    postnr: Mapped[Optional[str]] = mapped_column(String)
    heinum: Mapped[Optional[str]] = mapped_column(String)
    svfn: Mapped[str] = mapped_column(String)
    sveitarfelag: Mapped[str] = mapped_column(String)
    utgdag: Mapped[str] = mapped_column(String)
    thinglystdags: Mapped[str] = mapped_column(String)
    kaupverd: Mapped[str] = mapped_column(String)
    fasteignamat: Mapped[str] = mapped_column(String)
    fasteignamat_gildandi: Mapped[Optional[str]] = mapped_column(String)
    fyrirhugad_fasteignamat: Mapped[Optional[str]] = mapped_column(String)
    brunabotamat_gildandi: Mapped[Optional[str]] = mapped_column(String)
    byggar: Mapped[str] = mapped_column(String)
    fepilog: Mapped[str] = mapped_column(String)
    einflm: Mapped[str] = mapped_column(String)
    lod_flm: Mapped[Optional[str]] = mapped_column(String)
    lod_flmein: Mapped[Optional[str]] = mapped_column(String)
    fjherb: Mapped[Optional[str]] = mapped_column(String)
    tegund: Mapped[str] = mapped_column(String)
    fullbuid: Mapped[str] = mapped_column(String)
    onothaefur_samningur: Mapped[str] = mapped_column(String)

    def __repr__(self):
        return f'HMSRaw("{self.faerslunumer}", "{self.fastnum}")'


class HMS(Model):
    __tablename__ = "hms"
    __table_args__ = (
        PrimaryKeyConstraint("faerslunumer", "fastnum"),
        UniqueConstraint("faerslunumer", "fastnum", name="uq_faerslunumer_fastnum"),
    )
    faerslunumer: Mapped[str] = mapped_column(
        String(6), index=True, nullable=False, primary_key=True
    )
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
    onothaefur_samningur: Mapped[int] = mapped_column(
        Integer, default=0, nullable=False
    )

    def __repr__(self):
        return f'HMSBase({self.id}, "{self.faerslunumer}")'
