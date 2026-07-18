---
permalink: /
title: ""
excerpt: ""
author_profile: false
body_class: wiki-home-page
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

<div class="wiki-home">
  <header class="wiki-hero">
    <p class="wiki-hero__eyebrow">Research profile</p>
    <h1 class="wiki-hero__title">Dongping Chen</h1>
    <p class="wiki-hero__subtitle">Multimodal generation · Agentic intelligence</p>
  </header>

  <nav class="wiki-contents" aria-label="Page contents">
    <span class="wiki-contents__title">Contents</span>
    <ol>
      <li><a href="#biography" target="_self">Biography</a></li>
      <li><a href="#research-interests" target="_self">Research Interests</a></li>
      <li><a href="#publications" target="_self">Publications</a></li>
      <li><a href="#education" target="_self">Education</a></li>
    </ol>
  </nav>

  <section id="biography" class="wiki-section wiki-biography" aria-labelledby="biography-title">
    <h2 id="biography-title" class="visually-hidden">Biography</h2>

    <aside class="wiki-infobox" aria-label="Dongping Chen profile summary">
      <div class="wiki-infobox__name">Dongping Chen</div>
      <img src="images/head_2025_hq.png" alt="Portrait of Dongping Chen">
      <dl class="wiki-infobox__facts">
        <div><dt>Chinese name</dt><dd>陈东平</dd></div>
        <div><dt>Occupation</dt><dd>Ph.D. Student</dd></div>
        <div><dt>Institution</dt><dd>University of Maryland</dd></div>
        <div><dt>Fields</dt><dd>Multimodal AI, Agents, Evaluation</dd></div>
        <div><dt>Citations</dt><dd><span id="total_cit" aria-live="polite">—</span></dd></div>
        <div>
          <dt>Websites</dt>
          <dd>
            <a href="{{ site.author.googlescholar }}">Scholar</a>
            <a href="https://github.com/{{ site.author.github }}">GitHub</a>
            <a href="https://www.linkedin.com/in/{{ site.author.linkedin }}">LinkedIn</a>
          </dd>
        </div>
        <div><dt>Contact</dt><dd><a href="mailto:{{ site.author.email }}">{{ site.author.email }}</a></dd></div>
      </dl>
    </aside>

    <div class="wiki-biography__copy">
      <p class="wiki-lead"><strong>Dongping Chen (陈东平)</strong> is a Computer Science Ph.D. student at the University of Maryland. He currently works on multimodal generation and agents with Professor <a href="https://tianyizhou.github.io/">Tianyi Zhou</a> and Professor <a href="https://www.cs.umd.edu/people/dmanocha">Dinesh Manocha</a>.</p>
      <p>Previously, he was a visiting student at the University of Washington, where he worked with Professor <a href="https://ranjaykrishna.com/index.html">Ranjay Krishna</a> and <a href="https://jieyuz2.github.io/">Jieyu Zhang</a>. His academic journey has also included collaborations with <a href="https://lichao-sun.github.io/">Lichao Sun</a>, <a href="https://engineering.nd.edu/faculty/xiangliang-zhang/">Xiangliang Zhang</a>, and <a href="http://wanyao.me/">Yao Wan</a>.</p>
    </div>
  </section>

  <section id="research-interests" class="wiki-section" aria-labelledby="research-interests-title">
    <h2 id="research-interests-title">Research Interests</h2>
    <p>I study multimodal generative models and the agentic systems they power, with an emphasis on evaluation, tool use, efficiency, and trustworthy behavior.</p>
    <ul class="research-topics" aria-label="Research topics">
      <li>Multimodal Understanding and Generation</li>
      <li>Agentic AI</li>
    </ul>
  </section>

  <section id="publications" class="wiki-section publications" aria-labelledby="publications-title">
    <h2 id="publications-title">Publications</h2>
    <p class="publication-note"><span aria-hidden="true">*</span> indicates equal contribution. <span aria-hidden="true">‡</span> indicates project leaders.</p>

    <div class="publication-tabs" role="tablist" aria-label="Publication categories">
      <button class="publication-tab" id="publication-tab-contributions" type="button" role="tab" aria-selected="true" aria-controls="publication-panel-contributions">Main Contributions</button>
      <button class="publication-tab" id="publication-tab-led" type="button" role="tab" aria-selected="false" aria-controls="publication-panel-led" tabindex="-1">Projects Led</button>
    </div>

    <section class="publication-tab-panel" id="publication-panel-contributions" role="tabpanel" aria-labelledby="publication-tab-contributions">
      <div class="publication-list">
        <article class="publication-row">
          <div class="publication-row__media"><img src="images/VGI.png" alt="Measuring Visual Generative Intelligence project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">CVPR 2026 Findings</span></div>
            <h4>Measuring Visual Generative Intelligence</h4>
            <p class="publication-authors"><strong class="author-me">Dongping Chen</strong> *, Ruoxi Chen *, Xuanao Huang *, Yishan Wang *, Junqi Yang *, Yao Wan†, Ranjay Krishna†</p>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/ISG.png" alt="Interleaved Scene Graph project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">ICLR 2025 Spotlight</span></div>
            <h4><a href="https://arxiv.org/pdf/2411.17188">Interleaved Scene Graph for Interleaved Text-and-Image Generation Assessment</a></h4>
            <p class="publication-authors"><strong class="author-me">Dongping Chen</strong> *, Ruoxi Chen *, Shu Pu *, Zhaoyi Liu *, Yanru Wu *, Caixi Chen *, Benlin Liu, Yue Huang, Yao Wan, Pan Zhou, Ranjay Krishna†</p>
            <div class="publication-links" aria-label="Interleaved Scene Graph resources">
              <a href="https://arxiv.org/pdf/2411.17188">PDF</a>
              <a href="https://github.com/Dongping-Chen/ISG">GitHub</a>
              <a href="https://interleave-eval.github.io/">Website</a>
            </div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/GUI.png" alt="GUI-World project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">ICLR 2025</span></div>
            <h4><a href="https://arxiv.org/pdf/2406.10819">GUI-World: A Dataset for GUI-oriented Multimodal LLM-based Agents</a></h4>
            <p class="publication-authors"><strong class="author-me">Dongping Chen</strong> *, Yue Huang *, Siyuan Wu, Jingyu Tang, Liuyi Chen, Yilin Bai, Zhigang He, Chenlong Wang, Huichi Zhou, Yiqiang Li, Tianshuo Zhou, Yue Yu, Chujie Gao, Qihui Zhang, Yi Gui, Zhen Li, Yao Wan†, Pan Zhou†, Jianfeng Gao, Lichao Sun</p>
            <div class="publication-links" aria-label="GUI-World resources">
              <a href="https://arxiv.org/pdf/2406.10819">PDF</a>
              <a href="https://github.com/Dongping-Chen/GUI-World">GitHub</a>
              <a href="https://gui-world.github.io">Website</a>
            </div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/HonestLLM.png" alt="HonestLLM project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">NeurIPS 2024</span></div>
            <h4><a href="https://arxiv.org/pdf/2406.00380"><em>The Best of Both Worlds</em>: Toward an Honest and Helpful Large Language Model</a></h4>
            <p class="publication-authors">Chujie Gao *, Siyuan Wu *, Yue Huang *, <strong class="author-me">Dongping Chen</strong> *, Qihui Zhang *, Zhengyan Fu, Yao Wan†, Xiangliang Zhang, Lichao Sun</p>
            <div class="publication-links" aria-label="HonestLLM resources">
              <a href="https://arxiv.org/pdf/2406.00380">PDF</a>
              <a href="https://github.com/Flossiee/HonestyLLM">GitHub</a>
              <a href="https://honestllm.github.io/">Website</a>
            </div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/mllm-judge.jpg" alt="MLLM-as-a-Judge project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">ICML 2024 Oral</span></div>
            <h4><a href="https://arxiv.org/pdf/2402.04788">MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark</a></h4>
            <p class="publication-authors"><strong class="author-me">Dongping Chen</strong> *, Ruoxi Chen *, Shilin Zhang *, Yinuo Liu *, Yaochen Wang *, Huichi Zhou *, Qihui Zhang *, Yao Wan†, Pan Zhou†, Lichao Sun</p>
            <div class="publication-links" aria-label="MLLM-as-a-Judge resources">
              <a href="https://arxiv.org/pdf/2402.04788">PDF</a>
              <a href="https://github.com/Dongping-Chen/MLLM-Judge">GitHub</a>
              <a href="https://mllm-judge.github.io/">Website</a>
            </div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/mixcase.jpg" alt="LLM-as-a-Coauthor project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">NAACL 2024 Findings</span></div>
            <h4><a href="https://arxiv.org/pdf/2401.05952">LLM-as-a-Coauthor: The Challenges of Detecting LLM-Human Mixcase</a></h4>
            <p class="publication-authors">Qihui Zhang *, Chujie Gao *, <strong class="author-me">Dongping Chen</strong> *, Yue Huang, Yixin Huang, Zhenyang Sun, Shilin Zhang, Weiye Li, Zhengyan Fu, Yao Wan, Lichao Sun†</p>
            <div class="publication-links" aria-label="LLM-as-a-Coauthor resources">
              <a href="https://arxiv.org/pdf/2401.05952">PDF</a>
              <a href="https://github.com/Dongping-Chen/MixSet">GitHub</a>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section class="publication-tab-panel" id="publication-panel-led" role="tabpanel" aria-labelledby="publication-tab-led">
      <div class="publication-list">
        <article class="publication-row">
          <div class="publication-row__media"><img src="images/Paper2Web.png" alt="Paper2Web project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">Tech Report</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2510.15842">Paper2Web: Let's Make Your Paper Alive!</a></h4>
            <p class="publication-authors">Yuhang Chen, Tianpeng Lv, Siyi Zhang, Yixiang Yin, Yao Wan, Philip S. Yu, <strong class="author-me">Dongping Chen</strong>‡</p>
            <div class="publication-links" aria-label="Paper2Web resources"><a href="https://arxiv.org/pdf/2510.15842">PDF</a><a href="https://github.com/YuhangChen1/Paper2All">GitHub</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/Judge.png" alt="LLM-as-a-Judge assessment project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">Tech Report</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2512.16041">Are We on the Right Way to Assessing LLM-as-a-Judge?</a></h4>
            <p class="publication-authors">Yuanning Feng, Sinan Wang, Zhengxiang Cheng, Yao Wan, <strong class="author-me">Dongping Chen</strong>‡</p>
            <div class="publication-links" aria-label="LLM-as-a-Judge assessment resources"><a href="https://arxiv.org/pdf/2512.16041">PDF</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/ReVPT.png" alt="ReVPT project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">Tech Report</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2509.01656">Reinforced Visual Perception with Tools</a></h4>
            <p class="publication-authors">Zetong Zhou, <strong class="author-me">Dongping Chen</strong>‡, Zixian Ma, Zhihan Hu, Mingyang Fu, Sinan Wang, Yao Wan†, Zhou Zhao, Ranjay Krishna†</p>
            <div class="publication-links" aria-label="ReVPT resources"><a href="https://arxiv.org/pdf/2509.01656">PDF</a><a href="https://github.com/ls-kelvin/REVPT">GitHub</a><a href="https://huggingface.co/collections/Frywind/revpt-68b05161d2426128ea5db4d3">Model &amp; Dataset</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/double-bench.png" alt="Double-Bench project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">AAAI 2026</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2508.03644">Are We on the Right Way for Assessing Document Retrieval-Augmented Generation?</a></h4>
            <p class="publication-authors">Wenxuan Shen *, Mingjia Wang *, Yaochen Wang, <strong class="author-me">Dongping Chen</strong>‡, Junjie Yang, Yao Wan, Weiwei Lin†</p>
            <div class="publication-links" aria-label="Double-Bench resources"><a href="https://arxiv.org/pdf/2508.03644">PDF</a><a href="https://github.com/Episoode/Double-Bench">GitHub</a><a href="https://double-bench.github.io/">Website</a><a href="https://huggingface.co/datasets/Episoode/Double-Bench">Dataset</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/code_transformed.png" alt="code transformed project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">EACL 2026</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2506.12014">code_transformed: The Influence of Large Language Models on Code</a></h4>
            <p class="publication-authors">Yuliang Xu *, Siming Huang *, Mingmeng Geng†, Yao Wan†, Xuanhua Shi, <strong class="author-me">Dongping Chen</strong>‡</p>
            <div class="publication-links" aria-label="code transformed resources"><a href="https://arxiv.org/pdf/2506.12014">PDF</a><a href="https://github.com/ignorancex/LLM_code">GitHub</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/LC-R1.png" alt="LC-R1 project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">Tech Report</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2506.14755">Optimizing Length Compression in Large Reasoning Models</a></h4>
            <p class="publication-authors">Zhengxiang Cheng, <strong class="author-me">Dongping Chen</strong>‡, Mingyang Fu, Tianyi Zhou†</p>
            <div class="publication-links" aria-label="LC-R1 resources"><a href="https://arxiv.org/pdf/2506.14755">PDF</a><a href="https://github.com/zxiangx/LC-R1">GitHub</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/liveVQA.png" alt="LiveVQA project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">NeurIPS 2025 D&amp;B</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2504.05288">Seeking and Updating with Live Visual Knowledge</a></h4>
            <p class="publication-authors">Mingyang Fu*, Yuyang Peng*, <strong class="author-me">Dongping Chen</strong>‡, Zetong Zhou, Benlin Liu, Yao Wan†, Zhou Zhao, Philip S. Yu, Ranjay Krishna†</p>
            <div class="publication-links" aria-label="LiveVQA resources"><a href="https://arxiv.org/pdf/2504.05288">PDF</a><a href="https://github.com/fumingyang2004/LIVEVQA">GitHub</a><a href="https://huggingface.co/datasets/ONE-Lab/LiveVQA-new/tree/main">Dataset</a><a href="https://livevqa.github.io/">Website</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/multiref.png" alt="MultiRef project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">ACM MM 2025 Dataset</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2508.06905">MultiRef: Controllable Image Generation with Multiple Visual References</a></h4>
            <p class="publication-authors">Ruoxi Chen, <strong class="author-me">Dongping Chen</strong>‡, Siyuan Wu, Sinan Wang, Shiyun Lang, Petr Sushko, Gaoyang Jiang, Yao Wan, Ranjay Krishna†</p>
            <div class="publication-links" aria-label="MultiRef resources"><a href="https://arxiv.org/pdf/2508.06905">PDF</a><a href="https://github.com/Dipsy0830/MultiRef-code">GitHub</a><a href="https://huggingface.co/datasets/ONE-Lab/MultiRef-dataset">Dataset</a><a href="https://multiref.github.io/">Website</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/nowait.png" alt="Removing thinking tokens project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">EMNLP 2025 Findings</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2506.08343v2">Wait, We Don't Need to "Wait"! Removing Thinking Tokens Improves Reasoning Efficiency</a></h4>
            <p class="publication-authors">Chenlong Wang, Yuanning Feng, <strong class="author-me">Dongping Chen</strong>‡, Zhaoyang Chu, Ranjay Krishna, Tianyi Zhou†</p>
            <div class="publication-links" aria-label="Removing thinking tokens resources"><a href="https://arxiv.org/pdf/2506.08343v2">PDF</a><span>Code coming soon</span></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/JudgeAnything.png" alt="Judge Anything project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">KDD 2025 D&amp;B Oral</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2503.17489">Judge Anything: MLLM as a Judge Across Any Modality</a></h4>
            <p class="publication-authors">Shu Pu *, Yaochen Wang *, <strong class="author-me">Dongping Chen</strong>‡, Yuhang Chen, Guohao Wang, Qi Qin, Zhongyi Zhang, Zhiyuan Zhang, Zetong Zhou, Shuang Gong, Yi Gui, Yao Wan†, Philip S. Yu</p>
            <div class="publication-links" aria-label="Judge Anything resources"><a href="https://arxiv.org/pdf/2503.17489">PDF</a><a href="https://urrealhero.github.io/judgeanythingweb/">Website</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/Wikipedia.png" alt="Wikipedia in the era of LLMs project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">TMLR</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2503.02879">Wikipedia in the Era of LLMs: Evolution and Risks</a></h4>
            <p class="publication-authors">Siming Huang *, Yuliang Xu *, Mingmeng Geng†, Yao Wan†, <strong class="author-me">Dongping Chen</strong>‡</p>
            <div class="publication-links" aria-label="Wikipedia in the era of LLMs resources"><a href="https://arxiv.org/pdf/2503.02879">PDF</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/codesync.png" alt="CodeSync project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">ICML 2025</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2502.16645">CodeSync: Synchronizing Large Language Models with Dynamic Code Evolution at Scale</a></h4>
            <p class="publication-authors">Chenlong Wang, Zhaoyang Chu, Zhengxiang Cheng, Xuyi Yang, Kaiyue Qiu, Yao Wan, Zhou Zhao, Xuanhua Shi, <strong class="author-me">Dongping Chen</strong>‡</p>
            <div class="publication-links" aria-label="CodeSync resources"><a href="https://arxiv.org/pdf/2502.16645">PDF</a><a href="https://github.com/Lucky-voyage/Code-Sync">Code</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/nvAgent.png" alt="nvAgent project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">ACL 2025</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2502.05036">nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow</a></h4>
            <p class="publication-authors">Geliang Ouyang, Jingyao Chen, Zhihe Nie, Yi Gui, Yao Wan†, Hongyu Zhang, <strong class="author-me">Dongping Chen</strong>‡</p>
            <div class="publication-links" aria-label="nvAgent resources"><a href="https://arxiv.org/pdf/2502.05036">PDF</a><a href="https://github.com/geliang0114/nvAgent">Code</a></div>
          </div>
        </article>

        <article class="publication-row">
          <div class="publication-row__media"><img src="images/llm-speaking.png" alt="LLMs in academia project preview" loading="lazy"></div>
          <div class="publication-row__body">
            <div class="publication-row__meta"><span class="venue-label">ACL 2025 Findings</span><span class="lead-label">Project lead</span></div>
            <h4><a href="https://arxiv.org/pdf/2409.13686">The Impact of Large Language Models in Academia: from Writing to Speaking</a></h4>
            <p class="publication-authors">Mingmeng Geng†, Caixi Chen, Yanru Wu, <strong class="author-me">Dongping Chen</strong>‡, Yao Wan, Pan Zhou</p>
            <div class="publication-links" aria-label="LLMs in academia resources"><a href="https://arxiv.org/pdf/2409.13686">PDF</a></div>
          </div>
        </article>
      </div>
    </section>

    <script>
      (() => {
        const tablist = document.querySelector(".publication-tabs");
        if (!tablist) return;

        const tabs = Array.from(tablist.querySelectorAll('[role="tab"]'));
        const panels = tabs.map((tab) => document.getElementById(tab.getAttribute("aria-controls")));
        tablist.classList.add("publication-tabs--enhanced");

        const activateTab = (nextTab, moveFocus = false) => {
          tabs.forEach((tab, index) => {
            const isActive = tab === nextTab;
            tab.setAttribute("aria-selected", String(isActive));
            tab.tabIndex = isActive ? 0 : -1;
            panels[index].hidden = !isActive;
          });
          if (moveFocus) nextTab.focus();
        };

        tabs.forEach((tab) => tab.addEventListener("click", () => activateTab(tab)));
        tablist.addEventListener("keydown", (event) => {
          const currentIndex = tabs.indexOf(document.activeElement);
          if (currentIndex < 0) return;

          let nextIndex = currentIndex;
          if (event.key === "ArrowRight") nextIndex = (currentIndex + 1) % tabs.length;
          if (event.key === "ArrowLeft") nextIndex = (currentIndex - 1 + tabs.length) % tabs.length;
          if (event.key === "Home") nextIndex = 0;
          if (event.key === "End") nextIndex = tabs.length - 1;
          if (nextIndex === currentIndex && !["Home", "End"].includes(event.key)) return;

          event.preventDefault();
          activateTab(tabs[nextIndex], true);
        });

        activateTab(tabs.find((tab) => tab.getAttribute("aria-selected") === "true") || tabs[0]);
      })();
    </script>
  </section>

  <section id="education" class="wiki-section" aria-labelledby="education-title">
    <h2 id="education-title">Education</h2>
    <div class="education-list">
      <div class="education-item"><time>2025.08 — Current</time><p><strong>University of Maryland</strong><span>Ph.D. Student in Computer Science</span></p></div>
      <div class="education-item"><time>2024.08 — 2024.12</time><p><strong>University of Washington</strong><span>Visiting Scholar</span></p></div>
      <div class="education-item"><time>2021.09 — 2025.06</time><p><strong>Huazhong University of Science and Technology</strong><span>B.Eng.</span></p></div>
    </div>
  </section>

  <footer class="site-credit">
    <p>Design inspired by <a href="https://linxins.net/">Linxin Song</a>'s Wikipedia-style homepage. <a href="https://github.com/LinxinS97/LinxinS97.github.io">View the original source</a>.</p>
  </footer>
</div>
