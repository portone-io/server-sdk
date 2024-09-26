/**
 * 고정식 가상계좌 발급 유형
 *
 * pgAccountId, accountNumber 유형 중 한 개의 필드만 입력합니다.
 */
export type InstantPaymentMethodInputVirtualAccountOptionFixed = {
	/**
	 * Account ID 고정식 가상계좌
	 *
	 * 고객사가 가상계좌번호를 직접 관리하지 않고 PG사가 pgAccountId에 매핑되는 가상계좌번호를 내려주는 방식입니다.
	 * 동일한 pgAccountId로 가상계좌 발급 요청시에는 항상 같은 가상계좌번호가 내려옵니다.
	 */
	pgAccountId?: string
	/**
	 * Account Number 고정식 가상계좌
	 *
	 * PG사가 일정 개수만큼의 가상계좌번호를 발급하여 고객사에게 미리 전달하고 고객사가 그 중 하나를 선택하여 사용하는 방식입니다.
	 */
	accountNumber?: string
}
