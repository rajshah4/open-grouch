# Changelog

## [0.1.3](https://github.com/jpshackelford/open-grouch/compare/open-grouch-v0.1.2...open-grouch-v0.1.3) (2026-02-28)


### 🐛 Bug Fixes

* mock splash header for deterministic snapshot tests ([ef2a023](https://github.com/jpshackelford/open-grouch/commit/ef2a0234ddb5cd7d5449d385d2fdd523e252a96c))
* patch random.choice for deterministic snapshot tests ([afdca01](https://github.com/jpshackelford/open-grouch/commit/afdca0174b2445252c2976ff0d22253de5cfd061))
* resolve line length violations in personality.py ([f1ea6ce](https://github.com/jpshackelford/open-grouch/commit/f1ea6ce34d3a265672c3834957940edb543e0b84))
* seed random for deterministic snapshot tests ([156fbd6](https://github.com/jpshackelford/open-grouch/commit/156fbd68d9811cf1f3011fb66967ceb708a1a4ec))


### 🗑️ Grouch Personality

* add Oscar the Grouch personality to agent ([f17f1e1](https://github.com/jpshackelford/open-grouch/commit/f17f1e1c18ae2a91baccafbffb334633260675f1))

## [0.1.2](https://github.com/jpshackelford/open-grouch/compare/open-grouch-v0.1.1...open-grouch-v0.1.2) (2026-02-28)


### 🐛 Bug Fixes

* **ci:** prevent docs, chore, style, refactor, test, ci commits from triggering releases ([57a32ec](https://github.com/jpshackelford/open-grouch/commit/57a32ecb6a20a1bc7902fa3c7c7f796f65c42320))
* **ci:** prevent docs, chore, style, refactor, test, ci commits from triggering releases ([6389e3b](https://github.com/jpshackelford/open-grouch/commit/6389e3b22c3b13b9b9e95faa2b5bd3499e2ad69e))
* **ci:** use OpenHands LLM proxy for PR reviews ([303fdf3](https://github.com/jpshackelford/open-grouch/commit/303fdf3832187297cd31df27ab9a21e2c800dc44))
* **ci:** use ubuntu-24.04 for PR review workflow ([95d5c34](https://github.com/jpshackelford/open-grouch/commit/95d5c34d659ea741a5f11b3e8c7065b126271125))
* update splash screen to display Open Grouch branding and version ([599d08b](https://github.com/jpshackelford/open-grouch/commit/599d08bc4f886bc6d4a641bd4cdee836ad5796c9))
* update splash screen to display Open Grouch branding and version ([8d3cf0e](https://github.com/jpshackelford/open-grouch/commit/8d3cf0e7cfa3fc1996a98214dbdf450ebcaca5fe))

## [0.1.1](https://github.com/jpshackelford/open-grouch/compare/open-grouch-v0.1.0...open-grouch-v0.1.1) (2026-02-25)


### ✨ Features

* `/condense` command to force compact conversation history ([#191](https://github.com/jpshackelford/open-grouch/issues/191)) ([48f5782](https://github.com/jpshackelford/open-grouch/commit/48f578245a7b46ee95ee37e61a1f666d7f3dffb4))
* **acp:** Send LLM-generated summary to tool call title ([#332](https://github.com/jpshackelford/open-grouch/issues/332)) ([39919ec](https://github.com/jpshackelford/open-grouch/commit/39919eca949538f6db158ae863a7bbf57cf6a289))
* Add --always-approve and --llm-approve CLI arguments for confirmation mode ([#110](https://github.com/jpshackelford/open-grouch/issues/110)) ([d19029a](https://github.com/jpshackelford/open-grouch/commit/d19029a7aac3459642a97b2a1d16222e103af033))
* Add --version/-v flag support to print CLI version ([#113](https://github.com/jpshackelford/open-grouch/issues/113)) ([e7a45d2](https://github.com/jpshackelford/open-grouch/commit/e7a45d2ed842b2ee7696d76a1a748d90db3dc660)), closes [#112](https://github.com/jpshackelford/open-grouch/issues/112)
* Add dedicated plan window for agent task tracking ([#315](https://github.com/jpshackelford/open-grouch/issues/315)) ([b28106a](https://github.com/jpshackelford/open-grouch/commit/b28106a0f21dc0e80b2cfe3c5a9c9127ac0c17b2))
* Add details about recommended models and use cases in CLI settings ([#246](https://github.com/jpshackelford/open-grouch/issues/246)) ([#357](https://github.com/jpshackelford/open-grouch/issues/357)) ([b0f44ea](https://github.com/jpshackelford/open-grouch/commit/b0f44ead2c7210b35271bd04c58bb5d1a64c3926))
* Add drag-to-select auto-copy feature for conversation events ([#312](https://github.com/jpshackelford/open-grouch/issues/312)) ([29f7a8c](https://github.com/jpshackelford/open-grouch/commit/29f7a8c48a589ea4089833c8ab9f5c92ded16247)), closes [#296](https://github.com/jpshackelford/open-grouch/issues/296)
* add iterative refinement mode using critic model ([#447](https://github.com/jpshackelford/open-grouch/issues/447)) ([bb54d4e](https://github.com/jpshackelford/open-grouch/commit/bb54d4ef3d09bde8ea239f90968e219f4dd31aa5))
* add OpenHands stop hooks for pre-commit validation ([#487](https://github.com/jpshackelford/open-grouch/issues/487)) ([328326c](https://github.com/jpshackelford/open-grouch/commit/328326c0d018881920187534686fb85df60d6f8f))
* Add tabbed interface to settings modal ([#231](https://github.com/jpshackelford/open-grouch/issues/231)) ([d98c5bf](https://github.com/jpshackelford/open-grouch/commit/d98c5bf60ac20ac0beb3701f24f6b158b43e6b69))
* Add toggle for default cell expand/collapse state ([#295](https://github.com/jpshackelford/open-grouch/issues/295)) ([98c5a44](https://github.com/jpshackelford/open-grouch/commit/98c5a44023822bf06b1fdfe7df02022e865b7071))
* **cli:** add task & file params ([#131](https://github.com/jpshackelford/open-grouch/issues/131)) ([1549d83](https://github.com/jpshackelford/open-grouch/commit/1549d83a3d23465482983afece8d203c92534a98))
* **cli:** add threaded Ctrl-P pause listener for synchronous SDK ([#34](https://github.com/jpshackelford/open-grouch/issues/34)) ([83ea030](https://github.com/jpshackelford/open-grouch/commit/83ea0301f5a902002755effdabfbd3eaf7e7920d))
* Delegate conversation to cloud ([#230](https://github.com/jpshackelford/open-grouch/issues/230)) ([307b5e4](https://github.com/jpshackelford/open-grouch/commit/307b5e441af294c9beeab9f3d730f5c4406f087e))
* delegate tool for spawning sub-agents ([#341](https://github.com/jpshackelford/open-grouch/issues/341)) ([a1987e4](https://github.com/jpshackelford/open-grouch/commit/a1987e4c768d3c95e55dc7e635946d4fe821d818))
* **e2e:** add mock LLM server and full UI e2e tests ([#427](https://github.com/jpshackelford/open-grouch/issues/427)) ([f3ff2fc](https://github.com/jpshackelford/open-grouch/commit/f3ff2fc5333d31d55b766a9877eb883f415a2b0c))
* implement headless mode with auto-exit functionality ([#186](https://github.com/jpshackelford/open-grouch/issues/186)) ([2c3cb91](https://github.com/jpshackelford/open-grouch/commit/2c3cb91e8825d040cc220d81ec78ad899a7442e9))
* implement streaming LLM outputs for ACP implementation ([#254](https://github.com/jpshackelford/open-grouch/issues/254)) ([e54611d](https://github.com/jpshackelford/open-grouch/commit/e54611dce55d38269a2bdcba91345fb169b182d0))
* implement support for skills and legacy microagents in CLI ([#53](https://github.com/jpshackelford/open-grouch/issues/53)) ([ca220e2](https://github.com/jpshackelford/open-grouch/commit/ca220e2900e994e98b5c4b348759ac0f0698a80d))
* launch CLI as a browser app ([#247](https://github.com/jpshackelford/open-grouch/issues/247)) ([6fb6bf6](https://github.com/jpshackelford/open-grouch/commit/6fb6bf6292bd6f572cec523c153965c927a401e4))
* Load hooks from ~/.openhands/hooks.json in CLI ([#428](https://github.com/jpshackelford/open-grouch/issues/428)) ([2d7842f](https://github.com/jpshackelford/open-grouch/commit/2d7842fec141d0d452f9fa174818b957fd40a4d6))
* **mcp:** Add enable/disable functionality for MCP servers ([#242](https://github.com/jpshackelford/open-grouch/issues/242)) ([947b29e](https://github.com/jpshackelford/open-grouch/commit/947b29e307b8010f92241eeeb918e8910c567567))
* send metadata for models using llm-proxy base URLs ([#377](https://github.com/jpshackelford/open-grouch/issues/377)) ([8aa2a49](https://github.com/jpshackelford/open-grouch/commit/8aa2a491ce3b1364e3b16c594fc399bd9e17f8d1))
* Show context window and cost metrics in status bar ([#331](https://github.com/jpshackelford/open-grouch/issues/331)) ([afa8d3d](https://github.com/jpshackelford/open-grouch/commit/afa8d3d53046c0c82a3fe3cccceb33eb064147b4))
* show conversation list and ability to resume latest conversation ([#193](https://github.com/jpshackelford/open-grouch/issues/193)) ([8c802ab](https://github.com/jpshackelford/open-grouch/commit/8c802abfbd95da4e87f18ec5a3bb5b3b2f2d19d7))
* Show loaded resources (skills, hooks, MCPs) and add /skills command ([#474](https://github.com/jpshackelford/open-grouch/issues/474)) ([29e6930](https://github.com/jpshackelford/open-grouch/commit/29e6930b778801efe2c95456c9afa3df4c3d3431))
* support agent setup via environment variables ([#366](https://github.com/jpshackelford/open-grouch/issues/366)) ([9f5bef3](https://github.com/jpshackelford/open-grouch/commit/9f5bef3f6523907fec72f15db09b2244ebf6e616))
* support auth for local ACP agent ([#394](https://github.com/jpshackelford/open-grouch/issues/394)) ([01fadb7](https://github.com/jpshackelford/open-grouch/commit/01fadb70e9d694792de8a306d90f25cdee15e36d))
* truncate long commands in collapsed view with visual hierarchy ([d31f40c](https://github.com/jpshackelford/open-grouch/commit/d31f40ce1c2914cd881e9820285ed455cf0e358d)), closes [#334](https://github.com/jpshackelford/open-grouch/issues/334)
* **tui:** bind ctrl+a to select all text in input area ([#511](https://github.com/jpshackelford/open-grouch/issues/511)) ([0b98f5d](https://github.com/jpshackelford/open-grouch/commit/0b98f5d8b893681d57202e9b5e12a712c86d9153))
* **tui:** conversation history side panel ([#333](https://github.com/jpshackelford/open-grouch/issues/333)) ([8a0df43](https://github.com/jpshackelford/open-grouch/commit/8a0df4393b6293993a42df0cdc7fe584fdd12d71))


### 🐛 Bug Fixes

* **acp:** send session/update after session/new response ([#543](https://github.com/jpshackelford/open-grouch/issues/543)) ([4031e70](https://github.com/jpshackelford/open-grouch/commit/4031e70cd6aeb35d33a20897148b0a6c0f15888a))
* Check for openhands/ prefix instead of litellm_proxy ([#57](https://github.com/jpshackelford/open-grouch/issues/57)) ([d2bd402](https://github.com/jpshackelford/open-grouch/commit/d2bd40270153522d0a0d04df3ba6ceb1763c1b9d))
* **ci:** fix linting issues in grouch files and yaml formatting ([a4c42fa](https://github.com/jpshackelford/open-grouch/commit/a4c42fa43f2393c1108fea645fd57f6451b69edd))
* **ci:** rename acp.py to acp_cli.py to avoid import conflict with acp package ([32007b9](https://github.com/jpshackelford/open-grouch/commit/32007b97affc6b20b9693a77cd4b9d10db17ef0c))
* **ci:** update uv.lock for open-grouch package name and simplify release workflow ([32cd408](https://github.com/jpshackelford/open-grouch/commit/32cd40860ce0a7dbdfcec545923926d1845e4ae6))
* Clear values of settings modal using .clear() instead of setting as blank ([#514](https://github.com/jpshackelford/open-grouch/issues/514)) ([48c6dc5](https://github.com/jpshackelford/open-grouch/commit/48c6dc5f6c2162a0a70a10042085b2f1b5443d46))
* **cli:** add terminal compatibility detection ([#205](https://github.com/jpshackelford/open-grouch/issues/205)) ([c79c651](https://github.com/jpshackelford/open-grouch/commit/c79c6512aeb527e614198cb228e69b3bf5a1b700))
* clipboard copy when copy button is pressed ([#273](https://github.com/jpshackelford/open-grouch/issues/273)) ([0fe9e35](https://github.com/jpshackelford/open-grouch/commit/0fe9e35251a7347a302e48c1665797e31d3d2cd2))
* Correctly format LLM model names for litellm providers ([#322](https://github.com/jpshackelford/open-grouch/issues/322)) ([060769c](https://github.com/jpshackelford/open-grouch/commit/060769cb89fae9888ce51dd352e696299b4f73dd))
* critic - no module named posthog ([#448](https://github.com/jpshackelford/open-grouch/issues/448)) ([bc83841](https://github.com/jpshackelford/open-grouch/commit/bc838417d25294858b53cb065b3c967932db2408))
* default collapsibles to collapsed state ([#504](https://github.com/jpshackelford/open-grouch/issues/504)) ([a60470c](https://github.com/jpshackelford/open-grouch/commit/a60470cb61eefdb5c5b55b4c04b5f6b7c2967aa6))
* display agent MessageEvents in TUI when critic is enabled ([#400](https://github.com/jpshackelford/open-grouch/issues/400)) ([c1c5895](https://github.com/jpshackelford/open-grouch/commit/c1c5895026046f196cfc0a4ddafa28a26ac074d4))
* **docs:** restore AGENTS.md and fix PR types section ([0e556ce](https://github.com/jpshackelford/open-grouch/commit/0e556ce5155937054fa79ac8e5bc2dbdfa31fab5))
* hardcode base_url for OpenHands provider in CLI ([#168](https://github.com/jpshackelford/open-grouch/issues/168)) ([508dd66](https://github.com/jpshackelford/open-grouch/commit/508dd66cadd70c5cf47797e5b5e951c5ee34290d))
* **input:** implement auto-growing input with soft wrapping ([#276](https://github.com/jpshackelford/open-grouch/issues/276)) ([618016e](https://github.com/jpshackelford/open-grouch/commit/618016e25bc29227cad7675a8d0764e756043bf3))
* issue with memory condensation not being editable ([#372](https://github.com/jpshackelford/open-grouch/issues/372)) ([149ff3e](https://github.com/jpshackelford/open-grouch/commit/149ff3ee977cbc69a22b62307321e0e2bc8a1da9))
* **Makefile:** help and pre-commit ([#528](https://github.com/jpshackelford/open-grouch/issues/528)) ([7443e0c](https://github.com/jpshackelford/open-grouch/commit/7443e0c018885336382de3ad0e4392f312e9e319))
* pass Laminar API key as action input in PR review workflow ([#484](https://github.com/jpshackelford/open-grouch/issues/484)) ([e30f02d](https://github.com/jpshackelford/open-grouch/commit/e30f02db5b206b0e5e79150fdad9904a7dcd8511))
* pin rich&lt;14.3.0 to fix autocomplete shutdown crash ([#402](https://github.com/jpshackelford/open-grouch/issues/402)) ([9896d02](https://github.com/jpshackelford/open-grouch/commit/9896d02174071f8e78e51b4cd3adb4eefed6f9be))
* require --override-with-envs flag to apply LLM env vars ([#379](https://github.com/jpshackelford/open-grouch/issues/379)) ([3bed5c7](https://github.com/jpshackelford/open-grouch/commit/3bed5c72322fcf637cc815574351e4a79edc7667))
* Set prompt_continuation to empty string for cleaner multiline input ([#65](https://github.com/jpshackelford/open-grouch/issues/65)) ([d1a65de](https://github.com/jpshackelford/open-grouch/commit/d1a65de7bd67a60a1040c24a66a1adf8e401a53a))
* shorten comment line to stay within 88 character limit ([349fb3a](https://github.com/jpshackelford/open-grouch/commit/349fb3ac8a1a76fba93a9bd11a71e7b5eb310e87))
* Skip PR description update if uvx section already exists ([#279](https://github.com/jpshackelford/open-grouch/issues/279)) ([764d5d8](https://github.com/jpshackelford/open-grouch/commit/764d5d82f666ea0384559a52c1657042c94382a4))
* **tests:** disable input cursor blink for snapshots ([#0](https://github.com/jpshackelford/open-grouch/issues/0)) ([#476](https://github.com/jpshackelford/open-grouch/issues/476)) ([08b5c2e](https://github.com/jpshackelford/open-grouch/commit/08b5c2ef5a9ec3761421ff5b36dbfcd88b171d3c))
* **tests:** fix broken tests and update snapshots ([b24fa7e](https://github.com/jpshackelford/open-grouch/commit/b24fa7e1c239653b95af881c2b5cfec0112bddee))
* **tests:** make creating_agent_plan snapshot test deterministic ([#524](https://github.com/jpshackelford/open-grouch/issues/524)) ([4059e04](https://github.com/jpshackelford/open-grouch/commit/4059e0488e4bfab45c8742f21a7aace134f743d1))
* **tui:** add ComposeResult return type hints to compose() methods ([#509](https://github.com/jpshackelford/open-grouch/issues/509)) ([5e03331](https://github.com/jpshackelford/open-grouch/commit/5e03331794a2cab3cd843233cf17fd95d41fea76))
* **tui:** disable markup parsing for user messages to prevent crashes ([#286](https://github.com/jpshackelford/open-grouch/issues/286)) ([ad479be](https://github.com/jpshackelford/open-grouch/commit/ad479be5e8e7f365fb4ba7a55baed69b8bae7a7f))
* **tui:** reset token metrics when creating new conversation ([#439](https://github.com/jpshackelford/open-grouch/issues/439)) ([811604f](https://github.com/jpshackelford/open-grouch/commit/811604f78175c920d9efb3dd610ffdbcb3ad2319))
* **types:** add missing type hints to handle_resume_logic and _meta ([#532](https://github.com/jpshackelford/open-grouch/issues/532)) ([5f1510b](https://github.com/jpshackelford/open-grouch/commit/5f1510bf874aa738ad5735d2245d60e3346ba2c4))
* use ~/.open-grouch for config directory instead of ~/.openhands ([e93380e](https://github.com/jpshackelford/open-grouch/commit/e93380e4c15636003ef3c005298f383df6224cd9))
* use ~/.open-grouch for config directory instead of ~/.openhands ([34204c9](https://github.com/jpshackelford/open-grouch/commit/34204c9719218b50d42555b5e68f3ff3c8f7002b))
* use model_id without provider prefix when loading settings ([#280](https://github.com/jpshackelford/open-grouch/issues/280)) ([d2c4a03](https://github.com/jpshackelford/open-grouch/commit/d2c4a0397374b1bc48da8c11aa70721ae4d4330c))
* **widgets:** remove unnecessary type: ignore in collapsible.py ([#458](https://github.com/jpshackelford/open-grouch/issues/458)) ([7e56e1a](https://github.com/jpshackelford/open-grouch/commit/7e56e1a1fd8f2164b523bd2ea3788621d24f3c25))


### 🧹 Maintenance

* copy over V1 CLI from OpenHands/OpenHands repo ([#50](https://github.com/jpshackelford/open-grouch/issues/50)) ([fcb974d](https://github.com/jpshackelford/open-grouch/commit/fcb974df869ccaf9a3e7f300932f926177b4e8ef))
* ignore W291 (trailing whitespace) in pycodestyle ([a802781](https://github.com/jpshackelford/open-grouch/commit/a80278151f8eccfeef47195af5f6f94b0a28b9cd))
* Remove unused 'Display Cost Per Action' setting ([#347](https://github.com/jpshackelford/open-grouch/issues/347)) ([953a87e](https://github.com/jpshackelford/open-grouch/commit/953a87eeaa2bcc5f989b7b90306e6232e7602c93))
* rename files and directories ([#278](https://github.com/jpshackelford/open-grouch/issues/278)) ([ce1b108](https://github.com/jpshackelford/open-grouch/commit/ce1b108c04faf5a8aa8d6a5480ce13cb2bf6b041))
* reorganize files ([#248](https://github.com/jpshackelford/open-grouch/issues/248)) ([549a2d5](https://github.com/jpshackelford/open-grouch/commit/549a2d53eff3367bb247201c03bfd619ec3091e1))


### 📚 Documentation

* clarify lint before commits ([#0](https://github.com/jpshackelford/open-grouch/issues/0)) ([#467](https://github.com/jpshackelford/open-grouch/issues/467)) ([d0f8105](https://github.com/jpshackelford/open-grouch/commit/d0f81051caeac758aec66dce26fdd3b039180e46))
* clarify lint-before-commit guidance ([#460](https://github.com/jpshackelford/open-grouch/issues/460)) ([5a58305](https://github.com/jpshackelford/open-grouch/commit/5a58305a4723a6676c5b963c4521c6ac857c900c))
* clarify uv usage in AGENTS ([#425](https://github.com/jpshackelford/open-grouch/issues/425)) ([b6d2d38](https://github.com/jpshackelford/open-grouch/commit/b6d2d383ea17f97cb385efb603f4d6e2abdefc53))
* **CONTRIBUTING:** Correct install pre-commit hooks command in AGENTS.md ([#374](https://github.com/jpshackelford/open-grouch/issues/374)) ([2be6e10](https://github.com/jpshackelford/open-grouch/commit/2be6e101b39de2200c94228685ad15a6abf53c15))
* minor documentation tweaks ([#471](https://github.com/jpshackelford/open-grouch/issues/471)) ([b958b64](https://github.com/jpshackelford/open-grouch/commit/b958b64871ee7fd1b261ceec3829830b4ee8345f))
* rewrite README with concise quickstart and binary build instructions; add Development.md with detailed dev, packaging, and build guidance\n\nCloses [#19](https://github.com/jpshackelford/open-grouch/issues/19)\n\nCo-authored-by: openhands &lt;openhands@all-hands.dev&gt; ([#20](https://github.com/jpshackelford/open-grouch/issues/20)) ([e980c1a](https://github.com/jpshackelford/open-grouch/commit/e980c1a3b77c63b98080996e4c49f29c0f6604a9))
* update documentation for conventional commits workflow ([31e6998](https://github.com/jpshackelford/open-grouch/commit/31e699844e5ae764098cc1ef93b3d5454729f7b3))
* update skills path references ([#478](https://github.com/jpshackelford/open-grouch/issues/478)) ([53f0822](https://github.com/jpshackelford/open-grouch/commit/53f0822efe60620611c46910614b02fc95046992))


### ♻️ Refactoring

* add reactive state management + decouple main app from conversation management ([#421](https://github.com/jpshackelford/open-grouch/issues/421)) ([25e8e41](https://github.com/jpshackelford/open-grouch/commit/25e8e4136fb5eb657acc2798ec9e412b1bed1669))
* replace direct color usage with OPENHANDS_THEME colors ([#219](https://github.com/jpshackelford/open-grouch/issues/219)) ([91ae6f5](https://github.com/jpshackelford/open-grouch/commit/91ae6f5ee5f4d43734ccaede7af677fe43a302dd))
* use consolidated pr-review action from SDK ([#477](https://github.com/jpshackelford/open-grouch/issues/477)) ([a106cb9](https://github.com/jpshackelford/open-grouch/commit/a106cb9f474c781b47e85fff3dac1cb4de5fb731))


### 🧪 Tests

* add coverage for verify_agent_exists_or_setup_agent ([#121](https://github.com/jpshackelford/open-grouch/issues/121)) ([be05870](https://github.com/jpshackelford/open-grouch/commit/be05870aa51f0f3867c309fb988b6a1246a8930c))
* **cli:** ensure help text mentions key subcommands and flags ([#156](https://github.com/jpshackelford/open-grouch/issues/156)) ([08d8a0b](https://github.com/jpshackelford/open-grouch/commit/08d8a0b4b16fba52ddc83b91581aeb0d0f85d048))
* **snapshots:** update select_all e2e snapshots for v1.12.2 ([#522](https://github.com/jpshackelford/open-grouch/issues/522)) ([e69285d](https://github.com/jpshackelford/open-grouch/commit/e69285d6be11e362941f010d7d55318d87290cf0))
* update comment reference to OpenHands/extensions ([#505](https://github.com/jpshackelford/open-grouch/issues/505)) ([64f518b](https://github.com/jpshackelford/open-grouch/commit/64f518b57646c034a0bb5a1bf67336ffe00d454b))


### 🔧 CI/CD

* Add binary --version test to CI workflow ([#116](https://github.com/jpshackelford/open-grouch/issues/116)) ([b130941](https://github.com/jpshackelford/open-grouch/commit/b13094192bf515f8783427bd148bee34ff7a0a98))
* add conventional commits and automatic releases ([1e468ef](https://github.com/jpshackelford/open-grouch/commit/1e468efb19f1039c6cc5bf0d72895087576b0063))
* add daily good first issue labeler workflow ([#464](https://github.com/jpshackelford/open-grouch/issues/464)) ([870519a](https://github.com/jpshackelford/open-grouch/commit/870519a168da094fd257b9c0e609240349118e60))
* disable pull_request_target for PR review ([#523](https://github.com/jpshackelford/open-grouch/issues/523)) ([f97c377](https://github.com/jpshackelford/open-grouch/commit/f97c3778cd9e2af977a65679953f3303a4525ed9))
* disable uv cache in untrusted agent workflows ([#521](https://github.com/jpshackelford/open-grouch/issues/521)) ([4eb66f6](https://github.com/jpshackelford/open-grouch/commit/4eb66f6f462d4de5b8ff10436ab5d4de438f60d3))
* enhance type checking workflow with code quality analysis and auto-fix PRs ([#455](https://github.com/jpshackelford/open-grouch/issues/455)) ([80cd0f6](https://github.com/jpshackelford/open-grouch/commit/80cd0f6eefaaefde5e62a1fbe8b70cc77302bbca))
