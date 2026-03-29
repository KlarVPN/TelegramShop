from typing import Dict, List, Optional, Tuple

from aiogram.types import InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton

from config.settings import Settings


def get_main_menu_inline_keyboard(
    lang: str, i18n_instance, settings: Settings, show_trial_button: bool = False
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()

    if show_trial_button and settings.TRIAL_ENABLED:
        builder.row(
            InlineKeyboardButton(
                text=_(key="menu_activate_trial_button"),
                callback_data="main_action:request_trial",
                icon_custom_emoji_id="5296529806588943113",
            )
        )

    lk_button = InlineKeyboardButton(
        text=_(key="menu_lk_inline"),
        callback_data="main_action:lk",
        icon_custom_emoji_id="5296601030031614450",
    )
    builder.row(lk_button)

    row = []
    row.append(
        InlineKeyboardButton(
            text=_(key="menu_info_inline"),
            callback_data="main_action:info",
            icon_custom_emoji_id="5298652117433622027",
        )
    )

    if settings.SUPPORT_LINK:
        row.append(
            InlineKeyboardButton(
                text=_(key="menu_support_button"),
                url=settings.SUPPORT_LINK,
                icon_custom_emoji_id="5296661314192580241",
            )
        )

    builder.row(*row)

    builder.row(
        InlineKeyboardButton(
            text=_(key="menu_tg_proxy"),
            callback_data="main_action:proxy",
            icon_custom_emoji_id="5355019710607956483",
        )
    )

    builder.row(
        InlineKeyboardButton(
            text=_(key="menu_language_settings_inline"),
            callback_data="main_action:language",
            icon_custom_emoji_id=(
                "5296375222126026745" if lang == "ru" else
                "5296430537009831302" if lang == "en" else
                "5352538512296023102"
            )
        )
    )

    return builder.as_markup()


def get_proxy_keyboard(
        i18n_instance,
        settings: Settings,
        current_lang: str
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(current_lang, key, **kwargs)

    proxies = [
        {
            "name": "proxy_russia",
            "url": "https://t.me/proxy?server=sus.veil.watch&port=443&secret=ee434eb6b1335ef8d34a51a53df1d1f01d62726f777365722e79616e6465782e7275",
            "emoji_id": "5296375222126026745"
        },
        {
            "name": "proxy_germany",
            "url": "https://t.me/proxy?server=mtd.klarvpn.dev&port=443&secret=eee33f1d03af9c743d8f353f46f8a867f97777772e6d6963726f736f66742e636f6d",
            "emoji_id": "5298914385316582114"
        },
        {
            "name": "proxy_netherlands",
            "url": "https://t.me/proxy?server=mtn.klarvpn.dev&port=443&secret=eee33f1d03af9c743d8f353f46f8a867f97777772e6d6963726f736f66742e636f6d",
            "emoji_id": "5298504396328440599"
        },
        {
            "name": "proxy_finland",
            "url": "https://t.me/proxy?server=rizz.veil.watch&port=443&secret=eede4168f3ab6f28055531d1694abdc8ff6769746875622e636f6d",
            "emoji_id": "5298625303952793880"
        },
        {
            "name": "proxy_poland",
            "url": "https://t.me/proxy?server=pepe.veil.watch&port=443&secret=ee2ac3374495a1fc5cdd420e171a9842c96769746875622e636f6d",
            "emoji_id": "5296269510095969437"
        },
        {
            "name": "proxy_sweden",
            "url": "https://t.me/proxy?server=cheburnet.veil.watch&port=443&secret=ee2fae6b8af5404b7d04d1f85851239c436769746875622e636f6d",
            "emoji_id": "5298861299520806249"
        },
    ]

    builder = InlineKeyboardBuilder()

    for i, proxy in enumerate(proxies):
        button = InlineKeyboardButton(
            text=_(key=proxy['name']),
            url=proxy['url'],
            icon_custom_emoji_id=proxy['emoji_id'],
        )

        builder.add(button)

        if (i + 1) % 3 == 0:
            builder.adjust(3)  # или builder.row() если хочешь вручную

    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    )

    return builder.as_markup()


def get_info_keyboard(
    i18n_instance, settings: Settings, current_lang: str
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(current_lang, key, **kwargs)
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text=_(key="menu_about_inline"),
            callback_data="main_action:about",
            icon_custom_emoji_id="5296363118908190052",
        )
    )

    row = []

    row.append(
        InlineKeyboardButton(
            text=_(key="menu_instruction_inline"),
            callback_data="main_action:instruction",
            icon_custom_emoji_id="5296472189602669738",
        )
    )

    row.append(
        InlineKeyboardButton(
            text=_(key="menu_reviews_inline"),
            url="https://t.me/klar_reviews",
            icon_custom_emoji_id="5355171000830958183",
        )
    )

    builder.row(*row)
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    )

    return builder.as_markup()


