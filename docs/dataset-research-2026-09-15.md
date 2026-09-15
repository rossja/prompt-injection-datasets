# Dataset source review — 2026-09-15

This review expands the catalog to cover prompt injection, jailbreaks, general
safety targets (including CBRNE and hate speech), and benign controls. It includes
recent releases and older omissions; it is not an exhaustive landscape census.
The catalog keeps its `src,url,license` schema. Source roles and qualifications
live here rather than being lost in a flat URL list.

## Method and acceptance criteria

Three parallel discovery tracks covered injection/detection corpora,
agent/tool/web benchmarks, and jailbreak collections. A general-safety pass and
shared review reconciled their candidates with the existing manifest.

1. Use original author/publisher releases where identifiable. Follow papers and
   dataset cards to actual artifact files; a paper or generation harness alone
   does not qualify.
2. Prefer one canonical location per release. Exclude mirrors, format-only
   copies, and large aggregations whose additional value was not established.
   Keep meaningful new attacks, annotations, contexts or languages even when
   their seeds overlap, and record that relationship.
3. Record data-specific license declarations. Blank means unresolved or
   unspecified, not unrestricted. `MIT; CC-BY-SA-4.0` summarizes separately
   licensed components; it does not offer a choice of license. Repository
   licenses do not automatically settle rights in imported examples.
4. Check public cards, previews, file listings and relevant source files.
   Gated sources are explicitly marked. No access terms were accepted, no full
   dataset downloads were run, and downloader compatibility was checked with
   mocked dispatch rather than authenticated end-to-end downloads.

These are source-level decisions. Distinct URLs do not establish independent
examples. Counts below are publisher-reported, not locally recounted. Preserve
source IDs and train/test splits when later extracting records; an attack string
with different system instructions, tools, placement, image or conversation
history can be a different evaluation case. Do not flatten that context or train
on held-out benchmark records merely because they appear in this catalog.

## Accepted additions

44 source URLs were added and one existing byte-identical source was removed,
leaving 99 entries (previously 56). The two CyberSecEval text files are related
language variants, so this is not a claim of 44 independent corpora. Linked
source names identify the exact manifest entry; evidence links identify the
reviewed publisher card or relevant repository material.

### Injection and agent attacks

