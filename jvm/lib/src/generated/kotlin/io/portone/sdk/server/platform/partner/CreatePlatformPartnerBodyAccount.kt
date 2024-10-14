package io.portone.sdk.server.platform.partner

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.common.Currency
import kotlin.String
import kotlinx.serialization.Serializable

/** 파트너 계좌 등록을 위한 정보 */
@Serializable
public data class CreatePlatformPartnerBodyAccount(
  /** 은행 */
  val bank: Bank,
  /** 정산에 사용할 통화 */
  val currency: Currency,
  /** 계좌번호 */
  val number: String,
  /** 예금주명 */
  val holder: String,
  /** 계좌 검증 아이디 */
  val accountVerificationId: String? = null,
)