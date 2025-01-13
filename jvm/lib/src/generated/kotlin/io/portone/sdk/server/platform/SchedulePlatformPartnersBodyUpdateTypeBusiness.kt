package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformPartnerTaxationType
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class SchedulePlatformPartnersBodyUpdateTypeBusiness(
  /** 상호명 */
  val companyName: String? = null,
  /** 사업자 유형 */
  val taxationType: PlatformPartnerTaxationType? = null,
  /** 사업자등록번호 */
  val businessRegistrationNumber: String? = null,
  /** 대표자 이름 */
  val representativeName: String? = null,
  /** 사업장 주소 */
  val companyAddress: String? = null,
  /** 업태 */
  val businessType: String? = null,
  /** 업종 */
  val businessClass: String? = null,
  /** 사업자 조회 검증 아이디 */
  val companyVerificationId: String? = null,
)


