package io.portone.sdk.server.platform.company

import kotlin.String
import kotlinx.serialization.Serializable

/** 사업자등록 정보 */
@Serializable
public data class B2bBusinessInfo(
  /** 사업자등록번호 */
  val brn: String,
  /** 상호 */
  val name: String,
  /** 대표자명 */
  val ceoName: String,
  /** 우편번호 */
  val zipCode: String,
  /** 주소 */
  val address: String,
  /** 사업자 유형 */
  val businessEntityType: String,
  /** 사업 상태 */
  val businessStatus: String,
  /** 과세 유형 */
  val taxationType: String,
  /** 간이과세-일반과세 전환일 */
  val simplifiedTaxationTypeDate: String? = null,
  /** 폐업일 */
  val closingDate: String? = null,
  /** 개업일 */
  val openingDate: String,
  /** 업태 */
  val businessType: String,
  /** 종목 */
  val businessClass: String,
  /** 업종코드 */
  val businessCategoryCode: String,
  /** 법인등록번호 */
  val corpRegNo: String? = null,
  /** 전화번호 */
  val phoneNumber: String? = null,
  /** 관할세무서코드 */
  val taxOfficeCode: String? = null,
  /** 관할세무서명 */
  val taxOfficeName: String? = null,
)


