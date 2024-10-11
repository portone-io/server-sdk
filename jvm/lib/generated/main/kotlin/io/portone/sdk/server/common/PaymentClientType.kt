package io.portone.sdk.server.common

import kotlinx.serialization.Serializable

/** 결제가 발생한 클라이언트 환경 */
@Serializable
public enum class PaymentClientType {
  SDK_MOBILE,
  SDK_PC,
  API,
}
