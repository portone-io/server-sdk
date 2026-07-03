package io.portone.sdk.server.paymentsession

import io.portone.sdk.server.common.CheckoutPaymentMethod
import io.portone.sdk.server.common.Country
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.paymentsession.PaymentSessionAgreement
import io.portone.sdk.server.paymentsession.PaymentSessionColors
import io.portone.sdk.server.paymentsession.PaymentSessionProduct
import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 세션 */
@Serializable
public data class PaymentSession(
  /** 결제 세션 아이디 */
  val id: String,
  /** 상점 아이디 */
  val storeId: String,
  /** 결제 건 아이디 */
  val paymentId: String,
  /** 프로필 키 */
  val profileKey: String,
  /**
   * 결제 수단 지정
   *
   * 지정한 경우, 정보 추가 입력이 필요하지 않은 경우에 주문서를 건너뛰고 결제로 바로 이동합니다.
   */
  val paymentMethod: CheckoutPaymentMethod? = null,
  /** 국가 */
  val country: Country,
  /** 통화 */
  val currency: Currency,
  /** 전체 결제 금액 */
  val totalAmount: Long,
  /** 주문명 */
  val orderName: String,
  /**
   * 결제 완료 후 리다이렉트 URL
   *
   * 지정하지 않으면 기본 결과 페이지가 표시됩니다.
   */
  val redirectUrl: String? = null,
  /** 주문 항목 목록 */
  val products: List<PaymentSessionProduct>? = null,
  /** 구매자 이름 */
  val customerName: String? = null,
  /** 구매자 이메일 */
  val customerEmail: String? = null,
  /**
   * 상점 이름
   *
   * 페이지 헤더 및 결제사 UI에 표시됩니다.
   */
  val storeName: String? = null,
  /**
   * 사용자 지정 약관 목록
   *
   * 구매자가 모든 약관에 동의해야 결제 버튼이 활성화됩니다.
   */
  val agreements: List<PaymentSessionAgreement>? = null,
  /** 주문 대표 이미지 URL */
  val orderImageUrl: String? = null,
  /**
   * 사용자 지정 데이터
   *
   * 결제 완료 후 결제 건 조회에서도 확인할 수 있습니다.
   */
  val customData: String? = null,
  /** 체크아웃 페이지 색 설정 */
  val colors: PaymentSessionColors? = null,
  /** 생성 시각 */
  val createdAt: @Serializable(InstantSerializer::class) Instant,
  /** 만료 시각 */
  val expiresAt: @Serializable(InstantSerializer::class) Instant,
)


