from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, UniqueConstraint, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.db.base_class import Base

class PromoCode(Base):
    __tablename__ = "promo_codes"

    promo_code_id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String, unique=True, nullable=False, index=True)

    # Type field to distinguish promo code types
    promo_type = Column(String, nullable=False, default="bonus_days", index=True)
    # Values: "bonus_days" or "discount"

    # For bonus_days type: number of days to add to subscription
    bonus_days = Column(Integer, nullable=True)

    # For discount type: percentage discount (1-100)
    discount_percentage = Column(Integer, nullable=True)

    max_activations = Column(Integer, nullable=False)
    current_activations = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_by_admin_id = Column(BigInteger, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    valid_until = Column(DateTime(timezone=True), nullable=True)

    activations = relationship("PromoCodeActivation",
                               back_populates="promo_code",
                               cascade="all, delete-orphan")
    payments_where_used = relationship("Payment",
                                       back_populates="promo_code_used")


class PromoCodeActivation(Base):
    __tablename__ = "promo_code_activations"

    activation_id = Column(Integer, primary_key=True, autoincrement=True)
    promo_code_id = Column(Integer,
                           ForeignKey("promo_codes.promo_code_id"),
                           nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False)
    activated_at = Column(DateTime(timezone=True), server_default=func.now())
    payment_id = Column(Integer,
                        ForeignKey("payments.payment_id"),
                        nullable=True)

    promo_code = relationship("PromoCode", back_populates="activations")
    user = relationship("User", back_populates="promo_code_activations")
    payment = relationship("Payment")

    __table_args__ = (UniqueConstraint('promo_code_id',
                                       'user_id',
                                       name='uq_promo_user_activation'), )


class ActiveDiscount(Base):
    """Tracks pending discount promo code reservations awaiting payment."""
    __tablename__ = "active_discounts"

    user_id = Column(
        BigInteger,
        ForeignKey("users.user_id", ondelete="CASCADE"),
        primary_key=True,
    )
    promo_code_id = Column(
        Integer,
        ForeignKey("promo_codes.promo_code_id", ondelete="CASCADE"),
        nullable=False,
    )
    discount_percentage = Column(Integer, nullable=False)
    activated_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)

    promo_code = relationship("PromoCode")
    user = relationship("User")
