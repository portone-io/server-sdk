package io.portone.sdk.server.payment.billingkey

import io.portone.sdk.server.common.CustomerInput
import io.portone.sdk.server.payment.billingkey.InstantBillingKeyPaymentMethodInput
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonObject

/** 빌링키 발급 요청 양식 */
@Serializable
internal data class IssueBillingKeyBody(
  /**
   * 상점 아이디
   *
   * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
   */
  val storeId: String? = null,
  /** 빌링키 결제 수단 정보 */
  val method: InstantBillingKeyPaymentMethodInput,
  /**
   * 채널 키
   *
   * 채널 키 또는 채널 그룹 ID 필수
   */
  val channelKey: String? = null,
  /**
   * 채널 그룹 ID
   *
   * 채널 키 또는 채널 그룹 ID 필수
   */
  val channelGroupId: String? = null,
  /** 고객 정보 */
  val customer: CustomerInput? = null,
  /** 사용자 지정 데이터 */
  val customData: String? = null,
  val bypass: JsonObject? = null,
  /**
   * 웹훅 주소
   *
   * 빌링키 발급 시 요청을 받을 웹훅 주소입니다.
   * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
   * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
   */
  val noticeUrls: List<String>? = null,
)


