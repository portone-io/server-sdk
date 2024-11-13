package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정산 파라미터가 존재하지 않는 경우 */
@Serializable
@SerialName("PLATFORM_SETTLEMENT_PARAMETER_NOT_FOUND")
@ConsistentCopyVisibility
public data class PlatformSettlementParameterNotFoundError internal constructor(
  val message: String? = null,
) : CreatePlatformOrderTransferError
