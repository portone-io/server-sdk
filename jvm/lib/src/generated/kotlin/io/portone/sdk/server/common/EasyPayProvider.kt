package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 간편 결제사 */
@Serializable
public enum class EasyPayProvider {
  Samsungpay,
  Kakaopay,
  Naverpay,
  Payco,
  Ssgpay,
  Chai,
  Lpay,
  Kpay,
  Tosspay,
  Lgpay,
  Pinpay,
  Applepay,
  Skpay,
  TossBrandpay,
  KbApp,
  Alipay,
  Hyphen,
  Tmoney,
}
