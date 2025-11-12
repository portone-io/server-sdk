package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyAdditionalFee
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyDiscount
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyExternalPaymentDetail
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderTransferBodyOrderDetail
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import io.portone.sdk.server.platform.transfer.TransferParameters
import kotlin.String
import kotlinx.serialization.Serializable

/** 주문 정산건 생성을 위한 입력 정보 */
@Serializable
internal data class CreatePlatformOrderTransferBody(
  /** 파트너 아이디 */
  val partnerId: String,
  /**
   * 계약 아이디
   *
   * 기본값은 파트너의 기본 계약 아이디 입니다.
   */
  val contractId: String? = null,
  /** 메모 */
  val memo: String? = null,
  /** 결제 아이디 */
  val paymentId: String,
  /** 주문 정보 */
  val orderDetail: CreatePlatformOrderTransferBodyOrderDetail,
  /**
   * 주문 면세 금액
   *
   * 주문 항목과 면세 금액을 같이 전달하시면 최종 면세 금액은 주문 항목의 면세 금액이 아닌 전달해주신 면세 금액으로 적용됩니다.
   */
  val taxFreeAmount: Long? = null,
  /**
   * 정산 시작일
   *
   * 기본값은 결제 일시 입니다.
   * (yyyy-MM-dd)
   */
  val settlementStartDate: String? = null,
  /**
   * 정산일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val settlementDate: String? = null,
  /** 할인 정보 */
  val discounts: List<CreatePlatformOrderTransferBodyDiscount>,
  /** 추가 수수료 정보 */
  val additionalFees: List<CreatePlatformOrderTransferBodyAdditionalFee>,
  /**
   * 외부 결제 상세 정보
   *
   * 해당 정보가 존재하는 경우 외부 결제 정산건 으로 등록되고, 존재하지않은 경우 포트원 결제 정산건으로 등록됩니다.
   */
  val externalPaymentDetail: CreatePlatformOrderTransferBodyExternalPaymentDetail? = null,
  /**
   * 테스트 모드 여부
   *
   * Query Parameter의 test에 값이 제공된 경우 Query Parameter의 test를 사용하고 해당 값은 무시됩니다.
   * Query Parameter의 test와 Request Body의 isForTest에 모두 값이 제공되지 않으면 기본값인 false로 적용됩니다.
   */
  val isForTest: Boolean? = null,
  /** 정산 파라미터 (실험기능) */
  val parameters: TransferParameters? = null,
  /** 사용자 정의 속성 */
  val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
)


