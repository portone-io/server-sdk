package io.portone.sdk.server.payment.paymentschedule

import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.PaymentProduct
import java.time.Instant
import kotlin.Array
import kotlin.String
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 결제 예약 건 */
@Serializable(PaymentScheduleSerializer::class)
public sealed interface PaymentSchedule {
  @Serializable
  @JsonClassDiscriminator("status")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PaymentSchedule
}


public object PaymentScheduleSerializer : JsonContentPolymorphicSerializer<PaymentSchedule>(PaymentSchedule::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PaymentSchedule> =
    when (element.jsonObject["status"]?.jsonPrimitive?.contentOrNull) {
      "FAILED" -> FailedPaymentSchedule.serializer()
      "PENDING" -> PendingPaymentSchedule.serializer()
      "REVOKED" -> RevokedPaymentSchedule.serializer()
      "SCHEDULED" -> ScheduledPaymentSchedule.serializer()
      "STARTED" -> StartedPaymentSchedule.serializer()
      "SUCCEEDED" -> SucceededPaymentSchedule.serializer()
      else -> PaymentSchedule.Unrecognized.serializer()
    }
}
