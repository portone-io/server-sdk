package io.portone.sdk.server.errors

import io.portone.sdk.server.billingkey.ChannelSpecificFailure
import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.errors.ChannelSpecificError
import java.lang.Exception


/** 여러 채널을 지정한 요청에서, 채널 각각에서 오류가 발생한 경우 */
public class ChannelSpecificException(
  cause: ChannelSpecificError
) : Exception(cause.message) {
  public val failures: Array<ChannelSpecificFailure> = cause.failures
  /** (결제, 본인인증 등에) 선택된 채널 정보 */
  public val succeededChannels: Array<SelectedChannel> = cause.succeededChannels
}
