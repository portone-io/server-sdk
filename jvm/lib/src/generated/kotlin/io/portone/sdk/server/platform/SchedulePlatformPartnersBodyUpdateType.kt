package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdateTypeBusiness
import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdateTypeNonWhtPayer
import io.portone.sdk.server.platform.SchedulePlatformPartnersBodyUpdateTypeWhtPayer
import kotlinx.serialization.Serializable

/**
 * 파트너 유형별 정보 업데이트를 위한 입력 정보
 *
 * 파트너 유형별 추가 정보를 수정합니다.
 * 최초 생성된 유형 내에서 세부 정보만 수정할 수 있고 파트너의 유형 자체를 수정할 수는 없습니다.
 */
@Serializable
public data class SchedulePlatformPartnersBodyUpdateType(
  /** 사업자 추가 정보 */
  val business: SchedulePlatformPartnersBodyUpdateTypeBusiness? = null,
  /** 원천징수 대상자 추가 정보 */
  val whtPayer: SchedulePlatformPartnersBodyUpdateTypeWhtPayer? = null,
  /** 원천징수 비대상자 추가 정보 */
  val nonWhtPayer: SchedulePlatformPartnersBodyUpdateTypeNonWhtPayer? = null,
)
