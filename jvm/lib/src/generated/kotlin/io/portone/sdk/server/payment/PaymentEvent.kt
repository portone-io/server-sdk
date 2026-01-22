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
import java.time.Instant
import kotlin.String
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 결제 이벤트 */
@Serializable(PaymentEventSerializer::class)
public sealed interface PaymentEvent {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PaymentEvent {
    /** 결제 이벤트 아이디 */
    public val id: String
    /** 결제 건 아이디 */
    public val paymentId: String
    /** 결제 시도 아이디 */
    public val transactionId: String
    /** 고객사 아이디 */
    public val merchantId: String
    /** 상점 아이디 */
    public val storeId: String
    /** 결제수단 정보 */
    public val method: PaymentMethod?
    /** 결제 채널 */
    public val channel: SelectedChannel
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
    /** 웹훅 발송 내역 */
    public val webhooks: List<PaymentWebhook>?
    /** 결제 요청 시점 */
    public val requestedAt: Instant
    /** 이벤트 생성 시점 */
    public val createdAt: Instant
    /** 주문명 */
    public val orderName: String
    /** 총 결제 금액 관련 세부 정보 */
    public val totalAmount: PaymentAmount
    /** 통화 */
    public val currency: Currency
    /** 구매자 정보 */
    public val customer: Customer
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
    /** PG사 거래 아이디 */
    public val pgTxId: String?
    /** 현금영수증 */
    public val cashReceipt: PaymentCashReceipt?
    /** 거래 영수증 URL */
    public val receiptUrl: String?
    /** 프로모션 아이디 */
    public val promotionId: String?
    /**
     * 처리 금액
     *
     * 해당 이벤트에서 처리된 금액으로, 취소 이벤트인 경우 음수로 표기됩니다.
     */
    public val eventAmount: Long
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PaymentEvent
}


public object PaymentEventSerializer : JsonContentPolymorphicSerializer<PaymentEvent>(PaymentEvent::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PaymentEvent> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "CANCELLED" -> CancelledPaymentEvent.serializer()
      "PAID" -> PaidPaymentEvent.serializer()
      "PARTIAL_CANCELLED" -> PartialCancelledPaymentEvent.serializer()
      else -> PaymentEvent.Unrecognized.serializer()
    }
}
