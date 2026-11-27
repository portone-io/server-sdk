package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 건별 옵션이 켜진 플랫폼에서 음수 금액 수기 정산 생성을 시도한 경우 */
@Serializable
@SerialName("PLATFORM_NEGATIVE_AMOUNT_NOT_ALLOWED")
internal data class PlatformNegativeAmountNotAllowedError(
  override val message: String? = null,
) : CreatePlatformManualTransferError.Recognized


