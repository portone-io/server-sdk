package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyDiscount
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyExternalCancellationDetail
import io.portone.sdk.server.platform.transfer.CreatePlatformOrderCancelTransferBodyOrderDetail
import io.portone.sdk.server.platform.transfer.PlatformUserDefinedPropertyKeyValue
import kotlin.String
import kotlinx.serialization.Serializable

/**
 * 주문 취소 정산 등록을 위한 입력 정보
 *
 * 하나의 payment에 하나의 정산 건만 존재하는 경우에는 (partnerId, paymentId)로 취소 정산을 등록하실 수 있습니다.
 * 하나의 payment에 여러 개의 정산 건이 존재하는 경우에는 transferId를 필수로 입력해야 합니다.
 * transferId를 입력한 경우 (partnerId, paymentId)는 생략 가능합니다.
 */
@Serializable
internal data class CreatePlatformOrderCancelTransferBody(
  /** 취소 내역 아이디 */
  val cancellationId: String,
  /** 할인 정보 */
  val discounts: List<CreatePlatformOrderCancelTransferBodyDiscount>,
  /** 파트너 아이디 */
  val partnerId: String? = null,
  /** 결제 아이디 */
  val paymentId: String? = null,
  /** 정산건 아이디 */
  val transferId: String? = null,
  /** 메모 */
  val memo: String? = null,
  /** 주문 취소 정보 */
  val orderDetail: CreatePlatformOrderCancelTransferBodyOrderDetail? = null,
  /**
   * 주문 취소 면세 금액
   *
   * 주문 취소 항목과 취소 면세 금액을 같이 전달하시면 최종 취소 면세 금액은 주문 취소 항목의 면세 금액이 아닌 전달해주신 취소 면세 금액으로 적용됩니다.
   */
  val taxFreeAmount: Long? = null,
  /**
   * 정산 시작일
   *
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   */
  val settlementStartDate: String? = null,
  /**
   * 외부 결제 상세 정보
   *
   * 해당 정보가 존재하는 경우 외부 결제 취소 정산건으로 등록되고, 존재하지않은 경우 포트원 결제 취소 정산건으로 등록됩니다.
   */
  val externalCancellationDetail: CreatePlatformOrderCancelTransferBodyExternalCancellationDetail? = null,
  /**
   * 테스트 모드 여부
   *
   * 기본값은 false 입니다.
   */
  val isForTest: Boolean? = null,
  /** 사용자 정의 속성 */
  val userDefinedProperties: List<PlatformUserDefinedPropertyKeyValue>? = null,
)
