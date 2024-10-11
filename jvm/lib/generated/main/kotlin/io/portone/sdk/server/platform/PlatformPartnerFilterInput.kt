package io.portone.sdk.server.platform

import io.portone.sdk.server.common.Bank
import io.portone.sdk.server.common.Currency
import io.portone.sdk.server.platform.PlatformPartnerFilterInputKeyword
import kotlin.Array
import kotlin.String
import kotlinx.serialization.Serializable

/** 파트너 필터 입력 정보 */
@Serializable
public data class PlatformPartnerFilterInput(
  /**
   * 보관 조회 여부
   *
   * true 이면 보관된 파트너를 조회하고, false 이면 보관되지 않은 파트너를 조회합니다. 기본값은 false 입니다.
   */
  val isArchived: Boolean? = null,
  /** 하나 이상의 값이 존재하는 경우 해당 리스트에 포함되는 태그를 하나 이상 가지는 파트너만 조회합니다. */
  val tags: Array<String>? = null,
  /**
   * 은행
   *
   * 하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 계좌 은행을 가진 파트너만 조회합니다.
   */
  val banks: Array<Bank>? = null,
  /**
   * 통화 단위
   *
   * 하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 계좌 통화를 가진 파트너만 조회합니다.
   */
  val accountCurrencies: Array<Currency>? = null,
  /** 하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 아이디를 가진 파트너만 조회합니다. */
  val ids: Array<String>? = null,
  /** 하나 이상의 값이 존재하는 경우,  해당 리스트에 포함되는 기본 계약 id를 가진 파트너만 조회합니다. */
  val contractIds: Array<String>? = null,
  /** 검색 키워드 */
  val keyword: PlatformPartnerFilterInputKeyword? = null,
)