def get_lk_keyboard(
    i18n_instance, settings: Settings, current_lang: str
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(current_lang, key, **kwargs)
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text=_(key="menu_my_subscription_inline"),
            callback_data="main_action:my_subscription",
            icon_custom_emoji_id="5296363118908190052",
        )
    )

    row = []

    row.append(
        InlineKeyboardButton(
            text=_(key="menu_apply_promo_button"),
            callback_data="main_action:apply_promo",
            icon_custom_emoji_id="5298547526390026413",
        )
    )

    if settings.REFERRAL_ENABLED:
        row.append(
            InlineKeyboardButton(
                text=_(key="menu_referral_inline"),
                callback_data="main_action:referral",
                icon_custom_emoji_id="5296529806588943113",
            )
        )

    builder.row(*row)

    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    )

    return builder.as_markup()


def get_instuction_keyboard(
    i18n_instance, settings: Settings, current_lang: str
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(current_lang, key, **kwargs)
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(
            text="Android",
            url="https://docs.klar.icu/clients/android",
            icon_custom_emoji_id="5296740238511612457",
        ),
        InlineKeyboardButton(
            text="iOS",
            url="https://docs.klar.icu/clients/ios",
            icon_custom_emoji_id="5298535569201074120",
        ),
    )

    builder.row(
        InlineKeyboardButton(
            text="macOS",
            url="https://docs.klar.icu/clients/macos",
            icon_custom_emoji_id="5330152983835483851",
        ),
        InlineKeyboardButton(
            text="Windows",
            url="https://docs.klar.icu/clients/windows",
            icon_custom_emoji_id="5296371777562253543",
        ),
    )

    builder.row(
        InlineKeyboardButton(
            text="Linux",
            url="https://docs.klar.icu/clients/linux",
            icon_custom_emoji_id="5328051031135783164",
        )
    )

    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:info",
            icon_custom_emoji_id="5296412923348952548",
        )
    )

    return builder.as_markup()


def get_about_keyboard(
    i18n_instance, settings: Settings, current_lang: str
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(current_lang, key, **kwargs)
    builder = InlineKeyboardBuilder()

    if settings.REQUIRED_CHANNEL_LINK:
        builder.row(
            InlineKeyboardButton(
                text=_(key="menu_channel_button"),
                url=settings.REQUIRED_CHANNEL_LINK,
                icon_custom_emoji_id="5296599655642086597",
            )
        )

    web_buttons = []

    if settings.WEB_URL:
        web_buttons.append(
            InlineKeyboardButton(
                text=_(key="menu_web_button"),
                url=settings.WEB_URL,
                icon_custom_emoji_id="5298681396225677178",
            )
        )

    if settings.DOCS_URL:
        web_buttons.append(
            InlineKeyboardButton(
                text=_(key="menu_docs_button"),
                url=settings.DOCS_URL,
                icon_custom_emoji_id="5296472189602669738",
            )
        )

    if web_buttons:
        builder.row(*web_buttons)

    other_buttons = []

    if settings.SERVER_STATUS_URL:
        other_buttons.append(
            InlineKeyboardButton(
                text=_(key="menu_server_status_button"),
                url=settings.SERVER_STATUS_URL,
                icon_custom_emoji_id="5296649344118727461",
            )
        )

    if settings.TERMS_OF_SERVICE_URL:
        other_buttons.append(
            InlineKeyboardButton(
                text=_(key="menu_terms_button"),
                url=settings.TERMS_OF_SERVICE_URL,
                icon_custom_emoji_id="5298709356462773297",
            )
        )

    if other_buttons:
        builder.row(*other_buttons)

    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:info",
            icon_custom_emoji_id="5296412923348952548",
        )
    )

    return builder.as_markup()


