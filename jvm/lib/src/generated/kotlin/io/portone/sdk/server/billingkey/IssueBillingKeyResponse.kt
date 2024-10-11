package io.portone.sdk.server.billingkey

import io.portone.sdk.server.billingkey.BillingKeyInfoSummary
import io.portone.sdk.server.billingkey.ChannelSpecificFailure
import kotlinx.serialization.Serializable

/** 빌링키 발급 성공 응답 */
@Serializable
public data class IssueBillingKeyResponse(
  /** 빌링키 정보 */
  val billingKeyInfo: BillingKeyInfoSummary,
  /** 발급에 실패한 채널이 있을시 실패 정보 */
  val channelSpecificFailures: Array<ChannelSpecificFailure>? = null,
)
