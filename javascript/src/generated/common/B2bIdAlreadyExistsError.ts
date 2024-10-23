/** ID가 이미 사용중인 경우 */
export type B2bIdAlreadyExistsError = {
	type: "B2B_ID_ALREADY_EXISTS"
	message?: string
}
