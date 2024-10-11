package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.PlatformPartnerTaxationType
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class CreatePlatformPartnerBodyTypeBusiness(
  /** 상호명 */
  val companyName: String,
  /** 사업자등록번호 */
  val businessRegistrationNumber: String,
  /** 대표자 이름 */
  val representativeName: String,
  /**
   * 사업자 유형
   *
   * 값을 입력하지 않으면 일반 과세로 설정됩니다.
   */
  val taxationType: PlatformPartnerTaxationType? = null,
  /** 사업장 주소 */
  val companyAddress: String? = null,
  /** 업태 */
  val businessType: String? = null,
  /** 업종 */
  val businessClass: String? = null,
)
