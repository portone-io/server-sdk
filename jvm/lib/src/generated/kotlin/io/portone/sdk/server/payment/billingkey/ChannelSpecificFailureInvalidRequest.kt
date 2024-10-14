package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.billingkey.ChannelSpecificFailure
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 요청된 입력 정보가 유효하지 않은 경우
 *
 * 허가되지 않은 값, 올바르지 않은 형식의 요청 등이 모두 해당됩니다.
 */
@Serializable
@SerialName("INVALID_REQUEST")
public data class ChannelSpecificFailureInvalidRequest(
  override val channel: SelectedChannel,
  override val message: String? = null,
): ChannelSpecificFailure
