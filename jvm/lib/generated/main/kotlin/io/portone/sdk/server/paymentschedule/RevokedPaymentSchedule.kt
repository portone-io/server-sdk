package io.portone.sdk.server.paymentschedule

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.PaymentProduct
import kotlin.Array
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 예약 취소 상태 */
@Serializable
@SerialName("REVOKED")
public data class RevokedPaymentSchedule(
  /** 결제 예약 건 아이디 */
  override val id: String,
  /** 고객사 아이디 */
  override val merchantId: String,
  /** 상점 아이디 */
  override val storeId: String,
  /** 결제 건 아이디 */
  override val paymentId: String,
  /** 빌링키 */
  override val billingKey: String,
  /** 주문명 */
  override val orderName: String,
  /** 문화비 지출 여부 */
  override val isCulturalExpense: Boolean,
  /** 에스크로 결제 여부 */
  override val isEscrow: Boolean,
  /** 고객 정보 */
  override val customer: Customer,
  /** 사용자 지정 데이터 */
  override val customData: String,
  /** 결제 총 금액 */
  override val totalAmount: Long,
  /** 통화 */
  override val currency: Currency,
  /** 결제 예약 등록 시점 */
  override val createdAt: Instant,
  /** 결제 예정 시점 */
  override val timeToPay: Instant,
  /** 결제 취소 시점 */
  val revokedAt: Instant,
  /** 면세액 */
  override val taxFreeAmount: Long? = null,
  /** 부가세 */
  override val vatAmount: Long? = null,
  /** 할부 개월 수 */
  override val installmentMonth: Int? = null,
  /** 웹훅 주소 */
  override val noticeUrls: Array<String>? = null,
  /** 상품 정보 */
  override val products: Array<PaymentProduct>? = null,
): PaymentSchedule,
