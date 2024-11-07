package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 카드 브랜드 */
@Serializable
public enum class CardBrand {
  Local,
  Master,
  Unionpay,
  Visa,
  Jcb,
  Amex,
  Diners,
}
