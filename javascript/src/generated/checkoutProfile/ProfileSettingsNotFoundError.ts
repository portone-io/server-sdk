/** 프로필 설정이 존재하지 않는 경우 */
export type ProfileSettingsNotFoundError = {
	type: "PROFILE_SETTINGS_NOT_FOUND"
	message?: string
}
