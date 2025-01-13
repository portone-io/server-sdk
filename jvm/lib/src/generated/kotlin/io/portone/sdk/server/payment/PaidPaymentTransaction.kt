package io.portone.sdk.server.payment

import io.portone.sdk.server.common.ChannelGroupSummary
import io.portone.sdk.server.common.Country
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.PaymentProduct
import io.portone.sdk.server.common.PortOneVersion
import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.PaymentAmount
import io.portone.sdk.server.payment.PaymentCashReceipt
import io.portone.sdk.server.payment.PaymentEscrow
import io.portone.sdk.server.payment.PaymentMethod
import io.portone.sdk.server.payment.PaymentWebhook
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 완료 상태 건 */
@Serializable
@SerialName("PAID")
public data class PaidPaymentTransaction(
  /**
   * 결제 시도 아이디 (transactionId)
   *
   * V1 결제 건의 경우 imp_uid에 해당합니다.
   */
  override val id: String,
  /** 결제 건 아이디 */
  override val paymentId: String,
  /** 고객사 아이디 */
  override val merchantId: String,
  /** 상점 아이디 */
  override val storeId: String,
  /** 결제수단 정보 */
  override val method: PaymentMethod? = null,
  /** 결제 채널 */
  override val channel: SelectedChannel,
  /** 결제 채널 그룹 정보 */
  override val channelGroup: ChannelGroupSummary? = null,
  /** 포트원 버전 */
  override val version: PortOneVersion,
  /**
   * 결제 예약 건 아이디
   *
   * 결제 예약을 이용한 경우에만 존재
   */
  override val scheduleId: String? = null,
  /**
   * 결제 시 사용된 빌링키
   *
   * 빌링키 결제인 경우에만 존재
   */
  override val billingKey: String? = null,
  /** 웹훅 발송 내역 */
  override val webhooks: List<PaymentWebhook>? = null,
  /** 결제 요청 시점 */
  override val requestedAt: @Serializable(InstantSerializer::class) Instant,
  /** 업데이트 시점 */
  override val updatedAt: @Serializable(InstantSerializer::class) Instant,
  /** 상태 업데이트 시점 */
  override val statusChangedAt: @Serializable(InstantSerializer::class) Instant,
  /** 주문명 */
  override val orderName: String,
  /** 결제 금액 관련 세부 정보 */
  override val amount: PaymentAmount,
  /** 통화 */
  override val currency: Currency,
  /** 구매자 정보 */
  override val customer: Customer,
  /** 프로모션 아이디 */
  override val promotionId: String? = null,
  /** 문화비 지출 여부 */
  override val isCulturalExpense: Boolean? = null,
  /**
   * 에스크로 결제 정보
   *
   * 에스크로 결제인 경우 존재합니다.
   */
  override val escrow: PaymentEscrow? = null,
  /** 상품 정보 */
  override val products: List<PaymentProduct>? = null,
  /** 상품 갯수 */
  override val productCount: Int? = null,
  /** 사용자 지정 데이터 */
  override val customData: String? = null,
  /** 국가 코드 */
  override val country: Country? = null,
  /** 결제 완료 시점 */
  val paidAt: @Serializable(InstantSerializer::class) Instant,
  /** PG사 거래 아이디 */
  val pgTxId: String? = null,
  /** PG사 거래 응답 본문 */
  val pgResponse: String? = null,
  /** 현금영수증 */
  val cashReceipt: PaymentCashReceipt? = null,
  /** 거래 영수증 URL */
  val receiptUrl: String? = null,
) : PaymentTransaction.Recognized