def get_language_selection_keyboard(
    i18n_instance, current_lang: str
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(current_lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    en_button = InlineKeyboardButton(
        text="English",
        callback_data="set_lang_en",
        style="success" if current_lang == "en" else None,
        icon_custom_emoji_id="5296430537009831302",
    )
    ru_button = InlineKeyboardButton(
        text="Русский",
        callback_data="set_lang_ru",
        style="success" if current_lang == "ru" else None,
        icon_custom_emoji_id="5296375222126026745",
    )
    ch_button = InlineKeyboardButton(
        text="中文",
        callback_data="set_lang_ch",
        style="success" if current_lang == "ch" else None,
        icon_custom_emoji_id="5352538512296023102",
    )
    builder.row(en_button, ru_button, ch_button)

    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    )

    return builder.as_markup()


def get_trial_confirmation_keyboard(lang: str, i18n_instance) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_(key="trial_confirm_activate_button"),
        callback_data="trial_action:confirm_activate",
    )
    builder.button(
        text=_(key="cancel_button"), callback_data="main_action:back_to_main"
    )
    builder.adjust(1)
    return builder.as_markup()


def get_subscription_options_keyboard(
    subscription_options: Dict[float, Optional[float]],
    currency_symbol_val: str,
    lang: str,
    i18n_instance,
    traffic_mode: bool = False,
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()

    def _format_gb(val: float) -> str:
        return str(int(val)) if float(val).is_integer() else f"{val:g}"

    if subscription_options:
        for months, price in subscription_options.items():
            if price is not None:
                if traffic_mode:
                    button_text = _(
                        "buy_traffic_package_button",
                        traffic_gb=_format_gb(months),
                        price=price,
                        currency_symbol=currency_symbol_val,
                    )
                    callback_data = f"subscribe_period:{_format_gb(months)}"
                else:
                    button_text = _(
                        "subscribe_for_months_button",
                        months=months,
                        price=price,
                        currency_symbol=currency_symbol_val,
                    )
                    callback_data = f"subscribe_period:{months}"
                builder.button(text=button_text, callback_data=callback_data)
        builder.adjust(1)
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    )
    return builder.as_markup()


