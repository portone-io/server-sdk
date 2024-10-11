package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentWebhookPaymentStatus
import io.portone.sdk.server.payment.PaymentWebhookRequest
import io.portone.sdk.server.payment.PaymentWebhookResponse
import io.portone.sdk.server.payment.PaymentWebhookStatus
import io.portone.sdk.server.payment.PaymentWebhookTrigger
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 성공 웹훅 내역 */
@Serializable
public data class PaymentWebhook(
  /** 웹훅 아이디 */
  val id: String,
  /**
   * 웹훅이 발송된 url
   *
   * V1 결제 건인 경우, 값이 존재하지 않습니다.
   */
  val url: String,
  /**
   * 웹훅 발송 시 결제 건 상태
   *
   * V1 결제 건인 경우, 값이 존재하지 않습니다.
   */
  val paymentStatus: PaymentWebhookPaymentStatus? = null,
  /** 웹훅 상태 */
  val status: PaymentWebhookStatus? = null,
  /**
   * 비동기 웹훅 여부
   *
   * V1 결제 건인 경우, 값이 존재하지 않습니다.
   */
  val isAsync: Boolean? = null,
  /** 현재 발송 횟수 */
  val currentExecutionCount: Int? = null,
  /** 최대 발송 횟수 */
  val maxExecutionCount: Int? = null,
  /** 웹훅 실행 맥락 */
  val trigger: PaymentWebhookTrigger? = null,
  /** 웹훅 요청 정보 */
  val request: PaymentWebhookRequest? = null,
  /** 웹훅 응답 정보 */
  val response: PaymentWebhookResponse? = null,
  /** 웹훅 처리 시작 시점 */
  val triggeredAt: Instant? = null,
)
