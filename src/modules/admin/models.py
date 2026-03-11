from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey, UniqueConstraint, Text, BigInteger
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.db.base_class import Base

class MessageLog(Base):
    __tablename__ = "message_logs"

    log_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger,
                     ForeignKey("users.user_id"),
                     nullable=True,
                     index=True)
    telegram_username = Column(String, nullable=True)
    telegram_first_name = Column(String, nullable=True)
    event_type = Column(String, nullable=False, index=True)
    content = Column(Text, nullable=True)
    raw_update_preview = Column(Text, nullable=True)
    timestamp = Column(DateTime(timezone=True),
                       server_default=func.now(),
                       index=True)
    is_admin_event = Column(Boolean, default=False)
    target_user_id = Column(BigInteger,
                            ForeignKey("users.user_id"),
                            nullable=True,
                            index=True)

    author_user = relationship("User",
                               foreign_keys=[user_id],
                               back_populates="message_logs_authored")
    target_user = relationship("User",
                               foreign_keys=[target_user_id],
                               back_populates="message_logs_targeted")


class PanelSyncStatus(Base):
    __tablename__ = "panel_sync_status"

    id = Column(Integer, primary_key=True, default=1, autoincrement=False)
    last_sync_time = Column(DateTime(timezone=True), nullable=True)
    status = Column(String, nullable=True)
    details = Column(Text, nullable=True)
    users_processed_from_panel = Column(Integer, default=0)
    subscriptions_synced = Column(Integer, default=0)

    __table_args__ = (UniqueConstraint('id'), )


class AdCampaign(Base):
    __tablename__ = "ad_campaigns"

    ad_campaign_id = Column(Integer, primary_key=True, autoincrement=True)
    source = Column(String, nullable=False, index=True)
    start_param = Column(String, nullable=False, unique=True, index=True)
    cost = Column(Float, nullable=False, default=0.0)
    is_active = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    attributions = relationship(
        "AdAttribution",
        back_populates="campaign",
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"<AdCampaign(id={self.ad_campaign_id}, source='{self.source}', start_param='{self.start_param}', cost={self.cost})>"


class AdAttribution(Base):
    __tablename__ = "ad_attributions"

    user_id = Column(BigInteger, ForeignKey("users.user_id"), primary_key=True, index=True)
    ad_campaign_id = Column(Integer, ForeignKey("ad_campaigns.ad_campaign_id"), nullable=False, index=True)
    first_start_at = Column(DateTime(timezone=True), server_default=func.now())
    trial_activated_at = Column(DateTime(timezone=True), nullable=True)

    user = relationship("User")
    campaign = relationship("AdCampaign", back_populates="attributions")
