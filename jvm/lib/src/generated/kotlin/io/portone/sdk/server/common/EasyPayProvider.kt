package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 간편 결제사 */
@Serializable
public enum class EasyPayProvider {
  SAMSUNGPAY,
  KAKAOPAY,
  NAVERPAY,
  PAYCO,
  SSGPAY,
  CHAI,
  LPAY,
  KPAY,
  TOSSPAY,
  LGPAY,
  PINPAY,
  APPLEPAY,
  SKPAY,
  TOSS_BRANDPAY,
  KB_APP,
  ALIPAY,
  HYPHEN,
  TMONEY,
}
