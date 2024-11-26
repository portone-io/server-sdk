package io.portone.sdk.server.payment

import io.portone.sdk.server.payment.PaymentMethodGiftCertificateType
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 상품권 상세 정보 */
@Serializable
@SerialName("PaymentMethodGiftCertificate")
public data class PaymentMethodGiftCertificate(
  /** 상품권 종류 */
  val giftCertificateType: PaymentMethodGiftCertificateType? = null,
  /** 상품권 승인 번호 */
  val approvalNumber: String,
) : PaymentMethod.Recognized


