package io.portone.sdk.server.payment

import io.portone.sdk.server.common.CashReceiptType
import io.portone.sdk.server.common.Currency
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 결제 건 내 현금영수증 정보 */
@Serializable(PaymentCashReceiptSerializer::class)
public sealed interface PaymentCashReceipt {
  @Serializable
  @JsonClassDiscriminator("status")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PaymentCashReceipt {
    /** 현금영수증 유형 */
    public val type: CashReceiptType?
    /** PG사 영수증 발급 아이디 */
    public val pgReceiptId: String?
    /** 승인 번호 */
    public val issueNumber: String
    /** 총 금액 */
    public val totalAmount: Long
    /** 면세액 */
    public val taxFreeAmount: Long?
    /** 통화 */
    public val currency: Currency
    /** 현금영수증 URL */
    public val url: String?
    /** 발급 시점 */
    public val issuedAt: Instant
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PaymentCashReceipt
}


private object PaymentCashReceiptSerializer : JsonContentPolymorphicSerializer<PaymentCashReceipt>(PaymentCashReceipt::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["status"]?.jsonPrimitive?.contentOrNull) {
    "CANCELLED" -> CancelledPaymentCashReceipt.serializer()
    "ISSUED" -> IssuedPaymentCashReceipt.serializer()
    else -> PaymentCashReceipt.Unrecognized.serializer()
  }
}
