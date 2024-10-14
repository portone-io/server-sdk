import childProcess from "node:child_process";
import fs from "node:fs/promises";
import { type MkdistBuildEntry, defineBuildConfig } from "unbuild";
import tsConfig from "./tsconfig.json";

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
			const rev = await new Promise<string>((resolve, reject) =>
				childProcess.exec(
					"git describe --dirty --tags --match js-v* --first-parent",
					(error, stdout) => (error ? reject(error) : resolve(stdout)),
				),
			);
			const userAgent = `portone-server-sdk-js/${rev.trim()}`;
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
