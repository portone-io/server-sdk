package io.portone.sdk.server.platform.company

import io.portone.sdk.server.platform.company.PlatformBusinessStatus
import io.portone.sdk.server.platform.company.PlatformTaxationType
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformCompanyState(
  val taxationType: PlatformTaxationType,
  /**
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val taxationTypeDate: String? = null,
  val businessStatus: PlatformBusinessStatus,
  /**
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val closedSuspendedDate: String? = null,
)


