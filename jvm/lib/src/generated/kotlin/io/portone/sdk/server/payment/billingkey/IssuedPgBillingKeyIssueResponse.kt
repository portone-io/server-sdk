package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.billingkey.BillingKeyPaymentMethod
import io.portone.sdk.server.payment.billingkey.PgBillingKeyIssueResponse
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 빌링키 발급 성공 채널 응답 */
@Serializable
@SerialName("ISSUED")
public data class IssuedPgBillingKeyIssueResponse(
  /**
   * 채널
   *
   * 빌링키 발급을 시도한 채널입니다.
   */
  override val channel: SelectedChannel,
  /** PG사 거래 아이디 */
  val pgTxId: String? = null,
  /**
   * 빌링키 결제수단 상세 정보
   *
   * 채널에 대응되는 PG사에서 응답한 빌링키 발급 수단 정보입니다.
   */
  val method: BillingKeyPaymentMethod? = null,
): PgBillingKeyIssueResponse
