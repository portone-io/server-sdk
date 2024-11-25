package io.portone.sdk.server.payment

import io.portone.sdk.server.common.ChannelGroupSummary
import io.portone.sdk.server.common.Country
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.PaymentProduct
import io.portone.sdk.server.common.PortOneVersion
import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.PaymentAmount
import io.portone.sdk.server.payment.PaymentEscrow
import io.portone.sdk.server.payment.PaymentMethod
import io.portone.sdk.server.payment.PaymentWebhook
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 결제 건 */
@Serializable(PaymentSerializer::class)
public sealed interface Payment {
  @Serializable
  @JsonClassDiscriminator("status")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : Payment {
    /** 결제 건 아이디 */
    public val id: String
    /** 고객사 아이디 */
    public val merchantId: String
    /** 상점 아이디 */
    public val storeId: String
    /** 결제수단 정보 */
    public val method: PaymentMethod?
    /** 결제 채널 */
    public val channel: SelectedChannel?
    /** 결제 채널 그룹 정보 */
    public val channelGroup: ChannelGroupSummary?
    /** 포트원 버전 */
    public val version: PortOneVersion
    /**
     * 결제 예약 건 아이디
     *
     * 결제 예약을 이용한 경우에만 존재
     */
    public val scheduleId: String?
    /**
     * 결제 시 사용된 빌링키
     *
     * 빌링키 결제인 경우에만 존재
     */
    public val billingKey: String?
    /** 웹훅 발송 내역 */
    public val webhooks: List<PaymentWebhook>?
    /** 결제 요청 시점 */
    public val requestedAt: Instant
    /** 업데이트 시점 */
    public val updatedAt: Instant
    /** 상태 업데이트 시점 */
    public val statusChangedAt: Instant
    /** 주문명 */
    public val orderName: String
    /** 결제 금액 관련 세부 정보 */
    public val amount: PaymentAmount
    /** 통화 */
    public val currency: Currency
    /** 구매자 정보 */
    public val customer: Customer
    /** 프로모션 아이디 */
    public val promotionId: String?
    /** 문화비 지출 여부 */
    public val isCulturalExpense: Boolean?
    /**
     * 에스크로 결제 정보
     *
     * 에스크로 결제인 경우 존재합니다.
     */
    public val escrow: PaymentEscrow?
    /** 상품 정보 */
    public val products: List<PaymentProduct>?
    /** 상품 갯수 */
    public val productCount: Int?
    /** 사용자 지정 데이터 */
    public val customData: String?
    /** 국가 코드 */
    public val country: Country?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : Payment
}


private object PaymentSerializer : JsonContentPolymorphicSerializer<Payment>(Payment::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["status"]?.jsonPrimitive?.contentOrNull) {
    "CANCELLED" -> CancelledPayment.serializer()
    "FAILED" -> FailedPayment.serializer()
    "PAID" -> PaidPayment.serializer()
    "PARTIAL_CANCELLED" -> PartialCancelledPayment.serializer()
    "PAY_PENDING" -> PayPendingPayment.serializer()
    "READY" -> ReadyPayment.serializer()
    "VIRTUAL_ACCOUNT_ISSUED" -> VirtualAccountIssuedPayment.serializer()
    else -> Payment.Unrecognized.serializer()
  }
}
