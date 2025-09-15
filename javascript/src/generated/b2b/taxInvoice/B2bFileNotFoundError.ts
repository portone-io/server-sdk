/** 업로드한 파일을 찾을 수 없는 경우 */
export type B2bFileNotFoundError = {
	type: "B2B_FILE_NOT_FOUND"
	message?: string
}
