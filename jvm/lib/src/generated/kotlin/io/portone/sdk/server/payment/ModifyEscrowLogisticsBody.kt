package io.portone.sdk.server.payment

import io.portone.sdk.server.common.PaymentProduct
import io.portone.sdk.server.payment.PaymentEscrowReceiverInput
import io.portone.sdk.server.payment.PaymentEscrowSenderInput
import io.portone.sdk.server.payment.PaymentLogistics
import kotlin.String
import kotlinx.serialization.Serializable

/** 에스크로 배송 정보 수정 입력 정보 */
@Serializable
internal data class ModifyEscrowLogisticsBody(
  /**
   * 상점 아이디
   *
   * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 인증 정보의 상점 아이디를 사용합니다.
   */
  val storeId: String? = null,
  /** 에스크로 발송자 정보 */
  val sender: PaymentEscrowSenderInput? = null,
  /** 에스크로 수취인 정보 */
  val receiver: PaymentEscrowReceiverInput? = null,
  /** 에스크로 물류 정보 */
  val logistics: PaymentLogistics,
  /**
   * 이메일 알림 전송 여부
   *
   * 에스크로 구매 확정 시 이메일로 알림을 보낼지 여부입니다.
   */
  val sendEmail: Boolean? = null,
  /** 상품 정보 */
  val products: List<PaymentProduct>? = null,
)


