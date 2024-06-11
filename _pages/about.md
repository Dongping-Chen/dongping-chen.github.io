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

Welcome to my personal website!  I am Dongping Chen (陈东平), a Year 3 undergraduate at [HUST](https://hust.edu.cn).
=====
At present, I have the privilege of being a visiting student to LAIR, where I work with Professors [Lichao Sun](https://lichao-sun.github.io/) at Lehigh University and [Yao Wan](http://wanyao.me/) at HUST. Prior to this, my academic journey has also been enriched by a collaboration with [Prof. Bolong Zheng](https://bolongzheng.com/) at HUST.

My academic and research interests are deeply rooted in the latest advancements in Multi-modal perception, Diffusion models, LLM calibration and trustworthy AI. 

My resume and transcripts can be viewed at [Here](Resume.pdf).
# 💡 Research Interest

- Multi-modal Perception: diffusion models, multi-modal large language model (MLLM), etc.
- LLM-based Agents: tool usage, efficiency and utility.
- Trustworthy AI: safety, truthfulness, fairness, robustness, and privacy of AI model.
  
  
# 🔥 News
- *2024.06*: &nbsp;🥳🥳 Our **MLLM-as-a-Judge** is selected as **ICML 2024 Oral**!
- *2024.05*: &nbsp;🎉🎉 One paper has been accepted by **ACL 2024 Findings**! Congratulations to [Huichi](https://huichizhou.github.io/).
- *2024.05*: &nbsp;🎉🎉 One paper has been accepted by **ICML 2024**! Congratulations to [Ruoxi](https://scholar.google.com/citations?user=F7cDYF0AAAAJ), [Shilin](https://scholar.google.com/citations?hl=en&user=b_qLXToAAAAJ), [Yaochen](https://scholar.google.com/citations?hl=en&user=pcqtbQEAAAAJ), [Yinuo](https://scholar.google.com/citations?hl=en&user=MKPvCFIAAAAJ), [Huichi](https://scholar.google.com/citations?user=1IJyxpUAAAAJ), [Qihui](https://scholar.google.com/citations?user=ZdgtY0EAAAAJ&hl=en)!
- *2024.03*: &nbsp;🎉🎉 One paper has been accepted by **NAACL 2024 Findings**! Congratulations to [Qihui](https://scholar.google.com/citations?user=ZdgtY0EAAAAJ&hl=en), [Chujie](https://flossiee.github.io/) and [Yue](https://howiehwong.github.io/)! 
- *2024.02*: &nbsp;🎉🎉 This summer, I will start my summer intern with Senior [PhD. Jieyu](https://jieyuz2.github.io/) and [Prof. Ranjay Krishna](https://ranjaykrishna.com/index.html) in University of Washington.

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2024 Oral</div><img src='images/mllm-judge.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark** [[PDF]](https://arxiv.org/abs/2402.04788) [[Github]](https://github.com/Dongping-Chen/MLLM-Judge) [[Website]](https://mllm-judge.github.io/)

**Dongping Chen** \*, Ruoxi Chen \*, Shilin Zhang \*, Yinuo Liu \*, Yaochen Wang \*, Huichi Zhou \*, Qihui Zhang \*, Pan Zhou, Yao Wan, Lichao Sun


</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACL 2024 Findings</div><img src='images/ACL2024.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Evaluating the Validity of Word-level Adversarial Attacks with Large Language Models** [[PDF]](https://drive.google.com/file/d/1wq4iaSicSBiljMUt7lENMPOOLneZj4EO/view?usp=drive_link)  [[Github]](https://github.com/HuichiZhou/AVLLM)

Huichi Zhou \*, Zhaoyang Wang \*,  **Dongping Chen**, Wenhan Mu, Fangyuan Zhang, Hongtao Wang


</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NAACL 2024 Findings</div><img src='images/mixcase.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**LLM-as-a-Coauthor: The Challenges of Detecting LLM-Human Mixcase** [[PDF]](https://arxiv.org/abs/2401.05952) [[Github]](https://github.com/Dongping-Chen/MixSet)

Qihui Zhang \*, Chujie Gao \*, **Dongping Chen** \*, Yue Huang, Yixin Huang, Zhenyang Sun, Shilin Zhang, Weiye Li, Zhengyan Fu, Yao Wan, Lichao Sun

</div>
</div>

# 🍀 Preprint

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Preprint</div><img src='images/HonestLLM.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

***The Best of Both Worlds*: Toward an Honest and Helpful Large Language Model** [[PDF]](https://arxiv.org/abs/2406.00380) [[Github]](https://github.com/Flossiee/HonestyLLM) 

Chujie Gao \*, Qihui Zhang \*, **Dongping Chen** \*, Yue Huang, Siyuan Wu, Zhengyan Fu, Yao Wan, Xiangliang Zhang, Lichao Sun


</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Arxiv Preprint</div><img src='images/Aggregate.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

**Aggregate, Decompose, and Fine-Tune: A Simple Yet Effective Factor-Tuning Method for Vision Transformer** [[PDF]](https://arxiv.org/abs/2311.06749) [[Github]](https://github.com/Dongping-Chen/EFFT-EFfective-Factor-Tuning)

**Dongping Chen** 

- Notice: This work was completed in-person with personal server before internship with Professors [Lichao Sun](https://lichao-sun.github.io/) and [Yao Wan](http://wanyao.me/).
</div>
</div>

<!-- # 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  -->

# 📖 Educations
- *2021.09 - 2025.06 (expected)*, BEng.,  Huazhong University of Science and Technology. 
<!-- - *2015.09 - 2021.06*, Zhixin High School, Guangzhou, China.  -->

<!-- # 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/) -->

<!-- # 💻 Internships
- *2023.09 - now*, [Lichao Sun](https://lichao-sun.github.io/), remote intern, Lehigh University. -->

# 🐱 My Beloved Petite Creature

<div align="center">
    <img src="images/IMG_8497.GIF" alt="sym" width="49%" />
    <img src="images/IMG_8480.GIF" alt="sym" width="49%" />
    <img src="images/IMG_8528.GIF" alt="sym" width="98%" />
    <!-- <img src="images/IMG_0279.GIF" alt="sym" width="49%" /> -->
</div>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Map Widget</title>
    <style>
        .map-container {
            width: 300px; /* 设置你想要的宽度 */
            margin: 0 auto; /* 居中对齐 */
            text-align: center; /* 文字居中对齐 */
        }
        .map-container iframe {
            width: 100%; /* 使iframe适应容器宽度 */
            height: 300px; /* 设置你想要的高度 */
        }
    </style>
</head>
<body>
    <div class="map-container">
        <script type='text/javascript' id='mapmyvisitors' src='https://mapmyvisitors.com/map.js?cl=fbffc5&w=a&t=m&d=2DkJRDrBeg-CCyqtKLmfTsHaZGyMG4L1RfpChDpZ6is&co=9ff4f3&cmo=f96e6e&ct=ffffff'></script>
    </div>
</body>
</html>