| Source / evidence | License recorded | Published artifact and role | Access, lineage and extraction notes |
| --- | --- | --- | --- |
| [LLMail-Inject](https://huggingface.co/datasets/microsoft/llmail-inject-challenge) · [evidence](https://huggingface.co/datasets/microsoft/llmail-inject-challenge/blob/main/README.md) | MIT | Email subject/body injections, challenge outcomes and scenario context; JSONL under data/. | 461,640 raw submissions; deduplicated labeled variants are separate files in the same snapshot, not extra attacks. |
| [NotInject](https://huggingface.co/datasets/leolee99/NotInject) · [evidence](https://huggingface.co/datasets/leolee99/NotInject/blob/main/README.md) | MIT | 339 benign hard negatives for injection detectors; Parquet. | Control data, not attacks. Also included in PIGuard and other validation mixtures; select the original release. |
| [PromptShield](https://huggingface.co/datasets/hendzh/PromptShield) · [evidence](https://huggingface.co/datasets/hendzh/PromptShield/blob/main/README.md) | Apache-2.0 | 43,425 full-prompt detection examples; train/validation/test JSON. | Curated public datasets plus attack constructions; upstream overlap remains. Exclude downstream mirrors. |
| [AlignmentCheck evaluations](https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals) · [evidence](https://huggingface.co/datasets/facebook/llamafirewall-alignmentcheck-evals/blob/main/README.md) | MIT | Agent/tool injection messages, context and outcomes. | 577 underlying cases repeated across six models. Publisher specifies evaluation-only intended use; preserve prompt_id when extracting. |
| [SafeGuard prompt injection](https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection) · [evidence](https://huggingface.co/datasets/xTRam1/safe-guard-prompt-injection/blob/main/README.md) | Unspecified / unresolved | 10,296 binary detection examples in Parquet. | Synthetic attacks seeded partly by existing jackhhao/jailbreak-classification; dataset license not specified in reviewed card. |
| [SecFid](https://huggingface.co/datasets/mjhermon/SecFid) · [evidence](https://huggingface.co/datasets/mjhermon/SecFid/blob/main/README.md) | Apache-2.0 | 1,168 document-task probes plus 252 agentic cases; JSONL configurations. | Agentic extension derives from InjecAgent with MIT attribution; distinct task-fidelity annotations, not wholly new upstream scenarios. |
| [ASPI](https://huggingface.co/datasets/ScaleAI/aspi) · [evidence](https://huggingface.co/datasets/ScaleAI/aspi/blob/main/README.md) | CC-BY-4.0 | 728 scenario pairs with adversarial clarification answers; data/*.jsonl. | Extends AgentDojo; compares tool-output and user clarification channels. All-config repeats suite configs. Publisher specifies evaluation, not training. |
| [BIPIA](https://github.com/microsoft/BIPIA) · [evidence](https://github.com/microsoft/BIPIA/blob/main/LICENSE) | MIT; CC-BY-SA-4.0 | Text/code attack JSON and context JSONL in benchmark/. | Mixed component licenses: WikiTableQuestions and Stack Exchange data have CC-BY-SA-4.0 exceptions to MIT. Some web/summarization contexts require upstream reconstruction. |
| [InjecAgent](https://github.com/uiuc-kang-lab/InjecAgent) · [evidence](https://github.com/uiuc-kang-lab/InjecAgent/blob/main/LICENCE) | MIT | 1,054 reported tool-injection cases; data/test_cases_*.json and attacker_cases_*.jsonl. | Base/enhanced variants share cases. Keep task/tool context; avoid third-party HF copies. |
| [AgentDojo](https://github.com/ethz-spylab/agentdojo) · [evidence](https://github.com/ethz-spylab/agentdojo/blob/main/src/agentdojo/attacks/important_instructions_attacks.py) | MIT | Scenario data, source-embedded attack templates and published runs/. | Not a flat prompt corpus. Task objectives alone are not materialized attacks; repeated model trajectories share scenarios. |
| [Agent Security Bench](https://github.com/agiresearch/ASB) · [evidence](https://github.com/agiresearch/ASB/tree/main/data) | MIT | Malicious tool instructions and tasks in data/all_attack_tools.jsonl and agent_task.jsonl. | Subsets overlap the all_* files. Historical Zhang-Henry URL is not an additional source. |
| [CyberSecEval text injections](https://raw.githubusercontent.com/meta-llama/PurpleLlama/main/CybersecurityBenchmarks/datasets/prompt_injection/prompt_injection.json) · [evidence](https://github.com/meta-llama/PurpleLlama/tree/main/CybersecurityBenchmarks/datasets/prompt_injection) | MIT | System instructions, malicious prompts, evaluator questions and technique tags. | Use the exact data artifact rather than cloning all PurpleLlama components. |
| [CyberSecEval multilingual injections](https://raw.githubusercontent.com/meta-llama/PurpleLlama/main/CybersecurityBenchmarks/datasets/prompt_injection/prompt_injection_multilingual_machine_translated.json) · [evidence](https://github.com/meta-llama/PurpleLlama/blob/main/CybersecurityBenchmarks/LICENSE) | MIT | Machine-translated injection variants. | Shares underlying attacks with the English artifact; adds language coverage, not independent attack ideas. |
| [CyberSecEval visual injections](https://huggingface.co/datasets/facebook/cyberseceval3-visual-prompt-injection) · [evidence](https://huggingface.co/datasets/facebook/cyberseceval3-visual-prompt-injection/blob/main/README.md) | MIT | 1,000 image/text cases; test_cases.json and images/*.png. | Separate artifact from textual CyberSecEval. Preserve image assets and context. Publisher specifies evaluation-only intended use. |
| [WASP](https://github.com/facebookresearch/wasp) · [evidence](https://github.com/facebookresearch/wasp) | CC-BY-NC-4.0 | Web-agent tasks in experiment_config.raw.json and payload templates in constants.py. | Data license differs from incorporated code licenses. Archived repository remains published. WAInjectBench includes a WASP derivative. |
| [MCPTox](https://github.com/zhiqiangwang4/MCPTox-Benchmark) · [evidence](https://github.com/zhiqiangwang4/MCPTox-Benchmark/tree/main/def_tool) | Unspecified / unresolved | Malicious tool descriptions embedded in def_tool/*.py; pure_tool.json and response_all.json. | Author-linked AAAI release. No license found. Paper case count is not a verified count of released unique payloads. |
| [AgentDyn](https://github.com/SaFo-Lab/AgentDyn) · [evidence](https://github.com/SaFo-Lab/AgentDyn) | MIT | Shopping, GitHub and daily-life suite data/tasks plus published runs/. | AgentDojo fork also contains inherited suites and templates. New scenarios add coverage; do not count the inherited corpus twice. |

### Jailbreak attacks and behavior seeds

| Source / evidence | License recorded | Published artifact and role | Access, lineage and extraction notes |
| --- | --- | --- | --- |
| [WildJailbreak](https://huggingface.co/datasets/allenai/wildjailbreak) · [evidence](https://huggingface.co/datasets/allenai/wildjailbreak/blob/main/README.md) | ODC-By-1.0 | Adversarial/vanilla harmful and benign prompt-response examples; train/train.tsv and eval/eval.tsv. | Gated data: access conditions/contact sharing. Original WildTeaming-generated attacks; ReSA and XGuard reuse part of this lineage. |
| [In-the-wild jailbreak prompts](https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts) · [evidence](https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts/blob/main/README.md) | MIT | JailbreakHub research release; latest snapshot has 1,405 jailbreaks and 13,735 regular prompts. | Same release as verazuo/jailbreak_llms. Historical snapshots overlap; likely overlap with existing community jailbreak lists is unmeasured. |
| [JailbreakBench attack artifacts](https://github.com/JailbreakBench/artifacts) · [evidence](https://github.com/JailbreakBench/artifacts) | MIT | Submitted attack payloads in attack-artifacts/, including GCG, PAIR and other methods. | Distinct from JBB behavior seeds. Exclude test-artifact fixtures when extracting; shared methods do not prove identical attack text. |
| [Multi-turn human jailbreaks](https://huggingface.co/datasets/ScaleAI/mhj) · [evidence](https://huggingface.co/datasets/ScaleAI/mhj/blob/main/README.md) | CC-BY-NC-4.0 | Human attack conversations over HarmBench goals; harmbench_behaviors.csv. | Gated. Paper reports 537 conversations / 2,912 attack prompts. Goals overlap HarmBench; conversations add attack content. |
| [Gibbs multi-turn jailbreak datasets](https://huggingface.co/datasets/tom-gibbs/multi-turn_jailbreak_attack_datasets) · [evidence](https://huggingface.co/datasets/tom-gibbs/multi-turn_jailbreak_attack_datasets/blob/main/README.md) | MIT | Single/multi-turn cipher attacks and benign controls in four CSV files. | AdvBench-derived goals; preserve conversation/cipher variants. MIT metadata coexists with research-only usage text. |
| [JailbreakBench behaviors](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors) · [evidence](https://huggingface.co/datasets/JailbreakBench/JBB-Behaviors/blob/main/README.md) | MIT | 100 harmful behavior seeds plus benign controls and judge comparisons in data/*.csv. | Seeds, not jailbreak payloads. Source column identifies AdvBench/TDC/HarmBench-derived material; do not merge away attack artifacts. |
| [HarmBench](https://github.com/centerforaisafety/HarmBench) · [evidence](https://github.com/centerforaisafety/HarmBench/tree/main/data/behavior_datasets) | MIT | Text and multimodal behavior seeds in data/behavior_datasets/*.csv. | Declared repository MIT; no explicit data exception found. All/test/validation files overlap. External precomputed attacks were not verified as included in a plain clone. |
| [ReSA](https://huggingface.co/datasets/ByteDance-Seed/ReSA) · [evidence](https://huggingface.co/datasets/ByteDance-Seed/ReSA/blob/main/README.md) | ODC-By-1.0 | 79,552 released SFT examples and 153 adversarial self-harm evaluation cases; sft_train.json and eval_safe_completion.json. | Derived from WildJailbreak plus new attacks/reasoning responses; evaluation also uses StrongREJECT/HarmBench/AdvBench seeds. |
| [ReNeLLM jailbreaks](https://huggingface.co/datasets/Deep1994/ReNeLLM-Jailbreak) · [evidence](https://huggingface.co/datasets/Deep1994/ReNeLLM-Jailbreak/blob/main/README.md) | MIT | Nested jailbreak attacks in renellm_jailbreak.json. | Gated and research-only usage text. Official author release, transforms AdvBench goals. Exclude jc-detoxio transfer mirror. |
| [XGuard training data](https://huggingface.co/datasets/marslabucla/XGuard-Train) · [evidence](https://huggingface.co/datasets/marslabucla/XGuard-Train/blob/main/README.md) | Unspecified / unresolved | 30,695 multi-turn attack/refusal conversations in xguard-train.json. | Gated; no explicit dataset license found. WildJailbreak-derived harmful goals; harmful replies replaced with refusal responses. |
| [StrongREJECT behavior seeds](https://raw.githubusercontent.com/alexandrasouly/strongreject/main/strongreject_dataset/strongreject_dataset.csv) · [evidence](https://github.com/alexandrasouly/strongreject#license) | Unspecified / unresolved | 313 harmful-request seeds with source attribution. | Current dsbowen/strong_reject loader fetches this original file. Only custom questions have MIT; imported questions have varying/unspecified terms. |

### General safety targets and controls

| Source / evidence | License recorded | Published artifact and role | Access, lineage and extraction notes |
| --- | --- | --- | --- |
| [WildGuardMix](https://huggingface.co/datasets/allenai/wildguardmix) · [evidence](https://huggingface.co/datasets/allenai/wildguardmix/blob/main/README.md) | ODC-By-1.0 | Prompt/response harmfulness and refusal labels; train/wildguard_train.parquet and test/wildguard_test.parquet. | Gated. Synthetic, in-the-wild and annotator-written mixture; 86,759 train and 1,725 test records, not all independent attack prompts. |
| [Aegis 2.0](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0) · [evidence](https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0/blob/main/README.md) | CC-BY-4.0 | Risk-taxonomy safety labels and refusal examples; train/test/validation.json plus refusals JSON. | Meaningful newer release alongside existing Aegis 1.0. Reuses Anthropic/DAN/red-team sources; self-harm samples mentioned in card are not redistributed. |
| [BeaverTails](https://huggingface.co/datasets/PKU-Alignment/BeaverTails) · [evidence](https://huggingface.co/datasets/PKU-Alignment/BeaverTails/blob/main/README.md) | CC-BY-NC-4.0 | Prompt-response safety classifications across 14 harm categories; JSON. | Multiple release/split sizes overlap; do not add evaluation or converted mirrors as independent full corpora. |
| [PKU-SafeRLHF](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF) · [evidence](https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF/blob/main/README.md) | CC-BY-NC-4.0 | Paired responses with helpfulness/harmlessness preferences; data/Alpaca*/train.jsonl and test.jsonl. | Sibling of BeaverTails; default and per-model configurations reuse files. Preference labels add a different role; do not sum configs. |
| [WMDP](https://huggingface.co/datasets/cais/wmdp) · [evidence](https://huggingface.co/datasets/cais/wmdp/blob/main/README.md) | MIT | 3,668 multiple-choice hazardous-knowledge probes; wmdp-bio, wmdp-chem, wmdp-cyber Parquet. | Targets/probes, not ready-made jailbreaks or a complete CBRNE taxonomy. Choose canonical HF release instead of its archive mirrors. |
| [Do-Not-Answer](https://huggingface.co/datasets/LibrAI/do-not-answer) · [evidence](https://huggingface.co/datasets/LibrAI/do-not-answer/blob/main/README.md) | CC-BY-NC-SA-4.0 | 939 harmful-request seeds with taxonomy and response assessments; data_en.csv / Parquet. | Card header says Apache-2.0, but explicit License section assigns CC-BY-NC-SA-4.0 to datasets and Apache to source code; field follows the data-specific statement. |
| [XSTest](https://raw.githubusercontent.com/paul-rottger/xstest/main/xstest_prompts.csv) · [evidence](https://github.com/paul-rottger/xstest#license) | CC-BY-4.0 | Safe prompts and unsafe contrasts for refusal/over-refusal evaluation. | Exact prompt file selected; model-completion artifacts have separate terms and are not included. |
| [ToxiGen](https://huggingface.co/datasets/toxigen/toxigen-data) · [evidence](https://huggingface.co/datasets/toxigen/toxigen-data/blob/main/README.md) | Unspecified / unresolved | Implicit toxic and benign statements with target groups and human annotations; toxigen.csv and annotated CSV/Parquet. | Hate-speech targets and controls, not instruction-hijacking attacks. Dataset license absent from reviewed card; do not infer from generation-code license. Publisher describes research use. |
| [SORRY-Bench 2025/03](https://huggingface.co/datasets/sorry-bench/sorry-bench-202503) · [evidence](https://huggingface.co/datasets/sorry-bench/sorry-bench-202503/blob/main/README.md) | SORRY-Bench | 440 base unsafe instructions across 44 categories plus 20 mutations; question*.jsonl. | Gated, custom terms restrict redistribution. Select newer release rather than also adding 2024/06; mutations and reused prior-dataset seeds are related examples. |
| [FORTRESS](https://huggingface.co/datasets/ScaleAI/fortress_public) · [evidence](https://huggingface.co/datasets/ScaleAI/fortress_public/blob/main/README.md) | CC-BY-4.0 | 500 expert-authored adversarial requests paired with benign requests and rubrics; data/train-00000-of-00001.parquet. | CBRNE, political violence and illicit activity. Public subset; distinct from WMDP knowledge questions. ROK-FORTRESS adapts some cases. |
| [PatientSafetyBench](https://huggingface.co/datasets/microsoft/PatientSafetyBench) · [evidence](https://huggingface.co/datasets/microsoft/PatientSafetyBench/blob/main/README.md) | CDLA-Permissive-2.0 | 466 patient-oriented medical safety queries; patientsafetybench.jsonl. | Synthetic, filtered and manually reviewed single-turn requests. Safety stress tests, not clinical advice ground truth. |
| [AILuminate public demo](https://github.com/mlcommons/ailuminate) · [evidence](https://github.com/mlcommons/ailuminate) | CC-BY-4.0 | Public English/French airr_official_1.0_demo_*_prompt_set_release.csv files. | README specifies CC-BY-4.0 for data despite Apache repository badge. The 1,200-prompt demo is not the full private benchmark; locale versions are related. |
| [AIR-Bench 2024](https://huggingface.co/datasets/stanford-crfm/air-bench-2024) · [evidence](https://huggingface.co/datasets/stanford-crfm/air-bench-2024/blob/main/README.md) | CC-BY-4.0 | 5,694 risk-taxonomy harmful requests in category_*.csv plus separate judge templates. | Region configurations reuse files. Code is Apache-2.0 but data is CC-BY-4.0. This is the safety AIR-Bench, not the retrieval benchmark. |
| [ALERT](https://github.com/Babelscape/ALERT) · [evidence](https://github.com/Babelscape/ALERT) | CC-BY-NC-SA-4.0 | data/alert.jsonl and data/alert_adversarial.jsonl; base and adversarial harmful requests. | Mostly derives base prompts from already listed Anthropic HH-RLHF; adds taxonomy and adversarial variants. MIT_LICENSE.txt attributes upstream data, not the whole ALERT release. |
| [Aya red-teaming](https://huggingface.co/datasets/CohereLabs/aya_redteaming) · [evidence](https://huggingface.co/datasets/CohereLabs/aya_redteaming/blob/main/README.md) | Apache-2.0 | Human-authored harmful requests in eight languages; aya_*.jsonl, local/global labels and translations. | Native-language cultural coverage. Older CohereForAI name and walledai conversion are not extra sources; translations within rows are related. |
| [ROK-FORTRESS public subset](https://huggingface.co/datasets/ScaleAI/ROK-FORTRESS_public) · [evidence](https://huggingface.co/datasets/ScaleAI/ROK-FORTRESS_public/blob/main/README.md) | CC-BY-4.0 | 791 released Korean/English tasks with request variants and rubrics; Parquet and rok_fortress_public.tsv. | Gated despite public in name. Includes 450 adapted FORTRESS tasks and 341 newly authored tasks; 444 held-out tasks are not public. |

## Deduplication decisions and deferred candidates

| Candidate or family | Decision and evidence |
| --- | --- |
| Full PINT benchmark | Not added: the [current repository data directory](https://github.com/CheckPointSW/pint-benchmark/tree/main/benchmark/data) contains example data, not the full benchmark; the published notebook expects separately supplied data. The older Lakera fork is not a second dataset. |
| PIGuard / InjecGuard training mixture | Deferred: [published datasets](https://github.com/leolee99/PIGuard/tree/main/datasets) overlap NotInject, BIPIA, WildGuard and many other sources. Author augmentation may add value, but not accepted here as a wholly independent corpus. |
| ProtectAI validation | Deferred: [card](https://huggingface.co/datasets/protectai/prompt-injection-validation) shows multiple upstream evaluation sets, including a PINT-labeled subset whose provenance/terms were not resolved. Prefer original releases. |
| WildJailbreak, HarmBench, Aya and CyberSecEval mirrors | Use the original authors selected above, not walledai conversions. Also exclude liyucheng/wildjailbreak and duplicate prompt/format-only releases. |
| JailbreakHub GitHub versus HF | Select [TrustAIRLab HF](https://huggingface.co/datasets/TrustAIRLab/in-the-wild-jailbreak-prompts) rather than also adding [verazuo/jailbreak_llms](https://github.com/verazuo/jailbreak_llms). Historical snapshots overlap within that release. |
| ReNeLLM transfer mirror | Prefer Deep1994's author release; omit [jc-detoxio copy](https://huggingface.co/datasets/jc-detoxio/ReNeLLM-Jailbreak). |
| StrongREJECT code repository | The [maintained loader](https://github.com/dsbowen/strong_reject/blob/main/strong_reject/load_datasets.py) fetches the original CSV; catalog that raw file rather than assuming the current code clone contains the data. |
| WAInjectBench | Deferred: its [malicious data directory](https://github.com/Norrrrrrr-lyn/WAInjectBench/tree/main/data/text/malicious) includes WASP/VWA-derived files. Some other attacks may add value, but global data license and overlap need more work. |
| KoPI-Bench | Deferred: [card](https://huggingface.co/datasets/HaniMeni/KoPI-Bench) describes useful Korean translations of many selected/existing corpora, but viewer schema mismatch needs extraction review. Snapshot download may still work; no claim that the underlying files are unavailable. |
| jcanode/safeguard-prompt-injection | Deferred: [card](https://huggingface.co/datasets/jcanode/safeguard-prompt-injection) mixes raw/tokenized data with a viewer schema error and large benign mixtures. Distinct publisher from xTRam1 SafeGuard. |
| neuralchemy corpora | Deferred: [base card](https://huggingface.co/datasets/neuralchemy/Prompt-injection-dataset) has overlapping configurations and inconsistent totals; [Threat Matrix](https://huggingface.co/datasets/neuralchemy/prompt-injection-Threat-Matrix) adds taxonomy/augmentation over shared sources. More label and lineage review needed. |
| Bordair multimodal | Deferred: [card](https://huggingface.co/datasets/Bordair/bordair-multimodal) describes substantial external-source ingestion and synthetic expansion. Claimed scale is not a count of independent attack ideas; modality assets need review. |
| JailbreakDB / Cogensec / get-garak mixtures | Defer bulk aggregation pending per-source reconciliation: [JailbreakDB](https://huggingface.co/datasets/youbin2014/JailbreakDB), [Cogensec](https://huggingface.co/datasets/Cogensec/jailbreak-corpus), [get-garak discussion](https://huggingface.co/datasets/get-garak/input_classification/discussions/1). |
| Kaggle aggregation candidates | [Prompt injection in the wild](https://www.kaggle.com/datasets/arielzilber/prompt-injection-in-the-wild) and [MPDD](https://www.kaggle.com/datasets/mohammedaminejebbar/malicious-prompt-detection-dataset-mpdd) aggregate existing corpora; added embeddings or repackaging alone did not justify another source. |
| S-Labs / Shomi28 detection corpora | Deferred: public cards exist, but [S-Labs provenance](https://huggingface.co/datasets/S-Labs/prompt-injection-dataset) and [Shomi28 templating/counts](https://huggingface.co/datasets/Shomi28/prompt-injection-dataset) need stronger review before treating them as new coverage. |
| SORRY-Bench 2024/06 | Select the updated 2025/03 release rather than adding both overlapping versions. |
| AIR-BENCH Live | Deferred: [2026 author repository](https://github.com/rnaphade-afk/AIR-BENCH-Live) lists generated CSVs, but individual file inspection and data-specific license treatment were unresolved; some legacy material comes from AIR-Bench 2024. |
| TrustLLM | Deferred: [safety files](https://huggingface.co/datasets/TrustLLM/TrustLLM-dataset/tree/main/safety) are gated and aggregate other sources. |
| SafetyBench | [Valid public benchmark](https://huggingface.co/datasets/thu-coai/SafetyBench), deferred as lower-priority safety-knowledge coverage rather than a missing source of attack payloads. |

## Existing-source overlap findings

Removed `JasperLS/prompt-injections`, retaining `deepset/prompt-injections`.
The [JasperLS tree metadata](https://huggingface.co/api/datasets/JasperLS/prompt-injections/tree/main?recursive=true&expand=true)
and [deepset tree metadata](https://huggingface.co/api/datasets/deepset/prompt-injections/tree/main?recursive=true&expand=true)
report identical data-directory Git tree OID
`0cbed2722d1bdd00876c51bfa3c8f61b0b75477e` and identical LFS content hashes:

| Split | Bytes | SHA256 in both repositories |
| --- | ---: | --- |
| test | 10,892 | `39ac797cabc157eeed58435a08593b2952bb6cb16fc394a2d383f447cc7b246e` |
| train | 40,323 | `2e10bc7ab30f542c97e4e83e2a5683000b5057d25ec10908784c631d44124c04` |

This is payload identity, not merely matching row counts. Documentation differs;
the organization release has later license metadata. Its existing license cell
remains unchanged because this pass did not reconcile its conflicting metadata.

The existing [mcj311 SALAD metadata](https://huggingface.co/api/datasets/mcj311/saladbench_data/tree/main?recursive=true&expand=true)
and [OpenSafetyLab SALAD metadata](https://huggingface.co/api/datasets/OpenSafetyLab/Salad-Data/tree/main?recursive=true&expand=true)
confirm an identical `attack_enhanced_set.json` SHA256:
`389da12f029a7f0c4a562f753e1dd5e53aed46d873ef1f568919d9f4b72e7062`.
Three other files have matching sizes but Git-versus-LFS hashes that cannot be
directly compared. Both entries remain until those payloads are verified.
OpenSafetyLab also publishes a newer subset absent from the mcj311 listing.
Deadbits embedding variants were not verified and remain unchanged. This is
not a complete license, availability or overlap audit of the legacy catalog.

## Access and licensing details worth preserving

- Gated additions include WildJailbreak, WildGuardMix, MHJ, ReNeLLM, XGuard,
  SORRY-Bench and ROK-FORTRESS. Their files require publisher access approval or
  acceptance plus an authorized HF login. A public card is not evidence of an
  anonymous download. No mirror was selected to bypass a gate.
- [BIPIA's license](https://github.com/microsoft/BIPIA/blob/main/LICENSE)
  explicitly excepts third-party datasets. [CyberSecEval's MIT license](https://github.com/meta-llama/PurpleLlama/blob/main/CybersecurityBenchmarks/LICENSE)
  covers the selected component, not every PurpleLlama project.
- [Do-Not-Answer's data-specific license section](https://huggingface.co/datasets/LibrAI/do-not-answer/blob/main/README.md)
  assigns CC-BY-NC-SA-4.0 to data despite its Apache metadata header.
  [AILuminate](https://github.com/mlcommons/ailuminate) similarly distinguishes
  CC-BY-4.0 data from Apache code. These distinctions are reflected in the CSV.
- [StrongREJECT](https://github.com/alexandrasouly/strongreject#license) includes
  imported questions under differing or unspecified terms; its CSV license
  cell remains blank. SafeGuard, XGuard, MCPTox and ToxiGen also have blank cells
  where data licensing was not established.
- [SORRY-Bench](https://huggingface.co/datasets/sorry-bench/sorry-bench-202503/blob/main/README.md)
  uses a custom agreement with redistribution restrictions. The registry is a
  source catalog, not a claim that every listed release is unrestricted open
  source or suitable for training. Several cards specify evaluation-only or
  research-only intended use, as recorded above.

## Follow-up for example-level deduplication

A later ingestion pass should preserve original IDs, source release, split and
context, then hash exact examples and report cross-source matches. Review near
matches separately. Do not drop all records sharing a harmful behavior goal:
MHJ conversations, cipher attacks and JBB artifacts can attack the same goal
with materially different payloads. This review did not merge or rewrite data
inside any upstream dataset.
