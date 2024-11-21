package io.portone.sdk.server.payment.paymentschedule

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.PaymentProduct
import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 결제 예약 건 */
@Serializable
@JsonClassDiscriminator("status")
public sealed interface PaymentSchedule {
  public sealed interface Recognized : PaymentSchedule {
    /** 결제 예약 건 아이디 */
    public val id: String
    /** 고객사 아이디 */
    public val merchantId: String
    /** 상점 아이디 */
    public val storeId: String
    /** 결제 건 아이디 */
    public val paymentId: String
    /** 빌링키 */
    public val billingKey: String
    /** 주문명 */
    public val orderName: String
    /** 문화비 지출 여부 */
    public val isCulturalExpense: Boolean
    /** 에스크로 결제 여부 */
    public val isEscrow: Boolean
    /** 고객 정보 */
    public val customer: Customer
    /** 사용자 지정 데이터 */
    public val customData: String
    /** 결제 총 금액 */
    public val totalAmount: Long
    /** 면세액 */
    public val taxFreeAmount: Long?
    /** 부가세 */
    public val vatAmount: Long?
    /** 통화 */
    public val currency: Currency
    /** 할부 개월 수 */
    public val installmentMonth: Int?
    /** 웹훅 주소 */
    public val noticeUrls: List<String>?
    /** 상품 정보 */
    public val products: List<PaymentProduct>?
    /** 결제 예약 등록 시점 */
    public val createdAt: Instant
    /** 결제 예정 시점 */
    public val timeToPay: Instant
  }
  public data object Unrecognized : PaymentSchedule
}
