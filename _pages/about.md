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

Hi, I am Dongping Chen (陈东平).
=====
At present, I am working with Professor [Tianyi Zhou](https://tianyizhou.github.io/) at UMD. Prior to this, I have the privilege of being a visiting student to University of Washington, where I work with Professors [Ranjay Krishna](https://ranjaykrishna.com/index.html) and Senior PhD [Jieyu Zhang](https://jieyuz2.github.io/). My academic journey has also been enriched by a collaboration with [Lichao Sun](https://lichao-sun.github.io/) at Lehigh University, [Xiangliang Zhang](https://engineering.nd.edu/faculty/xiangliang-zhang/) at University of Notre Dame and [Yao Wan](http://wanyao.me/) at HUST. I am also leading [an undergrad research lab](https://oneslab.github.io) with Professor [Yao Wan](http://wanyao.me/), and very lucky to have the opportunity to work with my labmates. 

My research interests are deeply rooted in the latest advancements in generative models, especially multimodal, LLM-based agents and frontier trustworthy problems.

<span class="highlight-red">I'm looking for summer intern opportunities in 2026 summer and feel free to reach out.</span> 

I'm interested in connecting with students for research collaboration, mentorship, or just making friends! I especially encourage junior student or students from underrepresented groups to reach out. Feel free to schedule a meeting via [this link](https://calendly.com/dongping-umd/30min). 

<!-- My latest CV can be viewed at [Here](CV_latest.pdf). -->
<!-- # 💡 Research Interest

- Multimodal: T2I/T2V models, multimodal large language model (MLLM), etc.
- LLM-based Agents: agentic workflow, tool usage, efficiency and utility. -->


<!-- # 🔥 News
- *2025.02*: &nbsp;🎉🎉 Two papers have been accepted by **CVPR 2025**! Six papers is on Arxiv! Check [Yue](https://howiehwong.github.io/)'s latest fantastic work on [Trustworthy Foundation Models](https://arxiv.org/abs/2502.14296)!
- *2025.01*: &nbsp;🎉🎉 Four papers have been accepted by **ICLR 2025**! **Interleaved Scene Graph** is selected as **ICLR 2025 Spotlight**! Two other papers have been accepted by **WWW 2025**!
- *2024.09*: &nbsp;🎉🎉 **HonestLLM** has been accepted by **NeurIPS 2024**! 
- *2024.08*: &nbsp;🥳🥳 I start my intern with Senior [PhD. Jieyu](https://jieyuz2.github.io/) and [Prof. Ranjay Krishna](https://ranjaykrishna.com/index.html) in University of Washington.
- *2024.06*: &nbsp;🎉🎉 **Self-Cognition** has been accepted by **ICMLW 2024**! Congratulations to [Jiawen](https://scholar.google.com/citations?user=yy8oPX0AAAAJ&hl=en).   
- *2024.06*: &nbsp;🥳🥳 Our **MLLM-as-a-Judge** is selected as **ICML 2024 Oral**!
- *2024.05*: &nbsp;🎉🎉 **AVLLM** has been accepted by **ACL 2024 Findings**! Congratulations to [Huichi](https://huichizhou.github.io/).
- *2024.05*: &nbsp;🎉🎉 **MLLM-as-a-Judge** has been accepted by **ICML 2024**! Congratulations to [Ruoxi](https://scholar.google.com/citations?user=F7cDYF0AAAAJ), [Shilin](https://scholar.google.com/citations?hl=en&user=b_qLXToAAAAJ), [Yaochen](https://scholar.google.com/citations?hl=en&user=pcqtbQEAAAAJ), [Yinuo](https://scholar.google.com/citations?hl=en&user=MKPvCFIAAAAJ), [Huichi](https://scholar.google.com/citations?user=1IJyxpUAAAAJ), [Qihui](https://scholar.google.com/citations?user=ZdgtY0EAAAAJ&hl=en)!
- *2024.03*: &nbsp;🎉🎉 **LLM-as-a-Coauthor** has been accepted by **NAACL 2024 Findings**! Congratulations to [Qihui](https://scholar.google.com/citations?user=ZdgtY0EAAAAJ&hl=en), [Chujie](https://flossiee.github.io/) and [Yue](https://howiehwong.github.io/)!  -->


# 📝 Publications 
\* indicates equal contribution. ‡ indicates project leaders.

<style>
.publication-tabs {
    display: flex;
    margin-bottom: 20px;
    border-bottom: 2px solid #e0e0e0;
}

.tab-button {
    background: none;
    border: none;
    padding: 12px 24px;
    cursor: pointer;
    font-size: 16px;
    font-weight: 500;
    color: #666;
    border-bottom: 3px solid transparent;
    transition: all 0.3s ease;
    margin-right: 10px;
}

.tab-button:hover {
    color: #333;
    background-color: #f5f5f5;
}

.tab-button.active {
    color: #2c5aa0;
    border-bottom-color: #2c5aa0;
    background-color: #f8f9fa;
}

.tab-content {
    display: none;
}

.tab-content.active {
    display: block;
}

.empty-section {
    text-align: center;
    padding: 40px 20px;
    color: #666;
    font-style: italic;
    background-color: #f8f9fa;
    border-radius: 8px;
    margin: 20px 0;
}

.author-me {
    background-color: #E3F2FD;
    border: 1px solid #BBDEFB;
    border-radius: 4px;
    padding: 2px 6px;
    margin: 0 2px;
    color: #1565C0;
    font-weight: 500;
}

.highlight-red {
    background-color: #FFEBEE;
    border: 1px solid #FFCDD2;
    border-radius: 4px;
    padding: 4px 8px;
    margin: 2px 0;
    color: #C62828;
    font-weight: 600;
    display: inline-block;
}
</style>

<div class="publication-tabs">
    <button class="tab-button active" onclick="switchTab(event, 'mainly-contribute')">Papers I Mainly Contribute</button>
    <button class="tab-button" onclick="switchTab(event, 'projects-lead')">Projects that I Lead</button>
</div>

<div id="mainly-contribute" class="tab-content active">

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025 Spotlight</div><img src='images/ISG.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Interleaved Scene Graph for Interleaved Text-and-Image Generation Assessment** [[PDF]](https://arxiv.org/pdf/2411.17188) [[Github]](https://github.com/Dongping-Chen/ISG) [[Website]](https://interleave-eval.github.io/) 

<span class="author-me">**Dongping Chen**</span> \*, Ruoxi Chen \*, Shu Pu \*, Zhaoyi Liu \*, Yanru Wu \*, Caixi Chen \*, Benlin Liu, Yue Huang, Yao Wan, Pan Zhou, Ranjay Krishna†

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='images/GUI.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents** [[PDF]](https://arxiv.org/pdf/2406.10819) [[Github]](https://github.com/Dongping-Chen/GUI-World) [[Website]](https://gui-world.github.io)

<span class="author-me">**Dongping Chen**</span> \*, Yue Huang \*, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, Chenlong Wang, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan†, Pan Zhou†, Jianfeng Gao, Lichao Sun

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='images/HonestLLM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

***The Best of Both Worlds*: Toward an Honest and Helpful Large Language Model** [[PDF]](https://arxiv.org/pdf/2406.00380) [[Github]](https://github.com/Flossiee/HonestyLLM) [[Website]](https://honestllm.github.io/)

Chujie Gao \*, Siyuan Wu \*, Yue Huang \*, <span class="author-me">**Dongping Chen**</span> \*, Qihui Zhang \*, Zhengyan Fu, Yao Wan†, Xiangliang Zhang, Lichao Sun

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2024 Oral</div><img src='images/mllm-judge.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark** [[PDF]](https://arxiv.org/pdf/2402.04788) [[Github]](https://github.com/Dongping-Chen/MLLM-Judge) [[Website]](https://mllm-judge.github.io/)

<span class="author-me">**Dongping Chen**</span> \*, Ruoxi Chen \*, Shilin Zhang \*, Yinuo Liu \*, Yaochen Wang \*, Huichi Zhou \*, Qihui Zhang \*, Yao Wan†, Pan Zhou†, Lichao Sun

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2024 Findings</div><img src='images/mixcase.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**LLM-as-a-Coauthor: The Challenges of Detecting LLM-Human Mixcase** [[PDF]](https://arxiv.org/pdf/2401.05952) [[Github]](https://github.com/Dongping-Chen/MixSet) [[Website]](https://gui-world.github.io/)

Qihui Zhang \*, Chujie Gao \*, <span class="author-me">**Dongping Chen**</span> \*, Yue Huang, Yixin Huang, Zhenyang Sun, Shilin Zhang, Weiye Li, Zhengyan Fu, Yao Wan, Lichao Sun†

</div>
</div>

</div>

<div id="projects-lead" class="tab-content">

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/double-bench.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?** [[PDF]](https://arxiv.org/pdf/2508.03644) [[Github]](https://github.com/Episoode/Double-Bench) [[Website]](https://double-bench.github.io/) [[Dataset]](https://huggingface.co/datasets/Episoode/Double-Bench)

Wenxuan Shen \*, Mingjia Wang \*, Yaochen Wang, <span class="author-me">Dongping Chen</span>‡, Junjie Yang, Yao Wan, Weiwei Lin†

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/code_transformed.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**code_transformed: The Influence of Large Language Models on Code** [[PDF]](https://arxiv.org/pdf/2506.12014) [[Github]](https://github.com/ignorancex/LLM_code) 

Yuliang Xu \*, Siming Huang \*, Mingmeng Geng†, Yao Wan†, Xuanhua Shi, <span class="author-me">Dongping Chen</span>‡

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report</div><img src='images/LC-R1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Optimizing Length Compression in Large Reasoning Models** [[PDF]](https://arxiv.org/pdf/2506.14755) [[Github]](https://github.com/zxiangx/LC-R1) 

Zhengxiang Cheng, <span class="author-me">Dongping Chen</span>‡, Mingyang Fu, Tianyi Zhou†

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/liveVQA.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Seeking and Updating with Live Visual Knowledge** [[PDF]](https://arxiv.org/pdf/2504.05288) [[Github]](https://github.com/fumingyang2004/LIVEVQA) [[Dataset]](https://huggingface.co/datasets/ONE-Lab/LiveVQA-new/tree/main) [[Website]](https://livevqa.github.io/)

Mingyang Fu\*, Yuyang Peng\*, <span class="author-me">Dongping Chen</span>‡, Zetong Zhou, Benlin Liu, Yao Wan†, Zhou Zhao, Philip S. Yu, Ranjay Krishna†

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2025 Dataset Track</div><img src='images/multiref.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**MultiRef: Controllable Image Generation with Multiple Visual References** [[PDF]](https://arxiv.org/pdf/2508.06905) [[Github]](https://github.com/Dipsy0830/MultiRef-code) [[Dataset]](https://huggingface.co/datasets/ONE-Lab/MultiRef-dataset) [[Website]](https://multiref.github.io/)

Ruoxi Chen, <span class="author-me">Dongping Chen</span>‡, Siyuan Wu, Sinan Wang, Shiyun Lang, Petr Sushko, Gaoyang Jiang, Yao Wan, Ranjay Krishna†

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">EMNLP 2025 Findings</div><img src='images/nowait.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Wait, We Don't Need to "Wait"! Removing Thinking Tokens Improves Reasoning Efficiency** [[PDF]](https://arxiv.org/pdf/2506.08343v2) (Code Coming Soon)

Chenlong Wang, Yuanning Feng, <span class="author-me">Dongping Chen</span>‡, Zhaoyang Chu, Ranjay Krishna, Tianyi Zhou†

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2025 Dataset and Benchmark Track</div><img src='images/JudgeAnything.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Judge Anything: MLLM as a Judge Across Any Modality** [[PDF]](https://arxiv.org/pdf/2503.17489) [[Webpage]](https://urrealhero.github.io/judgeanythingweb/)

Shu Pu*, Yaochen Wang*, <span class="author-me">Dongping Chen</span>‡, Yuhang Chen, Guohao Wang, Qi Qin, Zhongyi Zhang, Zhiyuan Zhang, Zetong Zhou, Shuang Gong, Yi Gui, Yao Wan†, Philip S. Yu

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IC2S2 2025</div><img src='images/Wikipedia.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Wikipedia in the Era of LLMs: Evolution and Risks** [[PDF]](https://arxiv.org/pdf/2503.17489)

Siming Huang \*, Yuliang Xu \*, Mingmeng Geng†, Yao Wan†, <span class="author-me">Dongping Chen</span>‡

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='images/codesync.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale** [[PDF]](https://arxiv.org/pdf/2502.16645) [[Code]](https://github.com/Lucky-voyage/Code-Sync)

Chenlong Wang, Zhaoyang Chu, Zhengxiang Cheng, Xuyi Yang, Kaiyue Qiu, Yao Wan, Zhou Zhao, Xuanhua Shi, <span class="author-me">Dongping Chen</span>‡

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2025</div><img src='images/nvAgent.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow** [[PDF]](https://arxiv.org/pdf/2502.05036) [[Code]](https://github.com/geliang0114/nvAgent)

Geliang Ouyang, Jingyao Chen, Zhihe Nie, Yi Gui, Yao Wan†, Hongyu Zhang, <span class="author-me">Dongping Chen</span>‡

</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2025 Findings</div><img src='images/llm-speaking.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**The Impact of Large Language Models in Academia: from Writing to Speaking** [[PDF]](https://arxiv.org/pdf/2409.13686)

Mingmeng Geng†, Caixi Chen, Yanru Wu, <span class="author-me">Dongping Chen</span>‡, Yao Wan, Pan Zhou

</div>
</div>

</div>

<script>
function switchTab(evt, tabName) {
    var i, tabcontent, tablinks;
    
    // Hide all tab content
    tabcontent = document.getElementsByClassName("tab-content");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].classList.remove("active");
    }
    
    // Remove active class from all tab buttons
    tablinks = document.getElementsByClassName("tab-button");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].classList.remove("active");
    }
    
    // Show the selected tab and mark the button as active
    document.getElementById(tabName).classList.add("active");
    evt.currentTarget.classList.add("active");
}
</script>

<!-- - ![CVPR 2025](https://img.shields.io/badge/CVPR-2025-9AD7FF) [REALEDIT: Reddit Edits As a Large-scale Empirical Dataset for Image Transformations](https://arxiv.org/pdf/2502.03629) Peter Sushko, Ayana Bharadwaj, Zhi Yang Lim, Vasily Ilin, Ben Caffee, **Dongping Chen**, Mohammadreza Salehi, Cheng-Yu Hsieh, Ranjay Krishna†
- ![CVPR 2025](https://img.shields.io/badge/CVPR-2025-9AD7FF) [Perception Tokens Enhance Visual Reasoning in Multimodal Language Models](https://arxiv.org/pdf/2412.03548) Mahtab Bigverdi, Zelun Luo, Cheng-Yu Hsieh, Ethan Shen, **Dongping Chen**, Linda G. Shapiro, Ranjay Krishna†
- ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-e87213) [DataGen: A Unified Framework for Textual Dataset Generation Using Large Language Models](https://arxiv.org/pdf/2406.18966) Yue Huang \*, Siyuan Wu \*, Chujie Gao, **Dongping Chen**, Qihui Zhang, Yao Wan, Tianyi Zhou, Jianfeng Gao, Chaowei Xiao, Lichao Sun, Xiangliang Zhang†
- ![ICLR 2025](https://img.shields.io/badge/ICLR-2025-e87213) [Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge](https://arxiv.org/pdf/2410.02736) Jiayi Ye \*, Yanbo Wang \*, Yue Huang \*, **Dongping Chen**, Qihui Zhang, Nuno Moniz, Tian Gao, Werner Geyer, Chao Huang, Pin-Yu Chen, Nitesh V Chawla, Xiangliang Zhang†
- ![WWW 2025](https://img.shields.io/badge/WWW-2025-EACD76) [WebCode2M: A Real-World Dataset for Code Generation from Webpage Designs](https://openreview.net/forum?id=aeP5nmlw5B) Yi Gui, Zhen Li, Yao Wan†, Yemin Shi, Hongyu Zhang, Yi Su, Bohua Chen, **Dongping Chen**, Siyuan Wu, Xing Zhou, Wenbin Jiang, Hai Jin, Xiangliang Zhang
- ![WWW 2025](https://img.shields.io/badge/WWW-2025-EACD76) [UICopilot: Automating UI Synthesis via Hierarchical Code Generation from Webpage Designs](https://openreview.net/forum?id=faMbH0wkye) Yi Gui, Yao Wan, Zhen Li, Zhongyi Zhang, **Dongping Chen**, Hongyu Zhang, Yi Su, Bohua Chen, Xing Zhou, Wenbin Jiang, Xiangliang Zhang
- ![ACL 2024](https://img.shields.io/badge/ACL-2024-red) [Evaluating the Validity of Word-level Adversarial Attacks with Large Language Models](https://aclanthology.org/2024.findings-acl.292.pdf) Huichi Zhou \*, Zhaoyang Wang \*, Hongtao Wang†,  **Dongping Chen**, Wenhan Mu, Fangyuan Zhang
- ![ICMLW 2024](https://img.shields.io/badge/ICMLW-2024-c821f3) [Self-Cognition in Large Language Models: An Exploratory Study](https://arxiv.org/pdf/2407.01505) **Dongping Chen** \*, Jiawen Shi \*, Yao Wan†, Pan Zhou†, Neil Zhenqiang Gong, Lichao Sun
- ![NeurIPSW 2024](https://img.shields.io/badge/NeurIPSW-2024-c7be87) [The Impact of Large Language Models in Academia: from Writing to Speaking](https://arxiv.org/pdf/2409.13686) Mingmeng Geng, Caixi Chen, Yanru Wu, **Dongping Chen**, Yao Wan, Pan Zhou, Roberto Trotta

# 🍀 In Submission

- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [Judge Anything: MLLM as a Judge Across Any Modality](https://arxiv.org/pdf/2503.17489) Shu Pu*, Yaochen Wang*, **Dongping Chen**‡, Yuhang Chen, Guohao Wang, Qi Qin, Zhongyi Zhang, Zhiyuan Zhang, Zetong Zhou, Shuang Gong, Yi Gui, Yao Wan, Philip S. Yu
- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [On the Trustworthiness of Generative Foundation Models: Guideline, Assessment, and Perspective](https://arxiv.org/abs/2502.14296) Yue Huang, Chujie Gao, Siyuan Wu, ... **Dongping Chen** ..., Xiangliang Zhang†
- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow](https://arxiv.org/pdf/2502.05036) Geliang Ouyang, Jingyao Chen, Zhihe Nie, Yi Gui, Yao Wan, Hongyu Zhang, **Dongping Chen**
- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale](https://arxiv.org/pdf/2502.16645) Chenlong Wang, Zhaoyang Chu, Zhengxiang Cheng, Xuyi Yang, Kaiyue Qiu, Yao Wan, Zhou Zhao, Xuanhua Shi, **Dongping Chen**‡
- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [Wikipedia in the Era of LLMs: Evolution and Risks](https://arxiv.org/pdf/2503.02879) Siming Huang, Yuliang Xu, Mingmeng Geng, Yao Wan, **Dongping Chen**‡
- ![Preprint](https://img.shields.io/badge/Preprint-2025-87acc7) [CrowdSelect: Synthetic Instruction Data Selection with Multi-LLM Wisdom](https://arxiv.org/pdf/2503.01836) Yisen Li, Lingfeng Yang, Wenxuan Shen, Pan Zhou, Yao Wan, Weiwei Lin, **Dongping Chen**‡
- ![Preprint](https://img.shields.io/badge/Preprint-2024-87acc7) [ObscurePrompt: Jailbreaking Large Language Models via Obscure Input](https://arxiv.org/pdf/2406.13662) Yue Huang \*, Jingyu Tang \*, **Dongping Chen**, Bingda Tang, Yao Wan, Lichao Sun, Xiangliang Zhang† -->


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
- *2025.08 - Current*, CS PhD Student, University of Maryland.
- *2024.08 - 2024.12*, Visiting Scholar, University of Washington. 
- *2021.09 - 2025.06 (expected)*, BEng.,  Huazhong University of Science and Technology. 


<!-- # 💬 Talks
- *2024.07*, Oral Presentation of **MLLM-as-a-Judge** at ICML 2024. [\[video\]](https://icml.cc/virtual/2024/oral/35497)

# 💻 Services
- 2025, Reviewer for ARR Feb, ICCV/ICLR/ICASSP
- 2024, Reviewer for ICML/NeurIPS Workshops -->

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
