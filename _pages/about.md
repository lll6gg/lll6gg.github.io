---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

I'm currently a 2nd-year Ph.D candidate at [REAL LAB](https://zju-real.github.io), Zhejiang University, advised by [Yongliang Shen](https://person.zju.edu.cn/shenyongliang). Prior to this, I earned my B.E degree from [Chu Kochen Honors College](http://ckc.zju.edu.cn/ckcen/main.htm), Zhejiang University (浙江大学竺可桢学院) at 2024.

My research interests focus on AI Agents and LLM Post Training (RL included). My earlier work in 2025 focused on RL for GUI Agents, and my current research investigates Post-Training techniques for General Agents, including agent skills, on-policy distillation (OPD) and reinforcement learning (RL).

📢 I'm actively seeking research-internship opportunities in industry on the topics above. Feel free to reach out if there might be a fit.

🐈 Our lab is also recruiting remote / on-site interns — undergraduate and Master's students are warmly welcomed! See [Join](https://zju-real.github.io/join.html).

# 🔥 News
- *2026.07*: &nbsp;🎉🎉 One paper was accepted by ACMMM 2026.
- *2026.06*: &nbsp;🔥🔥 Our new work [OPID](https://arxiv.org/abs/2606.26790) and [DEAR](https://arxiv.org/abs/2606.22830) were released, about opd.
- *2026.06*: &nbsp;🎉🎉 One paper was accepted by ECCV 2026.
- *2026.05*: &nbsp;🔥🔥 Our new work [SDAR](https://arxiv.org/abs/2605.15155) was released, featured as 🤗 HF Daily Paper #2!
- *2026.05*: &nbsp;🔥🔥 Our new work [SKILL1](https://arxiv.org/abs/2605.06130) was released, featured as 🤗 HF Daily Paper #2!
- *2026.04*: &nbsp;🎉🎉 Four papers were accepted by ACL 2026, see you in San Diego, US.
- *2026.04*: &nbsp;🔥🔥 Our new work [SKILL0](https://arxiv.org/abs/2604.02268) was released, featured as 🤗 HF Daily Paper #2!
- *2026.02*: &nbsp;🎉🎉 One paper was accepted by CVPR 2026.
- *2025.11*: &nbsp;🎉🎉 Three papers were accepted by AAAI 2026.

# 📝 Publications 

## 🤖 Agentic Post Training

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/skill0.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization](https://arxiv.org/abs/2604.02268)

**<u>Zhengxi Lu</u>**, Zhiyuan Yao, Jinyang Wu, Chengcheng Han, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

[[Paper]](https://arxiv.org/abs/2604.02268) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27ZJU-REAL/SkillZero%27%5D&label=Code&style=social&logo=github)](https://github.com/ZJU-REAL/SkillZero)
- We propose an in-context agentic RL framework that internalizes external tool-use skills into the policy itself, enabling agents to retain reusable behaviors across tasks without repeated demonstrations.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/sdar.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SDAR: Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/abs/2605.15155)

**<u>Zhengxi Lu</u>**, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

[[Paper]](https://arxiv.org/abs/2605.15155) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27ZJU-REAL/SDAR%27%5D&label=Code&style=social&logo=github)](https://github.com/ZJU-REAL/SDAR)
- A self-distillation pipeline that lets an agent improve through its own high-reward trajectories, bridging on-policy distillation and RL to stabilize long-horizon multi-step training.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/opid.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning](https://arxiv.org/abs/2606.26790)

Shuo Yang, Jinyang Wu, **<u>Zhengxi Lu</u>**, Yuhao Shen, Fan Zhang, Lang Feng, Shuai Zhang, Haoran Luo, Zheng Lian, Zhengqi Wen, Jianhua Tao

[[Paper]](https://arxiv.org/abs/2606.26790) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27jinyangwu/OPID%27%5D&label=Code&style=social&logo=github)](https://github.com/jinyangwu/OPID)
- Extracts hierarchical skill supervision (episode- and step-level) directly from completed on-policy trajectories and injects it back into the interaction history; the log-probability shift between original and skill-augmented contexts yields a token-level self-distillation advantage that complements the outcome reward, providing dense, distribution-matched hindsight supervision without external skill memories.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/skill1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SKILL1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://arxiv.org/abs/2605.06130)

Yaorui Shi, Yuxin Chen, **<u>Zhengxi Lu</u>**, Yuchun Miao, Shugui Liu, Qi Gu, Xunliang Cai, Xiang Wang, An Zhang

[[Paper]](https://arxiv.org/abs/2605.06130) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27AlphaLab-USTC/Skill1%27%5D&label=Code&style=social&logo=github)](https://github.com/AlphaLab-USTC/Skill1)
- Jointly evolves the agent policy and its skill library through RL, allowing newly discovered skills and the controller to co-adapt instead of being optimized in isolation.
</div>
</div>

- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">Preprint</span> [Finding the Evidence: Discovering Decision-Supporting Tokens for On-Policy Reasoning Distillation](https://arxiv.org/abs/2606.22830), Jinwei Xiao, Zhuowen Han, Yueqing Sun, **<u>Zhengxi Lu</u>**, Yuxin Liu, Zhiyuan Yao, Wentao Chen, Qi Gu, Xunliang Cai
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">Preprint</span> [Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles](https://arxiv.org/abs/2605.22177), Jinyang Wu, Guocheng Zhai, Ruihan Jin, Yuhao Shen, **<u>Zhengxi Lu</u>**, Fan Zhang, Haoran Luo, Zheng Lian, Zhengqi Wen, Jianhua Tao [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27jinyangwu/Maestro%27%5D&label=Code&style=social&logo=github)](https://github.com/jinyangwu/Maestro) 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">Preprint</span> [Code-A1: Adversarial Evolving of Code LLM and Test LLM via Reinforcement Learning](https://arxiv.org/abs/2603.15611), Aozhe Wang, Yuchen Yan, Nan Zhou, **<u>Zhengxi Lu</u>**, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27ZJU-REAL/Code-A1%27%5D&label=Code&style=social&logo=github)](https://github.com/ZJU-REAL/Code-A1) 

## 📱 MLLM Agents
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='pub_images/uir1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)

**<u>Zhengxi Lu</u>**, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Han Xiao, Shuai Ren, Guanjing Xiong, Hongsheng Li

[[Paper]](https://arxiv.org/abs/2503.21620) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27lll6gg/UI-R1%27%5D&label=Code&style=social&logo=github)](https://github.com/lll6gg/UI-R1)
- The first work to apply rule-based reinforcement learning to GUI action prediction, improving the data efficiency and grounding accuracy of MLLM-based GUI agents.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='pub_images/uis1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning](https://arxiv.org/abs/2509.11543)

**<u>Zhengxi Lu</u>**, Jiabo Ye, Fei Tang, Yongliang Shen, Haiyang Xu, Ziwei Zheng, Weiming Lu, Ming Yan, Fei Huang, Jun Xiao, Yueting Zhuang

[[Paper]](https://arxiv.org/abs/2509.11543) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27X-PLUG/MobileAgent%27%5D&label=Code&style=social&logo=github)](https://github.com/X-PLUG/MobileAgent)
- A semi-online RL paradigm that mixes offline trajectories with on-policy rollouts to combine the stability of imitation with the exploration benefits of online RL for GUI agents.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report</div><img src='pub_images/mobileagentv3.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144)

Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu Gao, Junjie Cao, **<u>Zhengxi Lu</u>**, Jitong Liao, Qi Zheng, Fei Huang, Jingren Zhou, Ming Yan

[[Paper]](https://arxiv.org/abs/2508.15144) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27X-PLUG/MobileAgent%27%5D&label=Code&style=social&logo=github)](https://github.com/X-PLUG/MobileAgent)
- A foundation-agent framework for mobile GUI automation that unifies perception, planning, and execution roles, achieving strong performance across long-horizon real-device tasks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='pub_images/guig2.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GUI-G²: Gaussian Reward Modeling for GUI Grounding](https://arxiv.org/abs/2507.15846)

Fei Tang, Zhangxuan Gu, **<u>Zhengxi Lu</u>**, Xuyang Liu, Shuheng Shen, Changhua Meng, Wen Wang, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun Xiao, Yueting Zhuang

[[Paper]](https://arxiv.org/abs/2507.15846) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27ZJU-REAL/GUI-G2%27%5D&label=Code&style=social&logo=github)](https://github.com/ZJU-REAL/GUI-G2)
- Replaces binary hit/miss rewards with a Gaussian reward field over click coordinates, providing smoother gradients and substantially improving GUI grounding accuracy under RL.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2026</div><img src='pub_images/uicopilot.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization](https://arxiv.org/abs/2604.13822)

**<u>Zhengxi Lu</u>**, Fei Tang, Guangyi Liu, Kaitao Song, Xu Tan, Jin Ma, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

[[Paper]](https://arxiv.org/abs/2604.13822) | [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27ZJU-REAL/UI-Copilot%27%5D&label=Code&style=social&logo=github)](https://github.com/ZJU-REAL/UI-Copilot)
- Tool-integrated policy optimization that lets GUI agents call auxiliary tools mid-trajectory, extending effective horizon and credit assignment for long, multi-screen workflows.
</div>
</div>

- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">TMLR 2026</span> [LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838), Guangyi Liu, Pengxiang Zhao, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, Wenhao Wang, Tianze Wu, Linghao Li, Hao Wang, Guanjing Xiong, **<u>Zhengxi Lu</u>**, Siheng Chen, Yong Liu, Hongsheng Li [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents%27%5D&label=Code&style=social&logo=github)](https://github.com/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents) 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">ACL 2026 Findings</span> [LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805), Guangyi Liu, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, Shuai Ren, Hao Wang, **<u>Zhengxi Lu</u>**, Shibo He, Wenchao Meng [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27lgy0404/LearnAct%27%5D&label=Code&style=social&logo=github)](https://github.com/lgy0404/LearnAct) 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">AAAI 2026</span> [Test-Time Reinforcement Learning for GUI Grounding via Region Consistency](https://arxiv.org/abs/2508.05615), Yong Du, Yuchen Yan, Fei Tang, **<u>Zhengxi Lu</u>**, Chang Zong, Weiming Lu, Shengpei Jiang, Yongliang Shen [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27ZJU-REAL/gui-rcpo%27%5D&label=Code&style=social&logo=github)](https://github.com/ZJU-REAL/gui-rcpo) 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">ACL 2026</span> [MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](https://arxiv.org/abs/2509.06477), Pengxiang Zhao, Guangyi Liu, Yaozhen Liang, Weiqing He, **<u>Zhengxi Lu</u>**, Yuehao Huang, Yaxuan Guo, Kexin Zhang, Hao Wang, Liang Liu, Yong Liu [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27Pengxiang-zhao/MAS-Bench%27%5D&label=Code&style=social&logo=github)](https://github.com/Pengxiang-zhao/MAS-Bench) 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">CVPR 2026</span> [GUI-SAGE: Enhancing GUI Automation with Self-Explanatory Learning](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=wBu2GXEAAAAJ&citation_for_view=wBu2GXEAAAAJ:hC7cP41nSMkC), Fei Tang, Zhangxuan Gu, **<u>Zhengxi Lu</u>**, Shangzhan Zhang, Zhengwen Zeng, Shuheng Shen, Changhua Meng, Yuchen Yan, Wenqi Zhang, Yongliang Shen, Weiming Lu, Yueting Zhuang. 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">ECCV 2026</span> [Label-free GUI Grounding via Confidence-guided Negative Reinforcement Learning](https://openreview.net/forum?id=Hghm8tVvbs), **<u>Zhengxi Lu</u>**, et al. 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">ACMMM 2026</span> [MemGUI-Bench: Benchmarking Memory of Mobile GUI Agents in Dynamic Environments](https://arxiv.org/abs/2602.06075), Guangyi Liu, Pengxiang Zhao, Yaozhen Liang, Qinyi Luo, Shunye Tang, Yuxiang Chai, Weifeng Lin, Han Xiao, WenHao Wang, Siheng Chen, **<u>Zhengxi Lu</u>**, Gao Wu, Hao Wang, Liang Liu, Yong Liu [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27lgy0404/MemGUI-Bench%27%5D&label=Code&style=social&logo=github)](https://github.com/lgy0404/MemGUI-Bench) 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">Preprint</span> [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evaluation](https://arxiv.org/abs/2604.08455), Tongbo Chen, **<u>Zhengxi Lu</u>**, ..., Yongliang Shen [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27ZJU-REAL/KnowU-Bench%27%5D&label=Code&style=social&logo=github)](https://github.com/ZJU-REAL/KnowU-Bench) 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">Preprint</span> [UI-Zoomer: Uncertainty-Driven Adaptive Zoom-In for GUI Grounding](https://arxiv.org/abs/2604.14113), Fei Tang, Bofan Chen, **<u>Zhengxi Lu</u>**, Tongbo Chen, Songqin Nong, Tao Jiang, Wenhao Xu, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27ZJU-REAL/UI-Zoomer%27%5D&label=Code&style=social&logo=github)](https://github.com/ZJU-REAL/UI-Zoomer) 
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">Preprint</span> [GUI-CIDER: Mid-training GUI Agents via Causal Internalization and Density-aware Exemplar Reselection](https://arxiv.org/abs/2605.28534), Zheng Wu, Chengcheng Han, **<u>Zhengxi Lu</u>**, Tianjie Ju, Yanyu Chen, Qi Gu, Xunliang Cai, Zhuosheng Zhang [![](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Flll6gg%2Flll6gg.github.io%40github-star-stats%2Fstar_counts.json&query=%24%5B%27Wuzheng02/GUI-CIDER%27%5D&label=Code&style=social&logo=github)](https://github.com/Wuzheng02/GUI-CIDER)

## 🎨 Multimodal AI
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">ICLR 2025 / AI4Drug @ NIPS'24</span> [ProtPainter: Draw or Drag Protein via Topology-guided Diffusion](https://arxiv.org/abs/2504.14274), **<u>Zhengxi Lu</u>**, Shizhuo Cheng, Yuru Jiang, Yan Zhang, Min Zhang
- <span style="color:white;background-color:#00369f;padding:0 0.6em;font-size:0.8em;">Preprint</span> [M³-Verse: A "Spot the Difference" Challenge for Large Multimodal Models](https://arxiv.org/abs/2512.18735), Kewei Wei, Bocheng Hu, Jie Cao, Xiaohan Chen, **<u>Zhengxi Lu</u>**, Wubing Xia, Weili Xu, Jiaao Wu, Junchen He, Mingyu Jia, Ciyun Zhao, Ye Sun, Yizhi Li, Zhonghan Zhao, Jian Zhang, Gaoang Wang 


# 🎖 Honors and Awards 
- Second-Class Scholarship of Zhejiang University, 2021, 2022, 2023.

# 📖 Educations
- *2020.09 - 2024.06*: B.E student at [Chu Kochen Honors College](http://ckc.zju.edu.cn/ckcen/main.htm), Zhejiang University (浙江大学竺可桢学院).
- *2024.09 - now*: Ph.D candidate at REAL Lab, Zhejiang University.

# 💬 Misc
- **Invited Talks**: 
  - *2026.5.24*: I gave a talk about skills invited by ZJU AI Talk. [Link](https://mp.weixin.qq.com/s/YBJKW8RJ8aB06Jo6Ufi6xQ).
- **Reviewers**:
  - *2025*: ACMMM 2025, AAAI 2026, ICLR 2026.
  - *2026*: CVPR 2026, ECCV 2026, Nuerips 2026.

# 💻 Internships
- *2025.03 - 2025.06*: Research Intern at Vivo AI Lab, advised by [Liang Liu](https://scholar.google.com/citations?hl=zh-CN&user=Kkg3IPMAAAAJ).
- *2025.06 - 2025.11*: Research Intern at Alibaba Tongyi Lab, advised by [Haiyang Xu](https://scholar.google.com/citations?user=qZYvce8AAAAJ&hl=zh-CN&oi=ao) and [Ming Yan](https://scholar.google.com/citations?user=uIUfGxYAAAAJ&hl=zh-CN).
- *2026.03 - 2026 (now)*: Beidou Research Intern at [Meituan Longcat Team](https://github.com/meituan-longcat), advised by [Qi Gu](https://scholar.google.com/citations?hl=zh-CN&user=s_5-ctUAAAAJ).
