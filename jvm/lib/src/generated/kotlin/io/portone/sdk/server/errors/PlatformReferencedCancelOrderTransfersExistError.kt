package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 취소 정산건이 참조 중인 정산건이 포함된 경우 */
@Serializable
@SerialName("PLATFORM_REFERENCED_CANCEL_ORDER_TRANSFERS_EXIST")
internal data class PlatformReferencedCancelOrderTransfersExistError(
  val ids: List<String>,
  override val message: String? = null,
) : DeletePlatformPartnerSettlementsError.Recognized


