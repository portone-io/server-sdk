package io.portone.sdk.server.payment.paymentschedule

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.PaymentProduct
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약 취소 상태 */
@Serializable
@SerialName("REVOKED")
public data class RevokedPaymentSchedule(
  /** 결제 예약 건 아이디 */
  val id: String,
  /** 고객사 아이디 */
  val merchantId: String,
  /** 상점 아이디 */
  val storeId: String,
  /** 결제 건 아이디 */
  val paymentId: String,
  /** 빌링키 */
  val billingKey: String,
  /** 주문명 */
  val orderName: String,
  /** 문화비 지출 여부 */
  val isCulturalExpense: Boolean,
  /** 에스크로 결제 여부 */
  val isEscrow: Boolean,
  /** 고객 정보 */
  val customer: Customer,
  /** 사용자 지정 데이터 */
  val customData: String,
  /** 결제 총 금액 */
  val totalAmount: Long,
  /** 통화 */
  val currency: Currency,
  /** 결제 예약 등록 시점 */
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 결제 예정 시점 */
  val timeToPay: @Serializable(InstantSerializer::class) Instant,
  /** 결제 취소 시점 */
  val revokedAt: @Serializable(InstantSerializer::class) Instant,
  /** 면세액 */
  val taxFreeAmount: Long? = null,
  /** 부가세 */
  val vatAmount: Long? = null,
  /** 할부 개월 수 */
  val installmentMonth: Int? = null,
  /** 웹훅 주소 */
  val noticeUrls: List<String>? = null,
  /** 상품 정보 */
  val products: List<PaymentProduct>? = null,
) : PaymentSchedule