def get_payment_method_keyboard(
    months: int,
    price: float,
    stars_price: Optional[int],
    currency_symbol_val: str,
    lang: str,
    i18n_instance,
    settings: Settings,
    sale_mode: str = "subscription",
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()

    def _format_value(val: float) -> str:
        return str(int(val)) if float(val).is_integer() else f"{val:g}"

    value_str = _format_value(months)
    mode_suffix = f":{sale_mode}"
    for method in settings.payment_methods_order:
        if method == "severpay" and getattr(settings, "SEVERPAY_ENABLED", False):
            builder.button(
                text=_("pay_with_severpay_button"),
                callback_data=f"pay_severpay:{value_str}:{price}{mode_suffix}",
            )
        elif method == "freekassa" and settings.FREEKASSA_ENABLED:
            builder.button(
                text=_("pay_with_sbp_button"),
                callback_data=f"pay_fk:{value_str}:{price}{mode_suffix}",
            )
        elif method == "platega" and settings.PLATEGA_ENABLED:
            builder.button(
                text=_("pay_with_platega_button"),
                callback_data=f"pay_platega:{value_str}:{price}{mode_suffix}",
            )
        elif method == "yookassa" and settings.YOOKASSA_ENABLED:
            builder.button(
                text=_("pay_with_yookassa_button"),
                callback_data=f"pay_yk:{value_str}:{price}{mode_suffix}",
            )
        elif method == "stars" and settings.STARS_ENABLED and stars_price is not None:
            builder.button(
                text=_("pay_with_stars_button"),
                callback_data=f"pay_stars:{value_str}:{stars_price}{mode_suffix}",
            )
        elif method == "cryptopay" and settings.CRYPTOPAY_ENABLED:
            builder.button(
                text=_("pay_with_cryptopay_button"),
                callback_data=f"pay_crypto:{value_str}:{price}{mode_suffix}",
            )
    builder.button(text=_(key="cancel_button"), callback_data="main_action:subscribe")
    builder.adjust(1)
    return builder.as_markup()


def get_payment_url_keyboard(
    payment_url: str,
    lang: str,
    i18n_instance,
    back_callback: Optional[str] = None,
    back_text_key: str = "back_to_main_menu_button",
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.button(text=_(key="pay_button"), url=payment_url)
    if back_callback:
        builder.button(text=_(key=back_text_key), callback_data=back_callback)
    else:
        builder.button(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    builder.adjust(1)
    return builder.as_markup()


def get_yk_autopay_choice_keyboard(
    months: int,
    price: float,
    lang: str,
    i18n_instance,
    has_saved_cards: bool = True,
    sale_mode: str = "subscription",
) -> InlineKeyboardMarkup:
    """Keyboard for choosing between saved card charge or new card payment when auto-renew is enabled."""
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    price_str = str(price)

    def _format_value(val: float) -> str:
        return str(int(val)) if float(val).is_integer() else f"{val:g}"

    value_str = _format_value(months)
    suffix = f":{sale_mode}"
    if has_saved_cards:
        builder.row(
            InlineKeyboardButton(
                text=_(key="yookassa_autopay_pay_saved_card_button"),
                callback_data=f"pay_yk_saved_list:{value_str}:{price_str}{suffix}",
            )
        )
    builder.row(
        InlineKeyboardButton(
            text=_(key="yookassa_autopay_pay_new_card_button"),
            callback_data=f"pay_yk_new:{value_str}:{price_str}{suffix}",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_payment_methods_button"),
            callback_data=f"subscribe_period:{value_str}",
        )
    )
    return builder.as_markup()


def get_yk_saved_cards_keyboard(
    cards: List[Tuple[str, str]],
    months: int,
    price: float,
    lang: str,
    i18n_instance,
    page: int = 0,
    sale_mode: str = "subscription",
) -> InlineKeyboardMarkup:
    """Paginated keyboard for selecting a saved YooKassa card."""
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    per_page = 5
    total = len(cards)
    start = page * per_page
    end = min(total, start + per_page)
    price_str = str(price)

    def _format_value(val: float) -> str:
        return str(int(val)) if float(val).is_integer() else f"{val:g}"

    value_str = _format_value(months)
    suffix = f":{sale_mode}"

    for method_id, title in cards[start:end]:
        builder.row(
            InlineKeyboardButton(
                text=title,
                callback_data=f"pay_yk_use_saved:{value_str}:{price_str}:{method_id}{suffix}",
            )
        )

    nav_buttons: List[InlineKeyboardButton] = []
    if start > 0:
        nav_buttons.append(
            InlineKeyboardButton(
                text="⬅️",
                callback_data=f"pay_yk_saved_list:{value_str}:{price_str}:{page - 1}{suffix}",
            )
        )
    if end < total:
        nav_buttons.append(
            InlineKeyboardButton(
                text="➡️",
                callback_data=f"pay_yk_saved_list:{value_str}:{price_str}:{page + 1}{suffix}",
            )
        )
    if nav_buttons:
        builder.row(*nav_buttons)

    builder.row(
        InlineKeyboardButton(
            text=_(key="yookassa_autopay_pay_new_card_button"),
            callback_data=f"pay_yk_new:{value_str}:{price_str}{suffix}",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_autopay_method_choice_button"),
            callback_data=f"pay_yk:{value_str}:{price_str}{suffix}",
        )
    )
    return builder.as_markup()


def get_referral_link_keyboard(lang: str, i18n_instance) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_(key="referral_share_message_button"),
        callback_data="referral_action:share_message",
    )
    builder.button(
        text=_(key="back_to_main_menu_button"),
        callback_data="main_action:back_to_main",
        icon_custom_emoji_id="5296412923348952548",
    )
    builder.adjust(1)
    return builder.as_markup()


def get_back_to_main_menu_markup(
    lang: str, i18n_instance, callback_data: Optional[str] = None
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    if callback_data:
        builder.button(
            text=_(key="back_to_main_menu_button"),
            callback_data=callback_data,
            icon_custom_emoji_id="5296412923348952548",
        )
    else:
        builder.button(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    return builder.as_markup()


def get_subscribe_only_markup(lang: str, i18n_instance) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_(key="menu_subscribe_inline"), callback_data="main_action:subscribe"
    )
    return builder.as_markup()


def get_user_banned_keyboard(
    support_link: Optional[str], lang: str, i18n_instance
) -> Optional[InlineKeyboardMarkup]:
    if not support_link:
        return None
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.button(text=_(key="menu_support_button"), url=support_link)
    return builder.as_markup()


def get_channel_subscription_keyboard(
    lang: str,
    i18n_instance,
    channel_link: Optional[str],
    include_check_button: bool = True,
) -> Optional[InlineKeyboardMarkup]:
    """
    Return keyboard with buttons to open the required channel and trigger a subscription re-check.
    """
    if i18n_instance is None:
        return None

    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()

    has_buttons = False

    if channel_link:
        builder.button(
            text=_(key="channel_subscription_join_button"),
            url=channel_link,
        )
        has_buttons = True

    if include_check_button:
        builder.button(
            text=_(key="channel_subscription_verify_button"),
            callback_data="channel_subscription:verify",
            style="success",
        )
        has_buttons = True

    if not has_buttons:
        return None

    builder.adjust(1)
    return builder.as_markup()


def get_connect_and_main_keyboard(
    lang: str,
    i18n_instance,
    settings: Settings,
    config_link: Optional[str],
    connect_button_url: Optional[str] = None,
    preserve_message: bool = False,
) -> InlineKeyboardMarkup:
    """Keyboard with a connect button and a back to main menu button."""
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    button_target = connect_button_url or config_link

    if settings.SUBSCRIPTION_MINI_APP_URL:
        builder.row(
            InlineKeyboardButton(
                text=_("connect_button"),
                web_app=WebAppInfo(url=settings.SUBSCRIPTION_MINI_APP_URL),
            )
        )
    elif button_target:
        builder.row(InlineKeyboardButton(text=_("connect_button"), url=button_target))
    else:
        builder.row(
            InlineKeyboardButton(
                text=_("connect_button"),
                callback_data="main_action:my_subscription",
            )
        )

    back_callback = (
        "main_action:back_to_main_keep"
        if preserve_message
        else "main_action:back_to_main"
    )
    builder.row(
        InlineKeyboardButton(
            text=_("back_to_main_menu_button"),
            callback_data=back_callback,
            icon_custom_emoji_id="5296412923348952548",
        )
    )

    return builder.as_markup()


def get_payment_methods_manage_keyboard(
    lang: str, i18n_instance, has_card: bool
) -> InlineKeyboardMarkup:
    """Deprecated in favor of get_payment_methods_list_keyboard. Kept for backward compatibility."""
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=_(key="payment_method_bind_button"), callback_data="pm:bind"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    )
    return builder.as_markup()


def get_payment_methods_list_keyboard(
    cards: List[Tuple[str, str]],
    page: int,
    lang: str,
    i18n_instance,
) -> InlineKeyboardMarkup:
    """
    Build a paginated list of saved payment methods.
    cards: list of tuples (payment_method_id, display_title)
    page: 0-based page index
    """
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    per_page = 5
    total = len(cards)
    start = page * per_page
    end = start + per_page
    for pm_id, title in cards[start:end]:
        builder.row(InlineKeyboardButton(text=title, callback_data=f"pm:view:{pm_id}"))

    # Pagination controls if needed
    nav_buttons: List[InlineKeyboardButton] = []
    if start > 0:
        nav_buttons.append(
            InlineKeyboardButton(text="⬅️", callback_data=f"pm:list:{page - 1}")
        )
    if end < total:
        nav_buttons.append(
            InlineKeyboardButton(text="➡️", callback_data=f"pm:list:{page + 1}")
        )
    if nav_buttons:
        builder.row(*nav_buttons)

    # Bind new card and back
    builder.row(
        InlineKeyboardButton(
            text=_(key="payment_method_bind_button"), callback_data="pm:bind"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="main_action:back_to_main",
            icon_custom_emoji_id="5296412923348952548",
        )
    )
    return builder.as_markup()


def get_payment_method_delete_confirm_keyboard(
    pm_id: str, lang: str, i18n_instance
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=_(key="yes_button"), callback_data=f"pm:delete:{pm_id}"
        ),
        InlineKeyboardButton(
            text=_(key="cancel_button"), callback_data=f"pm:view:{pm_id}"
        ),
    )
    return builder.as_markup()


def get_payment_method_details_keyboard(
    pm_id: str, lang: str, i18n_instance
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=_(key="payment_method_tx_history_title"),
            callback_data=f"pm:history:{pm_id}",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=_(key="payment_method_delete_button"),
            callback_data=f"pm:delete_confirm:{pm_id}",
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="pm:list:0",
            icon_custom_emoji_id="5296412923348952548",
        )
    )
    return builder.as_markup()


