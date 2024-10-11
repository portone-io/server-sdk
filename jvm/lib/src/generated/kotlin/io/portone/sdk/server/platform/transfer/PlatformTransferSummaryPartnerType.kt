package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.Serializable

/** 파트너 유형 */
@Serializable
public enum class PlatformTransferSummaryPartnerType {
  /** 사업자 */
  BUSINESS,
  /** 원천징수 대상자 */
  WHT_PAYER,
  /** 원천징수 비대상자 */
  NON_WHT_PAYER,
}
