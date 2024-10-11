package io.portone.sdk.server.paymentschedule

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.PaymentProduct
import kotlin.Array
import kotlin.String
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 예약 건 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface PaymentSchedule {
  /** 결제 예약 건 아이디 */
  val id: String
  /** 고객사 아이디 */
  val merchantId: String
  /** 상점 아이디 */
  val storeId: String
  /** 결제 건 아이디 */
  val paymentId: String
  /** 빌링키 */
  val billingKey: String
  /** 주문명 */
  val orderName: String
  /** 문화비 지출 여부 */
  val isCulturalExpense: Boolean
  /** 에스크로 결제 여부 */
  val isEscrow: Boolean
  /** 고객 정보 */
  val customer: Customer
  /** 사용자 지정 데이터 */
  val customData: String
  /** 결제 총 금액 */
  val totalAmount: Long
  /** 면세액 */
  val taxFreeAmount: Long?
  /** 부가세 */
  val vatAmount: Long?
  /** 통화 */
  val currency: Currency
  /** 할부 개월 수 */
  val installmentMonth: Int?
  /** 웹훅 주소 */
  val noticeUrls: Array<String>?
  /** 상품 정보 */
  val products: Array<PaymentProduct>?
  /** 결제 예약 등록 시점 */
  val createdAt: Instant,
  /** 결제 예정 시점 */
  val timeToPay: Instant,
}
