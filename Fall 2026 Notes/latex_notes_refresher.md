# LaTeX Notes Organization & Formatting Refresher

Welcome back! With the new semester starting, this document summarizes how your LaTeX materials in [LaTex](file:///C:/Users/zsong/Desktop/LaTex) are organized and provides a review of your formatting style. Use this as a guide and refresher to kickstart your notes for the new semester.

---

## 1. Material Organization

Your directory structure is organized chronologically by semester and then subdivided by course. Here is a summary of how the folders are laid out:

```
C:\Users\zsong\Desktop\LaTex\
├── Syllabus\                    <-- Centralized syllabus directory
│   ├── 1 Fall 2024\
│   ├── 2 Spring 2025\
│   ├── 3 Summer 2025\
│   ├── 4 Fall 2025\
│   └── 5 Spring 2026\
├── Spring 2025\
├── Fall 2025 Notes\
│   ├── Diff Eq\
│   ├── Dynamics\
│   ├── Materials Science\
│   └── Physics\
├── Spring 2026 Notes\
│   ├── Circuits\
│   ├── Mech Mat\
│   ├── Modern Physics\
│   └── Systems\
└── Fall 2026 Notes\              <-- Empty (Ready for the new semester!)
```

### Key Strengths of Your Organization
* **Centralized Syllabi:** Keeping a dedicated [Syllabus](file:///C:/Users/zsong/Desktop/LaTex/Syllabus) directory numbered chronologically (e.g., `1 Fall 2024`, `2 Spring 2025`) prevents clutter in individual notes folders while maintaining an easy-to-reference historical record.
* **Course-Level Separation:** Each course has its own folder. For courses with large workloads (like `Circuits` or `Systems`), you successfully separate lectures, homework (`HW/`), labs (`Labs/`), and supplemental code (like MATLAB files) into logical subfolders.
* **Consolidated Lecture Notes:** For several courses (e.g., [Circuits.tex](file:///C:/Users/zsong/Desktop/LaTex/Spring%202026%20Notes/Circuits/Circuits.tex), [Mech Mat.tex](file:///C:/Users/zsong/Desktop/LaTex/Spring%202026%20Notes/Mech%20Mat/Mech%20Mat.tex), and [Systems.tex](file:///C:/Users/zsong/Desktop/LaTex/Spring%202026%20Notes/Systems/Systems.tex)), you maintain all primary lecture content in a single main document. This is highly effective for full-text search during review or exams.

---

## 2. LaTeX Formatting Review & Refreshers

Your recent documents showcase clean typesetting, strong organization, and effective layout strategies. Below is a detailed breakdown of your formatting patterns, along with a few recommendations to streamline your workflow this semester.

### Preamble and Document Layout
Your default document setup uses standard and powerful engineering/scientific packages:
```latex
\documentclass[12pt]{article}
\usepackage{amssymb, amsmath, amsfonts, bm, graphicx, geometry}
\usepackage{tabularx, booktabs, float, enumitem, multicol, mathtools}
\geometry{margin=1in}
```

#### Refresher Tips:
* **Custom Titles:** Currently, you leave standard metadata empty (`\title{}`, `\author{}`, `\date{}`) and manually format the document title at the top of the body (e.g., `\begin{center}{\LARGE ESC-221 Basic Principles... \par}\end{center}`). This is perfectly fine, but if you want standard header margins, consider using the `fancyhdr` package for automated running headers.
* **Line Breaks vs. Paragraphs:** You often use multiple line breaks (`\\\\` or `\newpage\noindent`) to separate ideas. 
  > [!TIP]
  > Importing the `parskip` package (`\usepackage{parskip}`) automatically adds a clean spacing between paragraphs and removes indentations. This saves you from having to type manual `\\\\` spacers.

---

### Side-by-Side Text & Diagrams
To prevent figures from floating away, you make excellent use of `minipage` environments paired with `\hfill` to keep diagrams side-by-side with their descriptions (e.g., in [Mech Mat.tex](file:///C:/Users/zsong/Desktop/LaTex/Spring%202026%20Notes/Mech%20Mat/Mech%20Mat.tex)):

```latex
\begin{minipage}[t]{0.6\textwidth} \vspace{0pt}
Normal stress is force divided by cross-sectional area:
\[ \sigma_{\text{avg}} = \frac{P}{A} \]
\end{minipage}
\hfill
\begin{minipage}[t]{0.4\textwidth} \vspace{0pt}\centering
\includegraphics[width=\textwidth]{Normal Stress.png}
\end{minipage}
```
* **Why this works:** The `[t]` alignment coupled with `\vspace{0pt}` ensures that the tops of the text and the graphic align perfectly. Keep using this pattern—it makes notes highly readable!

---

### Math Formatting & Alignments

#### 1. Avoid `eqnarray*` (Use `align*` instead)
In [Systems.tex](file:///C:/Users/zsong/Desktop/LaTex/Spring%202026%20Notes/Systems/Systems.tex#L95-L99), you typeset systems of equations using the older `eqnarray*` environment:
```latex
% Old Approach
\begin{eqnarray*}
y(t) &=& e^{rt}\\
y'(t) &=& re^{rt}\\
y''(t) &=& r^{2}e^{rt}\\
\end{eqnarray*}
```

> [!WARNING]
> `eqnarray` is considered deprecated in modern LaTeX. It introduces large, inconsistent spaces around the `=` signs and does not coordinate spacing with standard math blocks.

Instead, use `align*` from the `amsmath` package (which you already include in your preamble). Notice that you only use **one** `&` symbol per line:
```latex
% Recommended Approach
\begin{align*}
y(t) &= e^{rt} \\
y'(t) &= re^{rt} \\
y''(t) &= r^2 e^{rt}
\end{align*}
```

#### 2. Typesetting Units and Values
You write units by manually escaping math mode (e.g., `1\,\text{J} = 1\,\text{W} \times 1\,\text{s}` or `[12\,\text{V}]`).
To automate spacing and ensure standard unit symbols (like printing micro $\mu$ as upright in units), you can load the `siunitx` package:

```latex
\usepackage{siunitx}
...
We can write a quantity: \qty{12}{\volt} or \qty{1.602e-19}{\coulomb}
We can write standalone units: \unit{\joule} = \unit{\watt\second}
```
This guarantees consistent spacing and formatting (e.g., matching standard scientific publication guidelines).

#### 3. Bold Math Symbols
For bold variables in math, you use `\bm{...}` (from the `bm` package). This is the best practice! Using `\bm{...}` maintains the italicized style of math fonts (especially for Greek letters like `\bm{\theta}` or vector fields like `\bm{A}$`) whereas `\mathbf{...}` changes them to upright fonts.

#### 4. Custom Macros
You defined a handy custom macro in `Systems.tex` for the volume symbol:
```latex
\newcommand{\vol}{\mathord{\text{\ooalign{\hidewidth $V$\hidewidth\cr\kern-0.5pt\raisebox{0.8ex}{\rule[0pt]{1em}{0.5pt}}}}}}
```
This is a clever way to typeset a custom slashed-V for thermodynamic/fluid properties! If you find yourself needing other custom notations for the upcoming term, defining them in your preamble like this is highly recommended.

---

## 3. Ready for Fall 2026!

Since [Fall 2026 Notes](file:///C:/Users/zsong/Desktop/LaTex/Fall%202026%20Notes) is currently empty, you are ready to set up your templates. 

### Recommendation for Your Next File
When you create your first lecture notes file for this semester (e.g., `Fall 2026 Notes/Dynamics/Dynamics.tex`), feel free to use the template below which incorporates the clean formatting practices highlighted above:

```latex
\documentclass[12pt]{article}
\usepackage{amssymb, amsmath, amsfonts, bm, graphicx, geometry}
\usepackage{tabularx, booktabs, float, enumitem, multicol, mathtools}
\usepackage{parskip} % Auto-manages paragraph spacing and removes indentations
\usepackage{siunitx}  % Eases typesetting of numbers and units

\geometry{margin=1in}

\begin{document}

\begin{center}
{\LARGE [Course Code] [Course Name] Notes\par}
\end{center}
\hrule
\vspace{1.5em}

\section*{Lecture 1: Introduction}

\begin{minipage}[t]{0.6\textwidth} \vspace{0pt}
Write your concepts here. You can easily typeset quantities such as \qty{9.81}{\meter\per\second\squared} and format aligned equations:
\begin{align*}
F &= m \bm{a} \\
\bm{a} &= \frac{d\bm{v}}{dt}
\end{align*}
\end{minipage}
\hfill
\begin{minipage}[t]{0.35\textwidth} \vspace{0pt}\centering
% \includegraphics[width=\textwidth]{diagram.png}
% \caption{Diagram placeholder}
\end{minipage}

\end{document}
```
