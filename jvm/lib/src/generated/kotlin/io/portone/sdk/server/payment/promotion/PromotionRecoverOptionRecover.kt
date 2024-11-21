package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 결제 취소 시 프로모션 예산 복구 */
@Serializable
@SerialName("RECOVER")
public data object PromotionRecoverOptionRecover : PromotionRecoverOption.Recognized
