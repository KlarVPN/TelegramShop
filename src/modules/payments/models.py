from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey, UniqueConstraint, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.db.base_class import Base

class Payment(Base):
    __tablename__ = "payments"

    payment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger,
                     ForeignKey("users.user_id"),
                     nullable=False,
                     index=True)
    yookassa_payment_id = Column(String,
                                 unique=True,
                                 index=True,
                                 nullable=True)
    provider_payment_id = Column(String, unique=True, nullable=True)
    provider = Column(String, nullable=False, default="yookassa", index=True)
    idempotence_key = Column(String, unique=True, nullable=True)
    amount = Column(Float, nullable=False)  # Final amount paid (after discount if any)

    # Discount tracking fields
    original_amount = Column(Float, nullable=True)  # Amount before discount
    discount_applied = Column(Float, nullable=True)  # Discount amount (not percentage)

    currency = Column(String, nullable=False)
    status = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    subscription_duration_months = Column(Integer, nullable=True)
    promo_code_id = Column(Integer,
                           ForeignKey("promo_codes.promo_code_id"),
                           nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        onupdate=func.now(),
                        nullable=True)

    user = relationship("User", back_populates="payments")
    promo_code_used = relationship("PromoCode",
                                   back_populates="payments_where_used")


class UserBilling(Base):
    __tablename__ = "user_billing"

    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True)
    # Saved payment method for off-session recurring charges (YooKassa)
    yookassa_payment_method_id = Column(String, nullable=True, unique=True)
    card_last4 = Column(String, nullable=True)
    card_network = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    user = relationship("User")

class UserPaymentMethod(Base):
    __tablename__ = "user_payment_methods"

    method_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.user_id"), nullable=False, index=True)
    provider = Column(String, nullable=False, default="yookassa", index=True)
    provider_payment_method_id = Column(String, nullable=False, unique=True, index=True)
    card_last4 = Column(String, nullable=True)
    card_network = Column(String, nullable=True)
    is_default = Column(Boolean, default=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    user = relationship("User")
    __table_args__ = (
        UniqueConstraint('user_id', 'provider_payment_method_id', name='uq_user_provider_method'),
    )
