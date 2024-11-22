package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformProperties
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyAccount
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyContact
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyType
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 파트너 업데이트를 위한 입력 정보
 *
 * 값이 명시되지 않은 필드는 업데이트되지 않습니다.
 */
@Serializable
public data class UpdatePlatformPartnerBody(
  /** 파트너 법인명 혹은 이름 */
  val name: String? = null,
  /** 파트너 담당자 연락 정보 */
  val contact: UpdatePlatformPartnerBodyContact? = null,
  /** 정산 계좌 */
  val account: UpdatePlatformPartnerBodyAccount? = null,
  /** 파트너에 설정된 기본 계약 아이디 */
  val defaultContractId: String? = null,
  /** 파트너에 대한 메모 */
  val memo: String? = null,
  /** 파트너의 태그 리스트 */
  val tags: List<String>? = null,
  /** 파트너 유형별 정보 */
  val type: UpdatePlatformPartnerBodyType? = null,
  /** 사용자 정의 속성 */
  val userDefinedProperties: PlatformProperties? = null,
)


