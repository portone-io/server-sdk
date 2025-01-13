package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 사업자 정보를 찾을 수 없는 경우 */
@Serializable
@SerialName("PLATFORM_COMPANY_NOT_FOUND")
internal data class PlatformCompanyNotFoundError(
  override val message: String? = null,
) : GetPlatformCompanyStateError.Recognized


