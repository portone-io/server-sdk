package io.portone.sdk.server.platform.transfer

import io.portone.sdk.server.platform.transfer.PlatformPaymentMethodCardInput
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethodEasyPayInput
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethodGiftCertificateInput
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethodMobileInput
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethodTransferInput
import io.portone.sdk.server.platform.transfer.PlatformPaymentMethodVirtualAccountInput
import kotlinx.serialization.Serializable

/** 결제 수단 입력 정보 */
@Serializable
public data class PlatformPaymentMethodInput(
  /** 카드 */
  val card: PlatformPaymentMethodCardInput? = null,
  /** 계좌이체 */
  val transfer: PlatformPaymentMethodTransferInput? = null,
  /** 가상계좌 */
  val virtualAccount: PlatformPaymentMethodVirtualAccountInput? = null,
  /** 상품권 */
  val giftCertificate: PlatformPaymentMethodGiftCertificateInput? = null,
  /** 모바일 */
  val mobile: PlatformPaymentMethodMobileInput? = null,
  /** 간편 결제 */
  val easyPay: PlatformPaymentMethodEasyPayInput? = null,
)
