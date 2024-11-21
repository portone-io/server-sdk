package io.portone.sdk.server.platform.policy

import io.portone.sdk.server.platform.PlatformFeeInput
import io.portone.sdk.server.platform.PlatformPayer
import io.portone.sdk.server.platform.PlatformSettlementCycleInput
import kotlin.String
import kotlinx.serialization.Serializable

/** 계약 객체 생성을 위한 입력 정보 */
@Serializable
internal data class CreatePlatformContractBody(
  /**
   * 계약에 부여할 고유 아이디
   *
   * 명시하지 않는 경우 포트원이 임의의 아이디를 발급해드립니다.
   */
  val id: String? = null,
  /** 계약 이름 */
  val name: String,
  /** 계약 내부 표기를 위한 메모 */
  val memo: String? = null,
  /** 중개수수료 */
  val platformFee: PlatformFeeInput,
  /** 정산 주기 */
  val settlementCycle: PlatformSettlementCycleInput,
  /** 중개수수료에 대한 부가세 부담 주체 */
  val platformFeeVatPayer: PlatformPayer,
  /** 정산 시 결제금액 부가세 감액 여부 */
  val subtractPaymentVatAmount: Boolean,
)
