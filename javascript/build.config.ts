import fs from "node:fs/promises";
import { defineBuildConfig, MkdistBuildEntry } from "unbuild";
import tsConfig from "./tsconfig.json";
import packageJson from "./package.json";

export default defineBuildConfig({
	entries: (["esm", "cjs"] as const).map(
		(format): MkdistBuildEntry => ({
			builder: "mkdist",
			input: "./src",
			format,
			ext: (
				{
					esm: "mjs",
					cjs: "cjs",
				} as const
			)[format],
			declaration: true,
			addRelativeDeclarationExtensions: true,
			typescript: {
				compilerOptions: tsConfig.compilerOptions,
			},
		}),
	),
	hooks: {
		"mkdist:entry:build": async (_ctx, _entry, output) => {
			const userAgent = `portone-server-sdk-js/$${packageJson.version}`;
			await Promise.all(
				output.writtenFiles.map(async (file) => {
					const content = await fs.readFile(file, { encoding: "utf-8" });
					return fs.writeFile(
						file,
						content.replace("__USER_AGENT__", userAgent),
					);
				}),
			);
		},
	},
});
