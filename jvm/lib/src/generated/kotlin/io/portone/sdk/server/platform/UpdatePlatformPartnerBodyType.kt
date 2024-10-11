package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyTypeBusiness
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyTypeNonWhtPayer
import io.portone.sdk.server.platform.UpdatePlatformPartnerBodyTypeWhtPayer
import kotlinx.serialization.Serializable

/**
 * 파트너 업데이트를 위한 유형별 추가 정보
 *
 * 파트너 유형별 추가 정보를 수정합니다.
 * 기존과 다른 파트너 유형 정보가 입력된 경우, 파트너의 유형 자체가 변경됩니다.
 */
@Serializable
public data class UpdatePlatformPartnerBodyType(
  /** 사업자 추가 정보 */
  val business: UpdatePlatformPartnerBodyTypeBusiness? = null,
  /** 원천징수 대상자 추가 정보 */
  val whtPayer: UpdatePlatformPartnerBodyTypeWhtPayer? = null,
  /** 원천징수 비대상자 추가 정보 */
  val nonWhtPayer: UpdatePlatformPartnerBodyTypeNonWhtPayer? = null,
)
