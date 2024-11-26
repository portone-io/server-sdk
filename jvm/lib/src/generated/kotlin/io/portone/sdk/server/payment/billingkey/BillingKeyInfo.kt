package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.ChannelGroupSummary
import io.portone.sdk.server.common.Customer
import io.portone.sdk.server.common.SelectedChannel
import io.portone.sdk.server.payment.billingkey.BillingKeyPaymentMethod
import io.portone.sdk.server.payment.billingkey.PgBillingKeyIssueResponse
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 빌링키 정보 */
@Serializable(BillingKeyInfoSerializer::class)
public sealed interface BillingKeyInfo {
  @Serializable
  @JsonClassDiscriminator("status")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : BillingKeyInfo {
    /** 빌링키 */
    public val billingKey: String
    /** 고객사 아이디 */
    public val merchantId: String
    /** 상점 아이디 */
    public val storeId: String
    /**
     * 빌링키 결제수단 상세 정보
     *
     * 추후 슈퍼빌링키 기능 제공 시 여러 결제수단 정보가 담길 수 있습니다.
     */
    public val methods: List<BillingKeyPaymentMethod>?
    /**
     * 빌링키 발급 시 사용된 채널
     *
     * 추후 슈퍼빌링키 기능 제공 시 여러 채널 정보가 담길 수 있습니다.
     */
    public val channels: List<SelectedChannel>
    /** 고객 정보 */
    public val customer: Customer
    /** 사용자 지정 데이터 */
    public val customData: String?
    /** 고객사가 채번하는 빌링키 발급 건 고유 아이디 */
    public val issueId: String?
    /** 빌링키 발급 건 이름 */
    public val issueName: String?
    /** 발급 요청 시점 */
    public val requestedAt: Instant?
    /** 발급 시점 */
    public val issuedAt: Instant
    /** 채널 그룹 */
    public val channelGroup: ChannelGroupSummary?
    /**
     * 채널 별 빌링키 발급 응답
     *
     * 슈퍼빌링키의 경우, 빌링키 발급이 성공하더라도 일부 채널에 대한 빌링키 발급은 실패할 수 있습니다.
     */
    public val pgBillingKeyIssueResponses: List<PgBillingKeyIssueResponse>?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : BillingKeyInfo
}


private object BillingKeyInfoSerializer : JsonContentPolymorphicSerializer<BillingKeyInfo>(BillingKeyInfo::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["status"]?.jsonPrimitive?.contentOrNull) {
    "DELETED" -> DeletedBillingKeyInfo.serializer()
    "ISSUED" -> IssuedBillingKeyInfo.serializer()
    else -> BillingKeyInfo.Unrecognized.serializer()
  }
}
