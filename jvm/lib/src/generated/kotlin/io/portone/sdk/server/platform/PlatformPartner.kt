package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformAccount
import io.portone.sdk.server.platform.PlatformContact
import io.portone.sdk.server.platform.PlatformPartnerStatus
import io.portone.sdk.server.platform.PlatformPartnerType
import io.portone.sdk.server.platform.PlatformProperties
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 파트너
 *
 * 파트너는 고객사가 정산해주어야 할 대상입니다.
 * 기본 사업자 정보와 정산정보, 그리고 적용될 계약의 정보를 등록 및 관리할 수 있습니다.
 */
@Serializable
public data class PlatformPartner(
  /** 파트너 고유 아이디 */
  val id: String,
  val graphqlId: String,
  /** 파트너 법인명 혹은 이름 */
  val name: String,
  /** 파트너 담당자 연락 정보 */
  val contact: PlatformContact,
  /** 정산 계좌 */
  val account: PlatformAccount,
  /** 파트너의 상태 */
  val status: PlatformPartnerStatus,
  /** 파트너에 설정된 기본 계약 아이디 */
  val defaultContractId: String,
  /** 파트너에 대한 메모 */
  val memo: String? = null,
  /** 파트너의 태그 리스트 */
  val tags: List<String>,
  /** 파트너 유형별 정보 */
  val type: PlatformPartnerType,
  /** 보관 여부 */
  val isArchived: Boolean,
  /** 변경 적용 시점 */
  val appliedAt: @Serializable(InstantSerializer::class) Instant,
  /** 사용자 정의 속성 */
  val userDefinedProperties: PlatformProperties,
)
