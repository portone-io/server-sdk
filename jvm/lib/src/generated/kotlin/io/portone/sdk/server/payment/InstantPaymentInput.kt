package io.portone.sdk.server.payment

import io.portone.sdk.server.common.Country
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.common.CustomerInput
import io.portone.sdk.server.common.PaymentAmountInput
import io.portone.sdk.server.common.PaymentProduct
import io.portone.sdk.server.common.PaymentProductType
import io.portone.sdk.server.common.SeparatedAddressInput
import io.portone.sdk.server.payment.InstantPaymentMethodInput
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonObject

/** 수기 결제 요청 정보 */
@Serializable
internal data class InstantPaymentInput(
  /**
   * 상점 아이디
   *
   * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
   */
  val storeId: String? = null,
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
  /** 결제수단 정보 */
  val method: InstantPaymentMethodInput,
  /** 주문명 */
  val orderName: String,
  /**
   * 문화비 지출 여부
   *
   * 기본값은 false 입니다.
   */
  val isCulturalExpense: Boolean? = null,
  /**
   * 에스크로 결제 여부
   *
   * 기본값은 false 입니다.
   */
  val isEscrow: Boolean? = null,
  /** 고객 정보 */
  val customer: CustomerInput? = null,
  /** 사용자 지정 데이터 */
  val customData: String? = null,
  /** 결제 금액 세부 입력 정보 */
  val amount: PaymentAmountInput,
  /** 통화 */
  val currency: Currency,
  /** 결제 국가 */
  val country: Country? = null,
  /**
   * 웹훅 주소
   *
   * 결제 웹훅 주소입니다.
   * 상점에 설정되어 있는 값보다 우선적으로 적용됩니다.
   * 빈 배열은 무시됩니다.
   */
  val noticeUrls: List<String>? = null,
  /**
   * 상품 정보
   *
   * 입력된 값이 없을 경우에는 빈 배열로 해석됩니다.
   */
  val products: List<PaymentProduct>? = null,
  /** 상품 개수 */
  val productCount: Int? = null,
  /** 상품 유형 */
  val productType: PaymentProductType? = null,
  /** 배송지 주소 */
  val shippingAddress: SeparatedAddressInput? = null,
  /** 해당 결제에 적용할 프로모션 아이디 */
  val promotionId: String? = null,
  val bypass: JsonObject? = null,
)


