package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformPartnerBusinessStatus
import io.portone.sdk.server.platform.PlatformPartnerMemberCompanyConnectionStatus
import io.portone.sdk.server.platform.PlatformPartnerTaxationType
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/**
 * 사업자 파트너 정보
 *
 * 사업자 유형의 파트너 추가 정보 입니다.
 */
@Serializable
@SerialName("BUSINESS")
public data class PlatformPartnerTypeBusiness(
  /** 상호명 */
  val companyName: String,
  /** 과세 유형 */
  val taxationType: PlatformPartnerTaxationType,
  /** 사업자 상태 */
  val businessStatus: PlatformPartnerBusinessStatus,
  /** 사업자등록번호 */
  val businessRegistrationNumber: String,
  /** 대표자 이름 */
  val representativeName: String,
  /** 사업장 주소 */
  val companyAddress: String? = null,
  /** 업태 */
  val businessType: String? = null,
  /** 업종 */
  val businessClass: String? = null,
  /** 연동사업자 연동 상태 */
  val memberCompanyConnectionStatus: PlatformPartnerMemberCompanyConnectionStatus,
  /** 연동사업자 연동 실패 사유 */
  val memberCompanyConnectionFailedReason: String? = null,
) : PlatformPartnerType.Recognized


