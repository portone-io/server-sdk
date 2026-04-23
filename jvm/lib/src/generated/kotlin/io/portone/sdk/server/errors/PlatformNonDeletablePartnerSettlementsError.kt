package io.portone.sdk.server.errors

import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 삭제할 수 없는 정산건이 포함된 경우 */
@Serializable
@SerialName("PLATFORM_NON_DELETABLE_PARTNER_SETTLEMENTS")
internal data class PlatformNonDeletablePartnerSettlementsError(
  val ids: List<String>,
  val graphqlIds: List<String>,
  override val message: String? = null,
) : DeletePlatformPartnerSettlementsError.Recognized


