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

Hi, I am Dongping Chen (陈东平), a final-year undergraduate at [HUST](https://hust.edu.cn).
=====
At present, I am working with Professor [Yao Wan](http://wanyao.me/) at HUST. Prior to this, I have the privilege of being a visiting student to University of Washington, where I work with Professors [Ranjay Krishna](https://ranjaykrishna.com/index.html) and Senior PhD [Jieyu Zhang](https://jieyuz2.github.io/). My academic journey has also been enriched by a collaboration with [Lichao Sun](https://lichao-sun.github.io/) at Lehigh University and [Yao Wan](http://wanyao.me/), [Pan Zhou](https://scholar.google.com/citations?user=cTpFPJgAAAAJ&hl=en) at HUST. I am also leading [an undergrad research lab](https://oneslab.github.io) at HUST, and very lucky to have the opportunity to work with my labmates. 

My research interests are deeply rooted in the latest advancements in generative models, especially multimodal and LLM-based agents. 

<!-- My latest CV can be viewed at [Here](CV_latest.pdf). -->
# 💡 Research Interest

- Multimodal: T2I/T2V models, multimodal large language model (MLLM), etc.
- LLM-based Agents: agentic workflow, tool usage, efficiency and utility.


# 🔥 News
- *2025.02*: &nbsp;🎉🎉 Two papers have been accepted by **CVPR 2025**! Five papers is on Arxiv! Check [Yue](https://howiehwong.github.io/)'s latest fantastic work on [Trustworthy Foundation Models](https://arxiv.org/abs/2502.14296)!
- *2025.01*: &nbsp;🎉🎉 Four papers have been accepted by **ICLR 2025**! **Interleaved Scene Graph** is selected as **ICLR 2025 Spotlight**! Two other papers have been accepted by **WWW 2025**!
- *2024.09*: &nbsp;🎉🎉 **HonestLLM** has been accepted by **NeurIPS 2024**! 
- *2024.08*: &nbsp;🥳🥳 I start my intern with Senior [PhD. Jieyu](https://jieyuz2.github.io/) and [Prof. Ranjay Krishna](https://ranjaykrishna.com/index.html) in University of Washington.
- *2024.06*: &nbsp;🎉🎉 **Self-Cognition** has been accepted by **ICMLW 2024**! Congratulations to [Jiawen](https://scholar.google.com/citations?user=yy8oPX0AAAAJ&hl=en).   
- *2024.06*: &nbsp;🥳🥳 Our **MLLM-as-a-Judge** is selected as **ICML 2024 Oral**!
- *2024.05*: &nbsp;🎉🎉 **AVLLM** has been accepted by **ACL 2024 Findings**! Congratulations to [Huichi](https://huichizhou.github.io/).
- *2024.05*: &nbsp;🎉🎉 **MLLM-as-a-Judge** has been accepted by **ICML 2024**! Congratulations to [Ruoxi](https://scholar.google.com/citations?user=F7cDYF0AAAAJ), [Shilin](https://scholar.google.com/citations?hl=en&user=b_qLXToAAAAJ), [Yaochen](https://scholar.google.com/citations?hl=en&user=pcqtbQEAAAAJ), [Yinuo](https://scholar.google.com/citations?hl=en&user=MKPvCFIAAAAJ), [Huichi](https://scholar.google.com/citations?user=1IJyxpUAAAAJ), [Qihui](https://scholar.google.com/citations?user=ZdgtY0EAAAAJ&hl=en)!
- *2024.03*: &nbsp;🎉🎉 **LLM-as-a-Coauthor** has been accepted by **NAACL 2024 Findings**! Congratulations to [Qihui](https://scholar.google.com/citations?user=ZdgtY0EAAAAJ&hl=en), [Chujie](https://flossiee.github.io/) and [Yue](https://howiehwong.github.io/)! 


# 📝 Publications 
* indicates equal contribution. † indicates corresponding author. ‡ indicates project leaders.
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025 Spotlight</div><img src='images/ISG.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Interleaved Scene Graph for Interleaved Text-and-Image Generation Assessment** [[PDF]](https://arxiv.org/abs/2411.17188) [[Github]](https://github.com/Dongping-Chen/ISG) [[Website]](https://interleave-eval.github.io/) 

**Dongping Chen** \*, Ruoxi Chen \*, Shu Pu \*, Zhaoyi Liu \*, Yanru Wu \*, Caixi Chen \*, Benlin Liu, Yue Huang, Yao Wan, Pan Zhou, Ranjay Krishna†

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/GUI.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents** [[PDF]](https://arxiv.org/pdf/2406.10819) [[Github]](https://github.com/Dongping-Chen/GUI-World) [[Website]](https://gui-world.github.io)

**Dongping Chen** \*, Yue Huang \*, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, Chenlong Wang, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan†, Pan Zhou†, Jianfeng Gao, Lichao Sun

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/HonestLLM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

***The Best of Both Worlds*: Toward an Honest and Helpful Large Language Model** [[PDF]](https://arxiv.org/abs/2406.00380) [[Github]](https://github.com/Flossiee/HonestyLLM) [[Website]](https://honestllm.github.io/)

Chujie Gao \*, Siyuan Wu \*, Yue Huang \*, **Dongping Chen** \*, Qihui Zhang \*, Zhengyan Fu, Yao Wan†, Xiangliang Zhang, Lichao Sun


</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2024 Oral</div><img src='images/mllm-judge.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark** [[PDF]](https://arxiv.org/abs/2402.04788) [[Github]](https://github.com/Dongping-Chen/MLLM-Judge) [[Website]](https://mllm-judge.github.io/)

**Dongping Chen** \*, Ruoxi Chen \*, Shilin Zhang \*, Yinuo Liu \*, Yaochen Wang \*, Huichi Zhou \*, Qihui Zhang \*, Yao Wan†, Pan Zhou†, Lichao Sun

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2024 Findings</div><img src='images/mixcase.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**LLM-as-a-Coauthor: The Challenges of Detecting LLM-Human Mixcase** [[PDF]](https://arxiv.org/abs/2401.05952) [[Github]](https://github.com/Dongping-Chen/MixSet) [[Website]](https://gui-world.github.io/)

Qihui Zhang \*, Chujie Gao \*, **Dongping Chen** \*, Yue Huang, Yixin Huang, Zhenyang Sun, Shilin Zhang, Weiye Li, Zhengyan Fu, Yao Wan, Lichao Sun†

</div>
</div>

- ![CVPR 2025](https://img.shields.io/badge/CVPR-2025-9AD7FF) [REALEDIT: Reddit Edits As a Large-scale Empirical Dataset for Image Transformations](https://arxiv.org/pdf/2502.03629) Peter Sushko, Ayana Bharadwaj, Zhi Yang Lim, Vasily Ilin, Ben Caffee, **Dongping Chen**, Mohammadreza Salehi, Cheng-Yu Hsieh, Ranjay Krishna†
- ![CVPR 2025](https://img.shields.io/badge/CVPR-2025-9AD7FF) [Perception Tokens Enhance Visual Reasoning in Multimodal Language Models](https://arxiv.org/pdf/2412.03548) Mahtab Bigverdi, Zelun Luo, Cheng-Yu Hsieh, Ethan Shen, **Dongping Chen**, Linda G. Shapiro, Ranjay Krishna†
- ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-e87213) [DataGen: A Unified Framework for Textual Dataset Generation Using Large Language Models](https://arxiv.org/pdf/2406.18966) Yue Huang \*, Siyuan Wu \*, Chujie Gao, **Dongping Chen**, Qihui Zhang, Yao Wan, Tianyi Zhou, Jianfeng Gao, Chaowei Xiao, Lichao Sun, Xiangliang Zhang†
- ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-e87213) [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://arxiv.org/pdf/2410.02736) Jiayi Ye \*, Yanbo Wang \*, Yue Huang \*, **Dongping Chen**, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh V Chawla, Xiangliang Zhang†
- ![WWW 2025](https://img.shields.io/badge/WWW-2025-EACD76) [WebCode2M: A Real-World Dataset for Code Generation from Webpage Designs](https://openreview.net/forum?id=aeP5nmlw5B) Yi Gui, Zhen Li, Yao Wan†, Yemin Shi, Hongyu Zhang, Yi Su, Bohua Chen, **Dongping Chen**, Siyuan Wu, Xing Zhou, Wenbin Jiang, Hai Jin, Xiangliang Zhang
- ![WWW 2025](https://img.shields.io/badge/WWW-2025-EACD76) [UICopilot: Automating UI Synthesis via Hierarchical Code Generation from Webpage Designs](https://openreview.net/forum?id=faMbH0wkye) Yi Gui, Yao Wan, Zhen Li, Zhongyi Zhang, **Dongping Chen**, Hongyu Zhang, Yi Su, Bohua Chen, Xing Zhou, Wenbin Jiang, Xiangliang Zhang
- ![ACL 2024](https://img.shields.io/badge/ACL-2024-red) [Evaluating the Validity of Word-level Adversarial Attacks with Large Language Models](https://aclanthology.org/2024.findings-acl.292.pdf) Huichi Zhou \*, Zhaoyang Wang \*, Hongtao Wang†,  **Dongping Chen**, Wenhan Mu, Fangyuan Zhang
- ![ICMLW 2024](https://img.shields.io/badge/ICMLW-2024-c821f3) [Self-Cognition in Large Language Models: An Exploratory Study](https://arxiv.org/pdf/2407.01505) **Dongping Chen** \*, Jiawen Shi \*, Yao Wan†, Pan Zhou†, Neil Zhenqiang Gong, Lichao Sun
- ![NeurIPSW 2024](https://img.shields.io/badge/NeurIPSW-2024-c7be87) [The Impact of Large Language Models in Academia: from Writing to Speaking](https://arxiv.org/pdf/2409.13686) Mingmeng Geng, Caixi Chen, Yanru Wu, **Dongping Chen**, Yao Wan, Pan Zhou, Roberto Trotta

# 🍀 In Submission

- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective](https://arxiv.org/abs/2502.14296) Yue Huang, Chujie Gao, Siyuan Wu, ... **Dongping Chen** ..., Xiangliang Zhang†
- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow](https://arxiv.org/pdf/2502.05036) Geliang Ouyang, Jingyao Chen, Zhihe Nie, Yi Gui, Yao Wan, Hongyu Zhang, **Dongping Chen**‡
- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale](https://arxiv.org/pdf/2502.16645) Chenlong Wang, Zhaoyang Chu, Zhengxiang Cheng, Xuyi Yang, Kaiyue Qiu, Yao Wan, Zhou Zhao, Xuanhua Shi, **Dongping Chen**‡
- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [CrowdSelect: Synthetic Instruction Data Selection with Multi-LLM Wisdom](https://arxiv.org/pdf/2503.01836) Yisen Li, Lingfeng Yang, Wenxuan Shen, Pan Zhou, Yao Wan, Weiwei Lin, **Dongping Chen**‡
- ![Preprint](https://img.shields.io/badge/Preprint-2024-87acc7) [ObscurePrompt: Jailbreaking Large Language Models via Obscure Input](https://arxiv.org/pdf/2406.13662) Yue Huang \*, Jingyu Tang \*, **Dongping Chen**, Bingda Tang, Yao Wan, Lichao Sun, Xiangliang Zhang†


<!-- <div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/Aggregate.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Aggregate, Decompose, and Fine-Tune: A Simple Yet Effective Factor-Tuning Method for Vision Transformer** [[PDF]](https://arxiv.org/abs/2311.06749) [[Github]](https://github.com/Dongping-Chen/EFFT-EFfective-Factor-Tuning)

**Dongping Chen** 
</div>
</div> -->

<!-- # 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📖 Educations
- *2024.08 - 2024.12*, Visiting Scholar, University of Washington. 
- *2021.09 - 2025.06 (expected)*, BEng.,  Huazhong University of Science and Technology. 


# 💬 Talks
- *2024.07*, Oral Presentation of **MLLM-as-a-Judge** at ICML 2024. [\[video\]](https://icml.cc/virtual/2024/oral/35497)

# 💻 Services
- 2025, Reviewer for ICLR 2025, ICASSP 2025
- 2024, Reviewer for ICML Workshops 2024, NeurIPS Workshops 2024

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Map Widget</title>
    <style>
        .map-container {
            width: 300px; 
            margin: 0 auto; 
            text-align: center; 
        }
        .map-container iframe {
            width: 100%; 
            height: 300px; 
        }
    </style>
</head>
<body>
    <div class="map-container">
        <script type='text/javascript' id='mapmyvisitors' src='https://mapmyvisitors.com/map.js?cl=fbffc5&w=a&t=m&d=2DkJRDrBeg-CCyqtKLmfTsHaZGyMG4L1RfpChDpZ6is&co=9ff4f3&cmo=f96e6e&ct=ffffff'></script>
    </div>
</body>
</html>
