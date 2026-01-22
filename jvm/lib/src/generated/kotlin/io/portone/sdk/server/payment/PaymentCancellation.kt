package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.Trigger
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

/** 결제 취소 내역 */
@Serializable(PaymentCancellationSerializer::class)
public sealed interface PaymentCancellation {
  @Serializable
  @JsonClassDiscriminator("status")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PaymentCancellation {
    /** 취소 내역 아이디 */
    public val id: String
    /** PG사 결제 취소 내역 아이디 */
    public val pgCancellationId: String?
    /** 취소 금액 */
    public val totalAmount: Long
    /** 취소 금액 중 면세 금액 */
    public val taxFreeAmount: Long
    /** 취소 금액 중 부가세액 */
    public val vatAmount: Long
    /** 적립형 포인트의 환불 금액 */
    public val easyPayDiscountAmount: Long?
    /** 취소 사유 */
    public val reason: String
    /** 취소 시점 */
    public val cancelledAt: Instant?
    /** 취소 요청 시점 */
    public val requestedAt: Instant
    /** 취소 요청 경로 */
    public val trigger: Trigger?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PaymentCancellation
}


public object PaymentCancellationSerializer : JsonContentPolymorphicSerializer<PaymentCancellation>(PaymentCancellation::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PaymentCancellation> =
    when (element.jsonObject["status"]?.jsonPrimitive?.contentOrNull) {
      "FAILED" -> FailedPaymentCancellation.serializer()
      "REQUESTED" -> RequestedPaymentCancellation.serializer()
      "SUCCEEDED" -> SucceededPaymentCancellation.serializer()
      else -> PaymentCancellation.Unrecognized.serializer()
    }
}
