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

I'm currently a 2nd-year Phd candidate at [REAL LAB](https://zju-real.github.io), Zhejiang University, advised by [Yongliang Shen](https://person.zju.edu.cn/shenyongliang). Prior to this, I earned my B.E degree from [Chu Kochen Honors College](http://ckc.zju.edu.cn/ckcen/main.htm), Zhejiang University (浙江大学竺可桢学院) at 2024.

My research interests focus on AI Agents and LLM Post Training (RL included). My earlier work in 2025 focused on RL for GUI Agents, and my current research investigates Post-Training techniques for General Agents, including agent skills, on-policy distillation (OPD) and reinforcement learning (RL).


# 🔥 News
- *2026.05*: &nbsp;🔥🔥 Our new work [SDAR](https://arxiv.org/abs/2605.15155) was released, featured as 🤗 HF Daily Paper #2!
- *2026.05*: &nbsp;🔥🔥 Our new work [SKILL1](https://arxiv.org/abs/2605.06130) was released, featured as 🤗 HF Daily Paper #2!
- *2026.05*: &nbsp;🎉🎉 Four papers were accepted by ACL 2026, see you in San Diego, US.
- *2026.04*: &nbsp;🔥🔥 Our new work [SKILL0](https://arxiv.org/abs/2604.02268) was released, featured as 🤗 HF Daily Paper #2!
- *2026.02*: &nbsp;🎉🎉 One paper was accepted by CVPR 2026.
- *2025.11*: &nbsp;🎉🎉 Three papers were accepted by AAAI 2026.

# 📝 Publications 

## 🤖 Agentic RL
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/skill0.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization](https://arxiv.org/abs/2604.02268)

**Zhengxi Lu**, Zhiyuan Yao, Jinyang Wu, Chengcheng Han, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

[![](https://img.shields.io/badge/Paper-arXiv:2604.02268-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.02268)
[![](https://img.shields.io/github/stars/ZJU-REAL/SkillZero?style=social&label=Code)](https://github.com/ZJU-REAL/SkillZero)
- We propose an in-context agentic RL framework that internalizes external tool-use skills into the policy itself, enabling agents to retain reusable behaviors across tasks without repeated demonstrations.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/sdar.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SDAR: Self-Distilled Agentic Reinforcement Learning](https://arxiv.org/abs/2605.15155)

**Zhengxi Lu**, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

[![](https://img.shields.io/badge/Paper-arXiv:2605.15155-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.15155)
[![](https://img.shields.io/github/stars/ZJU-REAL/SDAR?style=social&label=Code)](https://github.com/ZJU-REAL/SDAR)
- A self-distillation pipeline that lets an agent improve through its own high-reward trajectories, bridging on-policy distillation and RL to stabilize long-horizon multi-step training.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/skill1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SKILL1: Unified Evolution of Skill-Augmented Agents via Reinforcement Learning](https://arxiv.org/abs/2605.06130)

Yaorui Shi, Yuxin Chen, **Zhengxi Lu**, Yuchun Miao, Shugui Liu, Qi Gu, Xunliang Cai, Xiang Wang, An Zhang

[![](https://img.shields.io/badge/Paper-arXiv:2605.06130-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.06130)
[![](https://img.shields.io/github/stars/ZJU-REAL/SkillZero?style=social&label=Code)](https://github.com/ZJU-REAL/SkillZero)
- Jointly evolves the agent policy and its skill library through RL, allowing newly discovered skills and the controller to co-adapt instead of being optimized in isolation.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/maestro.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles](https://arxiv.org/abs/2605.22177)

Jinyang Wu, Guocheng Zhai, Ruihan Jin, Yuhao Shen, **Zhengxi Lu**, Fan Zhang, Haoran Luo, Zheng Lian, Zhengqi Wen, Jianhua Tao

[![](https://img.shields.io/badge/Paper-arXiv:2605.22177-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2605.22177)
[![](https://img.shields.io/github/stars/jinyangwu/Maestro?style=social&label=Code)](https://github.com/jinyangwu/Maestro)
- An RL-trained orchestrator that routes among heterogeneous models and skills in a hierarchical ensemble, trading compute for capability under per-task budgets.
</div>
</div>

## 🤖 MLLM Agents
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/uir1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UI-R1: Enhancing Efficient Action Prediction of GUI Agents by Reinforcement Learning](https://arxiv.org/abs/2503.21620)

**Zhengxi Lu**, Yuxiang Chai, Yaxuan Guo, Xi Yin, Liang Liu, Hao Wang, Han Xiao, Shuai Ren, Guanjing Xiong, Hongsheng Li

[![](https://img.shields.io/badge/Paper-arXiv:2503.21620-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2503.21620)
[![](https://img.shields.io/github/stars/lll6gg/UI-R1?style=social&label=Code)](https://github.com/lll6gg/UI-R1)
- The first work to apply rule-based reinforcement learning to GUI action prediction, improving the data efficiency and grounding accuracy of MLLM-based GUI agents.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/uis1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UI-S1: Advancing GUI Automation via Semi-online Reinforcement Learning](https://arxiv.org/abs/2509.11543)

**Zhengxi Lu**, Yuxiang Chai, Yaxuan Guo, Hao Wang, Liang Liu, Shuai Ren, Han Xiao, Guanjing Xiong, Hongsheng Li, Xi Yin

[![](https://img.shields.io/badge/Paper-arXiv:2509.11543-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.11543)
[![](https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=social&label=Code)](https://github.com/X-PLUG/MobileAgent/tree/main/UI-S1)
- A semi-online RL paradigm that mixes offline trajectories with on-policy rollouts to combine the stability of imitation with the exploration benefits of online RL for GUI agents.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/mobileagentv3.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144)

Jiabo Ye, Xi Zhang, Haiyang Xu, Haowei Liu, Junyang Wang, Zhaoqing Zhu, Ziwei Zheng, Feiyu Gao, Junjie Cao, **Zhengxi Lu**, Jitong Liao, Qi Zheng, Fei Huang, Jingren Zhou, Ming Yan

[![](https://img.shields.io/badge/Paper-arXiv:2508.15144-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.15144)
[![](https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=social&label=Code)](https://github.com/X-PLUG/MobileAgent)
- A foundation-agent framework for mobile GUI automation that unifies perception, planning, and execution roles, achieving strong performance across long-horizon real-device tasks.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/guig2.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[GUI-G²: Gaussian Reward Modeling for GUI Grounding](https://arxiv.org/abs/2507.15846)

Fei Tang, Zhangxuan Gu, **Zhengxi Lu**, Xuyang Liu, Shuheng Shen, Changhua Meng, Wen Wang, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun Xiao, Yueting Zhuang

[![](https://img.shields.io/badge/Paper-arXiv:2507.15846-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2507.15846)
[![](https://img.shields.io/github/stars/ZJU-REAL/GUI-G2?style=social&label=Code)](https://github.com/ZJU-REAL/GUI-G2)
- Replaces binary hit/miss rewards with a Gaussian reward field over click coordinates, providing smoother gradients and substantially improving GUI grounding accuracy under RL.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/uicopilot.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UI-Copilot: Advancing Long-Horizon GUI Automation via Tool-Integrated Policy Optimization](https://arxiv.org/abs/2604.13822)

**Zhengxi Lu**, Fei Tang, Guangyi Liu, Kaitao Song, Xu Tan, Jin Ma, Wenqi Zhang, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

[![](https://img.shields.io/badge/Paper-arXiv:2604.13822-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2604.13822)
[![](https://img.shields.io/github/stars/ZJU-REAL/UI-Copilot?style=social&label=Code)](https://github.com/ZJU-REAL/UI-Copilot)
- Tool-integrated policy optimization that lets GUI agents call auxiliary tools mid-trajectory, extending effective horizon and credit assignment for long, multi-screen workflows.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Survey</div><img src='pub_images/survey.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LLM-Powered GUI Agents in Phone Automation: Surveying Progress and Prospects](https://arxiv.org/abs/2504.19838)

Guangyi Liu, Pengxiang Zhao, Liang Liu, Yaxuan Guo, Han Xiao, Weifeng Lin, Yuxiang Chai, Yue Han, Shuai Ren, Hao Wang, Xiaoyu Liang, Wenhao Wang, Tianze Wu, Linghao Li, Hao Wang, Guanjing Xiong, **Zhengxi Lu**, Siheng Chen, Yong Liu, Hongsheng Li

[![](https://img.shields.io/badge/Paper-arXiv:2504.19838-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.19838)
[![](https://img.shields.io/github/stars/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents?style=social&label=Code)](https://github.com/PhoneLLM/Awesome-LLM-Powered-Phone-GUI-Agents)
- A comprehensive survey of LLM-powered GUI agents for phone automation, covering datasets, agent architectures, training paradigms, evaluation benchmarks, and open challenges.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/learnact.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[LearnAct: Few-Shot Mobile GUI Agent with a Unified Demonstration Benchmark](https://arxiv.org/abs/2504.13805)

Guangyi Liu, Pengxiang Zhao, Liang Liu, Zhiming Chen, Yuxiang Chai, Shuai Ren, Hao Wang, **Zhengxi Lu**, Shibo He, Wenchao Meng

[![](https://img.shields.io/badge/Paper-arXiv:2504.13805-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2504.13805)
[![](https://img.shields.io/github/stars/lgy0404/LearnAct?style=social&label=Code)](https://github.com/lgy0404/LearnAct)
- Studies few-shot adaptation of mobile GUI agents from user demonstrations, accompanied by a unified benchmark that standardizes demonstration formats and evaluation protocols.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='pub_images/ttrlgui.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Test-Time Reinforcement Learning for GUI Grounding via Region Consistency](https://arxiv.org/abs/2508.05615)

Yong Du, Yuchen Yan, Fei Tang, **Zhengxi Lu**, Chang Zong, Weiming Lu, Shengpei Jiang, Yongliang Shen

[![](https://img.shields.io/badge/Paper-arXiv:2508.05615-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2508.05615)
[![](https://img.shields.io/github/stars/ZJU-REAL/gui-rcpo?style=social&label=Code)](https://github.com/ZJU-REAL/gui-rcpo)
- A label-free test-time RL approach that uses region-consistency among multiple predictions as a self-supervised reward to refine GUI grounding without ground-truth annotations.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Benchmark</div><img src='pub_images/masbench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MAS-Bench: A Unified Benchmark for Shortcut-Augmented Hybrid Mobile GUI Agents](https://arxiv.org/abs/2509.06477)

Pengxiang Zhao, Guangyi Liu, Yaozhen Liang, Weiqing He, **Zhengxi Lu**, Yuehao Huang, Yaxuan Guo, Kexin Zhang, Hao Wang, Liang Liu, Yong Liu

[![](https://img.shields.io/badge/Paper-arXiv:2509.06477-b31b1b?logo=arxiv&logoColor=white)](https://arxiv.org/abs/2509.06477)
[![](https://img.shields.io/github/stars/Pengxiang-zhao/MAS-Bench?style=social&label=Code)](https://github.com/Pengxiang-zhao/MAS-Bench)
- A unified benchmark for hybrid mobile GUI agents that can both interact via UI and invoke app shortcuts, providing fair comparison between pure-GUI and shortcut-augmented policies.
</div>
</div>


# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.
