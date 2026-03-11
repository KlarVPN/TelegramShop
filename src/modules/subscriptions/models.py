from sqlalchemy import Column, Integer, String, Boolean, DateTime, BigInteger, ForeignKey
from sqlalchemy.orm import relationship

from src.db.base_class import Base

class Subscription(Base):
    __tablename__ = "subscriptions"

    subscription_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger,
                     ForeignKey("users.user_id"),
                     nullable=False,
                     index=True)
    panel_user_uuid = Column(String, nullable=False, index=True)
    panel_subscription_uuid = Column(String,
                                     unique=True,
                                     index=True,
                                     nullable=True)
    start_date = Column(DateTime(timezone=True), nullable=True)
    end_date = Column(DateTime(timezone=True), nullable=False, index=True)
    duration_months = Column(Integer, nullable=True)
    is_active = Column(Boolean, default=True, index=True)
    status_from_panel = Column(String, nullable=True)
    traffic_limit_bytes = Column(BigInteger, nullable=True)
    traffic_used_bytes = Column(BigInteger, nullable=True)
    last_notification_sent = Column(DateTime(timezone=True), nullable=True)
    provider = Column(String, nullable=True)
    skip_notifications = Column(Boolean, default=False)
    auto_renew_enabled = Column(Boolean, default=True, index=True)

    user = relationship("User", back_populates="subscriptions")

    def __repr__(self):
        return f"<Subscription(id={self.subscription_id}, user_id={self.user_id}, panel_uuid='{self.panel_user_uuid}', ends='{self.end_date}')>"
