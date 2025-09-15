package io.portone.sdk.server.b2b.taxinvoice

import io.portone.sdk.server.b2b.taxinvoice.GetB2bTaxInvoicesBodyFilter
import kotlinx.serialization.Serializable

/** 세금 계산서 다건 조회를 위한 입력 정보 */
@Serializable
internal data class GetB2bTaxInvoicesBody(
  /**
   * 테스트 모드 여부
   *
   * true 이면 테스트 모드로 실행되며, false 이거나 주어지지 않은 경우 테스트 모드를 사용하지 않습니다.
   */
  val test: Boolean? = null,
  /**
   * 페이지 번호
   *
   * 0부터 시작하는 페이지 번호. 기본 값은 0.
   */
  val pageNumber: Int? = null,
  /**
   * 페이지 크기
   *
   * 각 페이지 당 포함할 객체 수. 기본 값은 500이며 최대 1000까지 요청가능합니다.
   */
  val pageSize: Int? = null,
  /** 필터 */
  val filter: GetB2bTaxInvoicesBodyFilter? = null,
)