def get_bind_url_keyboard(
    bind_url: str, lang: str, i18n_instance
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.button(text=_(key="payment_method_bind_button"), url=bind_url)
    builder.button(
        text=_(key="back_to_main_menu_button"),
        callback_data="pm:manage",
        icon_custom_emoji_id="5296412923348952548",
    )
    builder.adjust(1)
    return builder.as_markup()


def get_back_to_payment_methods_keyboard(
    lang: str, i18n_instance
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data="pm:list:0",
            icon_custom_emoji_id="5296412923348952548",
        )
    )
    return builder.as_markup()


def get_back_to_payment_method_details_keyboard(
    pm_id: str, lang: str, i18n_instance
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    # Back one step: return to specific payment method details
    builder.row(
        InlineKeyboardButton(
            text=_(key="back_to_main_menu_button"),
            callback_data=f"pm:view:{pm_id}",
            icon_custom_emoji_id="5296412923348952548",
        )
    )
    return builder.as_markup()


def get_autorenew_cancel_keyboard(lang: str, i18n_instance) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=_(key="autorenew_disable_button"), callback_data="autorenew:cancel"
        )
    )
    builder.row(
        InlineKeyboardButton(
            text=_(key="menu_my_subscription_inline"),
            callback_data="main_action:my_subscription",
        )
    )
    return builder.as_markup()


def get_autorenew_confirm_keyboard(
    enable: bool, sub_id: int, lang: str, i18n_instance
) -> InlineKeyboardMarkup:
    _ = lambda key, **kwargs: i18n_instance.gettext(lang, key, **kwargs)
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(
            text=_(key="yes_button"),
            callback_data=f"autorenew:confirm:{sub_id}:{1 if enable else 0}",
        ),
        InlineKeyboardButton(
            text=_(key="no_button"), callback_data="main_action:my_subscription"
        ),
    )
    return builder.as_markup()
