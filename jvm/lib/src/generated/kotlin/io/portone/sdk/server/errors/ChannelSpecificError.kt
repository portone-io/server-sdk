package io.portone.sdk.server.errors

import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.errors.DeleteBillingKeyError
import io.portone.sdk.server.errors.IssueBillingKeyError
import io.portone.sdk.server.payment.billingkey.ChannelSpecificFailure
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우 */
@Serializable
@SerialName("CHANNEL_SPECIFIC")
public data class ChannelSpecificError(
  val failures: List<ChannelSpecificFailure>,
  /** (결제, 본인인증 등에) 선택된 채널 정보 */
  val succeededChannels: List<SelectedChannel>,
  override val message: String? = null,
): DeleteBillingKeyError,
  IssueBillingKeyError
