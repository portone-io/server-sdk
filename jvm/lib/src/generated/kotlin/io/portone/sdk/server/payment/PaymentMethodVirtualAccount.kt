package io.portone.sdk.server.payment

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.payment.PaymentMethodVirtualAccountRefundStatus
import io.portone.sdk.server.payment.PaymentMethodVirtualAccountType
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 가상계좌 상세 정보 */
@Serializable
@SerialName("PaymentMethodVirtualAccount")
public data class PaymentMethodVirtualAccount(
  /** 표준 은행 코드 */
  val bank: Bank? = null,
  /** 계좌번호 */
  val accountNumber: String,
  /** 계좌 유형 */
  val accountType: PaymentMethodVirtualAccountType? = null,
  /** 계좌주 */
  val remitteeName: String? = null,
  /** 송금인(입금자) */
  val remitterName: String? = null,
  /** 입금만료시점 */
  val expiredAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 계좌발급시점 */
  val issuedAt: @Serializable(InstantSerializer::class) Instant? = null,
  /** 가상계좌 결제가 환불 단계일 때의 환불 상태 */
  val refundStatus: PaymentMethodVirtualAccountRefundStatus? = null,
) : PaymentMethod.Recognized
