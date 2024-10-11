package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyTypeBusiness
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyTypeNonWhtPayer
import io.portone.sdk.server.platform.partner.CreatePlatformPartnerBodyTypeWhtPayer
import kotlinx.serialization.Serializable

/** 파트너 생성을 위한 유형별 추가 정보 */
@Serializable
public data class CreatePlatformPartnerBodyType(
  /** 사업자 추가 정보 */
  val business: CreatePlatformPartnerBodyTypeBusiness? = null,
  /** 원천징수 대상자 추가 정보 */
  val whtPayer: CreatePlatformPartnerBodyTypeWhtPayer? = null,
  /** 원천징수 비대상자 추가 정보 */
  val nonWhtPayer: CreatePlatformPartnerBodyTypeNonWhtPayer? = null,
)
