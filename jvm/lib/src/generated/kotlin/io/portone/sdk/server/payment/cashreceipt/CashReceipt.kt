package io.portone.sdk.server.payment.cashreceipt

import io.portone.sdk.server.common.SelectedChannel
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 현금영수증 내역 */
@Serializable(CashReceiptSerializer::class)
public sealed interface CashReceipt {
  @Serializable
  @JsonClassDiscriminator("status")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CashReceipt {
    /** 고객사 아이디 */
    public val merchantId: String
    /** 상점 아이디 */
    public val storeId: String
    /** 결제 건 아이디 */
    public val paymentId: String
    /** 현금영수증 발급에 사용된 채널 */
    public val channel: SelectedChannel?
    /** 주문명 */
    public val orderName: String
    /** 수동 발급 여부 */
    public val isManual: Boolean
    /** 상태 업데이트 시점 */
    public val statusUpdatedAt: Instant?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CashReceipt
}


private object CashReceiptSerializer : JsonContentPolymorphicSerializer<CashReceipt>(CashReceipt::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["status"]?.jsonPrimitive?.contentOrNull) {
    "CANCELLED" -> CancelledCashReceipt.serializer()
    "ISSUED" -> IssuedCashReceipt.serializer()
    "ISSUE_FAILED" -> IssueFailedCashReceipt.serializer()
    else -> CashReceipt.Unrecognized.serializer()
  }
}
