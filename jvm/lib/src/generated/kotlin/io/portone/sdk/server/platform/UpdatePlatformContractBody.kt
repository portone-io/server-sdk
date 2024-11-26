package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.PlatformFeeInput
import io.portone.sdk.server.platform.PlatformPayer
import io.portone.sdk.server.platform.PlatformSettlementCycleInput
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 계약 업데이트를 위한 입력 정보. 값이 명시되지 않은 필드는 업데이트되지 않습니다.
 *
 * 값이 명시되지 않은 필드는 업데이트되지 않습니다.
 */
@Serializable
public data class UpdatePlatformContractBody(
  /** 계약 이름 */
  val name: String? = null,
  /** 계약 내부 표기를 위한 메모 */
  val memo: String? = null,
  /** 중개수수료 */
  val platformFee: PlatformFeeInput? = null,
  /** 정산 주기 */
  val settlementCycle: PlatformSettlementCycleInput? = null,
  /** 중개수수료에 대한 부가세 부담 주체 */
  val platformFeeVatPayer: PlatformPayer? = null,
  /** 정산 시 결제금액 부가세 감액 여부 */
  val subtractPaymentVatAmount: Boolean? = null,
)


