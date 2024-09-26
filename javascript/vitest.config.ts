import { defineConfig } from "vitest/config";

export default defineConfig({
	server: {
		fs: {
			// https://github.com/vitest-dev/vitest/issues/6152
			cachedChecks: false,
		},
	},
});
